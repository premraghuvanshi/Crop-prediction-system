import os
import jwt
from datetime import datetime , timedelta , timezone



SECRET_KEY = os.getenv("JWT_SECRET_KEY")
ALGORITHM = os.getenv("JWT_ALGORITHM")




def create_token(data : dict) -> str:

    payload = data.copy()
    
    expire = datetime.now(timezone.utc)+timedelta(hours=24)

    payload.update({"exp":expire})

    return jwt.encode(payload,SECRET_KEY ,algorithm = ALGORITHM)




def token_decoder(token : str) -> dict:

    payload = jwt.decode(token , SECRET_KEY , algorithms=[ALGORITHM])

    return payload

