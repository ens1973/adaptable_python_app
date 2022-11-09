# import mongoengine as me
from src.extensions import jwt
from src.extensions import db
from src.db import Document




class TokenBlocklist(Document):
    jti = db.StringField(max_length=36, nullable=False)
    type = db.StringField(max_length=16, nullable=False)
    created_at = db.DateTimeField(nullable=False)


@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload: dict) -> bool:
    jti = jwt_payload["jti"]
    # token = TokenBlocklist.objects(jti=jti).scalar()
    # print(token)
    # return token is not None
    token = TokenBlocklist.objects(jti=jti).first()

    return token is not None

