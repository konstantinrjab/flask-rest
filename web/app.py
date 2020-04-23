import os
from tables.controllers import mod_tables
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, abort

app = Flask(__name__)
app.secret_key = b'\x07]G\xc0S\x9b\xc1\xcb:jK\xd4\x9et\x12\xbe\x9a\xa4/\x10\x07\xdc\x12\xb6'
app.config.from_object(os.environ['APP_SETTINGS'])

db = SQLAlchemy(app)


@app.errorhandler(404)
def not_found(error):
    abort(404)


app.register_blueprint(mod_tables)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
