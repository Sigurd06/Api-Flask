from marshmallow import fields, validate
from marshmallow.decorators import pre_load
from app.ext import ma


fields.Field.default_error_messages['required'] = 'Este campo es requerido'

class AuthSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    username = fields.String(required=True, validate=validate.Length(min=4, max=25, error='Nombre de usuario fuera de rango'))
    password = fields.String(required=True, validate=validate.Length(min=4, error='La contraseña es muy corta'))

    # class Meta():
    #     fields = ('id', 'username')

auth_schema = AuthSchema()