FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Установить Playwright и браузеры
RUN python -m playwright install chromium


# Команда по умолчанию — запуск тестов
CMD ["pytest", "--alluredir=allure-results"]