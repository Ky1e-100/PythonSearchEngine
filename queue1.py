def addend(list, dict, value):
	list.append(value)
	if value in dict:
		dict[value] += 1
	else:
		dict[value] = 0
	
def removestart(list, dict):
	if len(list) == 0:
		return None
	if dict[list[0]] == 0:
		del dict[list[0]]
	else:
		dict[list[0]] -= 1
		
	return list.pop(0)

def containshash(dict,value):
	if value in dict:
		return True
	return False