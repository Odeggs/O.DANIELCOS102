from abc import ABC, abstractmethod

class coup_de_ecriva(ABC):
    @abstractmethod
    def Fan_Page(self):
        pass

class FC_Cirok(coup_de_ecriva):
    def Fan_Page(self):
        print("Welcome to FC_Cirok")

class Madiba_FC(coup_de_ecriva):
    def Fan_Page(self):
        print("Welcome to Madiba_FC")

class Blue_Jay_FC(coup_de_ecriva):
    def Fan_Page(self):
        print("Welcome to Blue_Jay_FC")

class TSG_Walker(coup_de_ecriva):
    def Fan_Page(self):
        print("Welcome to TSG_Walker")

club_name = input("Enter the name of the club you support: ")

if club_name == "FC_Cirok":
    fc_cirok = FC_Cirok()
    fc_cirok.Fan_Page()
elif club_name == "Madiba_FC":
    madiba_fc = Madiba_FC()
    madiba_fc.Fan_Page()
elif club_name == "Blue_Jay_FC":
    blue_jay_fc = Blue_Jay_FC()
    blue_jay_fc.Fan_Page()
elif club_name == "TSG_Walker":
    tsg_walker = TSG_Walker()
    tsg_walker.Fan_Page()
else:
    print("Invalid club name.")