from flask import Flask, request
from flask_restful import Api, Resource, abort

my_app = Flask(__name__)
my_api = Api(my_app)

superheroes_orig = {
     'batman': {'skill':'money','costume':'black','enemy':'joker'}
    ,'spider-man': {'skill':'web','costume':'red-blue','enemy':'green-goblin'}
    ,'thor':{'skill':'lightning','costume':'viking','enemy':'loki'}
}

class Superheroes(Resource):
    def get(self):
        return list(superheroes_orig.keys())
    
    def post(self):
        if request.json not in superheroes_orig:
            superheroes_orig[request.json] = {}
            return list(superheroes_orig.keys())
        else:
            return 'superhero already exists'


class Superhero(Resource):

    def get(self, name):
        if name in superheroes_orig:
            return superheroes_orig[name]
        else:
            abort(404)

    def put(self,name):
        name = request.json['name']
        attribute = request.json['attribute']
        value = request.json['value']
        if name in superheroes_orig:
            if attribute in superheroes_orig[name]:
                superheroes_orig[name][attribute] = value
                return superheroes_orig
            else:
                return 'Attribute does not exist'
        else:
            abort(404)
    
    def delete(self, name):
        if request.json in superheroes_orig:
            del superheroes_orig[request.json]
            return superheroes_orig
        else:
            abort(404)

my_api.add_resource(Superheroes, '/superheroes')
my_api.add_resource(Superhero, '/superhero/<name>')