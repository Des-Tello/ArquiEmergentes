from flask import Flask, jsonify, request
import sensordata, admin, delete, edit, get_all, get_one, auth
from db import create_tables

app = Flask(__name__)
# ADMIN
@app.route('/api/v1/create_company', methods = ["POST"])
def create_company():
    req = request.get_json()
    cred = request.headers['credential'].split('-')
    user = cred[0]
    password = cred[1]
    if auth.valida_admin(user, password):
        try:
            admin.create_company(req['company_name'], req['company_api_key'])
            response = {
                "response": "Compañia creada exitosamente!"
            }
        except:
            response = {
                "response": "Hubo un error al crear la compañia"
            }
    else:
        response = {
            "response": "Credenciales no validas"
        }        
    return jsonify(response)
    
@app.route('/api/v1/create_location', methods = ["POST"])
def create_location():
    req = request.get_json()
    cred = request.headers['credential'].split('-')
    user = cred[0]
    password = cred[1]
    if auth.valida_admin(user, password):
        try:
            if admin.create_location(req['company_id'], req['location_name'], req['location_county'], req['location_city'], req['location_meta']):
                response = {
                        "response": "Localidad creada exitosamente!"
                    }
            else:
                response = {
                    "response": "Company_id no encontrado"
                }                
        except Exception as e:
            # print(f"Ocurrió un error: {str(e)}")
            response = {
                "response": "Hubo un error al crear la localidad"
            }
    else:
        response = {
            "response": "Credenciales no validas"
        } 
    return jsonify(response)

@app.route('/api/v1/create_sensor', methods = ["POST"])
def create_sensor():
    req = request.get_json()
    cred = request.headers['credential'].split('-')
    user = cred[0]
    password = cred[1]
    if auth.valida_admin(user, password):
        if admin.create_sensor(req['location_id'], req['sensor_name'], req['sensor_category'], req['sensor_meta'], req['sensor_api_key']):
            response = {
                "response": "Sensor creado exitosamente!"
            }
        else:
            response = {
                "response": "location_id no encontrada"
            }
    else:
        response = {
            "response": "Credenciales no validas"
        } 
    return jsonify(response)
# FIN ADMIN

# MUESTRA TODO
@app.route('/api/v1/muestra_todo', methods = ["GET"])
def muestra_todo():
    req = request.get_json()
    response = {}
    location = []
    sensor = []
    sensor_data = []
    for row in get_all.location_get_all(req['company_api_key']):
        location.append(row)
    response['location'] = location
    for row in get_all.sensor_get_all(req['company_api_key']):
        sensor.append(row)
    response['sensor'] = sensor
    for row in get_all.sensor_data_get_all(req['company_api_key']):
        sensor_data.append(row)
    response['sensor_data'] = sensor_data

    return jsonify(response)

# MUESTRA UNO
@app.route('/api/v1/location_muestra_uno', methods = ["GET"])
def location_muestra_uno():
    req = request.get_json()
    data = False
    location = []
    for row in get_one.location_get_one(req['company_api_key'], req['id']):
        data = True
        location.append(row)

    if (data):
        response = {
                "locations": location
        }
    else:
        response = {
                "response": "No hay datos para mostrar"
        }
    return jsonify(response)

@app.route('/api/v1/sensor_muestra_uno', methods = ["GET"])
def sensor_muestra_uno():
    req = request.get_json()
    data = False
    sensor = []
    for row in get_one.sensor_get_one(req['company_api_key'], req['id']):
        sensor.append(row)
        data = True

    if (data):
        response = {
                "sensors": sensor
        }
    else:
        response = {
                "response": "No hay datos para mostrar"
        }
    return jsonify(response)

@app.route('/api/v1/sensordata_muestra_uno', methods = ["GET"])
def sensordata_muestra_uno():
    req = request.get_json()
    data = False
    sensor_data = []
    for row in get_one.sensor_data_get_one(req['company_api_key'], req['id']):
        sensor_data.append(row)
        data = True
    if (data):
        response = {
                "sensors_data": sensor_data
        }
    else:
        response = {
                "response": "No hay datos para mostrar"
        }
    return jsonify(response)

# EDITA
@app.route('/api/v1/edita_location', methods=['PUT'])
def edita_location():
    req = request.get_json()
    if edit.modify_location(req['company_api_key'], req['id'], req['name'], req['country'], req['city'], req['meta']):
        response = {
                "response": "Location editada correctamente"
        }
    else:
        response = {
                "response": "Problemas en la edicion de location"
        }
    return jsonify(response)

@app.route('/api/v1/edita_sensor', methods=['PUT'])
def edita_sensor():
    req = request.get_json()
    if edit.modify_sensor(req['company_api_key'], req['id'], req['name'], req['category'], req['meta']):
        response = {
                "response": "Sensor editado correctamente"
        }
    else:
        response = {
                "response": "Problemas en la edicion del sensor"
        }
    return jsonify(response)

@app.route('/api/v1/edita_sensor_data', methods=['PUT'])
def edita_sensor_data():
    req = request.get_json()
    if edit.modify_sensor_data(req['company_api_key'], req['id'], req['time'], req['data']):
        response = {
                "response": "Sensor data editada correctamente"
        }
    else:
        response = {
                "response": "Problemas en la edicion del sensor data"
        }
    return jsonify(response)

# DELETE
@app.route('/api/v1/delete_location', methods=['DELETE'])
def delete_location():
    req = request.get_json()
    if delete.delete_location(req['company_api_key'], req['id']):
        response = {
                "response": "Location eliminada correctamente"
        }       
    else:
        response = {
                "response": "Problemas en la eliminación de la location"
        }
    return jsonify(response)

@app.route('/api/v1/delete_sensor', methods=['DELETE'])
def delete_sensor():
    req = request.get_json()
    if delete.delete_sensor(req['company_api_key'], req['id']):
        response = {
                "response": "Sensor eliminada correctamente"
        }       
    else:
        response = {
                "response": "Problemas en la eliminación del sensor"
        }
    return jsonify(response)

@app.route('/api/v1/delete_sensor_data', methods=['DELETE'])
def delete_sensor_data():
    req = request.get_json()
    if delete.delete_sensor_data(req['company_api_key'], req['id']):
        response = {
                "response": "Sensor data eliminada correctamente"
        }       
    else:
        response = {
                "response": "Problemas en la eliminación de la sensor data"
        }
    return jsonify(response)

# INSERCION SENSOR DATA
@app.route('/api/v1/sensor_data', methods = ['POST'])
def insert_sensor_data():
    req = request.get_json()
    if auth.verificación_sensor(req['sensor_api_key']):
        if sensordata.insert_sensor_data(req['sensor_api_key'], req['time'], req['data']):
            response = {
                "response": "Sensor data insertada correctamente"
            }  
        else:
            response = {
                "response": "Error al insertar sensor data"
            }
    else: 
        response = {
                "response": "Sensor_api_key invalido"
            }
    return jsonify(response)

# CONSULTA SENSOR DATA
@app.route('/api/v1/sensor_data', methods = ['GET'])
def get_sensor_data():
    req = request.get_json()
    cred = request.headers['credential'].split('-')
    user = cred[0]
    password = cred[1]
    response = sensordata.query_sensor_data(req['company_api_key'], req['time_from'], req['time_to'], req['sensor_ids'])
    if auth.valida_admin(user, password):
        if response:
            response = {
                "Sensor_Data": response
            }  
        else:
            response = {
                "response": "Error al obtener sensor data"
            }   
    else:
        response = {
            "response": "Credenciales no validas"
        }      
    return jsonify(response)


if __name__ == "__main__":
    create_tables()
    app.run(host = '0.0.0.0', port = 8000, debug = True)