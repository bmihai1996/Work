class Agent():
    
    origin = "USA"
    
    def __init__(self,name,height,weight):
        self.name = name
        self.height = height
        self.weight = weight
        
    
x = Agent('Jose',6,170)
print(x.weight)



x.weight = 160
print(x.weight)
        