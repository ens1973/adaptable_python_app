import mongoengine as me

class Order(me.Document):
    customer_name = me.StringField(required=True, max_length=100)
    customer_phone = me.StringField(required=True, max_length=15)
    customer_address = me.StringField(required=True, max_length=255)
    receiver_name = me.StringField(required=True, max_length=100)
    receiver_phone = me.StringField(required=True, max_length=15)
    receiver_address = me.StringField(required=True, max_length=255)
    items = me.ListField(me.DictField())
    note = me.StringField()
    total_quantity = me.IntField(min_value=1)
    total_price = me.FloatField(min_value=1)
    paid = me.BooleanField(required=True, default=False) 
    type = me.IntField(min_value=0, max_value=4) # 0 to 4, 1=tiền mặt, 2=cà thẻ, 3=chuyển khoản, 4=COD
    status = me.IntField(min_value=0, max_value=4) # 0 to 4, 0=order, 1=processing, 2=shipping, 3=cancel, 4=done

    def __repr__(self):
        return f'<Order (customer name={self.customer_name})>'

