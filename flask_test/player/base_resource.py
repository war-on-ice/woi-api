from flask_restful import Resource
from flask_test.database import (
    Column,
    db,
    ReferenceCol,
    relationship,
)
from flask_test.utils import row2dict

class BaseResource(Resource):
    def __init__(self, resource_class=None, primary_key=None):
        self.resource_class = resource_class
        self.primary_key = primary_key
        self.request_parser = None
        self.session = db.session

    def _build_default_request_parser(self):
        self.request_parser = reqparse.RequestParser()

        # Create a base request parser instance, with all columns optional.
        location = ('json', 'values')
        for col in self.resource_class._columns:
            col_def = self.resource_class.__dict__[col].column

            db_type = str
            default = ''
            # If column type = x, set db_type to y

            self.request_parser.add_argument(
                col_def.column_name, type=db_type, location=location,
                required=False, default=default)

    def _get_resource_instance(self, query_filters):
        query_set = self.session.query(self.resource_class)
        for key, value in query_filters.items():
            query_set.filter_by(**{key:value})
        return query_set.first()

    def _get_resource_list(self, query_filters):
        if query_filters:
            pass
        else:
            # Search and return all limit 100
            resource_list = self.session.query(self.resource_class).limit(100)
        return resource_list

    def get(self, resource_id, dict_format=True):
        query_filters = {self.primary_key: resource_id}
        resource_instance = self._get_resource_instance(query_filters)
        try:
            resource_instance = self._get_resource_instance(query_filters)
        except Exception: #TODO: Use Doesnt exist sqlalchemy exception
            return "%s with filters %s does not exist in the database" % (
                self.resource_class.__name__, query_filters), 200
        return row2dict(resource_instance), 200
