# training data
training_data = [
    ['Green', 3, 'Apple'],
    ['Yellow', 3, 'Apple'],
    ['Red', 1, 'Grape'],
    ['Red', 1, 'Grape'],
    ['Yellow', 3, 'Lemon'],
]

# # # Column labels.
# # # These are used only to print the tree.
header = ["color", "diameter", "label"]


# classes
class QNode:
    def __init__(self, ques):
        self.ques = ques
        self.left = None
        self.right = None


class LabelNode:
    def __init__(self, label):
        self.label = label

    def __str__(self):
        return 'label >>>' + self.label


class Question:
    def __init__(self, col, value):
        self.col = col
        self.value = value

    def __str__(self):
        return 'question :' + str(self.col) + '-->' + str(self.value)


# basic functions


def label_counts(data):
    labels = {}
    for row in data:
        l = row[-1]
        if l not in labels:
            labels[l] = 0

        labels[l] += 1
    return labels


def giniIndex(data):
    # print(data)
    labels = label_counts(data)
    total = len(data)
    index = 0

    # print(labels, total)

    for i in labels:
        pi = labels[i]/total
        index += pi*(1-pi)
    return index


def giniGain(l, r):
    ll, lr = len(l), len(r)
    return (ll*giniIndex(l) + lr*giniIndex(r))/(ll+lr)


def compareValue(col, value):
    # print(col , value)
    if isinstance(value, int) or isinstance(value, float):
        return col >= value
    else:
        return col == value


def compareAtNode(row, ques):
    Qcol, Qvalue = ques.col, ques.value
    return compareValue(row[Qcol], Qvalue)


# tree helping functions
def partion(data, ques):
    true_data = []
    false_data = []

    for row in data:
        if compareAtNode(row, ques):
            true_data.append(row)
        else:
            false_data.append(row)

    return true_data, false_data


def find_best_split(data):
    ques = None
    best_gain = 1
    all_ques = []

    for row in data:
        vals = []
        for val in row[:-1]:
            vals.append(val)
        vals = set(vals)

        # adding all possible Q
        for val in vals:
            all_ques.append(Question(row.index(val), val))

    for q in all_ques:
        left_d, right_d = partion(data, q)
        x = giniGain(left_d, right_d)
        if x < best_gain:
            best_gain = x
            ques = q

    return best_gain, ques


# tree operations
def createTree(data):
    labels = label_counts(data)

    if (len(labels) == 1):
        # print(len(labels))
        return LabelNode(data[0][-1])

    else:
        gain, question = find_best_split(data)

        l, r = partion(data, question)

        if len(l) == 0 or len(r) == 0:
            print('false data , inaccurate data ,add more rows to dataset')
            print('---------------------')
            exit()

        node = QNode(question)
        node.left = createTree(l)
        # print(node.left.label)
        node.right = createTree(r)

        return node


def testTree(row, tree):
    if isinstance(tree, LabelNode):
        return tree.label
    else:
        if compareAtNode(row, tree.ques):
            return testTree(row, tree.left)
        else:
            return testTree(row, tree.right)


def printTree(tree, header, space='--'):
    if isinstance(tree, LabelNode):
        print(space, '<---------->', tree.label)
    else:
        print(space, tree.ques.value, '<=', header[tree.ques.col])
        space += '--'
        printTree(tree.left, header, space)
        printTree(tree.right, header, space)


def get_data(filename):
    import csv

    def read_csv(filename):
        with open(filename, newline='') as f_input:
            return [list(map(str, row)) for row in csv.reader(f_input)]

    NP = read_csv(filename)

    new_data = []

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
h = ["sepal.length", "sepal.width", "petal.length", "petal.width", "variety"]

tree = createTree(training_d)
print(testTree([6.3, 2.5, 4.9, 1.5], tree))
printTree(tree, h)
# tree = createTree(trai/ning_data)
