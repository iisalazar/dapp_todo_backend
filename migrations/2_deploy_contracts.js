const TodoList = artifacts.require("TodoList");
const fs = require('fs');

module.exports = (deployer) => {
	deployer.deploy(TodoList).then( instance => {
		var contract = instance;
		fs.writeFile(__dirname + "/../address.json", JSON.stringify({"TodoList": instance.address}), function(err){
				if(err) throw err;
		})
	})
}