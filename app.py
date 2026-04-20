(
echo from flask import Flask
echo.
echo app = Flask(__name__)
echo.
echo @app.route("/")
echo def home():
echo     return "Hello from LinkedIn API ECS NonProd!"
echo.
echo if __name__ == "__main__":
echo     app.run(host="0.0.0.0", port=5000)
) > app.py
