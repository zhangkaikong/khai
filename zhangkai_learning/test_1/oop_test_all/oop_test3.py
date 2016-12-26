class Parent(object):

    def __init__(self):
        self.name = 'I\'am the parent!'
        print 'Parent'

    def bar(self,name):
        print name,'from parent'

class Child(Parent):

    def __init__(self,name):
        Parent.__init__(self)
        self.name = name

    def bar(self,name):
        Parent.bar(self,name)
        print name,'from the child'

child = Child('Jack')
child.bar('kao')