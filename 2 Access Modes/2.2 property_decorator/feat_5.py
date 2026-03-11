class WindowDlg:
    def __init__(self, title, width, height):
        self.__title = title
        self.__width = None
        self.__height = None
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) == int and 0 <= value <= 10000:
            if self.__width:
                self.__width = self.width
                self.show()
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) == int and 0 <= value <= 10000:
            if self.__height:
                self.show()
            self.__height = value

    def show(self):
        print(f"{self.__title}: {self.__width}, {self.__height}")
