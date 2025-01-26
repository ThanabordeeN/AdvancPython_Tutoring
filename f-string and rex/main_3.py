import re

# ข้อความที่เก็บรายชื่อ Email Addresses
email_list_text = """
รายชื่ออีเมลลูกค้า:
- customer1@example.com
- support.team@company.co.th
- sales_department+promo2023@domain.net
- invalid-email@@address.org
- contact@website.info
- test.email.with.dots@sub.domain.com
"""

# Regular Expression สำหรับตรวจสอบ Email Address ที่ถูกต้อง
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

# ค้นหา Email Addresses ที่ถูกต้อง
valid_emails = re.findall(email_pattern, email_list_text)

# นับจำนวน Email Addresses ที่ถูกต้อง
num_valid_emails = len(valid_emails)

# สร้างข้อความสรุปผลการวิเคราะห์
summary = f"""
รายงานสรุป Email Addresses:

พบ Email Addresses ที่ถูกต้องทั้งหมด {num_valid_emails} รายการ:
{', '.join(valid_emails)}

**จบรายงาน**
"""

# แสดงผลลัพธ์
print(summary)