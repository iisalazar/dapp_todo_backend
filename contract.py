import json, os, datetime, time
from web3 import Web3

class Contract(object):

	def __init__(self, blockchain_url="http://localhost:8545"):
		self.web3 = Web3(Web3.HTTPProvider(blockchain_url))
		with open(os.path.join(os.getcwd(), "build/contracts/TodoList.json"), 'r') as FILE:	
			file = json.loads(FILE.read())
			abi = file['abi']
		with open(os.path.join(os.getcwd(), "address.json"), "r") as FILE:
			file = json.loads(FILE.read())
			contract_address = file['TodoList']
		address = self.web3.toChecksumAddress(contract_address)
		self.contract = self.web3.eth.contract(abi=abi, address=address)
		self.web3.eth.defaultAccount = self.web3.eth.accounts[0]


	def newList(self, title):
		if not isinstance(title, str):
			return False
		tx_hash = self.contract.functions.newList(title).transact()
		self.web3.eth.waitForTransactionReceipt(tx_hash)
		return True

	def newItem(self, list_id, description):
		if not isinstance(list_id, int) or not isinstance(description, str):
			return False
		timestamp = int(datetime.datetime.now().timestamp() * 10 ** 6)
		tx_hash = self.contract.functions.newItem(list_id, description, timestamp).transact()
		self.web3.eth.waitForTransactionReceipt(tx_hash)
		return 

	def getLists(self):
		IDs = self.contract.functions.getListIDs().call()
		lists = []
		for ID in IDs:
			if ID != 0:
				lists.append(self.getList(ID))
		return lists


	def getItems(self, list_id):
		IDs = self.contract.functions.getItemIDs(list_id).call()
		items = []
		for ID in IDs:
			if ID != 0:
				items.append(self.getItem(list_id, ID))
		return items

	def getList(self, ID):
		if not isinstance(ID, int):
			return False
		list = self.contract.functions.getList(ID).call()
		return {
			"id": ID,
			"title": list[0],
			"items": list[1]
		}

	def getItem(self, list_id, ID):
		if not isinstance(ID, int) or not isinstance(list_id, int):
			return False		
		if ID == 0:
			return
		item = self.contract.functions.getItem(list_id, ID).call()
		return {
			"id": ID,
			"description": item[0],
			"timestamp": item[1],
			"readable_time": time.ctime(item[1] / 10 ** 6),
			"done": item[2]
			}
	def updateList(self, ID, title):
		if not isinstance(ID, int) or not isinstance(title, str):
			return False
		tx_hash = self.contract.functions.updateList(ID, title).transact()
		self.web3.eth.waitForTransactionReceipt(tx_hash)
		return True

	def updateItem(self, list_id, ID, description):
		if not isinstance(ID, int) or not isinstance(description, str) or not isinstance(list_id, int):
			return False
		tx_hash = self.contract.functions.updateItem(list_id, ID, description).transact()
		self.web3.eth.waitForTransactionReceipt(tx_hash)

	def deleteItem(self, list_id, ID):
		if not isinstance(ID, int):
			return False

		tx_hash = self.contract.functions.deleteItem(list_id, ID).transact()
		self.web3.eth.waitForTransactionReceipt(tx_hash)

	def deleteList(self, ID):
		if not isinstance(ID, int):
			return False
		print(type(ID))
		tx_hash = self.contract.functions.deleteList(ID).transact()
		self.web3.eth.waitForTransactionReceipt(tx_hash)

	def toggleItem(self, list_id, ID):
		if not isinstance(ID, int) or not isinstance(list_id, int):
			return False
		print("LIST_ID {}".format(list_id))
		print("ITEM_ID {}".format(ID))
		tx_hash = self.contract.functions.toggleItem(list_id, ID).transact()
		self.web3.eth.waitForTransactionReceipt(tx_hash)

if __name__ == "__main__":
	c = Contract()
	c.deleteList(1)
'''
script
from contract import Contract
c = Contract()
c.deleteList(1)
c.newItem(1, "Item 1")
'''