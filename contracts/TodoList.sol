pragma solidity >=0.4.21 <=0.6.0;



contract TodoList {
	struct Item {
		string description;
		uint256 timestamp;
		bool done;
	}

	struct List {
		string title;
		uint[] itemIDs;
		mapping(uint => Item) Items;
	}

	uint[] listIDs;
	mapping (uint => List) Lists;

	function newList(string memory _title) public returns(bool){
		uint new_id = listIDs.length + 1;
		List storage list = Lists[new_id];

		list.title = _title;
		listIDs.push(new_id);
		return (true);
	}

	function newItem(uint _listID, string memory _description, uint256 _timestamp) public returns(bool){
		uint new_id = Lists[_listID].itemIDs.length + 1;
		Item storage new_item = Lists[_listID].Items[new_id];

		new_item.description = _description;
		new_item.timestamp = _timestamp;
		Lists[_listID].itemIDs.push(new_id);
		return (true);
	}

	function getListIDs() public view returns (uint[] memory){
		return listIDs;
	}

	function getList(uint _id) public view returns(string memory, uint[] memory){
		List memory list = Lists[_id];
		return(list.title, list.itemIDs);
	}

	function getItemIDs(uint _listID) public view returns(uint[] memory){
		List memory list = Lists[_listID];
		return (list.itemIDs);
	}

	function getItem(uint _listID, uint _itemID) public view returns(string memory, uint256, bool){
		Item memory item = Lists[_listID].Items[_itemID];
		return (item.description, item.timestamp, item.done);
	}

	function updateList(uint _id, string memory _title) public returns(string memory, uint[] memory){
		List storage list = Lists[_id];
		list.title = _title;
		return (list.title, list.itemIDs);
	}

	function updateItem(uint list_id, uint item_id, string memory _description) public returns (string memory){
		Item storage item = Lists[list_id].Items[item_id];
		item.description = _description;
		return(item.description);
	}

	function deleteItem(uint _list_id, uint _item_id) public returns(bool){
		delete Lists[_list_id].Items[_item_id];
		delete Lists[_list_id].itemIDs[_item_id-1];

		return true;
	}


	function deleteList(uint _ID) public returns(bool){
		uint listLength = Lists[_ID].itemIDs.length;
		for(uint i = 0; i < listLength; i++){
			deleteItem(_ID, Lists[_ID].itemIDs[i]);
		}
		Lists[_ID].title = "";
		delete listIDs[_ID-1];
		return true;
	}

	function toggleItem(uint _list_id, uint _item_id) public returns(bool){
		bool status = Lists[_list_id].Items[_item_id].done;
		Lists[_list_id].Items[_item_id].done = !status;
		return true;
	}



}