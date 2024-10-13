import urllib.request
import json
import flet as ft
from  datetime import datetime
class Api_functions():
    def date(self):
        fecha_hora_actual = datetime.now()
        fecha_hora_formateada = fecha_hora_actual.strftime("%d-%m-%Y %H:%M:%S")
        return(str(fecha_hora_formateada))
    
    def add_aud_com(self,datos:list,id):
        url=f'{self.url}/add_audiometria_completa'
        db_max_right_8000=0
        db_max_left_8000=0
        db_max_right_10000=0
        db_max_left_10000=0
        db_max_right_12000=0
        db_max_left_12000=0
        db_max_right_15000=0
        db_max_left_15000=0
        db_max_right_16000=0
        db_max_left_16000=0
        db_max_right_17000=0
        db_max_left_17000=0
        db_max_right_18000=0
        db_max_left_18000=0
        db_max_right_19000=0
        db_max_left_19000=0
        db_max_right_20000=0
        db_max_left_20000=0
        for dat in datos:
            if 8000 == dat[0] and 1 == dat[2]:
                db_max_right_8000=dat[1]
            if 8000 == dat[0] and -1 == dat[2]:
                db_max_left_8000=dat[1]

            if 10000 == dat[0] and 1 == dat[2]:
                db_max_right_10000=dat[1]
            if 10000 == dat[0] and -1 == dat[2]:
                db_max_left_10000=dat[1]

            if 12000 == dat[0] and 1 == dat[2]:
                db_max_right_12000=dat[1]
            if 12000 == dat[0] and -1 == dat[2]:
                db_max_left_12000=dat[1]

            if 15000 == dat[0] and 1 == dat[2]:
                db_max_right_15000=dat[1]
            if 15000 == dat[0] and -1 == dat[2]:
                db_max_left_15000=dat[1]

            if 16000 == dat[0] and 1 == dat[2]:
                db_max_right_16000=dat[1]
            if 16000 == dat[0] and -1 == dat[2]:
                db_max_left_16000=dat[1]

            if 17000 == dat[0] and 1 == dat[2]:
                db_max_right_17000=dat[1]
            if 17000 == dat[0] and -1 == dat[2]:
                db_max_left_17000=dat[1]

            if 18000 == dat[0] and 1 == dat[2]:
                db_max_right_18000=dat[1]
            if 18000 == dat[0] and -1 == dat[2]:
                db_max_left_18000=dat[1]

            if 19000 == dat[0] and 1 == dat[2]:
                db_max_right_19000=dat[1]
            if 19000 == dat[0] and -1 == dat[2]:
                db_max_left_19000=dat[1]
            
            if 20000 == dat[0] and 1 == dat[2]:
                db_max_right_20000=dat[1]
            if 20000 == dat[0] and -1 == dat[2]:
                db_max_left_20000=dat[1]
        data={
            'Id_aud_comp':f"{id}-{self.date()}",
            'db_max_right_8000':db_max_right_8000,'db_max_left_8000':db_max_left_8000,
            'db_max_right_10000':db_max_right_10000,'db_max_left_10000':db_max_left_10000,
            'db_max_right_12000':db_max_right_12000,'db_max_left_12000':db_max_left_12000,
            'db_max_right_15000':db_max_right_15000,'db_max_left_15000':db_max_left_15000,
            'db_max_right_16000':db_max_right_16000,'db_max_left_16000':db_max_left_16000,
            'db_max_right_17000':db_max_right_17000,'db_max_left_17000':db_max_left_17000,
            'db_max_right_18000':db_max_right_18000,'db_max_left_18000':db_max_left_18000,
            'db_max_right_19000':db_max_right_19000,'db_max_left_19000':db_max_left_19000,
            'db_max_right_20000':db_max_right_20000,'db_max_left_20000':db_max_left_20000
        }
        json_data = json.dumps(data).encode('utf-8')

        # Crear la solicitud POST con encabezado de JSON
        req = urllib.request.Request(
            url,
            data=json_data,
            headers={
                'Content-Type': 'application/json'
            },
            method='POST'
        )

        # Enviar la solicitud y manejar la respuesta
        try:
            with urllib.request.urlopen(req) as response:
                response_data = response.read().decode('utf-8')
                print("Respuesta del servidor:", response_data)
                return response_data
        except urllib.error.HTTPError as e:
            print(f"Error al enviar la solicitud: {e}")
            return None
        except :
            print(f"Error al enviar la solicitud:")
    def add_aud_sim(self,datos:list,id):
        url = f'{self.url}/add_audiometria'
        db_max_8000 = 0
        db_max_10000 = 0
        db_max_12000 = 0
        db_max_15000 = 0
        db_max_16000 = 0
        db_max_17000 = 0
        db_max_18000 = 0
        db_max_19000 = 0
        db_max_20000 = 0

        for dat in datos:
            if 8000 == dat[0]:
                db_max_8000=dat[1]
            if 10000 == dat[0]:
                db_max_10000=dat[1]
            if 12000 == dat[0]:
                db_max_12000=dat[1]
            if 15000 == dat[0]:
                db_max_15000=dat[1]
            if 16000 == dat[0]:
                db_max_16000=dat[1]
            if 17000 == dat[0]:
                db_max_17000=dat[1]
            if 18000 == dat[0]:
                db_max_18000=dat[1]
            if 19000 == dat[0]:
                db_max_19000=dat[1]
            if 20000 == dat[0]:
                db_max_20000=dat[1]
            #if dat[0]==8000:
        data = {
            'Id_aud_simp':f"{id}-{self.date()}"
            ,'db_max_8000':db_max_8000,'db_max_10000':db_max_10000,'db_max_12000':db_max_12000,'db_max_15000':db_max_15000,'db_max_16000':db_max_16000,'db_max_17000':db_max_17000,'db_max_18000':db_max_18000,'db_max_19000':db_max_19000,'db_max_20000':db_max_20000
        }
        # Convertir los datos en JSON
        json_data = json.dumps(data).encode('utf-8')

        # Crear la solicitud POST con encabezado de JSON
        req = urllib.request.Request(
            url,
            data=json_data,
            headers={
                'Content-Type': 'application/json'
            },
            method='POST'
        )

        # Enviar la solicitud y manejar la respuesta
        try:
            with urllib.request.urlopen(req) as response:
                response_data = response.read().decode('utf-8')
                print("Respuesta del servidor:", response_data)
                return response_data
        except urllib.error.HTTPError as e:
            print(f"Error al enviar la solicitud: {e}")
            return None
        except :
            print(f"Error al enviar la solicitud:")
                    
    def add_user(self, id, name, email, date, gender, occupation):
        # Crear la URL de la API (suponiendo que es la ruta /add_user)
        url = f'{self.url}/add_user'

        # Los datos del usuario que queremos enviar
        data = {
            "id": id,
            "name": name,
            "email": email,
            "date": date,
            "gender": gender,
            "occupation": occupation
        }

        # Convertir los datos en JSON
        json_data = json.dumps(data).encode('utf-8')

        # Crear la solicitud POST con encabezado de JSON
        req = urllib.request.Request(
            url,
            data=json_data,
            headers={
                'Content-Type': 'application/json'
            },
            method='POST'
        )

        # Enviar la solicitud y manejar la respuesta
        try:
            with urllib.request.urlopen(req) as response:
                response_data = response.read().decode('utf-8')
                print("Respuesta del servidor:", response_data)
                return response_data
        except urllib.error.HTTPError as e:
            print(f"Error al enviar la solicitud: {e}")
            return None
        except :
            print(f"Error al enviar la solicitud:")
            
            
    def __init__(self) -> None:
        self.url="http://127.0.0.1:5000/"