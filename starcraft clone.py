class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, target):
        print(f"{self.name}이(가) {target.name}을(를) 공격합니다! [공격력 {self.damage}]")
        target.take_damage(self.damage)

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            print(f"{self.name}이(가) 파괴되었습니다!")
        else:
            print(f"{self.name}이(가) {damage}의 피해를 입었습니다. [남은 체력 {self.hp}]")

class Marine(Unit):
    def __init__(self):
        super().__init__("마린", 40, 5)

class Tank(Unit):
    def __init__(self):
        super().__init__("탱크", 150, 35)

    def siege_mode(self):
        self.damage *= 2
        print(f"{self.name}이(가) 시즈 모드로 전환되었습니다! [공격력 {self.damage}]")

    def normal_mode(self):
        self.damage //= 2
        print(f"{self.name}이(가) 일반 모드로 전환되었습니다! [공격력 {self.damage}]")

class Game:
    def __init__(self):
        self.units = []

    def create_unit(self, unit_type):
        if unit_type == "marine":
            unit = Marine()
        elif unit_type == "tank":
            unit = Tank()
        else:
            print("알 수 없는 유닛 타입입니다.")
            return
        self.units.append(unit)
        print(f"{unit.name} 유닛이 생성되었습니다!")

    def list_units(self):
        print("현재 유닛 목록:")
        for i, unit in enumerate(self.units):
            print(f"{i + 1}. {unit.name} [체력: {unit.hp}, 공격력: {unit.damage}]")

    def attack(self, attacker_index, target_index):
        if attacker_index < 1 or attacker_index > len(self.units) or target_index < 1 or target_index > len(self.units):
            print("잘못된 인덱스입니다.")
            return
        attacker = self.units[attacker_index - 1]
        target = self.units[target_index - 1]
        attacker.attack(target)

    def start(self):
        while True:
            print("\n1. 유닛 생성\n2. 유닛 목록 보기\n3. 공격\n4. 종료")
            choice = input("선택: ")
            if choice == "1":
                unit_type = input("생성할 유닛 타입 (marine/tank): ").lower()
                self.create_unit(unit_type)
            elif choice == "2":
                self.list_units()
            elif choice == "3":
                self.list_units()
                attacker = int(input("공격 유닛 번호: "))
                target = int(input("공격 대상 유닛 번호: "))
                self.attack(attacker, target)
            elif choice == "4":
                print("게임을 종료합니다.")
                break
            else:
                print("잘못된 선택입니다.")

if __name__ == "__main__":
    game = Game()
    game.start()
