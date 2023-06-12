from db import get_db

def verificacion_company(company_api_key):
    db = get_db()
    cursor = db.cursor()
    query = "SELECT COUNT(*) FROM company WHERE company_api_key = ?"
    cursor.execute(query, (company_api_key,))
    resultado = cursor.fetchone()[0]
    cursor.close()
    return resultado > 0

def verificación_sensor(sensor_api_key):
    db = get_db()
    cursor = db.cursor()
    query = "SELECT COUNT(*) FROM Sensor WHERE SENSOR_API_KEY = ?"
    cursor.execute(query, (sensor_api_key,))
    count = cursor.fetchone()[0]
    cursor.close()
    return count > 0
        

def valida_admin(user, password):
    db = get_db()
    cursor = db.cursor()
    query = f"SELECT * FROM ADMIN WHERE username = ? AND password = ?"
    cursor.execute(query, (user, password))
    resultado = cursor.fetchone()
    if resultado:
        return True
    else:
        return False