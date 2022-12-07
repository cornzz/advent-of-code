X = [l.strip() for l in open('input.txt')][0]

def get_index(window):
	for i in range(len(X)):
		w = X[i:i+window]
		if len(set(w)) == window:
			return i + window

print(get_index(4))
print(get_index(14))
