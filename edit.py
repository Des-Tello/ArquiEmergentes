from db import get_db
from auth import verificacion_company, verificación_sensor



def modify_location(company_api_key, id, name, country, city, meta):
    db = get_db()
    cursor = db.cursor()
    query = "UPDATE LOCATION SET LOCATION_NAME = ?, LOCATION_COUNTRY = ?, LOCATION_CITY = ?, LOCATION_META = ? WHERE ID = ? AND COMPANY_ID = (SELECT ID FROM COMPANY WHERE COMPANY_API_KEY = ?)"
    result = cursor.execute(query, (name, country, city, meta, id, company_api_key))
    db.commit()

    if result.rowcount > 0:
        return True
    else:
        return False

def modify_sensor(company_api_key, id, name, category, meta):
    db = get_db()
    cursor = db.cursor()
    query = "UPDATE SENSOR SET SENSOR_NAME = ?, SENSOR_CATEGORY = ?, SENSOR_META = ? WHERE ID = ? AND LOCATION_ID = (SELECT LOCATION.ID FROM LOCATION, COMPANY WHERE LOCATION.COMPANY_ID = COMPANY.ID AND COMPANY.COMPANY_API_KEY = ?)"
    result = cursor.execute(query, (name, category, meta, id, company_api_key))
    db.commit()

    if result.rowcount > 0:
        return True
    else:
        return False

def modify_sensor_data(company_api_key, id, time, data):
    db = get_db()
    cursor = db.cursor()
    for variable in data:
        for llave, valor in variable.items():
            query = "UPDATE SENSOR_DATA SET TIME = ?, DATA = ?, VALUE = ? WHERE SENSOR_API_KEY = (SELECT SENSOR_DATA.SENSOR_API_KEY FROM SENSOR, LOCATION, COMPANY WHERE LOCATION.COMPANY_ID = COMPANY.ID AND SENSOR.LOCATION_ID = LOCATION.ID AND COMPANY.COMPANY_API_KEY = ?) AND ID = ?"
            result = cursor.execute(query, (time, llave, valor, company_api_key, id))
    db.commit()

    if result.rowcount > 0:
        return True
    else:
        return False