import sys
from pathlib import Path

from utils import (
    count_logs_by_level,
    display_filtered_log_info,
    display_log_counts,
    filter_logs_by_level,
    load_logs,
    parse_log_line,
)


def main():
    if len(sys.argv) < 2:
        print("❗ Error: You must specify a file path as the first argument.")
        return

    file_path = Path(sys.argv[1])
    args = sys.argv[2] if len(sys.argv) > 2 else None

    log_dicts = [parse_log_line(line) for line in load_logs(file_path)]
    if len(log_dicts) == 0:
        print("Error: No valid log entries found.")
        return

    filtered_logs = filter_logs_by_level(log_dicts, args)
    log_counts = count_logs_by_level(log_dicts)

    display_log_counts(log_counts)
    display_filtered_log_info(filtered_logs, args)


if __name__ == "__main__":
    main()
