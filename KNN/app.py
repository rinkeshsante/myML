class KNN:
  "the simple program to find k nearest neighbor using python"
  def __init__(self,data):
    'add data to obj'
    self.data = data
  

  def distance( self,l1 ,l2):
      'equclidian distance between two points in multidimensions'
      # print(l1,l2)
      import math
      sum = 0
      for i,j in zip(l1 ,l2):
        sum += (i-j)**2
      return math.sqrt(sum)
  
  
  def repetation_count(self ,data):
      'to find all reapeation in vales'
      ls = {}

      for i in data:
        if i  not in ls:
          ls[i] = 0
      
        ls[i]+=1

      return ls

  def predict(self, point ,k = 3):
    'application'
    dist_ls = []
    for row in self.data:
      dist = self.distance(row[:-1],point)
      dist_ls.append([dist , row[-1]])
    
    dist_ls.sort()
    
    label = []
    # print(dist_ls)

    for i in dist_ls[:k]:
      label.append(i[1])

    # print(dist_ls)

    rep = self.repetation_count(label)

    best_count = 0
    best_label = ''

    for i in rep:
      if rep[i] > best_count:
        best_count = rep[i]
        best_label = i

    # print(best_count , best_label)

    return (best_label)



# test data points
data_points = [
  [1,10,2,'A'],
  [1,1,3,'B'],
  [1,12,2,'A'],
  [1,2,3,'B'],
  [2,1,3,'B'],
  [2,2,2,'B'],
  [1,0,5,'B'],
]

model = KNN(data_points)
print(model.predict( [2,1,8] ))

# to load data from iris dataset
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

data_iris = get_data('iris.csv')
header_iris = ["sepal.length","sepal.width","petal.length","petal.width","variety"] 

model = KNN(data_iris)
print(model.predict( [6.3,3.3,6,2.5] , 10))



# def distance( l1 ,l2):
#   # print(l1,l2)
#   sum = 0
#   for i,j in zip(l1 ,l2):
#     sum += (i-j)**2
#   return math.sqrt(sum)


# def repetation_count(data):
#   ls = {}

#   for i in data:
#     if i  not in ls:
#       ls[i] = 0
  
#     ls[i]+=1

#   return ls


# def KNN(data ,  point ,k = 3):
#   dist_ls = []
#   for row in data:
#     dist = distance(row[:-1],point)
#     dist_ls.append([dist , row[-1]])
  
#   dist_ls.sort()
  
#   label = []
#   # print(dist_ls)

#   for i in dist_ls[:k]:
#     label.append(i[1])

#   # print(dist_ls)

#   rep = repetation_count(label)

#   best_count = 0
#   best_label = ''

#   for i in rep:
#     if rep[i] > best_count:
#       best_count = rep[i]
#       best_label = i

#   print(best_count , best_label)

#   return (best_label)


