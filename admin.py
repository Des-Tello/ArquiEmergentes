from db import get_db
import secrets
from auth import valida_admin

    
def create_company(company_name, company_api_key):
    db = get_db()
    cursor = db.cursor()
    query = "INSERT INTO COMPANY (COMPANY_NAME, COMPANY_API_KEY) VALUES (?, ?)"
    cursor.execute(query, (company_name, company_api_key))
    db.commit()
    return True

def create_location(company_id, location_name, location_country, location_city, location_meta):
    db = get_db()
    cursor = db.cursor()
    query_validate_company = "SELECT * FROM COMPANY WHERE ID = ?"
    cursor.execute(query_validate_company, (company_id,))
    rows = cursor.fetchone()
    if rows is None:
        return False

    query = "INSERT INTO LOCATION (COMPANY_ID, LOCATION_NAME, LOCATION_COUNTRY, LOCATION_CITY, LOCATION_META) VALUES (?, ?, ?, ?, ?)"
    cursor.execute(query, (company_id, location_name, location_country, location_city, location_meta))
    db.commit()
    return True

def create_sensor(location_id, sensor_name, sensor_category, sensor_meta, sensor_api_key):
    db = get_db()
    cursor = db.cursor()
    query_validate_location = "SELECT * FROM LOCATION WHERE ID = ?"
    cursor.execute(query_validate_location, (location_id,))
    rows = cursor.fetchone()
    if rows is None:
        return False
    
    query = "INSERT INTO SENSOR (LOCATION_ID, SENSOR_NAME, SENSOR_CATEGORY, SENSOR_META, SENSOR_API_KEY) VALUES (?, ?, ?, ?, ?)"
    cursor.execute(query, (location_id, sensor_name, sensor_category, sensor_meta, sensor_api_key))

    db.commit()

    return True