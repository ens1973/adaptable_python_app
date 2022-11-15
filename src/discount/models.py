import mongoengine as me
from src.db import Document
from datetime import datetime

class Discount(Document):
    code = me.StringField(unique=True, max_length=100)
    percent = me.FloatField(default=0)
    amount = me.FloatField(default=0)
    mfg_at = me.DateTimeField(default=datetime.now)
    exp_at = me.DateTimeField(default=datetime.now)

    def __repr__(self):
        return f'<Discount (code={self.code})>'

