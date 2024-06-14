
class Point:
    
    def __init__(self, val) -> None:
        self.x = val

    @property
    def x(self):
        return self.__esh
    
    @x.setter
    def x(self, val):
        self.__esh = val
        print('foo')
    
    @x.getter
    def x(self):
        print ('bar')
        return self.__esh

if __name__ == '__main__':
    
    p = Point(7)
    # p.x = 9

    print(p.x)

    # y = p.x
