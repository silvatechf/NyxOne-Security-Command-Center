# Usa Python leve para produção
FROM python:3.11-alpine

# Define diretório de trabalho
WORKDIR /app

# Instala dependências (psycopg2 precisa de bibliotecas de sistema)
RUN apk add --no-cache gcc musl-dev postgresql-dev
RUN pip install psycopg2-binary pyyaml

# Copia tudo para o container
COPY . .

# Comando padrão
CMD ["python", "scanner.py", "--target", "app.py"]