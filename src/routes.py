from flask import Flask
from schema import schema
import json
app = Flask(__name__)
app.debug = True


@app.route('/ping')
def test():
    return 'Henlo'


@app.route('/test_query')
def race():
    query = '''
      query getRace{
        race {
          traits
        }
      }
    '''
    result = schema.execute(query)
    return json.dumps(result.data, indent=4)

