#encoding:utf-8
class Student(object):
    def __init__(self,name,score):
        super(Student,self).__init__()
        self.name = name
        self.score = score

    def printScore(self):
        print '%s:%d'%(self.name,self.score)

st1 = {'name':'Jack','score':94}
st2 = {'name':'Rose','score':89}

print st1['score']


st3 = Student('Nima',60)
st4 = Student('Shejingbing',61)

st3.printScore()
st4.printScore()