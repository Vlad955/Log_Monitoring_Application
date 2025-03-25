import csv
from datetime import datetime, timedelta


file_name = "logs.csv"
jobs = {} # Dictionary that stores job information

# Open and read the logs.csv file
with open(file_name, "r", newline='') as f:
    reader = csv.reader(f)
    for row in reader:    
        # Cleans all row values by stripping whitespace to ensure no extra spaces
        # in time, task, status or job_id
        time, task, status, job_id = map(str.strip, row)
        
        # Initialize job entry
        if job_id not in jobs:
            jobs[job_id] = {"start": None, "end": None}
        
        # Stores the start and end times based on job status
        if status == "START":
            jobs[job_id]["start"] = time
        elif status == "END":
            jobs[job_id]["end"] = time


# Process each job
for job_id, time in jobs.items():
    
    # Verifies only jobs that have both START and END times
    if time["start"] and time ["end"]:
        
        # Convert time strings to datetime objects for calculation
        start_time = datetime.strptime(time["start"], "%H:%M:%S") 
        end_time = datetime.strptime(time["end"], "%H:%M:%S")
        
        # Calculates the duration of the job
        duration = end_time - start_time
        
        print(f"Job {job_id}: Start - {time['start']}, End - {time['end']}, Duration - {duration}")
        
        # Check for long running jobs and displays information based on their time
        if duration >= timedelta(minutes=5) and duration <= timedelta(minutes=10):
            print(f"WARNING: Job {job_id} took longer than 5 minutes")
        elif duration >= timedelta (minutes=10):
             print(f"ERROR: Job {job_id} took longer than 10 minutes")
    else:
        # Displays incomplete jobs 
        print(f"Task {job_id} is missing START or END time.")
        