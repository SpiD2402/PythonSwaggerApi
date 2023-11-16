from app import api
from flask_restx import Resource
from app.controllers.roles_controller import RolesController
from app.schemas.roles_schemas import RolesRequestSchema
from flask import request
from flask_jwt_extended import jwt_required

role_ns=api.namespace(
    
    name="Roles",
    description="Rutas del modeo de Roles",
    path='/roles'
)

request_schema = RolesRequestSchema(role_ns)

@role_ns.route('')
@role_ns.doc(security='Bearer')
class Roles(Resource):
    
    @jwt_required()
    @role_ns.expect(request_schema.all())
    def get(self):
        '''Listar Roles'''
        query= request_schema.all().parse_args()
        controller= RolesController()
        return controller.all(query)
    @jwt_required()
    @role_ns.expect(request_schema.create(),validate=True)
    def post(self):
        '''Agregar Roles'''
        controller = RolesController()
        return controller.create(request.json)

@role_ns.route('/<int:id>')
@role_ns.doc(security='Bearer')
class RolesById(Resource):
    @jwt_required() 
    def get(self,id):
        '''Buscar Roles por Id'''
        controller = RolesController()
        return controller.getById(id)
        
    @jwt_required()
    @role_ns.expect(request_schema.update(),validate=True)
    def put(self,id):
        '''Actualizar Rol'''
        controller = RolesController()
        return controller.update(id,request.json)
    
    @jwt_required()
    def delete(self,id):
        '''Deshabilidar Rol por Id'''
        controller = RolesController()
        return controller.delete(id)


