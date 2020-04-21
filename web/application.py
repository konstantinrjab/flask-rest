from common.app import app
from common.app import db


@app.route('/')
def example():
    db.create_all()
    return '{"name":"' + str(5) + '"}'


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
