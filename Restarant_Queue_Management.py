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
        super().__init__("A" + str(no), name, phone, party_size)

class MediumQueue(QueueItem):
    def __init__(self, no, name, phone, party_size):
        super().__init__("B" + str(no), name, phone, party_size)

class LargeQueue(QueueItem):
    def __init__(self, no, name, phone, party_size):
        super().__init__("C" + str(no), name, phone, party_size)

count_a = 1
count_b = 1
count_c = 1
queue_matrix = []

# โหลดข้อมูลเข้า 2D Array
try:
    with open("queue.txt", "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                data = line.strip().split("|")
                queue_matrix.append(data)
                
                q_no = data[0]
                prefix = q_no[0]
                num = int(q_no[1:])

                if prefix == "A" and num >= count_a:
                    count_a = num + 1
                elif prefix == "B" and num >= count_b:
                    count_b = num + 1
                elif prefix == "C" and num >= count_c:
                    count_c = num + 1
except FileNotFoundError:
    pass

while True:
    print('=====Menu=====\n[1] New Queue\n[2] Next Queue\n[3] All queue\n[4] Cancel queue\n[0] Exit')
    menu = input('number: ')
    if menu not in ('1','2','3','4','0'):
        print('***Menu not Found***')
    else:
        menu=int(menu)
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

        new_row = [q.QueueNo, q.name, q.phone, str(q.party_size)]
        queue_matrix.append(new_row)

        with open("queue.txt", "a", encoding="utf-8") as f:
            f.write(q.strfile() + "\n")

        print(f"Queue NO: {q.QueueNo}\n")

    elif menu == 2:
        if len(queue_matrix) == 0:
            print("Queue Not Found\n")
        else:
            next_queue = queue_matrix.pop(0)
            print(f"-> Next Queue: {next_queue[0]}")
            print(f"   Name: {next_queue[1]} (Call: {next_queue[2]}, Amount: {next_queue[3]})\n")

            with open("queue.txt", "w", encoding="utf-8") as f:
                for row in queue_matrix:
                    f.write("|".join(row) + "\n")

    elif menu == 3:
        if len(queue_matrix) == 0:
            print("Queue not found\n")
        else:
            print("===== All Queue =====")
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
            for row in queue_matrix:
                if row[0].upper() == cancel:
                    found = True
                else:
                    updated_matrix.append(row)
                    
            if found:
                queue_matrix = updated_matrix
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