import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# Crear el objeto de la familia Jackson
jackson_family = FamilyStructure("Jackson")

# Manejador de errores
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# Generar sitemap
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# Endpoint 1: Obtener todos los miembros de la familia
@app.route('/members', methods=['GET'])
def get_all_members():
    members = jackson_family.get_all_members()
    return jsonify(members), 200

# Endpoint 2: Obtener un miembro específico por su ID
@app.route('/member/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = jackson_family.get_member(member_id)
    if member:
        return jsonify(member), 200
    else:
        return jsonify({"error": "Member not found"}), 404

# Endpoint 3: Agregar un nuevo miembro
@app.route('/member', methods=['POST'])
def add_member():
    new_member = request.get_json()
    if not new_member:
        return jsonify({"error": "Invalid input"}), 400
    jackson_family.add_member(new_member)
    return jsonify({"message": "Member added successfully"}), 200

# Endpoint 4: Eliminar un miembro por su ID
@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    if jackson_family.delete_member(member_id):
        return jsonify({"done": True}), 200
    else:
        return jsonify({"error": "Member not found"}), 404

# Endpoint 5: Actualizar un miembro por su ID
@app.route('/member/<int:member_id>', methods=['PUT'])
def update_member(member_id):
    updated_member = request.get_json()
    if not updated_member:
        return jsonify({"error": "Invalid input"}), 400
    if jackson_family.update_member(member_id, updated_member):
        return jsonify({"message": "Member updated successfully"}), 200
    else:
        return jsonify({"error": "Member not found"}), 404

# Iniciar el servidor Flask
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)