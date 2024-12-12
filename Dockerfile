FROM python:3.11-slim

# تنظیم پوشه کاری
WORKDIR /app

# کپی فایل‌ها
COPY . /app

# نصب وابستگی‌ها
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# باز کردن پورت
EXPOSE 8000

# اجرای برنامه
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
