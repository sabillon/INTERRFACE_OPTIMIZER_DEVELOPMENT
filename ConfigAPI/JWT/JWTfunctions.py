from ConfigAPI.JWT.JWTmodels import UserClass
from ConfigAPI.core import DB,app,bcrypt


class JWT():
          def create_user(user1,password1):
                    User=UserClass(user=user1,password=password1)
                    DB.session.add(User)
                    DB.session.commit()                    
                    return True
          
          def autenticate_and_return_json(user1,password):
                    UserObj = UserClass.query.filter_by(user=user1).first()
                    if UserObj and bcrypt.check_password_hash(UserObj.password,password):
                              tocken = UserObj.encode_auth_token()
                    return tocken
          
          def checktocken(user,auth_header):
                    auth_token = auth_header
                    resp = UserClass.decode_auth_token(auth_token)
                    return resp == user