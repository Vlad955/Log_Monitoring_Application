# Log_Monitoring_Application
Log Monitoring Application that checks logs from a CSV file

# Features
- Reads log entries from a CSV file
- Parses job start and end times
- Verifies job duration
- Displays job duration
- Identifies jobs that are taking longer than 5 minutes and marks them as a WARNING
- Identifies jobs that are taking longer than 5 minutes and marks them as an ERROR

# How to use
- Place the logs in "login.csv" file
- Run the script: python3 log_monitoring.py

# Sample Output
Job 62401: Start - 12:05:59, End - 12:16:23, Duration - 0:10:24

ERROR: Job 62401 took longer than 10 minutes

Job 81470: Start - 12:08:30, End - 12:09:33, Duration - 0:01:03

Job 24482: Start - 12:10:38, End - 12:19:14, Duration - 0:08:36

WARNING: Job 24482 took longer than 5 minutes

Task 72897 is missing START or END time.

# Things to improve
Generate separate CSV files instead of console output:
    - warning_logs.csv --> Stores warning logs
    - error_logs.csv --> Stores error logs
    - incomplete_logs.csv --> For jobs that do not have a START or END time