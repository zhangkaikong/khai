class Parent(object):
    def __init__(self,name,title):
        self.name = name
        self.title = title
        print 'I am the parent!'

    def pregnant(self):
        print '%s gets pregnant and scream out %s'%(self.name,self.title)

class Child(Parent):
    def __init__(self,name,title):
        super(Child,self).__init__(name,title)
        self.pregnant()

    def pregnant(self):
        super(Child, self).pregnant()
        print 'The child can also get pregnant'

parent = Parent('Gao Sheng','Nima')
parent.pregnant()

child = Child('son','Nima')
child.pregnant()

