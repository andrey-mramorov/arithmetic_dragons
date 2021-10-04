# coding: utf-8
# license: GPLv3
from gameunit import *
from random import randint, choice

class Enemy(Attacker):
    pass


def generate_random_enemy():
    RandomEnemyType = choice(enemy_types)
    enemy = RandomEnemyType()
    return enemy


def generate_dragon_list(enemy_number):
    enemy_list = [generate_random_enemy() for i in range(enemy_number)]
    return enemy_list


class Dragon(Enemy):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer

class Troll(Enemy):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer

class GuessTroll(Troll):
    def __init__(self):
        self._health = 100
        self._attack = 10
        self._color = 'угадай-тролль'

    def question(self):
        x = randint(1,5)
        self.__quest = 'Угадай число от 1 до 5.'
        self.set_answer(x)
        return self.__quest
        
class SimpleTroll(Troll):
    def __init__(self):
        self._health = 100
        self._attack = 10
        self._color = 'простой-тролль'
	
    def __IsPrime__(self, n):
    	d = 2
    	while n % d != 0:
    		d += 1
    	
    	if d == n:
    		return "yes"
    	else:
    		return "no"

    def question(self):
        x = randint(1,50)
        self.__quest = 'Число ' + str(x) + ' - простое?\nЕсли да - пиши yes, если нет - no.'
        self.set_answer(__IsPrime__(x))
        return self.__quest
        
class DivideTroll(Troll):
    def __init__(self):
        self._health = 50
        self._attack = 20
        self._color = 'разложи-тролль'

    def __Factor__(self, n):
        Ans = []
        d = 2
        while d * d <= n:
            if n % d == 0:
                Ans.append(d)
                n //= d
            else:
                d += 1
        if n > 1:
            Ans.append(n)
        return Ans

    def question(self):
        x = randint(1,100)
        self.__quest = 'Разложи на множители число: ' + str(x)
        ans_str = ", ".join(map(str, __Factor__(x)))
        self.set_answer(ans_str)
        return self.__quest

class GreenDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 20
        self._color = 'зелёный дракон'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + ' + ' + str(y)
        self.set_answer(x + y)
        return self.__quest


class RedDragon(Dragon):
    def __init__(self):
        self._health = 150
        self._attack = 15
        self._color = 'красный дракон'

    def question(self):
        x = randint(1,100)
        y = randint(1,x)
        self.__quest = str(x) + ' - ' + str(y)
        self.set_answer(x - y)
        return self.__quest

class BlackDragon(Dragon):
    def __init__(self):
        self._health = 100
        self._attack = 10
        self._color = 'черный дракон'

    def question(self):
        x = randint(1,10)
        y = randint(1,10)
        self.__quest = str(x) + ' x ' + str(y)
        self.set_answer(x * y)
        return self.__quest
        
enemy_types = [GreenDragon, RedDragon, BlackDragon, GuessTroll, SimpleTroll, DivideTroll]
