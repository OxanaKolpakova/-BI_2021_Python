class my_class(list):

    def add(self, *a):
        for i in a:
           if i > 0:
             self.append(i)
        return(self)
