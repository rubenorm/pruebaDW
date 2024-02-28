from flask import (
	Blueprint, flash, g, redirect, render_template, request, url_for, jsonify, session
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db
import json

bp = Blueprint('api', __name__)

@bp.route('/')
def index():
	if (session.get('user_id') is not None):
		vehiculos = get_for_id(str(session.get('user_id'))).data
		vehiculos = vehiculos.decode().replace("'", '"')
		vehiculos = json.loads(vehiculos)['datos']
		return render_template('api/index.html', vehiculos=vehiculos)
	else:
		return redirect(url_for('auth.login'))

@bp.route('/api/getAll', methods=['GET'])
def get_all():
	if (session.get('user_id') is not None):
		object_data = {'datos' : []}
		db = get_db()
		vehiculos = db.execute(
			'SELECT id, dueno, placas, lat, lon'
			' FROM vehiculo'
		).fetchall()
		for vehiculo in vehiculos:
			aux = {
				'id': vehiculo['id'],
				'dueno': vehiculo['dueno'],
				'placas': vehiculo['placas'],
				'lat': vehiculo['lat'],
				'lon': vehiculo['lon'],
				
			}
			object_data['datos'].append(aux)
		return jsonify(object_data)

@bp.route('/api/getForId/<id>', methods=['GET'])
def get_for_id(id):
	if (session.get('user_id') is not None):
		object_data = {'datos' : []}
		db = get_db()
		vehiculos = db.execute(
			'SELECT id, dueno, placas, lat, lon'
			' FROM vehiculo WHERE dueno='+id
		).fetchall()
		for vehiculo in vehiculos:
			aux = {
				'id': vehiculo['id'],
				'dueno': vehiculo['dueno'],
				'placas': vehiculo['placas'],
				'lat': vehiculo['lat'],
				'lon': vehiculo['lon'],
				
			}
			object_data['datos'].append(aux)
		return jsonify(object_data)
	
@bp.route('/api/insert/<id>', methods=['POST'])
def insert(id):
	if (session.get('user_id') is not None):
		db = get_db()
		vehiculos = db.execute(
			'INSERT INTO vehiculo (dueno, placas, lat, lon)'
			' VALUES (?, ?, ?, ?)',
			(request.form['dueno'], request.form['placas'], request.form['lat'], request.form['lon'])
		)
		db.commit()
		return jsonify({'status': 'Success'}), 200

@bp.route('/api/delete/<id>', methods=['POST'])
def delete(id):
	if (session.get('user_id') is not None):
		db = get_db()
		vehiculos = db.execute(
			'DELETE FROM vehiculo'
			' WHERE id='+id
		)
		db.commit()
		return jsonify({'status': 'Success'}), 200
	

@bp.route('/api/update/<id>', methods=['POST'])
def update(id):
	if (session.get('user_id') is not None):
		db = get_db()
		vehiculos = db.execute(
			'UPDATE vehiculo SET placas="?", lat=?, lon=?'
			' WHERE id=?',
			(request.form['placas'], request.form['lat'], request.form['lon'], id)
		)
		db.commit()
		return jsonify({'status': 'Success'}), 200
	
