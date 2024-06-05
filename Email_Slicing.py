
print()
class EmailSlicing:
    def email(self):
        print('------------------------------------------------Welcomr to Email Slicing Programming-------------------------------------------------')

        mail=input('Enter your Email ID    :  ')
        print('-----------------------------------------------')
        
        if '@' not in mail or '.' not in mail:
            print('Invalid Email ID, (@) or (.) is not present \n Please provide Correct Email ID')
            print('-------------------------------------------------------------------------------------------------------------------------------------')
            self.email()

        elif len(mail)>320:
            print('Invalid Email ID,only 320 is maximum length \n Please provide Correct Email ID') 
            print('-------------------------------------------------------------------------------------------------------------------------------------')
            self.email()

        elif mail[0] in '1234567890' :
            print('starting character should not be numeric \n Please provide Correct Email ID')
            print('-------------------------------------------------------------------------------------------------------------------------------------')
            self.email()

        elif  mail[0] in "!$%&()*+,-/:;<=>?@[\\]^{|}~#":  
            print('starting character should not be special characters \n Please provide Correct Email ID') 
            print('-------------------------------------------------------------------------------------------------------------------------------------')
            self.email()
        
        elif mail[-1] in '1234567890' :
            print('Ending character should not be numeric \n Please provide Correct Email ID')
            print('-------------------------------------------------------------------------------------------------------------------------------------')
            self.email()

        elif  mail[-1] in "!$%&'()*+,-/:;<=>?@[\\]^`{|}~#":  
            print('Ending character should not be special characters \n Please provide Correct Email ID')   
            print('-------------------------------------------------------------------------------------------------------------------------------------')
            self.email()
        else:
                
            i=mail.index('@')
            j=mail.rindex('.')
            un=mail[0:i]
            dn=mail[i:]
            hn=mail[(i+1):]
            ex=mail[j:]

            print('User Name              : ',un)
            print('Domain Name            : ',dn)
            print('Host Name              : ',hn)
            print('Top Level Domain (TLD) : ',ex) 
            print('-------------------------------------------------------------------------------------------------------------------------------------')

check=EmailSlicing()
check.email()










    
