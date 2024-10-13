import urllib.request
import json

class Api_functions():
    def add_aud_sim(self,datos):
        url = f'{self.url}/add_audiometria'
        
        
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