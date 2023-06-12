from db import get_db
from auth import verificacion_company, verificación_sensor


def insert_sensor_data(sensor_api_key, time, data):
    db = get_db()
    cursor = db.cursor()
    try:
        for variable in data:
            for llave, valor in variable.items():
                query = "INSERT INTO SENSOR_DATA (SENSOR_API_KEY, TIME, DATA, VALUE) VALUES (?, ?, ?, ?)"
                cursor.execute(query, (sensor_api_key, time, llave, valor))
        db.commit()
        return True
    except Exception as e:
        print(f"Error al insertar datos del sensor: {e}")
        db.rollback()
        return False

def query_sensor_data(company_api_key, time_from, time_to, sensor_ids):
    db = get_db()
    cursor = db.cursor()
    # if not verificacion_company(company_api_key):
    #     return False
    data = []
    data_json = []
    for id in sensor_ids:
        query = "SELECT SENSOR_DATA.TIME, SENSOR_DATA.DATA, SENSOR_DATA.VALUE , COMPANY.ID, LOCATION.ID, SENSOR.ID FROM COMPANY, LOCATION, SENSOR, SENSOR_DATA WHERE SENSOR.SENSOR_API_KEY = SENSOR_DATA.SENSOR_API_KEY AND LOCATION.COMPANY_ID = COMPANY.ID AND SENSOR.LOCATION_ID = LOCATION.ID AND SENSOR.ID = ? AND SENSOR_DATA.TIME <= ? AND SENSOR_DATA.TIME >= ?"
        result = cursor.execute(query, (id, time_to, time_from))
        for row in result:
            data.append(row)
        json = {
            id: data
        }
        data_json.append(json)
    return data_json
