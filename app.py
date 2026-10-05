from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "project": "FlaskFlow",
        "message": "Welcome to FlaskFlow CI/CD!",
        "status": "running",
        "version": "1.0"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    }), 200

@app.route("/about")
def about():
    return jsonify({
        "project": "FlaskFlow",
        "description": "Python Flask CI/CD pipeline using AWS"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)