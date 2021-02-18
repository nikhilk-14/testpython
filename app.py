from flask import Flask, request, jsonify

from random import randint

#from flask_caching import Cache

#config = {
#    #"DEBUG": True,          # some Flask specific configs
#    "CACHE_TYPE": "simple", # Flask-Caching related configs
#    "CACHE_DEFAULT_TIMEOUT": 0
#}

#cache2 = Cache(config={ "CACHE_TYPE": "simple", "CACHE_DEFAULT_TIMEOUT": 0 })

app = Flask(__name__)
#app.config.from_mapping(config)
#cache2.init_app(app)

cache = dict()

@app.route("/")
def home():
    return "Hello flask"

@app.route('/sample', methods=['GET'])
def api_all():
    return jsonify({'name': 'nik', 'age': 29})

@app.route('/sample/getByName', methods=['GET'])
def api_getByName():
    if 'name' in request.args:
        name = request.args['name']
    else:
        return "Error: No id field provided. Please specify an name."

    return jsonify({'name': name, 'age': 27})

@app.route('/sample/get/<string:name>/<int:age>', methods=['GET'])
def api_name(name, age):
    return jsonify({'name': name, 'age': age})

@app.route('/testpost', methods=['POST'])
def testPost():
    testdata = request.get_json()
    return jsonify(testdata)

@app.route('/testcache')
def testcache():
    cached_data = []
    is_cached = None
    number = randint(1, 5)
    cache_key = f'test_num{number}'
    cached_num = cache.get(cache_key)
    if cached_num is None:
        is_cached = False
        cache[cache_key] = number
        cached_data.append(f"test_num{number}")
    else:
        is_cached = True
    return f'<h1>Test Cache: {number} - {is_cached}</h1><h2>{cache}</h2>'

#@app.route('/testcache2')
#def testcache2():
#    cached_data = []
#    is_cached = None
#    number = randint(1, 5)
#    cache_key = f'test_num{number}'
#    cached_num = cache2.get(cache_key)
#    if cached_num is None:
#        is_cached = False
#        cache2.set(cache_key, number)
#        cached_data.append(f"test_num{number}")
#    else:
#        is_cached = True
#    return f'<h1>Test Cache2: {number} - {is_cached}</h1><h2>{cache2.cache._cache}</h2>'

if __name__ == "__main__":
    app.run(host='0.0.0.0')