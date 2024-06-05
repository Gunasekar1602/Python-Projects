   
class Acronym_Generator():

    def __init__(self):
        self.acronym=''
        print('Welcome to Acronym Generator Program !!')

    def display(self):
        inp=input('Enter The Input : ') 
    
        try:   
            Title_inp=inp.title()
            for i in Title_inp :
                if i.isupper():
                    self.acronym+=i
            print(self.acronym)

        except TypeError:
            print('Invalid Input Please \n Input Should be in String Data Type Enter the Corrcet input')     

obj=Acronym_Generator() 
obj.display()       



