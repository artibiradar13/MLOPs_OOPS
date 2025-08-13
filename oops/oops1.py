#intialise a class
class employee:
    #special method/magic 
    def __init__(self):
        self.id =1234
        self.salary=450000
        self.designation="SDE"

    def travel(self,destination):
        print(f"emolyee is travelling to {destination} ")

#create a obj/instance  
sam =employee()

print(sam.salary)   

sam.travel("kerala") 