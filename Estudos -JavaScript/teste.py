number = 0 

def adicionar(n):
    number = n
    
    if number == 15000:
        pass
    else:
        number += 1
        print(number)
        adicionar(number)

adicionar(number)