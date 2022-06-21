from flask import Flask, request
from BaseConverter import duo, binary

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return {'output': str(duo(3.1234))}

if __name__ == "__main__":
    app.run()
