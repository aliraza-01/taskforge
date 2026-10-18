import jwt
from app.core.config import settings 
ALGORITHM = "HS256"
def create_token(user_id):
    playload={"sub":str(user_id)}
    token = jwt.encode(
        playload,
        settings.jwt_secret_key,
        algorithm=ALGORITHM
    )
    return token
def verify_token(token):
    playload = jwt.decode(
        token,
        settings.jwt_secret_key,
        algorithms=[ALGORITHM]
    )
    return playload