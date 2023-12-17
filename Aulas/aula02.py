#Trabalhando com strings

Topics:

print function
print('Hello World') - 'Hello Pikitos'

variables: snake_case - my_message

quotes: ' ' " " """ """ 'pikitos\'s course'

len()

index: print(my_message[0])  my_message[0:5] (my_message[:5])
                        #first is inclusive, last one isn't
                        this is called slicing (make a video about it)

methods (function of objects): lower upper count('i') split find('i') replace strip

concatenation: msg1 = 'Olá', msg2 = 'Pikitos'
                message = msg1 + ', ' + msg2

f string: message = f'{msg1}, {msg2.upper()}. Sejam bem vindos!'

immutability
msg = 'wiiii'
msg = msg.replace('w', 'x')
print(msg)