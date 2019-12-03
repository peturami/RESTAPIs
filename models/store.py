from db import db

class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    #items = db.relationship('ItemModel') #propoji s item pres cizi klice - definovane v item ## list of itemModels
    # vytvori item object pro kazdy item kde se shoduje store id se storem - draha operace
    items = db.relationship('ItemModel', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    # method that returns json format
    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}
        # pokud se pouzije lazy='dynamic' tak items neni list of items, ale query builder (musi se pouzit all() pro ziskani vsech itemu)
    # pokud se nezavola json method tak se nedivame do tabulky itemu a vytvoreni storu je jednoducha operace
    # kdyz se zavola json metoda tak se leze do tabulky itemu a je to pomale
    # je potreba zvazit rychlost vytvoreni storu VS rychlost json metody

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self): # upsert
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()