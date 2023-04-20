from datetime import timedelta, datetime
from typing import Dict

from jose import jwt





JWT_SECRET = '--very secret key--'
JWT_ALGORITHM = 'HS256'



def signJWT(user_id: str, type_jwt: str) -> Dict[str, str]:
    payload = {
        "user_id": user_id,
        "exp": 3,
        "type": type_jwt
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return {'access_token': token}



