from flask import Flask, request, json
from schema import Query, schema
import graphene
app = Flask(__name__)


@app.route('/')
def test():
    query = '''
      query FetchSpellQuery {
        spell(name: 'Acid Splash') {
          id
          description
        }
      }
      '''
    result = schema.execute(query)
    return result.data
