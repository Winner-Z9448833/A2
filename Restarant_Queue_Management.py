class QueueItem:
    def __init__(self, QueueNo, name, phone, party_size):
        self.QueueNo = QueueNo
        self.name = name
        self.phone = phone
        self.party_size = party_size

    def strfile(self):
        return f'{self.QueueNo}|{self.name}|{self.phone}|{self.party_size}'

# คิวโต๊ะเล็ก
class SmallQueue(QueueItem):
    def __init__(self, no, name, phone, party_size):
        QueueNo = "A" + str(no)
        super().__init__(QueueNo, name, phone, party_size)

# คิวโต๊ะกลาง
class MediumQueue(QueueItem):
    def __init__(self, no, name, phone, party_size):
        QueueNo = "B" + str(no)
        super().__init__(QueueNo, name, phone, party_size)

# คิวโต๊ะใหญ่
class LargeQueue(QueueItem):
    def __init__(self, no, name, phone, party_size):
        QueueNo = "C" + str(no)
        super().__init__(QueueNo, name, phone, party_size)


count_a = 1
count_b = 1
count_c = 1

# Array2D ไว้เก็บข้อมูล
queue_matrix = []
# ป้องกัน error
try:
    with open("queue.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            if line.strip():
                data = line.strip().split("|")
                queue_matrix.append(data)  # เพิ่มข้อมูลแต่ละแถวเข้า 2D Array
                
                q_no = data[0]
                prefix = q_no[0]        # ดึงชื่อต้น A, B, C
                num = int(q_no[1:])     # ดึงลำดับตัวเลข

                if prefix == "A" and num >= count_a:
                    count_a = num + 1
                elif prefix == "B" and num >= count_b:
                    count_b = num + 1
                elif prefix == "C" and num >= count_c:
                    count_c = num + 1
except FileNotFoundError:
    pass # ถ้ายังไม่มีไฟล์ ให้ใช้ค่าเริ่มต้น 1
#ส่วนของ loop รับเลข menu
while True:
    print('=====Menu=====\n[1] New Queue\n[2] Next Queue\n[3] All queue\n[4] Cancel queue\n[0] Exit')
    menu = int(input('number: '))
    print('==============')

    if menu == 1:
        name = input('name: ')
        phone = input('phone: ')
        amount = int(input('amount: '))
        print('==============')

        if 2 >= amount >= 1:
            q = SmallQueue(count_a, name, phone, amount)
            count_a += 1
        elif 4 >= amount > 2:
            q = MediumQueue(count_b, name, phone, amount)
            count_b += 1
        elif amount > 4:
            q = LargeQueue(count_c, name, phone, amount)
            count_c += 1

        # เพิ่มข้อมูลเข้าสู่ 2D Array (queue_matrix)
        new_row = [q.QueueNo, q.name, q.phone, str(q.party_size)]
        queue_matrix.append(new_row)

        # บันทึกลงไฟล์
        with open("queue.txt", "a", encoding="utf-8") as f:
            f.write(q.strfile() + "\n")

        print(f"Queue NO: {q.QueueNo}\n")

    elif menu == 2:
        if len(queue_matrix) == 0:
            print("Queue Not Found\n")
        else:
            # ดึงข้อมูลคิวแรกจาก 2D Array (แถวที่ 0)
            next_queue = queue_matrix.pop(0) 
            
            print(f"-> Next Queue: {next_queue[0]}")
            print(f"   Name: {next_queue[1]} (Call: {next_queue[2]}, Amount: {next_queue[3]})\n")

            # เขียนข้อมูลที่เหลือใน 2D Array กลับลงไปในไฟล์ใหม่
            with open("queue.txt", "w", encoding="utf-8") as f:
                for row in queue_matrix:
                    f.write("|".join(row) + "\n")

    elif menu == 3:
        if len(queue_matrix) == 0:
            print("Queue not found\n")
        else:
            print("===== All Queue (2D Array) =====")
            # วนลูปแสดงข้อมูลจาก 2D Array โดยตรง
            for row in queue_matrix:
                print(f"Queue: {row[0]} | Name: {row[1]} | Call: {row[2]} | Amount: {row[3]}")
            print("===========================\n")

    elif menu == 4:
        cancel= input("Queue cancel No: ").strip().upper()
        
        if len(queue_matrix) == 0:
            print("Queue not found\n")
        else:
            updated_matrix = []
            found = False
            
            # ค้นหาและกรองข้อมูลออกจาก 2D Array
            for row in queue_matrix:
                if row[0].upper() == cancel:
                    found = True
                else:
                    updated_matrix.append(row)
                    
            if found:
                queue_matrix = updated_matrix
                # เขียนข้อมูลที่เหลือกลับลงไฟล์
                with open("queue.txt", "w", encoding="utf-8") as f:
                    for row in queue_matrix:
                        f.write("|".join(row) + "\n")
                print(f"-> Cancel Queue {cancel} Completed\n")
            else:
                print(f"*** Queue not found {cancel} in file ***\n")

    elif menu == 0:
        print("Exit program")
        break
    else:
        print('***Not Found***')