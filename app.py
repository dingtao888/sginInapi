from flask import Flask

from flask_restful import Api,Resource,reqparse

app = Flask(__name__)
api = Api(app)


users = [
    { "id":1, 'username':'xiaoming'},
    { "id":2, 'username':'xiaohong'}
]


class Users(Resource):
    def get(self):
        result = {"success":True,"data":users}
        return result,200

    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument('username')
        args=parse.parse_args()
        for user in users:
            if user['username']==args['username']:
                msg = {
                    "success":False,
                    "msg":"用户{}不存在！".format(name)
                }
                return msg,400
        
        user = {
            "id":len(users)+1,
            "username":args['username']
        }
        users.append(user)
        msg = {
            "success":True,
            "data":user
        }
        return msg, 200
            

class User(Resource):
    def get(self,name):
        for user in users:
            if(name == user['username']):
                msg = {
                    "success":True,
                    "data":user
                }
                return msg, 200
        msg = {
            "success":False,
            "msg":"用户{}不存在！".format(name)
        }
        return msg,400

    def put(self,name):
        parse = reqparse.RequestParser()
        parse.add_argument('username')
        args = parse.parse_args()
        for user in users:
            if(name == user['username']):
                user['username'] = args['username']
                msg = {
                    "success":True,
                    "msg":user
                }
                return msg, 200
        msg = {
            "success":False,
            "msg":"用户{}不存在！".format(name)
        }
        return msg,400
                

    def delete(self,name):
        for user in users:
            if(name == user['username']):
                index = users.index(user)
                users.pop(index)
                return {"success":True,"msg":'删除用户{}成功'.format(name)}, 200
        
        msg = {
            "success":False,
            "msg":"用户{}不存在！".format(name)
        }
        return msg,400


if __name__ == "__main__":
    api.add_resource(User,'/user/<string:name>')
    api.add_resource(Users,'/users')
    app.run(debug=True)