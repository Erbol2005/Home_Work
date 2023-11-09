class SuperHero:
    people = 'people'
    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def get_name(self):
        print(self.name)

    def double_health(self):
        self.health_points *= 2

    def __str__(self):
        return f"Nickname: {self.nickname}, Superpower: {self.superpower}, Health Points: {self.health_points}"

    def __len__(self):
        return len(self.catchphrase)

hero = SuperHero("Бари Ален", "Флеш", "Скорость", 20, "Я самый быстрый человек на земле")
hero.get_name()
hero.double_health()
print(hero)
print(len(hero))

class AirHero(SuperHero):
    location = 'air'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = False

    def double_health(self):
        self.health_points = self.health_points ** 2
        self.fly = True

    def true_phrase(self, phrase):
        return phrase in self.catchphrase
class EarthHero(SuperHero):
    location = 'earth'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = False

    def double_health(self):
        self.health_points = self.health_points ** 2
        self.fly = True

    def true_phrase(self, phrase):
        return phrase in self.catchphrase
class SpaceHero(SuperHero):
    location = 'space'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = False

    def double_health(self):
        self.health_points = self.health_points ** 2
        self.fly = True

    def true_phrase(self, phrase):
        return phrase in self.catchphrase

class Villain(SpaceHero):
    people = 'monster'


    def gen_x(self):
        pass

    def crit(self, hero):
        hero.health_points = hero.health_points ** self.damage


air_hero = AirHero("Боб", "Летчик", "Телекинез", 15, "Я управляю воздухом!", 3)
earth_hero = EarthHero("Алиса", "Землянка", "Суперсила", 20, "Я защищаю землю!", 4)
space_hero = SpaceHero("Сэм", "Космонавт", "Манипулирование энергией", 25, "Я един с космосом!", 5)

air_hero.double_health()
print(air_hero)

print(air_hero.true_phrase("Я управляю воздухом!"))

villain = Villain("Макс", "Злодей", "Контроль разума", 30, "Я завоюю мир!", 6)

villain.crit(air_hero)
print(air_hero.health_points)





