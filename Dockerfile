# Usa Python leve para produção
FROM python:3.11-alpine

WORKDIR /app


RUN apk add --no-cache gcc musl-dev postgresql-dev
RUN pip install psycopg2-binary pyyaml


COPY . .

CMD ["python", "scanner.py", "--target", "app.py"]