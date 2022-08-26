class var():
    def __init__(self, name, kind, value):
        self.name = name
        self.kind = kind
        self.value = value

    def __repr__(self):
        return str(self.value)

    

class words(var):
    def __init__(self, name, kind, value):
        super.__init__(self, name, kind, value)
    
x = 'say("hello")'

prefix = x[0:x.index('(')]

print(prefix)