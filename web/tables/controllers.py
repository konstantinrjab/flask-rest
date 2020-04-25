import json
from flask import jsonify, request
from flask_restful import Resource
from common.functions import abort_on_entity_not_found


class TableSingle(Resource):
    def get(self, id):
        table = Table.query.get(id)
        if table is None:
            abort_on_entity_not_found()
        return json.loads(json.dumps(table.serialize))

    def put(self, id):
        table = Table.query.get(id)
        if table is None:
            abort_on_entity_not_found()
        table.creator_id = request.json['creator_id']
        db.session.commit()

        return json.loads(json.dumps(table.serialize))

    def delete(self, id):
        table = Table.query.get(id)
        db.session.delete(table)
        db.session.commit()
        return '', 204


class TableList(Resource):
    def get(self):
        return jsonify([i.serialize for i in Table.query.all()])

    def post(self):
        table = Table(creator_id=request.json['creator_id'])

        db.session.add(table)
        db.session.commit()
        return json.loads(json.dumps(table.serialize))


from tables.models import Table
from app import db
