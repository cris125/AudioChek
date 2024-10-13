# main.py
from flask import Flask, jsonify, request
from config import Config
from models import db, Usuario ,AudiometriaSimple ,AudiometriaCompleta

app = Flask(__name__)

# Cargar la configuración desde config.py
app.config.from_object(Config)

# Inicializar la base de datos con la configuración de la app
db.init_app(app)

# Crear una ruta para agregar o actualizar un usuario
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    
    # Verificar si el usuario con el ID proporcionado ya existe
    usuario_existente = Usuario.query.filter_by(id=data['id']).first()

    if usuario_existente:
        # Si el usuario ya existe, actualizar sus valores
        usuario_existente.name = data['name']
        usuario_existente.email = data['email']
        usuario_existente.date = data['date']         # Fecha en formato VARCHAR
        usuario_existente.gender = data['gender']
        usuario_existente.occupation = data['occupation']

        db.session.commit()  # Guardar los cambios en la base de datos
        return jsonify({"message": f"Usuario {usuario_existente.name} actualizado exitosamente"}), 200
    else:
        # Si no existe, crear un nuevo usuario
        nuevo_usuario = Usuario(
            id=data['id'],  # Hash proporcionado en la solicitud
            name=data['name'],
            email=data['email'],
            date=data['date'],  # Fecha en formato VARCHAR
            gender=data['gender'],
            occupation=data['occupation']
        )

        # Añadir el nuevo usuario a la base de datos
        db.session.add(nuevo_usuario)
        db.session.commit()

        return jsonify({"message": f"Usuario {nuevo_usuario.name} agregado exitosamente"}), 201

# Crear una ruta para obtener todos los usuarios
@app.route('/get_users', methods=['GET'])
def get_users():
    usuarios = Usuario.query.all()
    usuarios_data = [
        {
            "id": usuario.id,
            "name": usuario.name,
            "email": usuario.email,
            "date": usuario.date,
            "gender": usuario.gender,
            "occupation": usuario.occupation
        } for usuario in usuarios
    ]
    return jsonify(usuarios_data), 200


@app.route('/add_audiometria', methods=['POST'])
def add_audiometria():
    data = request.get_json()

    # Verificar si ya existe un registro con el mismo Id_aud_simp
    audiometria_existente = AudiometriaSimple.query.filter_by(Id_aud_simp=data['Id_aud_simp']).first()

    if audiometria_existente:
        return jsonify({"message": "El registro ya existe. No se ha realizado ninguna modificación."}), 400
    else:
        # Crear una nueva instancia del modelo AudiometriaSimple con los datos proporcionados
        nueva_audiometria = AudiometriaSimple(
            Id_aud_simp=data['Id_aud_simp'],
            db_max_8000=data.get('db_max_8000'),
            db_max_10000=data.get('db_max_10000'),
            db_max_12000=data.get('db_max_12000'),
            db_max_15000=data.get('db_max_15000'),
            db_max_16000=data.get('db_max_16000'),
            db_max_17000=data.get('db_max_17000'),
            db_max_18000=data.get('db_max_18000'),
            db_max_19000=data.get('db_max_19000'),
            db_max_20000=data.get('db_max_20000')
        )

        # Añadir el nuevo registro a la base de datos
        db.session.add(nueva_audiometria)
        db.session.commit()

        return jsonify({"message": "Registro agregado exitosamente"}), 201

# Ruta para obtener todos los registros de la tabla audiometria_simple
@app.route('/get_audiometria', methods=['GET'])
def get_audiometria():
    audiometrias = AudiometriaSimple.query.all()

    # Crear una lista con los datos de cada registro
    audiometria_data = [
        {
            "Id_aud_simp": audiometria.Id_aud_simp,
            "db_max_8000": audiometria.db_max_8000,
            "db_max_10000": audiometria.db_max_10000,
            "db_max_12000": audiometria.db_max_12000,
            "db_max_15000": audiometria.db_max_15000,
            "db_max_16000": audiometria.db_max_16000,
            "db_max_17000": audiometria.db_max_17000,
            "db_max_18000": audiometria.db_max_18000,
            "db_max_19000": audiometria.db_max_19000,
            "db_max_20000": audiometria.db_max_20000
        } for audiometria in audiometrias
    ]

    return jsonify(audiometria_data), 200

# Ruta para agregar un nuevo registro en la tabla audimetria_completa
@app.route('/add_audiometria_completa', methods=['POST'])
def add_audiometria_completa():
    data = request.get_json()

    # Verificar si ya existe un registro con el mismo Id_aud_simp
    audiometria_existente = AudiometriaCompleta.query.filter_by(Id_aud_simp=data['Id_aud_simp']).first()

    if audiometria_existente:
        return jsonify({"message": "El registro ya existe. No se ha realizado ninguna modificación."}), 400
    else:
        # Crear una nueva instancia del modelo AudiometriaCompleta con los datos proporcionados
        nueva_audiometria = AudiometriaCompleta(
            Id_aud_simp=data['Id_aud_simp'],
            db_max_right_8000=data.get('db_max_right_8000'),
            db_max_left_8000=data.get('db_max_left_8000'),
            db_max_right_10000=data.get('db_max_right_10000'),
            db_max_left_10000=data.get('db_max_left_10000'),
            db_max_right_12000=data.get('db_max_right_12000'),
            db_max_left_12000=data.get('db_max_left_12000'),
            db_max_right_15000=data.get('db_max_right_15000'),
            db_max_left_15000=data.get('db_max_left_15000'),
            db_max_right_16000=data.get('db_max_right_16000'),
            db_max_left_16000=data.get('db_max_left_16000'),
            db_max_right_17000=data.get('db_max_right_17000'),
            db_max_left_17000=data.get('db_max_left_17000'),
            db_max_right_18000=data.get('db_max_right_18000'),
            db_max_left_18000=data.get('db_max_left_18000'),
            db_max_right_19000=data.get('db_max_right_19000'),
            db_max_left_19000=data.get('db_max_left_19000'),
            db_max_right_20000=data.get('db_max_right_20000'),
            db_max_left_20000=data.get('db_max_left_20000')
        )

        # Añadir el nuevo registro a la base de datos
        db.session.add(nueva_audiometria)
        db.session.commit()

        return jsonify({"message": "Registro agregado exitosamente"}), 201

# Ruta para obtener todos los registros de la tabla audimetria_completa
@app.route('/get_audiometria_completa', methods=['GET'])
def get_audiometria_completa():
    audiometrias = AudiometriaCompleta.query.all()

    # Crear una lista con los datos de cada registro
    audiometria_data = [
        {
            "Id_aud_simp": audiometria.Id_aud_simp,
            "db_max_right_8000": audiometria.db_max_right_8000,
            "db_max_left_8000": audiometria.db_max_left_8000,
            "db_max_right_10000": audiometria.db_max_right_10000,
            "db_max_left_10000": audiometria.db_max_left_10000,
            "db_max_right_12000": audiometria.db_max_right_12000,
            "db_max_left_12000": audiometria.db_max_left_12000,
            "db_max_right_15000": audiometria.db_max_right_15000,
            "db_max_left_15000": audiometria.db_max_left_15000,
            "db_max_right_16000": audiometria.db_max_right_16000,
            "db_max_left_16000": audiometria.db_max_left_16000,
            "db_max_right_17000": audiometria.db_max_right_17000,
            "db_max_left_17000": audiometria.db_max_left_17000,
            "db_max_right_18000": audiometria.db_max_right_18000,
            "db_max_left_18000": audiometria.db_max_left_18000,
            "db_max_right_19000": audiometria.db_max_right_19000,
            "db_max_left_19000": audiometria.db_max_left_19000,
            "db_max_right_20000": audiometria.db_max_right_20000,
            "db_max_left_20000": audiometria.db_max_left_20000
        } for audiometria in audiometrias
    ]

    return jsonify(audiometria_data), 200


# Ejecutar la aplicación
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Crear las tablas si no existen
    app.run(debug=True)
