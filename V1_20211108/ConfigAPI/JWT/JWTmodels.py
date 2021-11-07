from ConfigAPI.core import DB,bcrypt,app
import datetime
import jwt


class UserClass(DB.Model):
    """ User Model for storing user related details """
    __tablename__ = "users"

    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    user = DB.Column(DB.String(255), unique=True, nullable=False)
    password = DB.Column(DB.String(255), nullable=False)
    registered_on = DB.Column(DB.DateTime, nullable=False,default=DB.func.now())
    admin = DB.Column(DB.Boolean, nullable=False, default=False)


    def __init__(self,user,password,admin=0):
        self.user = user
        self.password = bcrypt.generate_password_hash(
            password, 13
        ).decode()
        #self.id = id
        self.registered_on = datetime.datetime.now()
        self.admin = admin

    def encode_auth_token(self):
        """
        Generates the Auth Token
        :return: string
        """
        if True:#try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, minutes=5, seconds=30),
                'iat': datetime.datetime.utcnow(),
                'sub': self.user
            }
            return jwt.encode(payload, app.config.get('SECRET_KEY'), algorithm='HS256')
        #except Exception as e:
        #    return e

    def decode_auth_token(auth_token):
        """
        Decodes the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, app.config.get('SECRET_KEY'),algorithms='HS256')
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'


DB.create_all()
