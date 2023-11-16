from flask_restx import fields

class AuthRequestSchema:
    def __init__(self,namespace) -> None:
        self.namespace = namespace
    
    
    def signin(self):
        return self.namespace.model('Auth SignIn',{
            
            'username': fields.String(required=True),
            'password': fields.String(required=True)
            
        })
    
    
    def signup(self):
        return self.namespace.model('Auth SignUp',{                        
            
            'name':fields.String(required=True,min_length=2,max_length=80),
            'last_name':fields.String(required=True,min_length=2,max_length=120),
            'username':fields.String(required=True,min_length=4,max_length=80),
            'password':fields.String(required=True,min_length=4,max_length=120),
            'email':fields.String(required=True,min_length=3,max_length=140)
            })