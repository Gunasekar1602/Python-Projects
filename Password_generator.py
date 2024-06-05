import random
pass_length=int(input('Enter the length of password : '))
s='abcdefghijklmnopqrstuvwxyzQWERTYUIOPASDFGHJKLZXCVBNM1234567890~!@#$%^&*'

'''list to string >> .join()'''
'''string to list >> .split()'''

password=''.join(random.sample(s,pass_length))
print(password)