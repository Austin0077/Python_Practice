import pprint

game= {'rope':1,'torch':6,'gold coin':42,'dagger':1,'arrow':12}

def displayInventory(Inventory):
	print("Inventory:")
	item_total = 0
	for k,v in Inventory.items():
		print(str(v)+ ' '+ k)
		item_total += v
	print("Total number of items: "+ str(item_total))

displayInventory(game)