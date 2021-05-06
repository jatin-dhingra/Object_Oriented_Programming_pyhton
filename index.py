class Garrage:
    def __init__(self):
        self.name=[]
    def __len__(self):
        return len(self.name)
    def __getitem__(self,i):
        return self.name[i]

about=Garrage()
about.name.append("i10")
about.name.append("i20")
about.name.append("Verna")
about.name.append("Creta")
about.name.append("i30")

print(len(about))
print(about[1])  # alternative method of printing out index ,
                 # but here we defined a classical method of printing out index method print(about.name[2])


