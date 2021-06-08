from flask_restful import Api
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

api = Api()
ma = Marshmallow()
migrate = Migrate()