from db import get_db
from auth import verificacion_company, verificación_sensor


def location_get_one(company_api_key, id):
    db = get_db()
    cursor = db.cursor()
    query = "SELECT LOCATION.ID, LOCATION.COMPANY_ID, LOCATION.LOCATION_NAME, LOCATION.LOCATION_COUNTRY, LOCATION.LOCATION_CITY, LOCATION.LOCATION_META, COMPANY.ID FROM COMPANY, LOCATION WHERE LOCATION.COMPANY_ID = COMPANY.ID AND COMPANY.COMPANY_API_KEY = ? AND LOCATION.ID = ?"
    result = cursor.execute(query, (company_api_key, id))

    return result

def sensor_get_one(company_api_key, id):
    db = get_db()
    cursor = db.cursor()
    query = "SELECT SENSOR.ID, SENSOR.LOCATION_ID, SENSOR.SENSOR_NAME, SENSOR.SENSOR_CATEGORY, SENSOR.SENSOR_META, COMPANY.ID, LOCATION.ID FROM COMPANY, LOCATION, SENSOR WHERE LOCATION.COMPANY_ID = COMPANY.ID AND SENSOR.LOCATION_ID = LOCATION.ID AND COMPANY.COMPANY_API_KEY = ? AND SENSOR.ID = ?"
    result = cursor.execute(query, (company_api_key, id))

    return result

def sensor_data_get_one(company_api_key, id):
    db = get_db()
    cursor = db.cursor()
    query = "SELECT SENSOR_DATA.TIME, SENSOR_DATA.DATA, SENSOR_DATA.VALUE, COMPANY.ID, LOCATION.ID, SENSOR.ID, SENSOR_DATA.ID FROM COMPANY, LOCATION, SENSOR, SENSOR_DATA WHERE SENSOR.SENSOR_API_KEY = SENSOR_DATA.SENSOR_API_KEY AND LOCATION.COMPANY_ID = COMPANY.ID AND SENSOR.LOCATION_ID = LOCATION.ID AND COMPANY.COMPANY_API_KEY = ? AND SENSOR_DATA.ID = ?"
    result = cursor.execute(query, (company_api_key, id))
    
    return result