class demo:
    def getname(self,name):
        self.name=name
    def show(self):
        return self.name
    def saying(self):
        print("hello ....."+self.name)

first = demo()
second = demo()
first.getname("debasis")
first.saying()