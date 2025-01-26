import re

log_file_content = """
[2023-10-27 10:00:15] INFO: User 'admin' logged in successfully.
[2023-10-27 10:02:30] WARNING: High CPU usage detected.
[2023-10-27 10:05:00] ERROR: Database connection timeout.
[2023-10-27 10:05:05] ERROR: Failed to process order #12345.
[2023-10-27 10:07:45] INFO: System performance restored.
[2023-10-27 10:10:20] ERROR: Invalid input data format.
"""

# Regular Expression pattern เพื่อสกัดวันที่, เวลา, และข้อความ Error
pattern = r'\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\] ERROR: (.*)'

# ใช้ re.findall() เพื่อค้นหาข้อมูลที่ตรงกับ pattern
errors = re.findall(pattern, log_file_content)

# แสดงผลลัพธ์
print(errors)