print()
class Quizz_Game():
    def __init__(self):
        
        self.dict={'1.What is the National Animal of India' : 'tiger',
                   '2.Which river is considered the Holiest in Hinduism':'ganga',
                   '3.What is the Capital City of India': 'delhi',
                   '4.What is the National Bird of India':'peacock',
                   '5.What is the Biggest State in India':'rajasthan',
                   '6.What is the Highest Mountain Peak in India':'kanchenjunga'}
        self.C_a=0
        self.W_a=0
        print('---------------------------------------------------Welcome to the Quiz Game--------------------------------------------------')
        self.name=input('Enter your Name               : ')
        self.age=int(input('Enter your Age                : '))
        self.gender=input('Enter your Gender             : ')
        self.nationality=input('Enter your Nationality        : ')
        print()
    def Questions(self):
        print('------------------------Quiz Questions-------------------------')
        for i, j in self.dict.items():
            print(i) 
            print()
            ans=input('Enter Your Answer : ') 
            
            if ans.lower()==j:
                print('Correct Answer')
                print()
                self.C_a+=1
            else:
                print('Wrong Answer')
                print()
                self.W_a+=1    
        print()
        print('------------Personal Detaails-------------')
        
        print('Name               : ',self.name)
        print('Age                : ',self.age)
        print('Gender             : ',self.gender)
        print('Nationality        : ',self.nationality)
        print('-----------------Score-------------------')
        print('Correct Answers    :  ',self.C_a)
        print('Wrong Answers      :  ',self.W_a)
        print('Total marks        :  ',self.C_a-self.W_a)
obj=Quizz_Game()
obj.Questions()