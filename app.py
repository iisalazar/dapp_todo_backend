from flask import Flask
from resource import api_blueprint
from flask_cors import CORS

app = Flask(__name__)
app.config.from_pyfile('config.py')
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.register_blueprint(api_blueprint, url_prefix="/api")

@app.route('/')
def home():
	return '''
			<h1>This is the REST endpoint for Lists and Items.</h1>
			<h1>Endpoints</h1>
			<h2>Lists</h2>
			<ul>
				<li><b>CREATE</b> /api/lists</li>
				<li><b>RETRIEVE</b> /api/lists?list_id=[YOUR_LIST_ID]</li>
				<li><b>UPDATE</b> /api/lists?list_id=[YOUR_LIST_ID]</li>
				<li><b>DELETE</b> /api/lists?list_id=[YOUR_LIST_ID]</li>
				<li><b>LIST</b> /api/lists</li>
			</ul>
			<h2>Items</h2>
			<ul>
				<li><b>CREATE</b> /api/items</li>
				<li><b>RETRIEVE</b> /api/items?list_id=[YOUR_LIST_ID]&item_id=[YOUR_ITEM_ID]</li>
				<li><b>UPDATE</b> /api/items?list_id=[YOUR_LIST_ID]&item_id=[YOUR_ITEM_ID] <------ receives json body</li>
				<li><b>DELETE</b> /api/items?list_id=[YOUR_LIST_ID]&item_id=[YOUR_ITEM_ID]</li>
				<li><b>LIST</b> /api/items?list_id=[YOURLIST_ID]</li>
			</ul>
			'''

if __name__ == '__main__':
	app.run(debug=True)
