# training_data = [
#         ['Green', 3, 'Apple'],
#         ['Yellow', 3, 'Apple'],
#         ['Red', 1, 'Grape'],
#         ['Red', 1, 'Grape'],
#         ['Yellow', 3, 'Lemon'],
# ]

# # Column labels.
# # These are used only to print the tree.
# header = ["color", "diameter", "label"]



class Node:
    def __init__(self, data):
        self.data = data
        self.ques = None
        self.left = None
        self.right = None

class Question:
    def __init__(self, col , value):
        self.col = col
        self.value = value




def printTree( node ,header=[],f = '-'):
    if node != None:

        print(f,'>',end='' , sep='')

        if isinstance(node.ques, Question):
            print('condition :',header[ node.ques.col],',', node.ques.value)
        else:
            print('leaf',len(node.data), len(node.data))
        
        f += '--'
        printTree(node.left,header,f )
        printTree(node.right,header,f)
        f = f[:-2]
        


def label_counts(data):
    # print(data)
    labels = {}
    for row in data:
        # print(row)
        # last column will be label
        l = row[-1]

        if l not in labels:
            labels[l] = 0
        
        labels[l] += 1
    
    return labels

# print(label_counts(training_data))




def gini(data):
    # print(7)
    # print(data)
    # print(7)
    classes = label_counts(data)

    impurity = 1
    for lbl in classes:
        prob_of_lbl = classes[lbl] / float(len(data))
        impurity -= prob_of_lbl**2
    return impurity

    

def getInfoGain(current , left_data , right_data):
    
    p = float(len(left_data)) / (len(left_data) + len(right_data))
    return current - p * gini(left_data) - (1 - p) * gini(right_data)



def compareValue(col, value):
    # print(col , value)
    if isinstance(value, int) or isinstance(value, float):
        return col >= value
    else:
        return col == value

# print(compareValue(1,1))
# print(compareValue('1','1'))
# print(compareValue('1','2'))

# def unique_vals(rows, col):
#     """Find the unique values for a column in a dataset."""
#     return set([row[col] for row in rows])

def unique_data(data):
    d2 = []
    for i in data:
        if i not in d2:
            d2.append(i)
    
    return d2

# print(unique_data([(1,1),(1,2),(1,1)]))


def find_best_split(data):
    info = 0
    ques = None

    all_ques = []
    for row in data:
        for val in row[:-1]:
            all_ques.append(Question(row.index(val) , val))

            # print('ri , v',row.index(val) , val)
            
            # x = getInfoGain(data, row, col)
            # if x > info:
            # 	info = x
            # 	ques = [row, col]
    
    all_ques = set(all_ques)

    current_gain = gini(data)
    g_ls = []

    for q in all_ques:
        left_d , right_d = partion(data , q)
        # print('------')
        # print(left_d,right_d)
        x = getInfoGain(current_gain, left_d, right_d)
        # g_ls.append(x)
        if x > info:
            info = x
            ques = q
    
    
    # print('i ,q',info)
    return info, ques




def partion(data, ques):
    Qcol ,Qvalue = ques.col , ques.value
    true_data = []
    false_data = []

    for row in data:
        if compareValue(row[Qcol], Qvalue):
            true_data.append(row)
        else:
            false_data.append(row)

    
    # print('t', true_data)
    # print('f',false_data)
    return true_data , false_data


# print(partion(training_data , Question(1,2)))

def getTree(data ):
    info, question = find_best_split(data)

    node = Node(data)

    if info <= 0:
        return node

    left , right = partion(data , question)

    node.left = getTree(left)
    node.right = getTree(right)
    node.ques = question

    return node

def get_data(filename):
    import csv

    def read_csv(filename):
        with open(filename, newline='') as f_input:
            return [list(map(str, row)) for row in csv.reader(f_input)]

    NP = read_csv(filename)

    new_data=[]

    for row in NP:
        ls = []
        
        for d in row:
            try:
                ls.append(float(d))
            except:
                ls.append(d)
        new_data.append(ls)

    return new_data


training_d = get_data('iris.csv')
h = ["sepal.length","sepal.width","petal.length","petal.width","variety"]    

print(training_d)
# printTree(getTree(training_d),h)

def classify(row , tree):
    if isinstance(tree , Node):
        ques = tree.ques
        Qcol ,Qvalue = ques.col , ques.value

        
        if compareValue(row[Qcol], Qvalue):
            classify(tree.left)
        else:
            classify(tree.right)
        
    