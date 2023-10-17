# Using the Python modules os Links to an external site., psutil to an external site., 
# and CSVLinks to an external site., create a CSV file that lists all running processes 
# and has columns for process ID #, name, executable path, CPU usage, and mem usage. 

#############################################################################################
# Created by Kevin Edmond.
#
# This script is used to extract a snapshot of the host system's running processes and 
# outputs the data into a CSV file. The is formatted with the following column headers:
# Process ID #, Name, Executable Path, CPU Usage, Mem Usage. The CSV file will be named 
# 'running_processes.csv'.  
#
#
# Please read README.md for full notes on script.
#
#############################################################################################

import os
import psutil
import csv

# Create list for Processes
process_list = []


# Get running processes
for proc in psutil.process_iter(attrs=['pid', 'name', 'exe', 'cpu_percent', 'memory_percent']):
    try:
        process = proc.info
        process_list.append(process)
    except (psutil.NoSuchProcess):
        pass

# Uncomment to test output of For Loop
# print(processes)


# Create CSV File

# Create CSV Filename variable
# Create Column Headers variable: Process ID # |  Name |  Executable Path | CPU Usage | Mem Usage
csv_filename = "running_processes.csv"
csv_header = ["process ID #", "name" , "executable path", "CPU usage", "mem usage"]

# Create writable CSV 
with open(csv_filename, "w", newline='') as file:
    # Pass in filename alias being written to
    writer = csv.writer(file)
    # Write CSV headers to first row
    writer.writerow(csv_header)
    
    # Write system process data to CSV file
    for process in process_list:
        writer.writerow(
            [process['pid'], process['name'], process['exe'], process['cpu_percent'], process['memory_percent']]
            )


# Notify user CSV was created.
print(f"{csv_filename} has been created.")
