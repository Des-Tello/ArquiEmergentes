from db import get_db
from auth import verificacion_company, verificación_sensor


def delete_location(company_api_key, id):
    db = get_db()
    cursor = db.cursor()
    query = "DELETE FROM LOCATION WHERE LOCATION.ID IN (SELECT LOCATION.ID FROM COMPANY, LOCATION WHERE LOCATION.ID = ? AND LOCATION.COMPANY_ID = COMPANY.ID AND COMPANY.COMPANY_API_KEY = ?)"
    result = cursor.execute(query, (id, company_api_key))
    
    db.commit()

    if result.rowcount > 0:
        return True
    else:
        return False

def delete_sensor(company_api_key, id):
    db = get_db()
    cursor = db.cursor()
    query = "DELETE FROM SENSOR WHERE SENSOR.ID IN (SELECT SENSOR.ID FROM COMPANY, LOCATION, SENSOR WHERE LOCATION.COMPANY_ID = COMPANY.ID AND SENSOR.LOCATION_ID = LOCATION.ID AND COMPANY.COMPANY_API_KEY = ? AND SENSOR.ID = ?)"
    result = cursor.execute(query, (company_api_key, id))

    db.commit()

    if result.rowcount > 0:
        return True
    else:
        return False

def delete_sensor_data(company_api_key, id):
    db = get_db()
    cursor = db.cursor()
    query = "DELETE FROM SENSOR_DATA WHERE SENSOR_DATA.ID IN (SELECT SENSOR_DATA.ID FROM COMPANY, LOCATION, SENSOR, SENSOR_DATA WHERE LOCATION.COMPANY_ID = COMPANY.ID AND SENSOR.LOCATION_ID = LOCATION.ID AND SENSOR_DATA.SENSOR_API_KEY = SENSOR.SENSOR_API_KEY AND COMPANY.COMPANY_API_KEY = ? AND SENSOR_DATA.ID = ?)"
    result = cursor.execute(query, (company_api_key, id))

    db.commit()

    if result.rowcount > 0:
        return True
    else:
        return False