def mix2(x, y):
	yawConst = 1;
	outputBound = 255.0#the maximum absolute value of input
	inputBound = 1000.0#the maximum absolute value of input
	scaleConst = outputBound/inputBound

	left = (y+(x*yawConst))*scaleConst
	right = (y-(x*yawConst))*scaleConst

	#constrain the output to our outputBound
	if left > 255:
		left = 255
	if left < -255:
		left = -255
	if right > 255:
		right = 255
	if right < -255:
		right = -255
	#deadband isn't important because the motors aren't powerfull enough to overcome stiction.

	return left, right

cardinal = [
		[0, 1, 'forward'],
		[0, -1, 'backward'],
		[1, 0, 'right'],
		[-1, 0, 'left']
	]

forward = [
	[-1, 1, 'forward left'],
	[-.8, 1, 'forward softLeft'],
	[-.2, 1, 'forward driftLeft'],
	[0, 1, 'forward'],
	[.2, 1, 'forward driftRight'],
	[.8, 1, 'forward softRight'],
	[1, 1, 'forward right']
]


for coord in cardinal:
	print coord
	print mix2(coord[0]*1000, coord[1]*1000)
	print "---"

for coord in forward:
	print coord
	print mix2(coord[0]*1000, coord[1]*1000)
	print "---"
