import unittest
from app import calculate_time_diff, read_log_file, generate_report

class TestLogProcessing(unittest.TestCase):

    def test_calculate_time_diff(self):
        """Test if the time difference is calculated correctly."""
        start_time = "11:35:23"
        end_time = "11:36:23"
        result = calculate_time_diff(start_time, end_time)
        self.assertEqual(result, "0:01:00")  # Expecting 1 minute difference

    def test_process_log_file(self):
        """Test if log processing extracts correct job details."""
        test_log_file = "test_logs.log"
        
        # Create a sample test log file
        with open(test_log_file, "w") as file:
            file.write("11:35:23,background job xfg,START,12345\n")
            file.write("11:36:23,background job xfg,END,12345\n")

        expected_output = {
            12345: ['background job xfg', '11:35:23', '11:36:23']
        }
        
        output = process_log_file(test_log_file)
        self.assertEqual(output, expected_output)

    def test_generate_report(self):
        """Test if the report is generated correctly."""
        pid_dict = {
            12345: ['background job xfg', '11:35:23', '11:36:23']
        }
        report_file = "test_report.txt"
        generate_report(pid_dict, report_file)

        # Check if the report file contains the correct information
        with open(report_file, "r") as file:
            lines = file.readlines()
            self.assertIn("Job Report", lines[0])
            self.assertIn("12345", lines[3])  # Checking if PID 12345 is in the report

if __name__ == "__main__":
    unittest.main()
