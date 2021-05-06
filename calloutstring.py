class Garrage:
    def __init__(self):
        self.name=[]
        
#     def __len__(self):
#         return len(self.name)
#     def __getitem__(self,i):
#          return self.name[i]
    # def __repr__(self):                             #ALTERNATIVE METHOD TO CALL OUT THE STRING 
    #     return f'Garrage {self.name}'
    
    def __repr__(self):                                #MEHTOD TO CALL OUT THE STRING 
        return f'Garrage with {len(self)} cars'          

about=Garrage()
about.name.append("i10")
about.name.append("i20")
about.name.append("Verna")
about.name.append("Creta")
about.name.append("i30")

print(len(about))
print(about[1])
print(about)
# print(about.name[2])


