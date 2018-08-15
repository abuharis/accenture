from flask import Flask
from flask_restful import reqparse, abort, Api, Resource


class TodoList(Resource):
    def get(self):
        print ("Debug:sending full list")
        return TODOS

    def post(self):
        args = parser.parse_args()
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task':args['task']}
        print ("debug: added task with id '{}'".format(todo_id))
        return TODOS[todo_id], 201

TODOS = {
        'todo1': {'task1':'build an API'},
        'todo2': {'task2':'??????'}
        }

 #version 3
class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

#version 4


    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task':args['task']}
        TODOS[todo_id] = task
        return task, 201

    def delete(self, todo_id):
        print("debug:deleting task with id '{}'".format(todo_id))
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo with {} doesnt exist".format(todo_id))


app = Flask(__name__)
api = Api(app)


parser = reqparse.RequestParser()
parser.add_argument('task')




api.add_resource(TodoList, '/todos')


if __name__ == '__main__' :
    app.run(debug=True, host='0.0.0.0',port=8080)
