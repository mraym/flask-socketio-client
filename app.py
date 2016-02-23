from flask import Flask
from flask import render_template
from flask.ext.cors import CORS

app = Flask(__name__)
app.secret_key = 'testflasksocketioclient'
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    #app.run()
    # Insecure! Exposes port 5000 to outside world
    #app.run( host='0.0.0.0', debug=True )
    app.run( host='0.0.0.0', port=8999, debug=True )
    #pp.run( host='0.0.0.0', port=80 )
