import sys
import random
import timeit

def print_board(b,l, x, y):
	for i in range(l):
		for t in range(l):
			if x == i and y == t:
				print("X  ", end = "") 
			else:			
				print(str(b[i][t]) + " ",end = "")
				if b[i][t] < 10:
					print(" ", end = "")
		print("\n")



def pd(b,l):
	for i in range(l):
		for t in range(l):
			print(str(b[i][t]) + " " ,end = "")
			if b[i][t] < 10:
				print(" ", end = "")
		print("\n")



def used_board(b,x, y, l):
	summ = 0
	for i in range(l):
		for t in range(l):
			summ = summ + b[x+i][y+t]
	if summ == 0:
		return True
	else:
		return False

def tiling(b,x, y, v,step,c):

	if v == 2:
#		print("if step: " + str(step))
		for i in range(v):
			for t in range(v):
				if b[x+i][y+t] == 0:
					b[x+i][t+y] = step
		step = step + 1
#		print("fi step: " + str(step))
#		pd(b, c)
	
	else:
#		print("X Y V" + str(x) + "   " + str(y) + "   " + str(v))
		v = v//2
		if used_board(b, x, y, v):
			b[x+v-1][y+v-1] = step
		if used_board(b, x+v, y, v):
			b[x+v][y+v-1] = step
		if used_board(b, x, y+v, v):
			b[x+v-1][y+v] = step
		if used_board(b, x+v, y+v, v):
			b[x+v][y+v] = step
#		print("re step: " + str(step))
#		pd(b, c)
		step = step + 1
#		print("step:  " + str(step))
		step = tiling(b, x, y, v, step, c)
#		print("re step: " + str(step))
		step = tiling(b, x+v, y, v, step, c)
#		step = step+pow(2,v-2)
		step = tiling(b, x, y+v, v, step, c)
#		step = step+pow(2,v-2)
		step = tiling(b, x+v, y+v, v, step, c)


	return step

def main():

	v = int(sys.argv[1])
	v = pow(2, v)
	board = []
	for i in range(v):
		board.append([])
	for i in range(v):
		for t in range(v):
			board[i].append(0)
	
	x = random.randint(0,v-1)
	y = random.randint(0,v-1)
	board[x][y] = 1

	s = tiling(board, 0, 0, v, 1, v)
	print_board(board, v, x, y)




start = timeit.default_timer()
main()
stop = timeit.default_timer()
print (stop - start)

