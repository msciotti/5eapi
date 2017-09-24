from flask import Flask
from flask.ext.mysql import MySQL
import graphene

app = Flask(__name__)


class Spell(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    description = graphene.String()
    range = graphene.String()
    components = graphene.String()
    higher_levels = graphene.String()
    duration = graphene.String()
    level = graphene.Int()
    casting_time = graphene.String()
    school = graphene.String()


class Query(graphene.ObjectType):
    spell = graphene.Field(Spell, name=graphene.String())

    def resolve_spell(self, info):
        cursor.execute('select * from spells where name={}'.format(info.name))
        raw = cursor.fetchone()
        return raw


schema = graphene.Schema(query=Query)
