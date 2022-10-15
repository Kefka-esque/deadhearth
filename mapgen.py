# proof of concept to create a list of lists that will hold the game area to be rendered
# eventually this will be a fully-fledged semi-random mapgenerator

i = 0
test = [[]]
while i < 32:
	o = 0
	while o < 32:
		test[i].append(o)
		o += 1
	if i < 31:
		test.append([])
	i += 1

# let's test if it works properly
for item in test:
	print(item)
print(len(test))