
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#@created: 14.09.2021
#@author: Marina Popova

class CoffeeMachine:
    resources_name = ['water', 'milk', 'coffee beans', 'cups', 'money']
    def __init__(self, w = 400, m = 540, cb = 120, c = 9, mn = 550):
        self.resources = [w, m, cb, c, mn]
        self.workable = True
    
    def status(self):
        print('The coffee machine has:')
        for i in range(len(self.resources)-1):
            print(f'{self.resources[i]} of {CoffeeMachine.resources_name[i]}')
        print(f'${self.resources[-1]} of {CoffeeMachine.resources_name[-1]}')

    def fill(self):
        self.resources[0] += int(input('Write how many ml of water you want to add:'))
        self.resources[1] += int(input('Write how many ml of milk you want to add:'))
        self.resources[2] += int(input('Write how many grams of coffee beans you want to add:'))
        self.resources[3] += int(input('Write how many disposable coffee cups you want to add:'))

    def buy(self):
        check = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        choices = {'1': [250, 0, 16, 1, 4],
                    '2': [350, 75, 20, 1, 7],
                    '3': [200, 100, 12, 1, 6]}
        if check == 'back':
            return
        else:
            for i in range(len(self.resources)-1):
                if self.resources[i] - choices[check][i] < 1:
                    print(f'Sorry, not enough {CoffeeMachine.resources_name[i]}!')
                    return
            print('I have enough resources, making you a coffee!')
            for i in range(len(self.resources)-1):
                self.resources[i] -= choices[check][i]
            self.resources[4] += choices[check][4]
    def work(self):         
        while self.workable:
            action = input('Write action (buy, fill, take, remaining, exit): ')
            if action == 'remaining':
                CoffeeMachine.status(self)
            elif action == 'fill':
                CoffeeMachine.fill(self)
            elif action == 'take':
                print(f'I gave you ${self.resources[4]}')
                self.resources[4] = 0
            elif action == 'buy':
                CoffeeMachine.buy(self)
            elif action == 'exit':
                self.workable = False
            else:
                print('Not valid action')
            
myCoffeeMachine = CoffeeMachine()
myCoffeeMachine.work()
