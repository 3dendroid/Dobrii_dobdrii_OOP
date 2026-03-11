# def __new__(cls, *args, **kwargs):
#     return super ().__new__ (cls)
#
#
# class Parent:
#     def greet(self):
#         return "Hello from Parent"
#
#
# class Child (Parent):
#     def greet(self):
#         parent_greeting = super ().greet ()
#         return f"{parent_greeting} and Hello from Child"
#
#
# c = Child ()
# print (c.greet ())  # Hello from Parent and Hello from Child


# class Point:
#     def __new__(cls, *args, **kwargs):
#         print ('new for ' + str (cls))
#         return super ().__new__ (cls)
#
#     def __int__(self, x, y):
#         print('init for ' + str (self))
#         self.x = x
#         self.y = y
#
# pt=Point(1,2)
# print(pt)

class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        DataBase.__instance = None

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f'Connecting to DataBase: {self.user}, {self.psw}, {self.port}')

    def close(self):
        print('closing')

    def read(self):
        return 'data from db'

    def write(self, data):
        print(f'writing {data} to db')


db = DataBase('root', '123', 3306)
db2 = DataBase('root2', '555', 8888)

print(id(db), id(db2))

db.connect()
db2.connect()
