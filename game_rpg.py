class Hero:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def info(self):
        print(f"Hero: {self.name} | HP: {self.hp} | Power: {self.attack_power}")
    
    def serang(self, lawan):
        print(f"{self.name} menyerang {lawan.name}!")
        lawan.diserang(self.attack_power)

    def diserang(self, serangan):
        print(f"{self.name} diserang oleh {serangan}!")
        self.hp -= serangan

hero1 = Hero("Layla", 100, 15)
hero2 = Hero("Zilong", 120, 20)
hero3 = Hero("Jin", 150, 25)
hero4 = Hero("Xiao", 180, 30)
hero5 = Hero("Diluc", 200, 35)

hero1.info()
hero2.info()
hero3.info()
hero4.info()
hero5.info()

print("\n--- Pertarungan Dimulai ---")
hero1.serang(hero2)
hero2.serang(hero1)
hero3.serang(hero4)
hero4.serang(hero3)
hero5.serang(hero1)
hero1.serang(hero5)

class Mage(Hero):
    def __init__(self, name, hp, attack_power, mana):
        super().__init__(name, hp, attack_power)
        self.mana = mana
    def info(self):
        print(f"{self.name} [Mage] | HP: {self.hp} | Mana: {self.mana}")
    def skill_fireball(self, lawan):
        if self.mana >= 20:
            print(f"{self.name} menggunakan Fireball ke {lawan.name}!")
            self.mana -= 20
            lawan.diserang(self.attack_power * 2)
        else:
            print(f"{self.name} gagal skill! Mana tidak cukup.")

class Hero:
    def __init__(self, nama, hp_awal):
        self.nama = nama
        
        self.__hp = hp_awal
    def get_hp(self):
        return self.__hp

    def set_hp(self, nilai_baru):
        if nilai_baru < 0:
            self.__hp = 0
        elif nilai_baru > 1000:
            print("Cheat terdeteksi! HP dimaksimalkan ke 1000 saja.")
            self.__hp = 1000
        else:
            self.__hp = nilai_baru
            
    def diserang(self, damage):
        sisa_hp = self.get_hp() - damage
        self.set_hp(sisa_hp)
        print(f"{self.nama} terkena damage {damage}. Sisa HP: {self.get_hp()}")
        
print(f"Mencoba akses paksa: {hero1._Hero__hp}")

hero1 = Hero("Layla", 100)
hero1.set_hp(-50)
print(hero1.get_hp())

print("\n--- Update Class Hero ---")
eudora = Mage("Eudora", 80, 30, 100)
balmond = Hero("Balmond", 200, 10)

eudora.info()
eudora.serang(balmond)
eudora.skill_fireball(balmond)