from flask import (Blueprint , request, redirect)
from ballpython import models
import sys

bp = Blueprint('reptile', __name__, url_prefix='/reptiles')

@bp.route('/', methods=['GET', 'POST'])
def index():
    #POST Handling
    
    if request.method == 'POST':
        print(request)
        new_reptile = models.Reptile(
            common_name = request.form['common_name'],
            scientific_name = request.form['scientific_name'],
            conservation_status = request.form['conservation_status'],
            native_habitat = request.form['native_habitat'],
            fun_fact = request.form['fun_fact']
        )

        #add to database
        models.db.session.add(new_reptile)
        models.db.session.commit()

        return redirect('/reptiles')
    
    #GET Handling
    found_reptiles = models.Reptile.query.all()

    reptile_dict = {'reptiles': []}

    for reptile in found_reptiles:
        reptile_dict["reptiles"].append({
            'common_name': reptile.common_name,
            'scientific_name' : reptile.scientific_name,
            'conservation_status' : reptile.conservation_status,
            'native_habitat' : reptile.native_habitat,
            'fun_fact': reptile.native_habitat
        })
    
    return reptile_dict



@bp.route('/<int:id>')
def show(id):
    reptile = models.Reptile .query.filter_by(id=id).first()

    reptile_dict = {
        'common_name': reptile.common_name,
        'scientific-name' : reptile.scientific_name,
        'conservation_status' : reptile.conservation_status,
        'native_habitat' : reptile.native_habitat,
        'fun_fact' : reptile.fun_fact
    }

    return reptile_dict