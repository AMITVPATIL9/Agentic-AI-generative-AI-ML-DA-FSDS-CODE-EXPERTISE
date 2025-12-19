
    
#class define karne ka syntax,tu mat bata mein likh raha hu 
class house:
    def __inti__(self):
        self.hall = 1
        self.bedroom = 2
        self.toilet = 5
        
    def open_house(self):
        print('welcome to home')
        
        
my_house1 = house()
my_house2 = house()
# blueprnt se 2 object create kiya
# house 1 mein 2 chije hain 
#ist = attributes
#2nd = method(task,functon)


#---------------------------
#2nd house  ko banao
my_house2.bedroom = 5
my_house2.toilet = 10
my_house2.hall = 3
#-----------------------------------
my_house1.open_house()
print("---------------------------------------------------")
print('no of bedroms in house2',my_house2.bedroom)
print('no of toilets in house2',my_house2.toilet)
print('no of halls in house2',my_house2.hall)
print("---------------------------------------------------")
my_house2.open_house()


    