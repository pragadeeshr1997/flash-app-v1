from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>DevOps Flask App</h1>
    <p>Deployed using Jenkins + Docker</p>
    <p>this is the manually edited 1st line</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
