from functools import cmp_to_key

X = [l.strip() for l in open('input.txt')]
labels = 'AKQJT98765432'

def sorting(a, b):
	if a[0] != b[0]:
		return a[0] - b[0]
	for i in range(5):
		if a[1][i] != b[1][i]:
			return labels.index(a[1][i]) - labels.index(b[1][i])

def get_score(hand, p2=False):
	cards = { c: hand.count(c) for c in set(hand) }
	if p2 and 'J' in cards and len(cards) > 1:
		bonus = cards['J']
		del cards['J']
		max_key = max(cards, key=cards.get)
		cards[max_key] += bonus
	max_val = max(cards.values())
	if max_val == 5:
		score = 0
	elif max_val == 4:
		score = 1
	elif max_val == 3:
		score = 2 if 2 in cards.values() else 3
	elif max_val == 2:
		score = 4 if list(cards.values()).count(2) == 2 else 5
	else:
		score = 6
	return score

p1, p2 = [], []
for line in X:
	hand, bid = line.split()
	p1.append((get_score(hand), hand, int(bid)))
	p2.append((get_score(hand, True), hand, int(bid)))

p1.sort(key=cmp_to_key(sorting))
labels = ''.join(labels.split('J')) + 'J'
p2.sort(key=cmp_to_key(sorting))

get_winnings = lambda r: sum([(len(r) - i) * bid for i, (_, _, bid) in enumerate(r)])
print(get_winnings(p1))
print(get_winnings(p2))
