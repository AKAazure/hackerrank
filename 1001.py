def cutTheTree(data, edges):
    # Write your code here
    dot_dict=dict()
    min=0
    for i in range(len(data)):
        dot_dict[i+1]=dot(data[i])
        min+=data[i]

    for i in edges:
        print(i)
        dot_dict[i[0]].post.append(dot_dict[i[1]])
        dot_dict[i[1]].pre.append(dot_dict[i[0]])
    min+=1
    current=0
    for i in edges:
        current=cut_edge(i,dot_dict)
        if current<min:
            min=current
    return current

def cut_edge(i,dot_dict):
    dot_dict[i[0]].post=None
    dot_dict[i[1]].pre=None
    print(dot_dict[i[0]].post,dot_dict[i[0]].pre)
    resultA=tree_cal(dot_dict[i[0]])
    resultB=tree_cal(dot_dict[i[1]])
    dot_dict[i[0]].post=dot_dict[i[1]]
    dot_dict[i[1]].pre=dot_dict[i[0]]
    return abs(resultA-resultB)

def tree_cal(dots):
    counter=0
    if dots.pre:
        counter+=tree_cal(dots.pre)
    if dots.post:
        counter+=tree_cal(dots.post)
    return counter

class dot(object):
    def __init__(self,value):
        self.val=value
        self.post=[]
        self.pre=[]

cutTheTree(
    [100,200,100,500,100,600],[[1,2],[2,3],[2,5],[4,5],[5,6]])