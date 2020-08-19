from classes.game import Person,bcolors
from classes.magic import Spell
from classes.inventory import Item
import random

#black magic
fire = Spell("fire",10,100,"black")
blizzard = Spell("blizzard",15,150,"black")
thunder = Spell("thunder",20,200,"black")
meteor = Spell("meteor",12,120,"black")
quake = Spell("quake",5,50,"black")

#white magic
cure = Spell("cure",10,100,"white")
cura = Spell("cura",18,200,"white")

#creating item
potion = Item("potion","potion","heals 50 hp",50)
hipotion = Item("hi-potion","potion","heals 100 hp",100)
superpotion = Item("super potion","potion","heals 200 hp",200)
elixir = Item("elixir","elixir","heals one member hp/mp",10000)
megaelixir = Item("mega elixir","elixir","heals whole party hp/mp",10000)

grenade = Item("grenade","attack","damages 100 hp",100)

player_spells = [fire,blizzard,thunder,meteor,cura,cure]
enemy_spells = [fire,meteor,cure]
player_items = [{"item":potion,"quantity":15},{"item":hipotion,"quantity":5},{"item":superpotion,"quantity":1},{"item":elixir,"quantity":15},{"item":megaelixir,"quantity":2},{"item":grenade,"quantity":5}]
#INSTANTIATE PLAYERS
player1 = Person("SOHAM1", 6000, 300, 1050, 220, player_spells, player_items)
player2 = Person("SOHAM2", 4000, 350, 280, 110, player_spells, player_items)
player3 = Person("SOHAM3", 5000, 400, 230, 80, player_spells, player_items)
players=[player1, player2, player3]
#ENEMY INSTANTIATION
enemy1 = Person("HELLA", 18800, 400, 363, 50, enemy_spells, [])
enemy2 = Person("HELLO", 2800, 420, 463, 320, enemy_spells, [])
enemy3 = Person("HELLI", 2800, 430, 463, 220, enemy_spells, [])
enemies = [enemy1,enemy2,enemy3]
running = True

print(bcolors.FAIL+bcolors.BOLD+"An Enemy Attacks"+bcolors.ENDC)

while running:
    print("=======================")
    print("\n")
    print(bcolors.BOLD+"NAME                               HP                                          MP"+bcolors.ENDC)

    #PLAYER STATS
    for player in players:
        player.get_stats()
    print("\n")
    #ENEMY STATS
    for enemy in enemies:
        enemy.get_stats(bcolors.FAIL)
    #ENEMY ATTACKS
    for enemy in enemies:
        enemy_choice = random.randrange(0,2)
        enemy_target = random.randrange(0,len(players))
        if enemy_choice == 0:
            enemy_dmg = enemy.generateDamage()
            players[enemy_target].takeDamage(enemy_dmg)
            print(bcolors.BOLD + bcolors.FAIL + enemy.name + " attacked "+players[enemy_target].name+" for", str(enemy_dmg) + bcolors.ENDC)
        elif enemy_choice == 1:
            spell_choice = random.randrange(0,len(enemy_spells))
            enemy_dmg = enemy_spells[spell_choice].generate_damage()
            enemy.reduce_mp(enemy_spells[spell_choice].cost)
            if enemy_spells[spell_choice].type == "black":
                players[enemy_target].takeDamage(enemy_dmg)
                print(bcolors.BOLD + bcolors.FAIL + enemy.name + " attacks with "+enemy_spells[spell_choice].name+" "+players[enemy_target].name+" for", str(enemy_dmg) + bcolors.ENDC)
            elif enemy_spells[spell_choice].type == "white":
                enemy.heal(enemy_dmg)
                print(bcolors.BOLD+bcolors.WARNING+enemy.name+" healed for "+str(enemy_dmg)+bcolors.ENDC)
    #IF PLAYER DIES
    for player in range(len(players)):
        if players[player].get_hp() == 0:
            print(bcolors.FAIL + bcolors.BOLD + players[player].name +" has DIED."+bcolors.ENDC)
            del players[player]
    #PLAYERS TURNS
    for player in players:
        target = player.choose_target(enemies)
        enemy = enemies[target]
        player.choose_action()
        choice = input("Choose action")
        index = int(choice)-1
        if index ==0:
            dmg = player.generateDamage()
            enemy.takeDamage(dmg)
            print(enemy.name+" took damage for",dmg)
        elif index==1:
            player.choose_magic()
            magic_choice = int(input("Choose Magic : "))-1
            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()
            if player.get_mp()<spell.cost:
                print(bcolors.FAIL+"you do not have enough mp"+bcolors.ENDC)
                continue
            player.reduce_mp(spell.cost)
            if spell.type == "white":
                player.heal(magic_dmg)
                print(bcolors.OKBLUE+"you healed for ", str(magic_dmg) +bcolors.ENDC)
            elif spell.type == "black":
                enemy.takeDamage(magic_dmg)
                print(bcolors.OKBLUE+"you attacked enemy for ", str(magic_dmg) + bcolors.ENDC)
        elif index == 2:
            player.choose_items()
            item_choice = int(input("choose item : ")) - 1
            if item_choice == -1:
                continue
            item = player.items[item_choice]
            if item["quantity"] == 0:
                print(bcolors.FAIL + "You dont have this " + bcolors.ENDC)
                continue
            item["quantity"] -= 1
            if item["item"].type == "potion":
                player.heal(item["item"].prop)
                print(bcolors.OKGREEN + "healed for " + str(item["item"].prop) + bcolors.ENDC)
            elif item["item"].type == "elixir":
                if item["item"].name == "mega elixir":
                    for p in players:
                        p.hp = p.maxhp
                        p.mp = p.maxmp
                player.hp = player.maxhp
                player.mp = player.maxmp
                print(bcolors.OKGREEN + "player completely healed" + bcolors.ENDC)
            elif item["item"].type == "attack":
                enemy.takeDamage(item["item"].prop)
                print(bcolors.FAIL+bcolors.BOLD + "hits enemy for " + str(item["item"].prop) + bcolors.ENDC)
            #IF ENEMY DIES REMOVE FROM LIST
            if enemy.get_hp() == 0:
                print(bcolors.OKGREEN + bcolors.BOLD + enemy.name + " has DIED." + bcolors.ENDC)
                del enemies[target]
    #CHECK IF THE BATTLE IS OVER
    if len(enemies) <= 1:
        print(bcolors.OKGREEN+"█████████████████████████You Won !!█████████████████████████"+bcolors.ENDC)
        running = False
    elif len(players) == 0:
        print(bcolors.FAIL+"You lost"+bcolors.ENDC)
        running = False
