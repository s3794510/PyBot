# create a outer class
class Geeksforgeeks:  
    
    def __init__(self):
        # create a inner class object
        self.name = 'Geek'
        self.Inner = self.Inner(self.name)
    def show(self):
        print('This is an outer class')

    # create a 1st inner class 
    class Inner:
        def __init__(self, name):
            self.name = name
            # create a inner class of inner class object
            self.innerclassofinner = self.Innerclassofinner()

        def show(self, name):
            print(self.name, 'This is the inner class ', name)

        # create a inner class of inner
        class Innerclassofinner:
                        
            def show(self):
                print('This is an inner class of inner class')
    

obj = Geeksforgeeks()
obj.Inner.show(' DDD')