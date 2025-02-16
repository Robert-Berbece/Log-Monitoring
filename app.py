import logging
from datetime import datetime
import pprint

# Set up logging configuration to log to a file
logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    handlers=[logging.StreamHandler(),
                              logging.FileHandler("Report_logs.txt", mode="w")])

logger = logging.getLogger()

# Function 1: Read log file and create the pid_dict
def read_log_file(file_path):
    pid_dict = {}
    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            columns = line.split(",")
            if len(columns) < 4:
                continue

            timestamp_str = columns[0].strip()
            job_description_full = columns[1].strip()
            status = columns[2].strip()
            pid_str = columns[3].strip()

            try:
                pid = int(pid_str)
            except ValueError:
                continue  # Skip if PID is not a valid integer

            if "scheduled task" in job_description_full:
                job_description = job_description_full
            elif "background job" in job_description_full:
                job_description = job_description_full
            else:
                job_description = job_description_full

            if pid not in pid_dict:
                pid_dict[pid] = [job_description, None, None]

            if status == "START":
                pid_dict[pid][1] = timestamp_str
            elif status == "END":
                pid_dict[pid][2] = timestamp_str
    return pid_dict


file_path = "/home/robert/Desktop/Scripts/Assesment/logs.log"

