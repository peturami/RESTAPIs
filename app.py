import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
# pri pouziti flask_restful se pak nemusi pouzivat jsonify


from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# heroku vytvoří proměnnou DATABASE_URL, takže si stačí načíst hodnotu v proměnné, druhý parametr to vezme pokud neexistuje var DATABASE_URL (např.při spuštění na locale)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # turns off Flask sqlalchemy changes tracker
app.secret_key = 'jose' #key for encryption
api = Api(app)


jwt = JWT(app, authenticate, identity)
# JWT creates new endpoint /auth , then we send it username + pass and JWT sends it to authenticate function - if thats ok auth endpoint returns JWT token

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
# funguje stejně jako kdyby vypsal  @app.route(..)
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)