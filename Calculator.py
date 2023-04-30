def canculator(num, num2, operator):
    if operator == '+':
        print('sum', num + num2) # 
    elif operator == '-': 
        print('Subtraction [səbˈtrakSH(ə)n]' , num - num2)
    elif operator == '*': 
        print('Multiplication [məltəpləˈkāSH(ə)n]', num * num2)
    elif operator == '/': 
        print('Division [dəˈviZHən] [dɪˈvɪʒən]', num / num2)


    
while True: # До : загаловок, а после инструкция 

    num = float(input('num1'))
    operator = input('operator')
    num2 = float(input('num2'))
    canculator(num, num2, operator)

   
