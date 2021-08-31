import abc
class Drawable(metaclass=abc.ABCMeta):
    def __init__(self, x, y, visible=True):
        self.__x = x
        self.__y = y
        self.__visible = visible

    def getLoc(self):
        return (self.__x, self.__y)

    def getY(self):
        return self.__y

    def getVisible(self):
        return self.__visible

    def setVisible(self, temp):
        self.__visible = False

    def getX(self):
        return self.__x
    def setLoc(self,p):
        self.__x = p[0]
        self.__y = p[1]

    @abc.abstractmethod
    def draw(self, surface):
        pass

    @abc.abstractmethod
    def getRect(self):
        pass