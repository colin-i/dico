
import hubs

def add(tree,path,column,model):
	it=model.get_iter(path)
	adr=model.get_value(it,hubs.COLUMNS.ADDRESS)