from abc import ABC, abstractmethod
class Father (ABC):
    @abstractmethod
    def disp (Self):
        pass
    def show (self):
        print("Concrete method")
class Child(Father):
    def disp(Self):
        print("defining abstract method")

c= Child()
c.disp()
c.show()
