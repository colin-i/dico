
import hubs
import reqs

def add(tree,path,column,model):
	it=model.get_iter(path)
	adr=model.get_value(it,hubs.COLUMNS.ADDRESS)
	reqs.requ("hub.add",{"enc" : "", "huburl" : adr})