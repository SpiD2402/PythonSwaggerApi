from app import api 
from flask_restx import Resource
from app.schemas.auth_schemas import AuthRequestSchema
from app.controllers.auth_controller import AuthController
from flask_jwt_extended import jwt_required
from flask import request


auth_ns = api.namespace(
    
    name ='Autenticacion',
    description ='Rutas del modulo Autenticacion',
    path='/auth'
)

request_schema =AuthRequestSchema(auth_ns)


@auth_ns.route('/signin')
class SignIn(Resource):
    
    @auth_ns.expect(request_schema.signin(),validate=True)
    def post(self):
        ''''Login de Usuario '''
        controller = AuthController()
        return controller.signIn(request.json)
        


@auth_ns.route('/signup')
class SingUp(Resource):
    @auth_ns.expect(request_schema.signup(),validate=True)
    def post(self):
        '''Registro de Usuarios'''
        
        controller =  AuthController()
        return controller.singUp(request.json)
         