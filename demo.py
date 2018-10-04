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
	def __str__(self):
		return 'left:'+ str(self.v)+ ', right:'+str(self.v)+', threshold:'+ str(self.v)+'\n'

def get_column_array(matrix, i):#get a column array of index i
	column_array = []
	for j in range(0, len(matrix)):# j is the row number of the matrix
		column_array.append(matrix[j][i])
	return column_array

def get_threshold(column_array):#get threshold of a column array
	return sum(column_array)/len(column_array)
	

def get_groups(column_array, v):#based on a threshold v, divde array into two groups	
	print 'column: ', column_array
	greater_array = []
	smaller_array = []
	for j in range(0,len(column_array)):	
		greater_tuple = {'row': 0, 'value':0}
		smaller_tuple = {'row': 0, 'value':0}
		if column_array[j]>v:
			greater_tuple['row'] = j
			greater_tuple['value'] =column_array[j]
			greater_array.append(greater_tuple)
		else:
			smaller_tuple['row'] = j
			smaller_tuple['value'] = column_array[j]
			smaller_array.append(smaller_tuple)	
	return greater_array, smaller_array

def get_groups_matrix(matrix, i, v):
	column_array = get_column_array(matrix, i)
	greater_array, smaller_array = get_groups(column_array, v)
#	print 'greater array:', greater_array
#
#	print 'smaller array:', len(smaller_array)
	greater_index = []
	smaller_index = []
	for i in range(0, len(greater_array)):
		greater_index.append(greater_array[i]['row'])

	for i in range(0, len(smaller_array)):
		smaller_index.append( smaller_array[i]['row'])

	greater_matrix = []
	smaller_matrix = []
	for i in range(0, len(greater_index)):
		greater_matrix.append(matrix[greater_index[i]])

	for i in range(0, len(smaller_index)):
		smaller_matrix.append( matrix[smaller_index[i]])

	return greater_matrix, smaller_matrix
	

def evaluate(greater, smaller, best, i):#update the best ratio and correspoding index number
	abs_ratio = abs(len(greater)/len(smaller))
	if(abs_ratio-1<best['value']):
		best['value'] = abs_ratio
		best['index'] = i
	return best


def get_gini(matrix):
	num_attr = len(matrix[0])
	best = {'index':0,'value':10}
	for i in range(0,num_attr-1):#i is the index number
		column_array = get_column_array(matrix, i)
		#print column_array #optional output
		v = get_threshold(column_array)
		#print 'v:',v # ==========optional output
		greater, smaller = get_groups(column_array, v)
		#print greater #==========optional output
		#print smaller #===========optional output
		best = evaluate(greater, smaller, best, i)
		#print best #==========optional outpu
	return best['index']			


def build_tree(matrix, d):
	if d <2:
		print '\nbuilding tree node, depth:', d
		best_index = get_gini(matrix)
		print 'best index is: ', best_index #==========optional output 
		column_array = get_column_array(matrix, best_index)
		v = 	get_threshold(column_array)
		print "threshold is: ", v
		greater_matrix, smaller_matrix = get_groups_matrix(matrix, best_index, v)
		print 'greater matrix:',greater_matrix#==========optional output
		print 'smaller matrix:',smaller_matrix	#==========optional output
		d +=1
		left = build_tree(greater_matrix,d)
		#right = build_tree(smaller_matrix,d)
		node = Node(left, 4, v)
	else:
		node = Node(None, None, None)
	return node

#example 1 to demostrate how get_gini() works
a = [\
	[3,5,2,1],\
   [7,6,5,1],\
	[8,9,7,0]]
#b = load_bird()
print get_gini(a)


#building tree
root = build_tree(a,0)
print root

