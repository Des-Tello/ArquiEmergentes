from db import get_db

def verificacion(company_api_key):
    db = get_db()
    cursor = db.cursor()
    query = "SELECT COUNT(*) FROM company WHERE company_api_key = ?"
    cursor.execute(query, (company_api_key,))
    resultado = cursor.fetchone()[0]
    cursor.close()
    return resultado > 0

def location_get_all(company_api_key):
    db = get_db()
    cursor = db.cursor()
    query = "SELECT LOCATION.ID, LOCATION.COMPANY_ID, LOCATION.LOCATION_NAME, LOCATION.LOCATION_COUNTRY, LOCATION.LOCATION_CITY, LOCATION.LOCATION_META, COMPANY.ID FROM COMPANY, LOCATION WHERE LOCATION.COMPANY_ID = COMPANY.ID AND COMPANY.COMPANY_API_KEY = ?"
    result = cursor.execute(query, (company_api_key,))

    return result

def sensor_get_all(company_api_key):
    db = get_db()
    cursor = db.cursor()
    query = "SELECT SENSOR.ID, SENSOR.LOCATION_ID, SENSOR.SENSOR_NAME, SENSOR.SENSOR_CATEGORY, SENSOR.SENSOR_META, COMPANY.ID, LOCATION.ID FROM COMPANY, LOCATION, SENSOR WHERE LOCATION.COMPANY_ID = COMPANY.ID AND SENSOR.LOCATION_ID = LOCATION.ID AND COMPANY.COMPANY_API_KEY = ?"
    result = cursor.execute(query, (company_api_key,))

    return result

def sensor_data_get_all(company_api_key):
    db = get_db()
    cursor = db.cursor()
    query = "SELECT SENSOR_DATA.TIME, SENSOR_DATA.HUMIDITY, SENSOR_DATA.TEMPERATURE, SENSOR_DATA.DISTANCE, SENSOR_DATA.PRESSURE, SENSOR_DATA.LIGHT_LEVEL, COMPANY.ID, LOCATION.ID, SENSOR.ID FROM COMPANY, LOCATION, SENSOR, SENSOR_DATA WHERE SENSOR.SENSOR_API_KEY = SENSOR_DATA.SENSOR_API_KEY AND LOCATION.COMPANY_ID = COMPANY.ID AND SENSOR.LOCATION_ID = LOCATION.ID AND COMPANY.COMPANY_API_KEY = ?"
    result = cursor.execute(query, (company_api_key,))


    return result