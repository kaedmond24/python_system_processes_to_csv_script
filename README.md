# Python System Processes to CSV Script

---

Created By Kevin Edmond

Repository for Python System Processes to CSV Script: Snapshot of Running System Processes as CSV File

### Instructions:

1. Install Python 3 for your system using instructions [here](https://www.python.org/downloads/).<br>

2. Install required packages.<br>

   > command: `python3 pip install psutil`

3. Run the script.<br>

   > command: `python3 processes.py`

### Script Logic:

1. Create empty `process_list` list to hold running system processes.

2. Create a `for loop` that iterates through the content of `psutil.process_iter()` method. This method returns a list of runnning system processes. Aditionally, a list of attributes can be passed to the method curate the data being returned. The attributes returned for this script include: `pid`, `name`, `exe`, `cpu_percent`, `memory_percent`. This returned data is addedd to the `process_list` list.

3. A writable CSV file is created using the `open()` method.

4. The column headers are written to the first row of the CSV. Next, A `for loop` is used to write each row of the CSV file using the `process_list` list.

5. A notification regarding the CSV creation is displayed.
