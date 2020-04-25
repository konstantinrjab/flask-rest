from flask_restful import abort


def abort_on_entity_not_found():
    abort(404, message="Entity not found")
