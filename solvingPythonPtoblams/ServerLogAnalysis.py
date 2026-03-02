#Create a dictionary where the keys are the log levels (e.g., "INFO", "ERROR") and the values are the count of how many times that level appears in the logs.
logs = [
    "2024-03-01 10:00:01 [INFO] System started",
    "2024-03-01 10:05:00 [ERROR] Connection timeout",
    "2024-03-01 10:05:30 [WARNING] High memory usage",
    "2024-03-01 10:10:00 [ERROR] Database connection failed",
    "2024-03-01 10:15:00 [INFO] Backup complete",
    "2024-03-01 10:20:00 [ERROR] Connection timeout",
    "2024-03-01 10:30:00 [CRITICAL] System crash"
]

log_counts = {
    "INFO": 0,
    "ERROR": 0,
    "WARNING": 0,
    "CRITICAL": 0
}
for i in logs:
    if "[ERROR]" in i:
        log_counts["ERROR"] += 1
    elif "[INFO]" in i:
        log_counts["INFO"] += 1
    elif "[CRITICAL]" in i:
        log_counts["CRITICAL"] += 1
    else:
        log_counts["WARNING"] += 1
print(log_counts)