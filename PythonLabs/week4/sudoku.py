import math
sudokugrid = [
        [7,0,0,0,3,4,8,0,0],
        [8,0,4,6,0,0,0,0,0],
        [0,3,9,0,5,0,0,0,0],
        [1,0,0,5,0,0,6,0,0],
        [0,4,0,7,0,9,0,3,0],
        [0,0,3,0,0,8,0,0,9],
        [0,0,0,0,7,0,3,2,0],
        [0,2,6,0,0,1,9,0,5],
        [0,0,7,9,2,0,0,0,4]
]

size = len(sudokugrid)
print("sudoku grid is " + str(size) + " by " + str(size))
for row in range(size):
	print(sudokugrid[row])
area = int(math.sqrt(size))	
print("Size of each area: " + str(area) + " by " + str(area))
gridUpdated = True
while (gridUpdated):
	gridUpdated = False
target = 1
row = 0
while (row < size):
	col = 0
	while(col < size):
		print("\nChecking the following area for target value: ",
		target)
		print("start row: ", row)
		print("end row: ", row + area - 1)
		print("start col: ", col) 
		print("end col: ", col + area - 1) 
		print()
		# print ("Looking for ", target)
		foundtarget = False
		for r in range(row, row + area):
			for c in range(col, col + area):
				# print ("Checking - Row: ", r, " Column: ", c, end="")
				if (sudokugrid[r][c] == target):
					# print (" - Target is already in area")
					foundtarget = True
					break
				# else:	
				# 	print (" - Not here")
		print ("The target value ", target, end="")
		if not foundtarget:
			print(" was not in area")
			placetarget = []
			for r in range(row, row+area):
				for c in range(col, col+area):
					print ("Checking row ", r, " column ", c)
					if (sudokugrid[r][c] == 0):
						print("Square available")
						currentRowValues = sudokugrid[r]
						# and values for the column
						currentColValues = [item[c] for item in sudokugrid]
						print ("Row contains ", currentRowValues)
						print ("Col contains ", currentColValues)
						if target not in currentRowValues and target not in currentColValues:
							print("Could place ",target," at (",r,",",c,")")
							placetarget.append([r,c])
						if (len(placetarget) == 1):
						 	print ("placed ", target, " at ", placetarget[0][0], " x ", placetarget[0][1])
						 	sudokugrid[placetarget[0][0]][placetarget[0][1]] = target	
						 	gridUpdated = True
			print(" was found in area")	
		col += area
	row += area

for row in range(size):
	print (sudokugrid[row])	
