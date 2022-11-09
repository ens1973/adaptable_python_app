from .extensions import db

class Document(db.Document):
    """
    Abstract base class. You should inherit all your models from this to save
    time down the road. Chances are you will want all your models to share a
    set of functions or to override others (like changing save behavior)
    """
    meta = {
        'abstract': True,
    }
    item_per_page = 20

    @classmethod
    def all_subclasses(cls):
        return cls.__subclasses__() + [g for s in cls.__subclasses__()
                                       for g in s.all_subclasses()]
