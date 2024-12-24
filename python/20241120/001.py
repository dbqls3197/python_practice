# class Student:

#     def __init__ (self,name,scores):
#         self.name = name
#         self.scores = scores
        

#     def total_score(self):
#         return sum(self.scores.values())

#     def avg_score(self):
#         return self.total_score() / len(self.scores)

#     def show_info(self):
#         print(f"학생 이름: {self.name}")
#         for subject, score in self.scores.items():
#             print(f"{subject} : {score}")
#         print(f"총점: {self.total_score()}, 평균{self.avg_score():.2f}\n") 

# students =[]

# students.append(Student("홍길동",{"국어":85, "영어": 90, "수학":78}))
# students.append(Student("김영희",{"국어":92, "영어": 88, "수학":95}))
# students.append(Student("이철수",{"국어":70, "영어": 75, "수학":80}))

# '''std =Student("홍길동",{"국어":85, "영어": 90, "수학":78})
# std.show_info()
# '''
# # print(students)
# for student in students:
#     student.show_info()
# # name, scores
# # Student("홍길동",{"국어":85, "영어": 90, "수학":78})




'''
1. 항목 추가
2. 항목 삭제
3. 목록 보기
4. 종료
원하는 작업을 선택하세요:
'''
# 항목: 두부, 오이...
import os
def shopping_list():
    items = []

    while True:

        print("1. 항목 추가") 
        print("2. 항목 삭제") 
        print("3. 목록 보기") 
        print("4. 종료")

        print(f"\n{items}\n")

        choice = input("원하는 작업을 선택하세요: ")

        if choice =="1":
            item =input("--> 추가할 상품은? ")
            if item:
                items.append(item)
                print(f"{item}이 추가되었습니다.")
                input("아무키나 누르세요...")
        elif choice == "2":
            item = input ("--> 삭제할 상품은? ")
            if item in items:
                items.remove(item)
                print(f"{item}이 삭제되었습니다.")
                input("아무키나 누르세요...")
            else:
                print("장바구니가 비어 있습니다")
                input("아무키나 누르세요...")
        elif choice == "3":
            if items:
                print(" == 현재 장바구니 목록==")
                for item in items:
                    print(f"{item}")
                input("아무키나 누르세요...")
            else:
                print("장바구니가 비어 있습니다.")
                input("아무키나 누르세요...")
        elif choice == "4":
            print("프로그램을 종료합니다.")
            break

shopping_list()