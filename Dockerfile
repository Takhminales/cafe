# Используем официальный образ Python
FROM python:3.8-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл зависимостей в контейнер
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы проекта в контейнер
COPY . .

# Открываем порт для работы приложения (например, 8000)
EXPOSE 8000

# Запускаем команду для запуска сервера Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
