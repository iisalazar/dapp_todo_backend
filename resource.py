from flask import Blueprint
from flask_restful import Api, Resource, request
from contract import Contract
# A new way of accepting parsed data
from webargs import fields, validate
from webargs.flaskparser import use_args, use_kwargs, parser, abort

api_blueprint = Blueprint('resource', __name__)

api = Api(api_blueprint)

c = Contract()

class ListResource(Resource):

	get_parser = {
		"list_id": fields.Int(required=False, validate=validate.Range(min=1)),
	}

	post_parser = {
		"title": fields.Str(required=True)
	}

	update_parser = {
		"list_id": fields.Int(required=True),
		"title": fields.Str(required=False)
	}

	@use_args(get_parser)
	def get(self, data):
		ID = data.get('list_id') or request.args.get('list_id') or None
		if ID is not None:
			return { "data": c.getList(ID) }
		else:
			return { "data" : c.getLists() }

	@use_kwargs(post_parser)
	def post(self, title):
		if c.newList(title):
			return { "success" : True }
		else:
			return { "success" : False }

	@use_kwargs(update_parser)
	def put(self, list_id, title):
		ID = list_id or request.args.get('list_id')
		c.updateList(ID, title)
		return { "success" : True }

	@use_kwargs(get_parser)
	def delete(self, list_id):
		ID = list_id or int(request.args.get('list_id'))
		c.deleteList(ID)
		return { "success" : True}

class ItemResource(Resource):
	post_parser = {
		"list_id" : fields.Int(required=True),
		"description": fields.Str(required=True)
	}

	update_parser = {
		"list_id" : fields.Int(required=False),
		"description": fields.Str(required=True),
		"item_id" : fields.Int(required=False)
	}


	# Only accepts url arguments e.g. http://localhost:5000/api/items?list_id={ID}
	def get(self):
		list_id = int(request.args.get("list_id"))
		item_id = request.args.get("item_id") or None
		if item_id is None:
			return { "data" : c.getItems(list_id) }
		else:
			return { "data" : c.getItem(list_id, int(item_id)) }

	@use_kwargs(post_parser)
	def post(self, list_id, description):
		ID = list_id or request.args.get('list_id')
		c.newItem(int(ID), description)
		return True

	@use_args(update_parser)
	def put(self, parser):
		list_id = parser.get('list_id') or request.args.get('list_id')
		item_id = parser.get('item_id') or request.args.get('item_id')
		print(list_id)
		print(item_id)
		print(parser.get('description'))
		c.updateItem(list_id, item_id, parser.get('description'))
		return { "success" : True }


	def delete(self):
		list_id = int(request.args.get('list_id'))
		item_id = int(request.args.get('item_id'))
		c.deleteItem(list_id, item_id)
		return { "success" : True}

class ToggleItem(Resource):

	def get(self):
		list_id = int(request.args.get('list_id'))
		item_id = int(request.args.get('item_id'))
		print(list_id)
		print(item_id)
		c.toggleItem(list_id, item_id)
		return { "success" : True }

# This error handler is necessary for usage with Flask-RESTful
@parser.error_handler
def handle_request_parsing_error(err, req, schema, error_status_code, error_headers):
    """webargs error handler that uses Flask-RESTful's abort function to return
    a JSON error response to the client.
    """
    abort(error_status_code, errors=err.messages)

api.add_resource(ListResource, '/lists')
api.add_resource(ItemResource, '/items')
api.add_resource(ToggleItem, '/items/toggle')