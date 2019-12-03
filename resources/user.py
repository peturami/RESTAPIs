# vytvorim objekt User abych nemusel v securiity.py pracovat s dict

import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

# bude fungovat jen tak, že se zavolá post s parametrem, což vytvoří registraci
class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )

    def post(self):
        data = UserRegister.parser.parse_args()

        # check if user exists
        if UserModel.find_by_username(data['username']):
            return {"message":  "User already exists"}, 400

        #user = UserModel(data['username'], data['password'])
        user = UserModel(**data)
        user.save_to_db()

        return {"message": "User created successfully."}, 201

