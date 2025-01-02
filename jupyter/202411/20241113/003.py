# 일정추가
# 일정출력
# 예정된 일정 출력
# [('회의','2024-11-15 15:30')],[('회의2','2024-11-17 14:00')]
#import datetime # datetime.datetime
from datetime import datetime # datetime

# 일정 목록 초기화
events = []

# 화면 클리어
def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

# 파일에 저장된 일정을 일정목록 변수로 초기화
def load_events(filename="events.txt"):
    global events
    with open(filename,'r',encoding="utf-8") as f:
        for line in f:
            event_name, event_date_str= line.strip().split("|")
            event_date = datetime.strptime(event_date_str,"%Y-%m-%d %H:%M")
            events.append((event_name,event_date))

#일정 파일로 저장
    
def save_event(filename="events.txt"):
    with open(filename,"w",encoding="utf-8") as f:
        for event_name,event_date in events:
            f.write(f"{event_name}|{event_date.strftime("%Y-%m-%d %H:%M")}\n")

# 일정추가
def add_event(event_name, event_date):
    events.append((event_name, event_date))

# 모든 일정 출력
def show_events():

    if not events:
        print("일정이 없습니다")
        return
        
    print("[모든 일정]: ")
    for event_name, event_date in events:
        print(f"-{event_name}: {event_date.strftime('%Y-%m-%d %H:%M')}")

# 남은 일정 출력
def show_upcoming_events():
    now = datetime.now()
    upcoming_events =[event for event in events if event[1] >= now]

    print()
    print("[남은 일정]")

    for event_name, event_date in upcoming_events:
            days_left = (event_date -now).days
            print(f"-{event_name}: {event_date.strftime('%Y-%m-%d %H:%M')}(남은일수: {days_left}일)")


add_event("회의",datetime(2024, 10, 20, 14,0))
add_event("생일 파티",datetime(2024, 12, 5, 18,30))
add_event("발표 준비",datetime(2024, 11, 15, 9,0))
print(events)

#모든 일정보기
show_events()

#남은 일정보기
show_upcoming_events()

def main():
    load_events()
    while True:
        print("\n일정 관리 프로그램")
        print("1. 일정 추가")
        print("2. 모든 일정 보기")
        print("3. 다가오는 일정 보기")
        print("4. 종료")

        choice = input("원하는 작업을 선택하세요 (1~4): ")

        if choice =="1":
            event_name = input("일정 이름을 입력하세요:")
            event_date_str = input("일정 날짜와 시간을 입력하세요 (YYYY-MM-DD HH:MM):")
            event_date = datetime.strptime(event_date_str,'%Y-%m-%d %H:%M')
            add_event(event_name, event_date)
        elif choice =="2":
            show_events()
        elif choice =="3":
            show_upcoming_events()
        elif choice =="4":
            print("프로그램을 종료합니다")
            break
        else:
            print("잘못된 선택입니다. 다시 시도하세요")
main()