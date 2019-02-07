import json

def check_params_exist(parameters, list):
	if parameters == None:
		return list[0]
	for l in list:
		if l not in parameters.keys():
			return l
	return None
	
	
	