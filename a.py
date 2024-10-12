from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista para simular una base de datos en memoria
usuarios = []

# Método para añadir un nuevo usuario
def add_user(id, name, email, date, gender, ocupation):
    # Crear un diccionario con los datos del usuario
    nuevo_usuario = {
        'id': id,
        'name': name,
        'email': email,
        'date': date,
        'gender': gender,
        'ocupation': ocupation
    }
    
    # Añadir el usuario a la lista (simulando el guardado en una base de datos)
    usuarios.append(nuevo_usuario)
    
    return {'message': f'Usuario {name} agregado con éxito'}, 201

# Ruta para manejar la solicitud POST y llamar a add_user
@app.route('/add_user', methods=['POST'])
def api_add_user():
    # Verificar si los datos llegan en formato JSON
    if request.is_json:
        data = request.json
        id_un = data.get('id')
        name = data.get('name')
        email = data.get('email')
        date = data.get('date')
        gender = data.get('gender')
        ocupation = data.get('occupation')

        # Llamar al método add_user con los parámetros proporcionados
        result = add_user(id=id_un, name=name, email=email, date=date, gender=gender, ocupation=ocupation)
        return jsonify(result)
    else:
        return jsonify({'error': 'La solicitud no contiene JSON válido'}), 400

if __name__ == '__main__':
    app.run(debug=True)
