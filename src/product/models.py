import mongoengine as me

class Product(me.Document):
    name = me.StringField(max_length=255)
    price = me.FloatField()
    category = me.StringField(default='shop')
    sku = me.StringField(default='SKU')
    short_description = me.StringField()
    description = me.StringField()
    specs = me.ListField(me.DictField())

    def __repr__(self):
        return f'<Product (name={self.name})>'

# {
#     "name": "Sản phẩm 1",
#     "price": 300000,
#     "category": "shop",
#     "short_description": "Nội dung ngắn của sản phẩm 1",
#     "description": "Nội dung chi tiết của sản phẩm 1, Nội dung chi tiết của sản phẩm 1, Nội dung chi tiết của sản phẩm 1",
#     "specs": [
#         {"key": "dai","value": "30"}, {"key": "rong","value": "30"}, {"key": "cao","value": "30"}, {"key": "khoiluong","value": "30"}
#     ]
# }

# [
#   {
#     "name": "Sản phẩm 1",
#     "price": 300000,
#     "category": "shop",
#     "short_description": "Nội dung ngắn của sản phẩm 1",
#     "description": "Nội dung chi tiết của sản phẩm 1, Nội dung chi tiết của sản phẩm 1, Nội dung chi tiết của sản phẩm 1",
#     "specs": [
#       {"key": "dai","value": "30"}, {"key": "rong","value": "30"}, {"key": "cao","value": "30"}, {"key": "khoiluong","value": "30"}
#     ]
#   },{
#     "name": "Sản phẩm 2",
#     "category": "shop",
#     "price": 400000,
#     "short_description": "Nội dung ngắn của sản phẩm 2",
#     "description": "Nội dung chi tiết của sản phẩm 2, Nội dung chi tiết của sản phẩm 2, Nội dung chi tiết của sản phẩm 2",
#     "specs": [
#       {"key": "dai","value": "40"}, {"key": "rong","value": "40"}, {"key": "cao","value": "40"}, {"key": "khoiluong","value": "40"}
#     ]
#   },{
#     "name": "Sản phẩm 3",
#     "category": "shop",
#     "price": 500000,
#     "short_description": "Nội dung ngắn của sản phẩm 3",
#     "description": "Nội dung chi tiết của sản phẩm 3, Nội dung chi tiết của sản phẩm 3, Nội dung chi tiết của sản phẩm 3",
#     "specs": [
#       {"key": "dai","value": "50"}, {"key": "rong","value": "50"}, {"key": "cao","value": "50"}, {"key": "khoiluong","value": "50"}
#     ]
#   },{
#     "name": "Sản phẩm 4",
#     "category": "shop",
#     "price": 100000,
#     "short_description": "Nội dung ngắn của sản phẩm 4",
#     "description": "Nội dung chi tiết của sản phẩm 4, Nội dung chi tiết của sản phẩm 4, Nội dung chi tiết của sản phẩm 4",
#     "specs": [
#       {"key": "dai","value": "10"}, {"key": "rong","value": "10"}, {"key": "cao","value": "10"}, {"key": "khoiluong","value": "10"}
#     ]
#   },{
#     "name": "Sản phẩm 5",
#     "category": "shop",
#     "price": 2000000,
#     "short_description": "Nội dung ngắn của sản phẩm 5",
#     "description": "Nội dung chi tiết của sản phẩm 5, Nội dung chi tiết của sản phẩm 5, Nội dung chi tiết của sản phẩm 5",
#     "specs": [
#       {"key": "dai","value": "200"}, {"key": "rong","value": "200"}, {"key": "cao","value": "200"}, {"key": "khoiluong","value": "200"}
#     ]
#   },{
#     "name": "Sản phẩm 6 (stone)",
#     "category": "stone",
#     "price": 2100000,
#     "short_description": "Nội dung ngắn của sản phẩm 6",
#     "description": "Nội dung chi tiết của sản phẩm 6, Nội dung chi tiết của sản phẩm 6, Nội dung chi tiết của sản phẩm 6",
#     "specs": [
#       {"key": "dai","value": "200"}, {"key": "rong","value": "200"}, {"key": "cao","value": "200"}, {"key": "khoiluong","value": "200"}
#     ]
#   },{
#     "name": "Sản phẩm 7 (stone)",
#     "category": "stone",
#     "price": 1900000,
#     "short_description": "Nội dung ngắn của sản phẩm 7",
#     "description": "Nội dung chi tiết của sản phẩm 7, Nội dung chi tiết của sản phẩm 7, Nội dung chi tiết của sản phẩm 7",
#     "specs": [
#       {"key": "dai","value": "200"}, {"key": "rong","value": "200"}, {"key": "cao","value": "200"}, {"key": "khoiluong","value": "200"}
#     ]
#   },{
#     "name": "Sản phẩm 8 (website)",
#     "category": "website",
#     "price": 2150000,
#     "short_description": "Nội dung ngắn của sản phẩm 8",
#     "description": "Nội dung chi tiết của sản phẩm 8, Nội dung chi tiết của sản phẩm 8, Nội dung chi tiết của sản phẩm 8",
#     "specs": [
#       {"key": "dai","value": "200"}, {"key": "rong","value": "200"}, {"key": "cao","value": "200"}, {"key": "khoiluong","value": "200"}
#     ]
#   },{
#     "name": "Sản phẩm 9 (website)",
#     "category": "website",
#     "price": 2500000,
#     "short_description": "Nội dung ngắn của sản phẩm 9",
#     "description": "Nội dung chi tiết của sản phẩm 9, Nội dung chi tiết của sản phẩm 9, Nội dung chi tiết của sản phẩm 9",
#     "specs": [
#       {"key": "dai","value": "200"}, {"key": "rong","value": "200"}, {"key": "cao","value": "200"}, {"key": "khoiluong","value": "200"}
#     ]
#   }
# ]