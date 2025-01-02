import tkinter as tk
from tkinter import messagebox
import random
import json
from datetime import datetime, timedelta


class Pet:
    def __init__(self, name, kind, birth_date=None):
        self.name = name
        self.kind = kind
        self.hunger = 50
        self.happiness = 50
        self.health = 100
        self.game_date = datetime.now()
        self.birth_date = birth_date if birth_date else datetime.now()
        self.birthday_rewarded = False

    def check_birthday(self):
        if self.game_date.date() == self.birth_date.date() and not self.birthday_rewarded:
            self.happiness = min(100, self.happiness + 20)
            self.birthday_rewarded = True
            return f"{self.name}의 생일입니다! 행복이 20 증가했습니다!"
        elif self.game_date.date() != self.birth_date.date():
            self.birthday_rewarded = False
        return None

    def feed(self):
        self.hunger = max(0, self.hunger - 15)
        self.happiness = min(100, self.happiness + 5)
        return f"{self.name}에게 먹이를 줬습니다!"

    def play(self):
        self.happiness = min(100, self.happiness + 10)
        self.hunger = min(100, self.hunger + 5)
        return f"{self.name}와 함께 놀았습니다!"

    def heal(self):
        self.health = min(100, self.health + 20)
        self.happiness = max(0, self.happiness - 5)
        return f"{self.name}를 병원에 데려갔습니다!"

    def walk(self):
        self.hunger = max(0, self.hunger - 5)
        self.happiness = min(100, self.happiness + 15)
        return f"{self.name}와 산책을 갔습니다!"

    def sleep(self):
        sleep_time = random.randint(8, 12)
        self.happiness = min(100, self.happiness + 10)
        self.game_date += timedelta(hours=sleep_time)
        return f"{self.name}가 {sleep_time}시간 동안 잠을 잡니다."

    def random_event(self, action_type):
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
        if random.randint(1, 10) > 7:  # 30% 확률로 발생
            event = random.choice(events[action_type])
            self.happiness = min(100, max(0, self.happiness + event["happiness"]))
            self.health = min(100, max(0, self.health + event["health"]))
            self.hunger = max(0, self.hunger + event["hunger"])
            return f"이벤트 발생! {event['description']}"
        return None


    def show_status(self):
        return f"이름: {self.name} ({self.kind})\n건강: {self.health}, 배고픔: {self.hunger}, 행복: {self.happiness}\n날짜: {self.game_date.strftime('%Y-%m-%d %H:%M:%S')}"


class PetApp:
    def __init__(self, root):
        self.root = root
        self.pet = None
        self.setup_ui()

    def setup_ui(self):
        self.root.title("반려동물 키우기")
        self.root.geometry("400x400")

        tk.Button(self.root, text="시작하기", command=self.start_game).pack(pady=10)
        tk.Button(self.root, text="불러오기", command=self.load_game).pack(pady=10)

    def start_game(self):
        self.clear_ui()

        tk.Label(self.root, text="반려동물 이름").pack()
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()

        tk.Label(self.root, text="반려동물 종류").pack()
        self.kind_var = tk.StringVar(value="강아지")
        tk.Radiobutton(self.root, text="강아지", variable=self.kind_var, value="강아지").pack()
        tk.Radiobutton(self.root, text="고양이", variable=self.kind_var, value="고양이").pack()

        tk.Button(self.root, text="게임 시작", command=self.initialize_pet).pack()

    def initialize_pet(self):
        name = self.name_entry.get()
        kind = self.kind_var.get()
        if not name:
            messagebox.showerror("오류", "반려동물 이름을 입력하세요.")
            return
        self.pet = Pet(name, kind)
        self.show_main_screen()

    def show_main_screen(self):
        self.clear_ui()

        tk.Label(self.root, text=self.pet.show_status()).pack()
        tk.Button(self.root, text="먹이 주기", command=self.feed_pet).pack()
        tk.Button(self.root, text="놀아주기", command=self.play_with_pet).pack()
        tk.Button(self.root, text="병원 가기", command=self.heal_pet).pack()
        if self.pet.kind == "강아지":
            tk.Button(self.root, text="산책하기", command=self.walk_pet).pack()
        tk.Button(self.root, text="잠자기", command=self.sleep_pet).pack()
        tk.Button(self.root, text="저장", command=self.save_game).pack()
        tk.Button(self.root, text="불러오기", command=self.load_game).pack()

    def clear_ui(self):
        for widget in self.root.winfo_children():
            widget.destroy()
    def update_status(self, action, action_type):
        result = action()  # 행동 수행
        birthday_msg = self.pet.check_birthday()  # 생일 체크
        random_event_msg = self.pet.random_event(action_type)  # 해당 행동에 따른 랜덤 이벤트 발생

        status_msg = [result]
        if birthday_msg:
            status_msg.append(birthday_msg)
        if random_event_msg:
            status_msg.append(random_event_msg)

        messagebox.showinfo("결과", "\n".join(status_msg))
        self.show_main_screen()


    def feed_pet(self):
        self.update_status(self.pet.feed, "feed")

    def play_with_pet(self):
        self.update_status(self.pet.play, "play")

    def heal_pet(self):
        self.update_status(self.pet.heal, "default")

    def walk_pet(self):
        self.update_status(self.pet.walk, "walk")

    def sleep_pet(self):
        self.update_status(self.pet.sleep, "sleep")

        

    def save_game(self):
        data = {
            "name": self.pet.name,
            "kind": self.pet.kind,
            "hunger": self.pet.hunger,
            "happiness": self.pet.happiness,
            "health": self.pet.health,
            "birth_date": self.pet.birth_date.isoformat(),
            "game_date": self.pet.game_date.isoformat(),
        }
        with open("pet_game_save.json", "w") as file:
            json.dump(data, file)
        messagebox.showinfo("저장", "게임이 저장되었습니다.")

    def load_game(self):
        try:
            with open("pet_game_save.json", "r") as file:
                data = json.load(file)
            self.pet = Pet(
                data["name"],
                data["kind"],
                datetime.fromisoformat(data["birth_date"]),
            )
            self.pet.hunger = data["hunger"]
            self.pet.happiness = data["happiness"]
            self.pet.health = data["health"]
            self.pet.game_date = datetime.fromisoformat(data["game_date"])
            self.show_main_screen()
            messagebox.showinfo("불러오기", "게임을 불러왔습니다.")
        except FileNotFoundError:
            messagebox.showerror("오류", "저장된 파일이 없습니다.")


if __name__ == "__main__":
    root = tk.Tk()
    app = PetApp(root)
    root.mainloop()


