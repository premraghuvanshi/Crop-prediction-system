import os
import jwt
from datetime import datetime , timedelta , timezone



SECRET_KEY = os.getenv("JWT_SECRET_KEY")
ALGORITHM = os.getenv("JWT_ALGORITHM")




def create_token(payload : dict) -> str:

    data = payload.copy()
    
    expire = datetime.now(timezone.utc)+timedelta(hours=24)

    data.update({"exp":expire})

    return jwt.encode(data,SECRET_KEY ,algorithm = ALGORITHM)




def token_decoder(token : str) -> dict:

    return jwt.decode(token , SECRET_KEY , algorithms=[ALGORITHM])

    

