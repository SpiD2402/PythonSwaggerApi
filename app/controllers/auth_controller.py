from app.models.users_model import UserModel
from app import db
from flask_jwt_extended import create_access_token,create_refresh_token


class AuthController:
    def __init__(self) -> None:
        self.model = UserModel()
        self.rol_id= 2
        
        
    def signIn(self,data):
        try:
            username = data['username']
            password=data['password']
            
            #1 Validar que el usuario exista y  no este inhabilitado
            record=self.model.where(username=username,status=True).first()
            if record:
                #Validar la contraasea sea correcta
                if record.checkPassword(password):
                    
                    #Creacion de JWT (Access Token y Refresh Token)
                    user_id=record.id
                    access_token=create_access_token(identity=user_id)
                    refresh_token=create_refresh_token(identity=user_id)
                    return {
                        'access_token': access_token,
                        'refresh_token': refresh_token
                    },200
                    
                else:
                    raise Exception('La contrseña es incorrecta')
                
            raise Exception('No se encontro el usuario')
            
        except Exception as e:
            db.session.rollback
            return{
                'message':'Ocurrio un error',
                'error':str(e)
                
            },500
    
        
    def singUp(self,data):
        try:
            #Ingresar o insertar  el rol_id
            data['rol_id'] = self.rol_id
            new_record=self.model.create(**data)
            new_record.hashPassword()
            db.session.add(new_record)
            db.session.commit()
            return{
                'message':'El usuario se creo con exito'
            },201
            
        except Exception as e:
            db.session.rollback
            return{
                'message':'Ocurrio un error',
                'error':str(e)
                
            },500