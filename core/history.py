from browser_history import get_history

print('==== LOADING BROWSER HISTORY ====')
info = get_history().histories


history = []
for element in info :
	history.append({
		'time': str(element[0]),
		'link': element[-1]
	})