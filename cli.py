from contract import Contract
import sys, pprint, datetime


class CLI(object):

	def greet(self):
		print('''
1. Create new list
2. Get lists
3. Get a single list
4. Get items in a list
5. Get a single item
6. Update an list
7. Update an item
8. Delete a list
9. Delete an item
10. Add new item
			''')


	def choice(self, inp, contract):
		if inp == 1:
			contract.newList(str(input("Title of list: ")))
		elif inp == 2:
			lists = contract.getLists()
			pprint.pprint(lists)
		elif inp == 3:
			list = contract.getList(int(input("ID of list: ")))
			pprint.pprint(list)
		elif inp == 4:
			items =contract.getItems(int(input("ID of list: ")))
			pprint.pprint(items)
		elif inp == 5:
			list_id = int(input("ID of list: "))
			item_id = int(input("ID of item: "))
			item = contract.getItem(list_id, item_id)
			pprint.pprint(item)

		elif inp == 6:
			list_id = int(input("ID of list: "))
			title = str(input("New title for list with an ID of {}: ".format(list_id)))
			contract.updateList(list_id, title)

		elif inp == 7:
			list_id = int(input("ID of list: "))
			item_id = int(input("ID of item: "))
			description = str(input("New description of item: "))
			contract.updateItem(list_id, item_id, description)

		elif inp == 8:
			list_id = int(input("ID of list: "))
			contract.deleteList(list_id)

		elif inp == 9:
			list_id = int(input("ID of list: "))
			item_id = int(input("ID of item: "))
			contract.deleteItem(list_id, item_id)

		elif inp == 10:
			list_id = int(input("ID of list: "))
			description = str(input("Description of item: "))
			contract.newItem(list_id, description)

if __name__ == '__main__':
	c = Contract()
	cli = CLI()
	while True:
		try:
			cli.greet()
			inp = int(input("Number [1-8] "))
			if inp < 1 or inp > 10:
				raise ValueError
		except KeyboardInterrupt:
			sys.exit()
		except ValueError:
			print("Only pick a number from 1 - 8")

		cli.choice(inp, c)

