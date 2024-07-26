import os

from flask import Flask
from app.configuration.database import db
from app.controllers.userController import userRoute

app = Flask(__name__)
app.register_blueprint(userRoute)


if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))
  with app.app_context():
      db.create_all()