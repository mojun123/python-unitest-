def deduplicate_list(l_data):
	if not isinstance(l_data, list):
		raise Exception("param is not list")

	if not l_data:
		print("[Warning]param is null")
		return l_data

	new_l_data = list(set(l_data))
	new_l_data.sort(key = l_data.index)

	return new_l_data