from sys import argv
import string
from collections import defaultdict

script, filename = argv

open_file = open(filename).read().lower()

d = defaultdict(int)
for word in open_file.split():
	word = word.strip(",?!.'\"*@#%^()[]{}|\\/<>~-_=+")
 	d[word] += 1

sorted_list = [x for x in d.iteritems()]
sorted_list.sort(key=lambda x: x[0]) # sorts by key
sorted_list.reverse() # reverses so like items will be in order after 2nd sort

sorted_list.sort(key=lambda x: x[1]) # sorts by value
sorted_list.reverse()

for items in sorted_list:
	print items