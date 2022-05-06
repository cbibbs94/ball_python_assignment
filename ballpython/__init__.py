from flask import Flask
from flask_migrate import Migrate

# The Factory
def create_app():
    app = Flask(__name__)

    #postgres connection
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Kyuubichan15!@localhost:5432/ballpy'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    #models middleware??    
    from . import models
    models.db.init_app(app)

    #index route
    @app.route('/')
    def hello():
        return 'You are connected buddy!'

    #Register blueprint
    from . import reptile
    app.register_blueprint(reptile.bp)
    migrate = Migrate(app, models.db)


    return app    