from flask_restx import Namespace, Resource, fields
from flask import request
from prod.db_models.user_db_model import UserDBModel

ns = Namespace(
    'users/login',
    description='Users login operations'
)


@ns.route('')
class UsersLoginResource(Resource):
    MISSING_ARGS_ERROR = 'Missing arguments'
    WRONG_DATA_ERROR = 'Email or password incorrect'
    WRONG_PASS_ERROR = 'wrong_password'

    body_swg = ns.model('LoginInput', {
        'email': fields.String(required=True, description='The user email'),
        'password': fields.String(
            required=True, description='The user password')
    })

    code_200_swg = ns.model('LoginOutput200', {
        'email': fields.String(description='The user email'),
        'id': fields.Integer(description='The user id')
    })

    code_400_swg = ns.model('LoginOutput400', {
        'status': fields.String(example=MISSING_ARGS_ERROR)
    })

    code_401_swg = ns.model('LoginOutput401', {
        'status': fields.String(example=WRONG_PASS_ERROR)
    })

    @ns.expect(body_swg)
    @ns.response(200, 'Success', code_200_swg)
    @ns.response(400, MISSING_ARGS_ERROR, code_400_swg)
    @ns.response(401, 'Wrong password', code_401_swg)
    def post(self):
        data = request.get_json()
        if not self.check_values(data, ["email", "password"]):
            ns.abort(400, status=self.MISSING_ARGS_ERROR)
        required_id = UserDBModel.get_id(data['email'], data['password'])
        if required_id == -1:
            ns.abort(401, status=self.WRONG_PASS_ERROR)
        response_object = {
            "email": data['email'],
            "id": required_id
        }
        return response_object, 200

    @staticmethod
    def check_values(json, field_list):
        for value in field_list:
            if value not in json:
                return False
        return True
