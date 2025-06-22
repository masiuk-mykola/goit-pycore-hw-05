levels = ["DEBUG", "INFO", "WARNING", "ERROR"]


def load_logs(file_path: str) -> list:
    try:
        with open(file_path, encoding="utf-8") as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []


def parse_log_line(line: str) -> dict:

    [date, time, level, *message] = line.split(" ")
    log_dict = {
        "date": date,
        "time": time,
        "level": level,
        "message": " ".join(message),
    }
    return log_dict


def filter_logs_by_level(logs: list, level: str) -> list:

    if not level:
        return logs
    elif not level in levels:
        print(
            f"Error: Invalid log level '{level}'. Valid levels are: {', '.join(levels)}"
        )

    return [log for log in logs if log.get("level") == level.upper()]


def count_logs_by_level(logs: list) -> dict:

    counts = {}
    for log in logs:
        level = log.get("level")
        if level:
            counts[level] = counts.get(level, 0) + 1
    return counts


def display_log_counts(counts: dict):

    print("Log level | Count")
    print("----------|----------")

    for level, count in counts.items():
        print(f"{level.ljust(10)}| {str(count).ljust(9)}")


def display_filtered_log_info(logs: list, level: str):

    if not logs or not level:
        return

    print("")
    print(f"Log details for level '{level.upper()}':")
    for log in logs:
        print(f"{log['date']} {log['time']} - {log['message']}")
