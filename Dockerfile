FROM python:3.10

RUN apt-get update && apt-get install -y \
    pkg-config \
    libmariadb-dev \
    && apt-get clean

WORKDIR /champions_stats

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "localhost:8000"]
