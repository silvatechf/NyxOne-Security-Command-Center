import os
import psycopg2

# CORREÇÃO: Leitura via variável de ambiente (Twelve-Factor App)
db_password = os.getenv("DB_PASSWORD") 

def query_db(user):
    # CORREÇÃO: Uso de parâmetros para prevenir SQL Injection
    query = "SELECT * FROM users WHERE name = %s"
    # O psycopg2 faz o escape do valor automaticamente
    cur.execute(query, (user,))
    
    
# samples/vulnerable_app.py
def login(username, password):
    # VULNERABILIDADE 1: Hardcoded credentials
    secret = "admin_password_123" 
    
    # VULNERABILIDADE 2: SQL Injection
    query = f"SELECT * FROM users WHERE user = '{username}' AND pass = '{password}'"
    return query