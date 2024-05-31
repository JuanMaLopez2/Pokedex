from flask import Blueprint, jsonify, render_template
import random
from .models import pokeneas

bp = Blueprint('routes', __name__)

@bp.route('/pokeneas/json', methods=['GET'])
def get_pokeneas_json():
    pokenea = random.choice(pokeneas)
    response = {
        'id': pokenea['id'],
        'nombre': pokenea['nombre'],
        'altura': pokenea['altura'],
        'habilidad': pokenea['habilidad'],
        'json_id': id(bp)
    }
    return jsonify(response)

@bp.route('/pokeneas/display', methods=['GET'])
def display_pokenea():
    pokenea = random.choice(pokeneas)
    return render_template('index.html', pokenea=pokenea, json_id=id(bp))