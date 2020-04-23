from flask import Blueprint, jsonify

mod_tables = Blueprint('tables', __name__, url_prefix='/api/tables')


@mod_tables.route('/', methods=['GET'])
def get_all():
    from tables.models import Table

    return jsonify(json_list=[i.serialize for i in Table.query.all()])
