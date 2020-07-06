from collections import OrderedDict as od
import pyperclip

results = od()
p5Characters = ['Morgana', 'Joker', 'Ryuji', 'Ann', 'Yusuke', 'Makoto', 'Futaba', 'Haru', 'Akechi', 'Kasumi', 'Phantom Kirby', 'Shinya Kirby']
pins_string = ' Pins'
one_of_each = 'Yes, I want 1 of each.'
sourceText = pyperclip.paste()

for item in p5Characters:
	results[item] = sourceText.count(item)

for num_of_pin in range(3, 10):
	results['Phantom Kirby'] += sourceText.count(str(num_of_pin) + pins_string)

for item in results.keys():
	results[item] += sourceText.count(one_of_each)

for k, v in results.items():
	print(f'{k:>13}: {v:>3}')