class cylinder:
   
 def __init__(self,h=None,r=None):
         self.__h = h
         self.__r = r  # private data members
 def __str__(self):
        return "cylinder with height {} and radius {}".format(self.h,self.r)
 def volume(self):
        return 3.14*self.__r*self.__r*self.__h  

c1 = cylinder(12,3)
#c2=cylinder()

#c2.h=6
#c2.r=10
#print(c2)

print(c1.volume())  
