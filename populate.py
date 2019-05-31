from contract import Contract
import random


def populate_w_items(list_id, n=10):
	c = Contract()
	for i in range(n):
		c.newItem(list_id, "dsadzxcasdas")


def populate_w_lists(n = 10):
	c = Contract()
	for i in range(n):
		c.newList("List {}".format(n))

if __name__ == '__main__':
	populate_w_lists()
	for i in range(10):
		populate_w_items(random.randint(1,10), n=3)

		