FROM python:3.8.13-slim
WORKDIR /app
COPY . .
RUN python3 -m pip install --no-cache-dir --upgrade pip
RUN pip3 install -r requirements.txt --no-cache-dir
CMD ["python3", "bot.py"]
