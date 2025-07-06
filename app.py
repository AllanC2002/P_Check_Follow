# app/app.py
from flask import Flask
from interface.controllers.follow_controller import bp as follow_bp

app = Flask(__name__)
app.register_blueprint(follow_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
