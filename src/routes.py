from flask import Flask
from schema import schema
app = Flask(__name__)
app.debug = True


@app.route('/ping')
def test():
    return 'Henlo'


@app.route('/test_query')
def race():
    query = '''
      query getRace {
        race(name: $name) {
          traits
        }
      }
    '''
    result = schema.execute(query, variable_values={'name': 'Dwarf'})
    return result.data

