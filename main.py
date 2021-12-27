import time
import random
from datetime import datetime

todays_date = datetime.now()


def dates():
    x = todays_date.second
    z = todays_date.hour
    y = todays_date.minute
    now = "{z}:{y}:{x}".format(z=z, y=y, x=x)
    return now


def opening():
    print(57 * "#" + "\n" + "##" + 18 * " " + "R.P.G simple game" + 18 * " " + "##")
    print("##" + 20 * " " + "made by Frez" + 21 * " " + "##\n" + 57 * "#" + "\n")
    time.sleep(1)
    print("there is grammatical error but lets' ignore :v")
    time.sleep(1)


class Player:
    def __init__(self, hp, phy_damage, magic_damage, name, level):
        self.hp = hp
        self.phy_damage = phy_damage
        self.magic_damage = magic_damage
        self.name = name
        self.level = level

    def get_hp(self):
        return self.hp

    def get_phy_damage(self):
        return self.phy_damage

    def get_magic_damage(self):
        return self.magic_damage

    def get_name(self):
        return self.name

    def get_level(self):
        return self.level

    def set_hp(self, hp):
        self.hp = hp

    def set_phy_damage(self, phy_damage):
        self.phy_damage = phy_damage

    def set_magic_damage(self, magic_damage):
        self.magic_damage = magic_damage

    def set_name(self, name):
        self.name = name

    def set_level(self, level):
        self.level = level


class Enemy:
    def __init__(self, hp, damage, true_damage, name):
        self.hp = hp
        self.damage = damage
        self.true_damage = true_damage
        self.name = name

    def get_hp(self):
        return self.hp

    def get_damage(self):
        return self.damage

    def get_true_damage(self):
        return self.true_damage

    def get_name(self):
        return self.name

    def set_hp(self, hp):
        self.hp = hp

    def set_damage(self, damage):
        self.damage = damage

    def set_true_damage(self, true_damage):
        self.true_damage = true_damage

    def set_name(self, name):
        self.name = name


def story1():
    choice = input("Do you want to read storyline? type 'yes' or 'no'\n")
    if choice.lower() != "yes" and choice.lower() == "no":
        player_name = input("type your name :")
        x = input("1.Physical or 2.magic damage? type '1' or '2'  :")
        while x != "1" and x != "2":
            print("error selection")
            time.sleep(0.7)
            x = input("'1' or '2'?  :")
        if x == "1":
            player_phy_damage = 25
            player_magic_damage = 20
        elif x == "2":
            player_phy_damage = 20
            player_magic_damage = 25
        time.sleep(0.3)
        print("here your stat:")
        time.sleep(0.5)
        print(20 * "#" + "\nphysical damage: {a}".format(a=player_phy_damage))
        print("magic damage: {a}\n".format(a=player_magic_damage) + 20 * "#")
        time.sleep(1)
        res = input("are you satisfied with this stat? type 'yes' or 'no'\n")
        if res.lower() == "yes":
            time.sleep(0.3)
            print("okay lets start our adventure!")

        elif res.lower() == "no":
            time.sleep(0.3)
            print("Okay, I gonna random out some number..")
            time.sleep(0.6)
            while res.lower() == "no":
                player_phy_damage = random.randint(10, 35)
                player_magic_damage = random.randint(10, 35)
                print("this is new stat:")
                time.sleep(0.5)
                print(20 * "#" + "\nphysical damage: {a}".format(a=player_phy_damage))
                print("magic damage: {a}\n".format(a=player_magic_damage) + 20 * "#")
                res = input("Are you satisfied? enter 'yes' or 'no'\n")
                time.sleep(1.5)
        else:
            pass

    else:
        print("Wake up..")
        time.sleep(1.2)
        player_name = input("What's your name chosen one?  :")
        time.sleep(0.5)
        print("For now... I'll tell you a story that happened thousand years ago..")
        time.sleep(1)
        print("Back then human live peacefully and the land was stretched out with green scenery..")
        time.sleep(1.5)
        print("Right now, you the only human left..")
        time.sleep(1)
        print("the only hero that can save the world..")
        time.sleep(1)
        x = input("Is your skill is 1.physical or a 2.magic attack? enter '1' or '2' only.\n")
        time.sleep(0.5)
        while x != "1" and x != "2":
            print("error selection")
            time.sleep(0.7)
            x = input("Enter '1' or '2'!")
        if x == "1":
            time.sleep(0.7)
            print("Seem like you masculine, and that's good")
            player_phy_damage = 25
            player_magic_damage = 20
        elif x == "2":
            time.sleep(0.7)
            print("so, you go to magic academy didn't you? I hope you will defeat demon king for us!")
            player_phy_damage = 20
            player_magic_damage = 25
        time.sleep(1.5)
        print("anyways, we will looking forward for meeting you again in future {}.".format(player_name))
        time.sleep(1.3)
        print(20 * "#" + "\nphysical damage: {a}".format(a=player_phy_damage))
        print("magic damage: {a}\n".format(a=player_magic_damage) + 20 * "#")
        time.sleep(1.5)
        res = input("are you satisfied with this stat? type 'yes' or 'no'\n")
        if res.lower() == "yes":
            time.sleep(0.3)
            print("okay lets start our adventure!")

        elif res.lower() == "no":
            time.sleep(0.3)
            print("Okay, I gonna random out some number..")
            while res.lower() == "no":
                time.sleep(0.8)
                player_phy_damage = random.randint(10, 35)
                player_magic_damage = random.randint(10, 35)
                print("this is new stat:")
                time.sleep(0.5)
                print(20 * "#" + "\nphysical damage: {a}".format(a=player_phy_damage))
                print("magic damage: {a}\n".format(a=player_magic_damage) + 20 * "#")
                time.sleep(1.5)
                res = input("Are you satisfied? enter 'yes' or 'no'\n")

        else:
            time.sleep(0.3)
            print("seem like you enter wrong key.")
            time.sleep(0.4)
            print("but nevermind, lets start the game.")

    return player_name, player_phy_damage, player_magic_damage


def enemy_ability(basic_damage, special_damage):
    percentage = [0, 0, 1, 0, 1, 0]
    attack = random.choice(percentage)
    if attack == 0:
        return basic_damage
    else:
        return special_damage


def enemy_attack(attack_value, name):
    print("{} is going winding up for an attack".format(name))
    time.sleep(0.6)
    percentage = [1, 0, 1, 0, 1]
    hit = random.choice(percentage)
    if hit == 0:
        print("It's hit you..")
        time.sleep(0.8)
        print("your health is decrease as much {}".format(attack_value))
        time.sleep(0.8)
        return attack_value
    else:
        print("{} has miss target.".format(name))
        time.sleep(0.7)
        return 0


def player_attack():
    percentage = [1, 1, 1, 1, 0, 0]
    hit = random.choice(percentage)
    if hit == 0:
        return False
    else:
        return True


def is_dead(health):
    if health < 0:
        return True
    else:
        return False


def loot(player, enemy_):
    percentage = [0, 1, 1, 1, 1]
    luck = random.choice(percentage)
    player.set_level(player.get_level() + 1)

    if luck == 0:
        print("SIKKKKKKKKKEEEE No loot here!")
        time.sleep(0.5)

    else:
        print("Yes, the drop is..")
        file = open("asset/physical.txt.", "r")
        lines = file.readlines()
        physical = lines[random.randint(0, len(lines) - 1)][:-1]
        file.close()
        file = open("asset/magic.txt.", "r")
        lines = file.readlines()
        magic = lines[random.randint(0, len(lines) - 1)][:-1]
        file.close()

        if enemy_.hp <= 100:
            health = random.randint(35, 45)
            phy_damage = random.randint(10, 15)
            magic_damage = random.randint(10, 15)
            time.sleep(0.7)
            print("healing:{}".format(health))
            time.sleep(0.7)
            print(str(physical) + " sword:" + str(magic_damage))
            time.sleep(0.7)
            print(str(magic) + " ore:" + str(magic_damage))
            player.set_phy_damage(player.get_phy_damage() + phy_damage)
            player.set_hp(player.get_hp() + health)
            player.set_magic_damage(player.get_magic_damage() + magic_damage)

        elif enemy_.hp >= 100:
            if enemy_.hp <= 450:
                health = random.randint(500, 600)
                phy_damage = random.randint(25, 35)
                magic_damage = random.randint(25, 35)
                time.sleep(0.7)
                print("healing:{}".format(health))
                time.sleep(0.7)
                print(str(physical) + " sword:" + str(magic_damage))
                time.sleep(0.7)
                print(str(magic) + " ore:" + str(magic_damage))
                player.set_phy_damage(player.get_phy_damage() + phy_damage)
                player.set_hp(player.get_hp() + health)
                player.set_magic_damage(player.get_magic_damage() + magic_damage)
            else:
                health = random.randint(750, 800)
                phy_damage = random.randint(45, 55)
                magic_damage = random.randint(25, 55)
                time.sleep(0.7)
                print("healing:{}".format(health))
                time.sleep(0.7)
                print(str(physical) + " sword:" + str(magic_damage))
                time.sleep(0.7)
                print(str(magic) + " ore:" + str(magic_damage))
                player.set_phy_damage(player.get_phy_damage() + phy_damage)
                player.set_hp(player.get_hp() + health)
                player.set_magic_damage(player.get_magic_damage() + magic_damage)
        time.sleep(0.3)
        print("your Hp now is {a},level is {b}.".format(a=player.get_hp(), b=player.get_level()))
        time.sleep(1)
        print("physical damage:{a} & magic damage:{b}.".format(a=player.get_phy_damage(), b=player.get_magic_damage()))
        time.sleep(1)


def game_over(enemy_dead):
    if enemy_dead:
        print("we will keep going in this path to defeat demon king..\n")
        time.sleep(1.5)
    else:
        print("you are dead..")
        time.sleep(1.5)
        print("the journey has ended, goodbye..")
        time.sleep(1.5)
        print("\n*alarm clock ringing at time {}*".format(dates()))
        time.sleep(1.5)
        print("Ahh.. it all was a dream..")
        time.sleep(1.5)
        print("it was good dream to be honest. now time to go to school..")
        time.sleep(1.5)
        print("game has ended here")
        time.sleep(1.5)
        print("\n" + 30 * "#" + "\n")
        time.sleep(1.5)
        print("thanks for playing my game!\neven though this is lame coding..")
        time.sleep(1.5)
        print("you can give me feedback about this game!")
        time.sleep(1.5)
        print("this code will end here.")
        time.sleep(1.5)
        exit()


def battle(enemys, player):
    if enemys.get_hp() <= 100:
        time.sleep(0.3)
        print("I see something coming toward me..")
        time.sleep(0.5)
        print("It's {}".format(enemys.get_name()))
        time.sleep(1.0)
        print("Ahh.. just weak creature,i can level up with this things.")
        time.sleep(1.0)
        print("but before that, I need to check it's stat just in case.")
        time.sleep(1.0)
        enemy_stat(enemys)
        print("lets' level up!")
        time.sleep(0.5)
    elif 600 > enemys.get_hp() > 300:
        time.sleep(0.3)
        print("I see something on the horizon..")
        time.sleep(1.0)
        print("It's {}.".format(enemys.get_name()))
        time.sleep(1.0)
        print("now this is real fight! hope i don't mess up")
        time.sleep(1.0)
        print("but before that, I need to check it's stat")
        time.sleep(1.0)
        enemy_stat(enemys)
        print("lets fight!")
        time.sleep(0.5)
    elif enemys.get_hp() >= 950:
        time.sleep(0.3)
        print("Finally, I arrived at demon king castle..")
        time.sleep(1.0)
        print("I see blood everywhere..")
        time.sleep(1.0)
        print("i will take revenge of the innocent people that he killed")
        time.sleep(1.0)
        print("but before that, I need to check it's stat")
        time.sleep(1.0)
        enemy_stat(enemys)
        print("alright, let kill him.")
        time.sleep(0.3)

    zz = input("Do you want convert your damage to health? enter 'yes' or 'no'\n")
    if zz == "yes":
        time.sleep(0.3)
        chosen(player)
    else:
        pass

    battles = True
    while battles:

        time.sleep(0.3)
        print("Do you want to use 1.physical or 2.magic damage to defeat {}?".format(enemys.get_name()))
        choice = input()
        while choice != "1" and choice != "2" and choice != "y":
            time.sleep(0.5)
            print("error selection")
            time.sleep(0.5)
            choice = input("Hurry,physical(1),magic(2) or you want to commit suicide(y)?\n".format(enemys.get_name()))

        if choice == "1":
            damage = player.get_phy_damage()
        elif choice == "2":
            damage = player.get_magic_damage()
        else:
            play = False
            game_over(play)

        hit = player_attack()
        if hit:
            enemys.set_hp(enemys.get_hp() - damage)
            time.sleep(0.7)
            print("You've hit {}!".format(enemys.get_name()))
            time.sleep(0.7)
            print("The enemy health is {}.".format(enemys.get_hp()))
            time.sleep(0.7)

        else:
            print("your attack is miss")
            time.sleep(0.7)

        enemy_dead = is_dead(enemys.get_hp())
        attack = enemy_ability(enemys.get_damage(), enemys.get_true_damage())

        if not enemy_dead:
            player.set_hp(player.get_hp() - enemy_attack(attack, enemys.get_name()))

            player_dead = is_dead(player.get_hp())
            if player_dead:
                return False
            else:
                print("your remaining health is {}.".format(player.get_hp()))
                time.sleep(0.6)

        else:
            print("you have defeat the {}".format(enemys.get_name()))
            time.sleep(0.8)
            print("it's drop any loot?")
            time.sleep(0.6)
            loot(player, enemys)
            return True


def enemy_generator(player):
    player_level = player.level
    if 10 >= player_level >= 0:
        file = open("asset/adjective.txt", "r")
        lines = file.readlines()
        adjective = lines[random.randint(0, len(lines) - 1)][:-1]
        file.close()
        file = open("asset/creature.txt", "r")
        lines = file.readlines()
        creature = lines[random.randint(0, len(lines) - 1)][:-1]
        file.close()

        health = random.randint(50, 60)
        damage = random.randint(10, 15)
        true_damage = random.randint(15, 18)

        return Enemy(health, damage, true_damage, adjective + " " + creature)

    elif 19 >= player_level > 10:
        file = open("asset/SAO_character.txt", "r")
        lines = file.readlines()
        sao = lines[random.randint(0, len(lines) - 1)][:-1]
        file.close()

        if sao == "Kirito":
            health = random.randint(450, 500)
            damage = random.randint(90, 100)
            true_damage = random.randint(110, 120)
            return Enemy(health, damage, true_damage, sao)
        elif sao == "Asuna":
            health = random.randint(400, 450)
            damage = random.randint(80, 100)
            true_damage = random.randint(100, 110)
            return Enemy(health, damage, true_damage, sao)
        else:
            health = random.randint(400, 500)
            damage = random.randint(80, 100)
            true_damage = random.randint(100, 120)
            return Enemy(health, damage, true_damage, sao)

    else:
        health = random.randint(1000, 1010)
        damage = random.randint(150, 200)
        true_damage = random.randint(200, 220)
        return Enemy(health, damage, true_damage, "Saido")


def level_generator(py):
    char_dead = battle(enemy_generator(py), py)
    game_over(char_dead)


def stat(py):
    print("Currently your Hp is {}.".format(py.get_hp()))
    time.sleep(0.6)
    print("physical damage: {a}".format(a=py.get_phy_damage()))
    time.sleep(0.6)
    print("magic damage: {a}\n".format(a=py.get_magic_damage()))
    time.sleep(0.6)


def ending():
    print("I finally defeat the demon king!!")
    time.sleep(1.5)
    print("now I will reverse all of this wrong doing to this land.")
    time.sleep(1.5)
    print("i can sense the harem vibe.. woman around me.")
    time.sleep(1.5)
    print("wait what's that sound..")
    time.sleep(1.5)
    print("It's me demon king, Hahaha thought you have kill me?")
    time.sleep(1.5)
    print("and then I realize I soo dead..")
    time.sleep(1.5)
    x = input("so what i want to do now, surrender(1) or fight(2) him... \n")
    time.sleep(1.5)
    if x == "1":
        print("demon king: owh you want to surrender? good choice")
        time.sleep(1.5)
        print("i will give harem to you ^-^\nwe don't need to fight because I and you are nonetheless same")
        time.sleep(1.5)
        print("Me: i guess this win win situation. i'm okay with it")
        time.sleep(1.5)
        print("you have won apparently, even though the world is falling..")
    elif x == "2":
        print("you dead, lmao")
        time.sleep(1.5)
        print("thinks you can defeat demon king ha? joke on. you can't ")
        time.sleep(1.5)
        print("you dead. i do thought it was bad idea")
    else:
        print("why you stupid? enter 1 or 2 only.")
        time.sleep(1.5)
        print("you dead")
    time.sleep(1.5)
    print("\n*alarm clock ringing at time {}*".format(dates()))
    time.sleep(1.5)
    print("It all was a dream..")
    time.sleep(1.5)
    print("it was good dream to be honest. now time to go to school..")
    time.sleep(1.5)
    print("game has ended here")
    time.sleep(1.5)
    print("\n" + 30 * "#" + "\n")
    time.sleep(1.5)
    print("thanks for playing my game!\neven though this is lame coding..")
    time.sleep(1.5)
    print("you can give me feedback about this game!")
    time.sleep(1.5)
    print("this code will end here.")
    time.sleep(1.5)
    exit()


def leveling(py):
    print("level {}..".format(py.level))  # 1
    level_generator(py)
    print("level {}..".format(py.level))  # 2
    level_generator(py)
    print("level {}..".format(py.level))  # 3
    level_generator(py)
    print("level {}..".format(py.level))  # 4
    level_generator(py)
    print("level {}..".format(py.level))  # 5
    level_generator(py)
    levels()
    print("level {}..".format(py.level))  # 6
    level_generator(py)
    print("level {}..".format(py.level))  # 7
    level_generator(py)
    print("level {}..".format(py.level))  # 8
    level_generator(py)
    print("level {}..".format(py.level))  # 9
    level_generator(py)
    print("level {}..".format(py.level))  # 10
    level_generator(py)
    levels()
    print("level {}..".format(py.level))  # 11
    level_generator(py)
    print("level {}..".format(py.level))  # 12
    level_generator(py)
    print("level {}..".format(py.level))  # 13
    level_generator(py)
    print("level {}..".format(py.level))  # 14
    level_generator(py)
    print("level {}..".format(py.level))  # 15
    level_generator(py)
    levels()
    print("level {}..".format(py.level))  # 16
    level_generator(py)
    print("level {}..".format(py.level))  # 17
    level_generator(py)
    print("level {}..".format(py.level))  # 18
    level_generator(py)
    print("level {}..".format(py.level))  # 19
    level_generator(py)
    print("level {}..".format(py.level))  # 20
    level_generator(py)


def enemy_stat(enemy_):
    print("Do you want to check enemy stat? type 'yes' or 'no'")
    choice = input()
    if choice.lower() != "yes" and choice.lower() == "no":
        pass
    else:
        time.sleep(0.2)
        print(30 * "#")
        print("name:{a}\nhealth:{b}".format(a=enemy_.get_name(), b=enemy_.get_hp()))
        print("damage: {c}\nspecial skill: {d}".format(c=enemy_.get_damage(), d=enemy_.get_true_damage()))
        print(30 * "#")
        time.sleep(2.0)


def convert_magic(py):
    new_health = py.get_magic_damage()
    py.set_hp(py.get_hp() + new_health)
    py.set_magic_damage(0)


def convert_physical(py):
    new_health = py.get_phy_damage()
    py.set_hp(py.get_hp() + new_health)
    py.set_phy_damage(0)


def levels():
    print("do you want to continue? enter 'yes' or 'no'")
    ww = input()
    if ww == "no":
        game = False
        game_over(game)
    else:
        pass


def chosen(py):
    print("Do you want to convert 1.physical or 2.magic damage?")
    types = input()
    if types == "1":
        convert_physical(py)
        time.sleep(0.3)
        stat(py)
    elif types == "2":
        convert_magic(py)
        time.sleep(0.3)
        stat(py)
    else:
        time.sleep(0.3)
        print("I assume, you don't want convert it.")


def main():
    opening()
    class_data = story1()
    py = Player(50, class_data[1], class_data[2], class_data[0], 1)
    stat(py)
    leveling(py)
    ending()


main()
