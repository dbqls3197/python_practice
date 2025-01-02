import time
import random
from datetime import datetime, timedelta

class Pet:
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind
        self.hunger = 50
        self.happiness = 50
        self.health = 100
        self.game_time = 0
        self.game_date = datetime.now()
        self.birth_date = self.game_date
        self.birthday_rewarded = False

    def check_birthday(self):
        if (
            self.game_date.date() == self.birth_date.date()
            and not self.birthday_rewarded
        ):
            print(f"{self.name}의 생일입니다! 특별한 선물을 받았습니다! 행복이 20 증가!")
            self.happiness = min(100, self.happiness + 20)
            self.birthday_rewarded = True  
        elif self.game_date.date() != self.birth_date.date():
            self.birthday_rewarded = False

    def feed(self):
        self.hunger = max(0, self.hunger - 20)
        self.happiness = min(100, self.happiness + 5)
        print(f"{self.name}에게 먹이를 줬습니다!")
        self.game_time += 0.5
        self.game_date += timedelta(hours=0.5)
        self.check_birthday()

    def play(self):
        self.happiness = min(100, self.happiness + 10)
        self.hunger = min(100, self.hunger + 5)
        print(f"{self.name}와 함께 놀았습니다!")
        self.game_time += 1
        self.game_date += timedelta(hours=1)
        self.check_birthday()

    def heal(self):
        self.health = min(100, self.health + 20)
        self.happiness = max(0, self.happiness - 5)
        print(f"{self.name}를 병원에 데려갔습니다!")
        self.game_time += 2
        self.game_date += timedelta(hours=2)
        self.check_birthday()

    def walk(self):
        self.hunger = max(0, self.hunger - 5)
        self.happiness = min(100, self.happiness + 15)
        print(f"{self.name}와 산책을 갔습니다!")
        self.game_time += 1
        self.game_date += timedelta(hours=1)
        self.check_birthday()

    def sleep(self):
        sleep_time = random.randint(8, 12)
        self.happiness = min(100, self.happiness + 10)
        print(f"{self.name}가 {sleep_time}시간 동안 잠을 잡니다.")
        self.game_time += sleep_time
        self.game_date += timedelta(hours=sleep_time)
        self.check_birthday()

    def show_status(self):
        print(f"이름: {self.name} ({self.kind})")
        print(f"건강: {self.health}, 배고픔: {self.hunger}, 행복: {self.happiness}, 게임 내 시간: {self.game_time}시간")
        print(f"게임 내 날짜: {self.game_date.strftime('%Y-%m-%d %H:%M:%S')}")

    def update_status(self):
        self.hunger = min(100, self.hunger + 5)
        self.happiness = max(0, self.happiness - 5)

        if self.hunger > 80:
            self.health = max(0, self.health - 10)
        
        if self.happiness < 20:
            self.health = max(0, self.health - 5)

        if self.health == 0:
            print(f"{self.name}가 더 이상 건강하지 않습니다. 게임 오버!")
            return False
        return True

    def random_event(self, action=None):
        events = {
            "walk": [
                {"description": "산책 중에 보물을 발견했습니다! 행복 +15", "happiness": 15, "hunger": 0, "health": 0},
                {"description": "산책 중에 반려동물이 물에 빠져 놀랐습니다. 건강 -10, 행복 -5", "happiness": -5, "hunger": 0, "health": -10},
                {"description": "산책 중에 맛있는 간식을 얻었습니다! 배고픔 -10, 행복 +5", "happiness": 5, "hunger": -10, "health": 0},
                {"description": "다른 반려동물을 만나 친구가 되었습니다! 행복 +20", "happiness": 20, "hunger": 0, "health": 0},
                {"description": "산책 중 갑자기 비가 내려 반려동물이 감기에 걸렸습니다. 건강 -15", "happiness": 0, "hunger": 0, "health": -15},
                {"description": "산책 중에 달리기를 하다가 다리를 삐었습니다. 건강 -10", "happiness": -5, "hunger": 0, "health": -10},
                {"description": "산책 중에 아주 귀여운 작은 동물을 봤습니다! 행복 +10", "happiness": 10, "hunger": 0, "health": 0},
            ],
            "default": [
                {"description": "반려동물이 병에 걸렸습니다. 건강 -20", "happiness": 0, "hunger": 0, "health": -20},
                {"description": "예쁜 새 장난감을 선물 받았습니다! 행복 +10", "happiness": 10, "hunger": 0, "health": 0},
                {"description": "반려동물이 심심해 보입니다. 행복 -10", "happiness": -10, "hunger": 0, "health": 0},
                {"description": "건강 검진을 받고 건강이 좋아졌습니다! 건강 +10", "happiness": 0, "hunger": 0, "health": 10},
                {"description": "갑자기 소음이 들려 반려동물이 불안해합니다. 행복 -5", "happiness": -5, "hunger": 0, "health": 0},
                {"description": "반려동물이 특별한 간식을 받았습니다! 행복 +15, 배고픔 -10", "happiness": 15, "hunger": -10, "health": 0},
                {"description": "반려동물이 자고 있을 때 자리를 바꿔서 불편해했습니다. 행복 -5", "happiness": -5, "hunger": 0, "health": 0},
                {"description": "반려동물이 새로운 친구를 만났습니다! 행복 +10", "happiness": 10, "hunger": 0, "health": 0},
                {"description": "반려동물이 무언가를 먹고 토했습니다. 건강 -5", "happiness": -5, "hunger": 5, "health": -5},
                {"description": "반려동물이 구석에 숨어서 잠을 자고 있습니다. 행복 +5", "happiness": 5, "hunger": 0, "health": 0},
            ],
            "play": [
                {"description": "놀다가 발을 살짝 다쳤습니다. 건강 -5", "happiness": -5, "hunger": 0, "health": -5},
                {"description": "새로운 놀이 방법을 발견했습니다! 행복 +20", "happiness": 20, "hunger": 0, "health": 0},
                {"description": "놀다가 너무 많이 뛰었습니다. 배고픔 +10", "happiness": 0, "hunger": 10, "health": 0},
                {"description": "놀이 중에 에너지를 많이 소모했습니다. 배고픔 +15, 행복 +5", "happiness": 5, "hunger": 15, "health": 0},
                {"description": "놀이 도중 반려동물이 스스로를 다치지 않게 잘 돌봤습니다! 건강 +10", "happiness": 0, "hunger": 0, "health": 10},
                {"description": "너무 과격하게 놀다가 스트레스를 받았습니다. 행복 -10", "happiness": -10, "hunger": 0, "health": 0},
                {"description": "놀이 중에 친구와 함께 놀았더니 행복이 증가했습니다! 행복 +25", "happiness": 25, "hunger": 0, "health": 0},
            ],
            "feed": [
                {"description": "먹이가 상해서 배탈이 났습니다. 건강 -10", "happiness": -10, "hunger": 0, "health": -10},
                {"description": "특별히 좋아하는 음식을 먹었습니다! 행복 +15", "happiness": 15, "hunger": -10, "health": 0},
                {"description": "먹이를 너무 많이 먹어서 속이 불편합니다. 건강 -5", "happiness": -5, "hunger": 10, "health": -5},
                {"description": "먹이가 너무 부족해서 배고픔이 증가했습니다. 배고픔 +15", "happiness": 0, "hunger": 15, "health": 0},
                {"description": "새로운 음식이 반려동물의 입맛에 맞았습니다! 행복 +20", "happiness": 20, "hunger": -5, "health": 0},
                {"description": "먹이를 주었지만 반려동물이 먹지 않았습니다. 배고픔 +10", "happiness": 0, "hunger": 10, "health": 0},
                {"description": "먹이가 너무 많이 남았네요. 반려동물이 좀 아깝다고 느낍니다. 행복 -5", "happiness": -5, "hunger": 0, "health": 0},
            ],
            "sleep": [
                {"description": "잠을 자다가 꿈에서 뛰어다녔습니다. 행복 +5", "happiness": 5, "hunger": 0, "health": 0},
                {"description": "자다가 꺠서 반려동물이 스트레스를 받았습니다. 행복 -10", "happiness": -10, "hunger": 0, "health": 0},
                {"description": "잠을 자는 동안 악몽을 꾸었습니다. 행복 -5", "happiness": -5, "hunger": 0, "health": 0},
                {"description": "잠을 자는 동안 신나는 꿈을 꾸었습니다! 행복 +15", "happiness": 15, "hunger": 0, "health": 0},
            ],
        }

        # 특정 행동에 맞는 이벤트와 기본 이벤트 병합
        event_pool = events.get(action, []) + events["default"]

        # 랜덤 이벤트 선택
        if random.randint(1, 10) > 7:  # 30% 확률로 이벤트 발생
            event = random.choice(event_pool)
            print(f"이벤트 발생! {event['description']}")
            self.happiness = min(100, max(0, self.happiness + event['happiness']))
            self.hunger = min(100, max(0, self.hunger + event['hunger']))
            self.health = min(100, max(0, self.health + event['health']))


    
    def check_event_trigger(self):
        if random.randint(1, 10) > 7:
            self.random_event()

def pet_actions(pet):
    last_input_time = time.time()
    last_real_time = time.time()

    while pet.health > 0:
        print("\n1. 상태 확인\n2. 먹이 주기\n3. 놀이하기\n4. 병원 가기")
        if pet.kind == "강아지":
            print("5. 산책 가기\n6. 잠자기\n7. 종료")
        elif pet.kind == "고양이":
            print("5. 잠자기\n6. 종료")

        choice = input("선택 (아무것도 안 하면 시간이 흐릅니다): ")
        current_time = time.time()

        real_time_passed = current_time - last_real_time
        if real_time_passed >= 60:
            game_time_increment = 0.5 * (real_time_passed // 60)
            pet.game_time += game_time_increment
            pet.game_date += timedelta(hours=game_time_increment)
            print(f"현실 시간 {real_time_passed:.1f}초 경과, 게임 내 시간이 {game_time_increment:.1f}시간 추가되었습니다.")
            last_real_time = current_time

        if choice == "1":
            pet.show_status()
        elif choice == "2":
            pet.feed()
            pet.check_event_trigger()
            pet.show_status()
        elif choice == "3":
            pet.play()
            pet.check_event_trigger()
            pet.show_status()
        elif choice == "4":
            pet.heal()
            pet.check_event_trigger()
            pet.show_status()
        elif choice == "5" and pet.kind == "강아지":
            pet.walk()
            pet.check_event_trigger()
            pet.show_status()
        elif choice == "5" and pet.kind == "고양이":
            pet.sleep()
            pet.check_event_trigger()
            pet.show_status()
        elif choice == "6" and pet.kind == "강아지":
            pet.sleep()
            pet.check_event_trigger()
            pet.show_status()
        elif choice == "6" and pet.kind == "고양이":
            print("게임을 종료합니다.")
            break
        elif choice == "7" and pet.kind == "강아지":
            print("게임을 종료합니다.")
            break
        else:
            print("올바른 옵션을 선택하세요.")

        if not pet.update_status():
            break

def main():
    name = input("반려동물의 이름을 입력하세요: ")
    print("\n반려동물 종류를 선택하세요:")
    print("1. 강아지")
    print("2. 고양이")
    
    choice = input("선택 (1-2): ")

    if choice == "1":
        kind = "강아지"
    elif choice == "2":
        kind = "고양이"
    else:
        print("잘못된 선택입니다. 강아지로 설정됩니다.")
        kind = "강아지"
    
    pet = Pet(name, kind)
    
    print("\n반려동물 상태:")
    pet.show_status()
    
    pet_actions(pet)

if __name__ == "__main__":
    main()
