import flask

from flask import Flask, render_template, url_for, send_from_directory
app = Flask(__name__)

@app.route('/')
def index():
    #return render_template('index.html')
    
    return render_template('index.html')
    #return render_template('index.html')
#    return send_from_directory('templates',path)


@app.route('/<path:path>')
def model(path):
    print(path)
    return send_from_directory('Model',path)
if __name__ == "__main__":
    app.run(debug=True)