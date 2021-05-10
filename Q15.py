# hyphen-separated sequence after sorting them alphabetically
str="green-red-yellow-black-white"
items=[n for n in str.split('-')]
items.sort()
print('-'.join(items))
