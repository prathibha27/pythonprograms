class basic :
    def __init__(self,name):
     self.name=name;
    def show (self):
        print('basic--name :%s'%self.name)

obj1=basic('apricot')
obj1.show()
dir(basic)
dir(obj1)
