from datetime import datetime
import os
  
start_date = datetime(2024, 12, 21)


today = datetime.today()


days_passed = (today - start_date).days


print(f"Сегодня прошло {days_passed} дней.")
os.system("pause")  