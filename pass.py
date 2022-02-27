import random

lowers = 'qwertyuiopasdfghjklzxcvbnm'
uppers = 'QWERTYUIOPASDFGHJKLZXCVBNM'
numbers = '0123456789'
symbols = '!@#$%^&'

All = lowers + uppers + numbers + symbols
Length = 16

password = ''.join(random.sample(All, Length))
print("Password: ", password)