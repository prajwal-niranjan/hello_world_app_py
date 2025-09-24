FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY src ./src

ENV PORT=5000
EXPOSE 5000

CMD ["python", "src/main.py"]
