import mongoengine as me

class TelegramBot(me.Document):
    name = me.StringField(unique=True, max_length=100)
    bot_key = me.StringField(max_length=255)
    group_id = me.StringField(max_length=50)

    def __repr__(self):
        return f'<TelegramBot (name={self.name})>'


# name: orderbot
# key: 5671961880:AAHbCxQ5nCCcZ39ZNjC_tF1HDbsQNOA8vNU
# group: -850402121