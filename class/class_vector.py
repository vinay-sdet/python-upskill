class TwoDVector:
    def __init__(self,i,j):
        self.i = i
        self.j = j

    def show(self):
        print(self.i, self.j)

class ThreeDVector(TwoDVector):        
    def __init__(self, i, j,k):
        super().__init__(i, j)
        self.k = k
    
    def show(self):
        print(self.i, self.j,self.k)


obj2D = TwoDVector(2,3)
obj2D.show()
obj3D = ThreeDVector(4,5,6)
obj3D.show()
obj3D_new = ThreeDVector(4,5,7)
obj3D_new.show()



