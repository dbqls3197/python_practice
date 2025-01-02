import uuid
note_id = str(uuid.uuid4())
#######################################
import time
counter = 0 # 카운터 초기화
note_id = f'{int(time.time())}_{counter}'
counter += 1 # 각 요청마다 카운터 증가


#######################################
import random
import string
def generate_random_id(length=30):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

note_id = generate_random_id()

#######################################
print(note_id)