import csv
def load_bird():
	with open('birds.csv', 'rb') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
		data = []
		iterreader = iter(spamreader)
		next(iterreader)
		for row in iterreader:
			tuple =[]
			tuple.append(row[1])
			tuple.append(row[2])
			tuple.append(row[3])
			data.append(tuple)
	print "=================\n"
	print data
	print "=================\n"
	return data

class Node:
	def __init__(self, left, right, v):
		self.left = left
		self.right = right
		self.v = v

def get_column_array(matrix, i):#get a column array of index i
	column_array = []
	for j in range(0, len(matrix)):# j is the row number of the matrix
		column_array.append(matrix[j][i])
	return column_array

def get_threshold(column_array):#get threshold of a column array
	return sum(column_array)/len(column_array)
	

def get_groups(array, v):#based on a threshold v, divde array into two groups	
	greater_tuple = {'row': 0, 'value':0}
	smaller_tuple = {'row': 0, 'value':0}
	greater_array = []
	smaller_array = []
	for i in range(0,len(array)):
		if array[i]>v:
			greater.append(array[i])
		else:
			smaller.append(array[i])
			
	return greater, smaller

def get_groups_with_row_number(matrix, i, v):
	column_array = get_column_array(matrix, i)
	

def evaluate(greater, smaller, best, i):#update the best ratio and correspoding index number
	abs_ratio = abs(len(greater)/len(smaller))
	if(abs_ratio-1<best['value']):
		best['value'] = abs_ratio
		best['index'] = i
	return best


def get_gini(matrix):
	num_attr = len(matrix[0])
	best = {'index':0,'value':10}
	for i in range(0,num_attr):#i is the index number
		column_array = get_column_array(matrix, i)
		#print column_array #optional output
		v = get_threshold(column_array)
		#print 'v:',v # ==========optional output
		greater, smaller = get_groups(column_array, v)
		#print greater #==========optional output
		#print smaller #===========optional output
		best = evaluate(greater, smaller, best, i)
		print best #==========optional outpu
	return best['index']			


def build_tree(matrix):
	best_index = get_gini(matrix)
	column_array = get_column_array(matrix, best_index)
	


	root = Node(1,2,3)

	return root

#example 1 to demostrate how get_gini() works
a = [[3,5],[7,6],[8,9]]
#b = load_bird()
print get_gini(a)


#building tree
build_tree(a)


