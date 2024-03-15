from flask import Flask

app = Flask(__name__)

@app.route('/') #decorators
def hello_world():
  return "Hello Pujan!"

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)