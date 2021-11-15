
def hailstone(num):
	if num == 1: 
		return [num] #base case
	else:
		if num % 2 == 0:
			return [num] + hailstone(num//2) #if it is even number divide by two
		else:
			return [num] + hailstone(3*num+1) #if it is odd, perform operation

hailstone()