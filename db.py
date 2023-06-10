import sqlite3
DATABASE_NAME = "tarea.db"

def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn

def create_tables():
    db = get_db()
    cursor = db.cursor()
    cursor.executescript(
    '''
        CREATE TABLE IF NOT EXISTS ADMIN(
            USERNAME TEXT PRIMARY KEY,
            PASSWORD TEXT
        );

        CREATE TABLE IF NOT EXISTS COMPANY(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            COMPANY_NAME TEXT,
            COMPANY_API_KEY TEXT
        );

        CREATE TABLE IF NOT EXISTS LOCATION(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            COMPANY_ID INTEGER,
            LOCATION_NAME TEXT,
            LOCATION_COUNTRY TEXT,
            LOCATION_CITY TEXT,
            LOCATION_META TEXT,
            FOREIGN KEY (COMPANY_ID) 
                REFERENCES COMPANY (ID) 
                    ON DELETE CASCADE 
                    ON UPDATE NO ACTION
        );

        CREATE TABLE IF NOT EXISTS SENSOR(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            LOCATION_ID INTEGER,
            SENSOR_NAME INTEGER,
            SENSOR_CATEGORY TEXT,
            SENSOR_META TEXT,
            SENSOR_API_KEY TEXT,
            FOREIGN KEY (LOCATION_ID) 
                REFERENCES LOCATION (ID) 
                    ON DELETE CASCADE 
                    ON UPDATE NO ACTION
        );

        CREATE TABLE IF NOT EXISTS SENSOR_DATA(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            SENSOR_API_KEY TEXT,
            TIME INTEGER,
            HUMIDITY REAL,
            TEMPERATURE REAL,
            DISTANCE REAL,
            PRESSURE REAL,
            LIGHT_LEVEL REAL,
            FOREIGN KEY (SENSOR_API_KEY) 
                REFERENCES SENSOR (SENSOR_API_KEY) 
                    ON DELETE CASCADE 
                    ON UPDATE NO ACTION
        );
    '''
    )
    db.commit()