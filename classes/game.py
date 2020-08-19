import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Person:
    def __init__(self,name,hp,mp,atk,df,magic,items):
        self.maxhp=hp
        self.name = name
        self.maxmp= mp
        self.hp=hp
        self.mp=mp
        self.atkl=atk-10
        self.atkh=atk+10
        self.df=df
        self.items = items
        self.magic=magic
        self.actions = ["Attack","Magic","Items"]
    def generateDamage(self):
        return random.randrange(self.atkl,self.atkh)

    def takeDamage(self,dmg):
        self.hp -=dmg
        if self.hp<0:
            self.hp=0
        return self.hp
    def heal(self,dmg):
        self.hp+=dmg
        if self.hp>self.maxhp:
            self.hp=self.maxhp
    def get_hp(self):
        return self.hp
    def get_max_hp(self):
        return self.maxhp
    def get_mp(self):
        return self.mp
    def get_max_mp(self):
        return self.maxmp
    def reduce_mp(self,cost):
        self.mp-=cost

    def choose_action(self):
        i=1
        print(bcolors.BOLD+self.name+bcolors.ENDC)
        print(bcolors.OKBLUE+bcolors.BOLD+"    Actions"+bcolors.ENDC)
        for item in self.actions:
            print("    ",str(i),":",item)
            i+=1
    def choose_magic(self):
        i=1
        print(bcolors.OKBLUE+bcolors.BOLD+"    Magic"+bcolors.ENDC)
        for item in self.magic:
            print("    ",str(i),":",item.name,"(",str(item.cost),")")
            i+=1
    def choose_items(self):
        i=1
        print(bcolors.OKBLUE+bcolors.BOLD+"    ITEMS :"+bcolors.ENDC)
        for item in self.items:
            print("    ",str(i),":",item["item"].name,"(",str(item["item"].description),")", "quantity " , str(item["quantity"]))
            i+=1
    def choose_target(self,enemies):
        i=1
        print(bcolors.FAIL+bcolors.BOLD+"    TARGETS :"+bcolors.ENDC)
        for enemy in enemies:
            print("    ",str(i),":",enemy.name, " : Target HP ", str(enemy.get_hp()))
            i+=1
        target_choice = int(input("Choose your target : "))-1
        return target_choice
    def get_stats(self,bar_color=bcolors.OKGREEN):
        hp_ticks = (self.hp/self.maxhp)*25
        mp_ticks = (self.mp/self.maxmp)*10
        mp_bar = "█"*int(mp_ticks)
        hp_bar = "█"*int(hp_ticks)
        while len(hp_bar)<25:
            hp_bar+=" "
        while  len(mp_bar)<10:
            mp_bar+=" "
        hp_rep = str(self.hp)+"/"+str(self.maxhp)
        mp_rep = str(self.mp)+"/"+str(self.maxmp)
        hp_rep = " "*(11-len(hp_rep)) + hp_rep
        mp_rep = " "*(7-len(mp_rep)) + mp_rep
        spaces = 20-len(self.name)*" "
        print("                                   _________________________                   __________")
        print(bcolors.BOLD+self.name+" :"+spaces+hp_rep+bar_color+" |"+hp_bar+"|         "+bcolors.ENDC+bcolors.BOLD+mp_rep+bcolors.OKBLUE+" |"+mp_bar+"|"+bcolors.ENDC)
