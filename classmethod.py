class Classmethod():

    @classmethod                #important key (@classmethod)
                                #this classmethod provide us prevent the use of the 'self' class ,  however we can also name whatever we want
                                
    def randomm(just):
        print(just.__name__)

jatin=Classmethod()
jatin.randomm()
