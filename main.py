class Huymans():
    def __init__(self, health, damage, armor):
        self.health = health
        self.damage = damage
        self.armor = armor

    def ShowHealth(self):
        print(f"Собересь у тебя осталось {self.health} здоровья")

    def Attack(self, enemy):
        enemy.health = enemy.health - self.damage * (1 - enemy.armor / 100)

huyman1 = Huymans(100,15,50 )
huyman2 = Huymans(100,25,5)
while huyman2.health > 0 or huyman1.health > 0 :
    huyman2.ShowHealth()
    huyman1.Attack(huyman2)
    huyman2.ShowHealth()

    huyman1.ShowHealth()
    huyman2.Attack(huyman1)
    huyman1.ShowHealth()

if huyman2.health > 0:
    print("Игрок 2 победил")
else:
    print("Игрок 1 победил")