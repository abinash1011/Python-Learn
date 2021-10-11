'''
File Created: Monday, 11th October 2021 5:48:43 pm
@Author: Abinash1011
-----
Last Modified: Monday, 11th October 2021 6:08:22 pm
Modified By: Abinash1011
-----
'''
f = open('file_handling/jh/1200px-Image_created_with_a_mobile_phone.png', 'rb')

f1 = open('file_handling/jh/pic.jpg', 'wb')

for i in f:
    f1.write(i)