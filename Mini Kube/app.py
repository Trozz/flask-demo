from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    output = """
    <h1>Hello and welcome to the world of Kubernetes</h1>
    <p>Try the following endpoints:</p>
    <ul>
        <li><a href="/health">/health</a></li>
        <li><a href="/hello">/hello</a></li>
        <li><a href="/hello/Bob">/hello/Bob</a></li>
    </ul>
    """
    return output

@app.route('/health')
def health():
    return 'OK'

@app.route('/hello')
def hello_base():
    return 'Hi there'

@app.route('/hello/<name>')
def hello(name):
    return 'Hello, {}!'.format(name)

app.run(host='0.0.0.0', port=80)
