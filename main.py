import random

berserk = {'hp': 10,
           'power': 7,
           'stelth': 3,
           'mana': 4,
           'lvl': 0,
           'progres_bar': 0}

mag = {'hp': 5,
       'power': 3,
       'stelth': 4,
       'mana': 10,
       'lvl': 0}

arrowman = {'hp': 7,
            'power': 5,
            'stelth': 8,
            'mana': 5,
            'lvl': 0}

monster = {'hp': 3,
           'power': 2}

def chek_lvl():
    if user_person == '1':
        pg = berserk['progres_bar']
        if pg > 0 and pg < 149:
            berserk['lvl'] = 0
        elif pg > 149 and pg < 299:
            berserk['lvl'] = 1
        elif pg > 300 and pg < 499:
            berserk['lvl'] = 2
            
        print(berserk['lvl'])

def battle():
    if user_person == '1':
        hp = berserk['hp']
        power = berserk['power']
        stelth = berserk['stelth']
        mana = berserk['mana']
        
        
        if power > monster['hp']:
            berserk['progres_bar'] = berserk['progres_bar'] + 50
            print("Победа")
    

def go_map():
    while True:
        hod = random.randint(0, 5)
        if hod == 0:
            print("Shop")
            print(berserk['progres_bar'])
            dey = input('Пройти дальше?')
            if dey == 'да':
                continue
            if dey == 'инфо':
                chek_lvl()
                continue
        if hod == 1:
            print("Monster")
            dey = input('Пройти дальше?')
            if dey == 'да':
                continue
            if dey == 'сразиться':
                battle()
                continue
                
        else:
            print('Бродим...')
    



while True:
    user_person = input("Выберите персонажа которым хотите играть:\n"+
                        "1) Берсерк\n"+
                        "2) Маг\n"+
                        "3) Лучник\n")
    
    if user_person == '1':
        print(f'Характеристики берсерка:\n'+
            f'Здоровье = {berserk["hp"]}\n'+
            f'Сила = {berserk["power"]}\n'+
            f'Ловкость = {berserk["stelth"]}\n'+
            f'Мана = {berserk["mana"]}\n')
        say = input("Выбрать этого персонажа?\n")
        if say == 'нет':
            continue
        elif say == 'да':
            break
        
    if user_person == '2':
        print(f'Характеристики мага:\n'+
            f'Здоровье = {mag["hp"]}\n'+
            f'Сила = {mag["power"]}\n'+
            f'Ловкость = {mag["stelth"]}\n'+
            f'Мана = {mag["mana"]}\n')
        say = input("Выбрать этого персонажа?\n")
        if say == 'нет':
            continue
        elif say == 'да':
            break
        
    if user_person == '3':
        print(f'Характеристики лучника:\n'+
            f'Здоровье = {arrowman["hp"]}\n'+
            f'Сила = {arrowman["power"]}\n'+
            f'Ловкость = {arrowman["stelth"]}\n'+
            f'Мана = {arrowman["mana"]}\n')
        say = input("Выбрать этого персонажа?\n")
        if say == 'нет':
            continue
        elif say == 'да':
            break
        
print("Тогда начнем путешествие...")
print(user_person)
go_map()
