from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return '<h1>HOME BEEF<h1>'

if __name__ == "__main__":
    app.run()
