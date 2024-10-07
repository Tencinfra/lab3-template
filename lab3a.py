#!/usr/bin/env python3

# return_text_value() function
def return_text_value():
    name = 'Terry'
    greeting = 'Good Morning ' + name
    return greeting

text = return_text_value()
print(text)

# Author ID: Ctenzin

# return_number_value()  function
def return_number_value():
    num1 = 10
    num2 = 5
    num3 = num1 + num2
    return num3

number = return_number_value()
print(number)
print(number + 5)
print(return_number_value() + 10)


# Main Program

if __name__ == '__main__':
    print('python code')
    import lab3a
    text = lab3a.return_text_value()
    print(text)
    print(lab3a.return_number_value())
