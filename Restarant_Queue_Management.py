class QueueItem:
    def __init__(self, QueueNo, name, phone, party_size):
        self.QueueNo = QueueNo
        self.name = name
        self.phone = phone
        self.party_size = party_size

    def strfile(self):
        return f'{self.QueueNo}|{self.name}|{self.phone}|{self.party_size}'


class SmallQueue(QueueItem):
    def __init__(self, no, name, phone, party_size):
        QueueNo = "A" + str(no)
        super().__init__(QueueNo, name, phone, party_size)


class MediumQueue(QueueItem):
    def __init__(self, no, name, phone, party_size):
        QueueNo = "B" + str(no)
        super().__init__(QueueNo, name, phone, party_size)


class LargeQueue(QueueItem):
    def __init__(self, no, name, phone, party_size):
        QueueNo = "C" + str(no)
        super().__init__(QueueNo, name, phone, party_size)

count_a = 1
count_b = 1
count_c = 1

try:
    with open("queue.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            if line.strip():
                data = line.strip().split("|")
                q_no = data[0]
                
                prefix = q_no[0]         # ดึงหมวด A, B, C
                num = int(q_no[1:])      # ดึงลำดับตัวเลข

                if prefix == "A" and num >= count_a:
                    count_a = num + 1
                elif prefix == "B" and num >= count_b:
                    count_b = num + 1
                elif prefix == "C" and num >= count_c:
                    count_c = num + 1
except FileNotFoundError:
    pass # ถ้ายังไม่มีไฟล์ ให้ใช้ค่าเริ่มต้น 1

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

        with open("queue.txt", "a", encoding="utf-8") as f:
            f.write(q.strfile() + "\n")

        print(f"Queue NO: {q.QueueNo}\n")

    
    elif menu == 2:
        try:
            with open("queue.txt", "r", encoding="utf-8") as f:
                lines = f.readlines()

            if len(lines) == 0:
                print("Queue Not Found\n")
            else:
                next_queue = lines[0].strip()
                data = next_queue.split("|")
                
                print(f"-> Next Queue: {data[0]}")
                print(f"   Name: {data[1]} (Call: {data[2]}, Amount: {data[3]})\n")

                with open("queue.txt", "w", encoding="utf-8") as f:
                    f.writelines(lines[1:])

        except FileNotFoundError:
            print("NO Queue (add Queue first)\n")
    elif menu == 3:
        try:
            with open("queue.txt", "r", encoding="utf-8") as f:
                lines = f.readlines()

            if len(lines) == 0:
                print("Queue not found\n")
            else:
                print("===== All Queue =====")
                for line in lines:
                    data = line.strip().split("|")
                    print(f"Queue: {data[0]} | Name: {data[1]} | Call: {data[2]} | Amount: {data[3]}")
                print("===========================\n")
        except FileNotFoundError:
            print("NO Queue (add Queue first)\n")
    elif menu == 4:
        cancel_no = input("Queue cancel No: ").strip().upper()
        
        try:
            with open("queue.txt", "r", encoding="utf-8") as f:
                lines = f.readlines()

            if len(lines) == 0:
                print("Queue not found\n")
            else:
                updated_lines = []
                found = False
                for line in lines:
                    data = line.strip().split("|")
                    if data[0].upper() == cancel_no:
                        found = True
                    else:
                        updated_lines.append(line)
                if found:
                    with open("queue.txt", "w", encoding="utf-8") as f:
                        f.writelines(updated_lines)
                    print(f"-> Cancel Queue {cancel_no} Completed\n")
                else:
                    print(f"*** Queue not found {cancel_no} in file ***\n")

        except FileNotFoundError:
            print("Queue not found\n")
    elif menu == 0:
        print("Exit program")
        break
    else:
        print('***Not Found***')