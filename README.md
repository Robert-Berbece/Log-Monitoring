# Log Monitoring Script  

## Overview  
This Python script (`app.py`) monitors log files, calculates job execution times, and logs warnings/errors for jobs exceeding predefined durations. A test script (`test.py`) ensures correctness.  

## Features  
- Reads log files and extracts job execution data.  
- Logs Warnings for jobs taking longer than 5 minutes.  
- Logs Errors for jobs taking longer than 10 minutes.  
- Generates a report (`Report_logs.txt`).  
- Includes unit tests (`test.py`).  

## Usage  
1. Clone the repository:  
   
   git clone https://github.com/Robert-Berbece/Log-Monitoring.git  
   cd Log-Monitoring

2. Run the script:

   python3 app.py

3. Run test:

  python3 test.py OR python3 -m unittest test.py  
