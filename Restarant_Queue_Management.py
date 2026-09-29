class QueueItem:
    def __init__(self, QueueNo, name, phone, party_size, status):
        self.QueueNo=QueueNo
        self.name=name
        self.phone=phone
        self.party_size=party_size
        self.status=status
    def strfile(self):
        return f'{self.QueueNo}|{self.name}|{self.phone}|{self.party_size}|{self.status}'

class SmallQueue(QueueItem):
    def __init__(self, name, phone, party_size, status):
        super().__init__(QueueNo, name, phone, party_size, status)
        
class MediumQueue(QueueItem):
    def __init__(self, name, phone, party_size, status):
        super().__init__(QueueNo, name, phone, party_size, status)
        self.Queue_no=Queue_no
        
class LargeQueue(QueueItem):
    def __init__(self, name, phone, party_size, status):
        super().__init__(QueueNo, name, phone, party_size, status)
        self.Queue_no=Queue_no

while True:
    print('=====Menu=====\n[1] New Queue\n[2] Next Queue\n[3] All queue\n[4] Cancel queue\n[0] Exit')
    menu=int(input('number: '))
    print('==============')
    if menu==1:
        amount=int(input('amount: '))
        print('==============')
        if 2>=amount>=1:
            pass
        elif 4>=amount>2:
            pass
        elif amount>4:
            pass
    elif menu==2:
        pass
    elif menu==3:
        pass
    elif menu==4:
        pass
    elif menu==0:
        pass
    else:
        print('***Not Found***')