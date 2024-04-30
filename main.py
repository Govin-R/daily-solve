def sum(a):
	val = [x in a if x>0]
	return sum(val)

print(sum([1,2,3,4,5]))