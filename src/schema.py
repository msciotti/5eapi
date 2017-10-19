from flask import Flask
import json
import graphene

app = Flask(__name__)

with open('data/races.json') as json_races:
    races = json.load(json_races)


class Race(graphene.ObjectType):
    traits = graphene.List(of_type=graphene.String)


class Query(graphene.ObjectType):
    race = graphene.Field(type=Race)

    def resolve_race(self, info):
        print('here')
        return Race(traits=['meme', 'yup'])


schema = graphene.Schema(query=Query)
