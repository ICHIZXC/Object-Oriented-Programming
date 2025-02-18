class User:
    def __init__(self, citizen_id: str, name: str):
        self.__citizen_id = citizen_id
        self.__name = name
        self.__accounts = []
        
    def add_account(self, account):
        self.__accounts.append(account)

class Account:
    def __init__(self, account_number: str, owner: User):
        self.__account_number = account_number
        self.__owner = owner
        self.__balance = 0
        self.__transactions = []
        
    @property
    def account_number(self):
        return self.__account_number
    
    @property
    def balance(self):
        return self.__balance
    
    def get_balance(self):
        return self.__balance
        
    def deposit(self, amount: float, atm_number: str):
        if amount < 0:
            return "Error"
        self.__balance += amount
        self.__transactions.append(f"D-ATM:{atm_number}-{amount}-{self.__balance}")
        return "success"
            
    def withdraw(self, amount: float, atm_number: str):
        if amount < 0 or amount > self.__balance:
            return "Error"
        self.__balance -= amount
        self.__transactions.append(f"W-ATM:{atm_number}-{amount}-{self.__balance}")
        return "success"
    
    def transfer(self, amount: float, recipient, atm_number: str):
        if amount <= 0 or amount > self.__balance:
            return "Error"
        self.__balance -= amount
        recipient.deposit(amount, atm_number)
        self.__transactions.append(f"TW-ATM:{atm_number}-{amount}-{self.__balance}")
        
    def get_transactions(self):
        return self.__transactions

class ATMCard:
    def __init__(self, card_number: str, account: Account, pin: str):
        self.__card_number = card_number
        self.__account = account
        self.__pin = pin
    
    @property
    def card_number(self):
        return self.__card_number
    
    @property
    def account(self):
        return self.__account
    
    def validate_pin(self, pin: str):
            return self.__pin == pin

class ATMMachine:
    def __init__(self, machine_id: str, initial_amount: float = 1000000):
        self.__machine_id = machine_id
        self.__amount = initial_amount
        
    @property
    def machine_id(self):
        return self.__machine_id
    
    def get_balance(self):
        return self.__amount
        
    def insert_card(self, card: str, pin: str):
        if card.validate_pin(pin):
            return card.account
        else:
            return "Invalid PIN"
        
    def deposit(self, account: Account, amount: float):
        if amount < 0:
            return "Error"
        result = account.deposit(amount, self.__machine_id)
        if result == 'success':
            self.__amount += amount
        
    def withdraw(self, account: Account, amount: float, max_limit: float = 40000):
            
        if amount > self.__amount:
            return "ATM has insufficient funds"
        
        if amount > max_limit:
            return "Exceeds daily withdrawal limit of 40,000 baht"
            
        result = account.withdraw(amount, self.__machine_id)

        if result == 'success':
                self.__amount -= amount
        return result

    def transfer(self, sender: Account, recipient: Account, amount: float):
        return sender.transfer(amount, recipient, self.__machine_id)

class Bank:
    def __init__(self, name: str):
        self.name__ = name
        self.__users = []
        self.__accounts = []
        self.__atms = []
        
    def add_user(self, user):
        self.__users.append(user)
        
    def add_account(self, account):
        self.__accounts.append(account)
        
    def add_atm(self, atm):
        self.__atms.append(atm)
        
    def add_card(self, card):
        self.__cards.append(card)
        
    def get_atm(self, machine_id: str):
        for atm in self.__atms:
            if atm.machine_id == machine_id:
                return atm
        return None

# Class Code


##################################################################################

# กำหนดให้ ชื่อคลาส (Class Name) ต้องเป็น Pascal case เช่น BankAccount
# กำหนดให้ ชื่อ instance และ variables ใดๆ ต้องเป็น snake case เช่น my_book
# กำหนดให้ เมื่อรับพารามิเตอร์เข้าใน method ต้องทำ validate data type และกรอบของค่า parameter ก่อนใช้เสมอ
# กำหนดให้ method ที่จัดการข้อมูลใด ต้องอยู่ในคลาสนั้น และพยายามอย่า access attribute นอกคลาส

# กำหนดรูปแบบของ user ดังนี้ {รหัสประชาชน : [ชื่อ, หมายเลขบัญชี, หมายเลข ATM , จำนวนเงิน]}
user = {
        '1-1101-12345-82-0':['Harry Potter','1234567890','12345',20000],
        '1-1101-12345-83-0':['Hermione Jean Granger','0987654321','12346',1000]
        }

atm = {'1001':1000000,'1002':200000}

bank = Bank('ICHIZXC')

user1 = User('1-1101-12345-82-0', user["1-1101-12345-82-0"][0])
user2 = User('1-1101-12345-83-0', user["1-1101-12345-83-0"][0])

atm1 = ATMMachine('1001', atm['1001'])
atm2 = ATMMachine('1002', atm['1002'])

account1 = Account(user['1-1101-12345-82-0'][1], user1)
account2 = Account(user['1-1101-12345-83-0'][1], user2)

card1 = ATMCard(user['1-1101-12345-82-0'][2], account1, '1234')
card2 = ATMCard(user['1-1101-12345-83-0'][2], account2, '1234')

bank.add_user(user1)
bank.add_user(user2)

bank.add_account(account1)
bank.add_account(account2)

bank.add_atm(atm1)
bank.add_atm(atm2)

user1.add_account(account1)
user2.add_account(account2)

account1.deposit(20000, 1001)
account2.deposit(1000, 1001)


# TODO 1 : จากข้อมูลใน user ให้สร้าง instance ของผู้ใช้ โดยมีข้อมูล
# TODO :   key:value โดย key เป็นรหัสบัตรประชาชน และ value เป็นข้อมูลของคนนั้น ประกอบด้วย
# TODO :   [ชื่อ, หมายเลขบัญชี, หมายเลขบัตร ATM, จำนวนเงินในบัญชี]
# TODO :   return เป็น instance ของธนาคาร
# TODO :   และสร้าง instance ของเครื่อง ATM จำนวน 2 เครื่อง
# TODO :   ต้อง validate ข้อมุลทุกอย่าง ก่อนสร้าง instance ใดๆ


# TODO 2 : เขียน method ที่ทำหน้าที่สอดบัตรเข้าเครื่อง ATM มี parameter 2 ตัว ได้แก่ 1) instance ของธนาคาร
# TODO     2) instance ของ atm_card
# TODO     return ถ้าบัตรถูกต้องจะได้ instance ของ account คืนมา ถ้าไม่ถูกต้องได้เป็น None
# TODO     ควรเป็น method ของเครื่อง ATM


# TODO 3 : เขียน method ที่ทำหน้าที่ฝากเงิน โดยรับ parameter 3 ตัว คือ 1) instance ของเครื่อง atm
# TODO     2) instance ของ account 3) จำนวนเงิน
# TODO     การทำงาน ให้เพิ่มจำนวนเงินในบัญชี และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0


# TODO 4 : เขียน method ที่ทำหน้าที่ถอนเงิน โดยรับ parameter 3 ตัว คือ 1) instance ของเครื่อง atm
# TODO     2) instance ของ account 3) จำนวนเงิน
# TODO     การทำงาน ให้ลดจำนวนเงินในบัญชี และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0 และ ไม่ถอนมากกว่าเงินที่มี


# TODO 5 : เขียน method ที่ทำหน้าที่โอนเงิน โดยรับ parameter 4 ตัว คือ 1) instance ของเครื่อง atm
# TODO     2) instance ของ account ตนเอง 3) instance ของ account ที่โอนไป 4) จำนวนเงิน
# TODO     การทำงาน ให้ลดจำนวนเงินในบัญชีตนเอง และ เพิ่มเงินในบัญชีคนที่โอนไป และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0 และ ไม่ถอนมากกว่าเงินที่มี


# Test case #1 : ทดสอบ การ insert บัตร โดยค้นหาเครื่อง atm เครื่องที่ 1 และบัตร atm ของ harry
# และเรียกใช้ function หรือ method จากเครื่อง ATM
# ผลที่คาดหวัง : พิมพ์ หมายเลข account ของ harry อย่างถูกต้อง และ พิมพ์หมายเลขบัตร ATM อย่างถูกต้อง
# Ans : 12345, 1234567890, Success
test1 = atm1.insert_card(card1, '1234')
print(f"{card1.card_number}, {test1.account_number}, Success\n")


# Test case #2 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 1000 บาท
# ให้เรียกใช้ method ที่ทำการฝากเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนฝาก หลังฝาก และ แสดง transaction
# Hermione account before test : 1000
# Hermione account after test : 2000
print(account2.balance)
atm2.deposit(account2, 1000)
print(account2.balance)
print()


# Test case #3 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน -1 บาท
# ผลที่คาดหวัง : แสดง Error
print(atm2.deposit(account2, -1))
print()


# Test case #4 : ทดสอบการถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 500 บาท
# ให้เรียกใช้ method ที่ทำการถอนเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน และ แสดง transaction
# Hermione account before test : 2000
# Hermione account after test : 1500
print(account2.balance)
atm2.withdraw(account2, 500)
print(account2.balance)
print()


# Test case #5 : ทดสอบถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 2000 บาท
# ผลที่คาดหวัง : แสดง Error
print(atm2.withdraw(account2, 2000))
print()

# Test case #6 : ทดสอบการโอนเงินจากบัญชีของ Harry ไปยัง Hermione จำนวน 10000 บาท ในเครื่อง atm เครื่องที่ 2
# ให้เรียกใช้ method ที่ทำการโอนเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Harry ก่อนถอน หลังถอน และ แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน แสดง transaction
# Harry account before test : 20000
# Harry account after test : 10000
# Hermione account before test : 1500
# Hermione account after test : 11500
print(account1.balance)
print(account2.balance)

atm2.transfer(account1, account2, 10000)

print(account1.balance)
print(account2.balance)
print()


# Test case #7 : แสดง transaction ของ Hermione ทั้งหมด 
# ผลที่คาดหวัง
# Hermione transaction : D-ATM:1002-1000-2000
# Hermione transaction : W-ATM:1002-500-1500
# Hermione transaction : TD-ATM:1002-10000-11500
for i in account2.get_transactions():
    print(f"Hermione transaction : {i}")
print()


# Test case #8 : ทดสอบการใส่ PIN ไม่ถูกต้อง 
# ให้เรียกใช้ method ที่ทำการ insert card และตรวจสอบ PIN
atm_machine = bank.get_atm('1001')
test_result = atm_machine.insert_card(card1, '9999')  # ใส่ PIN ผิด
print(test_result)
print()
# ผลที่คาดหวัง
# Invalid PIN

# Test case #9 : ทดสอบการถอนเงินเกินวงเงินต่อวัน (40,000 บาท)
atm_machine = bank.get_atm('1001')
account = atm_machine.insert_card(card1, '1234')  # PIN ถูกต้อง
harry_balance_before = account.get_balance()
print(f"Harry account before test: {harry_balance_before}")
print("Attempting to withdraw 45,000 baht...")
result = atm_machine.withdraw(account, 45000)
print(f"Expected result: Exceeds daily withdrawal limit of 40,000 baht")
print(f"Actual result: {result}")
print(f"Harry account after test: {account.get_balance()}")
print("-------------------------")

# Test case #10 : ทดสอบการถอนเงินเมื่อเงินในตู้ ATM ไม่พอ
atm_machine = bank.get_atm('1002')  # สมมติว่าตู้ที่ 2 มีเงินเหลือ 200,000 บาท
account = atm_machine.insert_card(card1, '1234')
print("Test case #10 : Test withdrawal when ATM has insufficient funds")
print(f"ATM machine balance before: {atm_machine.get_balance()}")
print("Attempting to withdraw 250,000 baht...")
result = atm_machine.withdraw(account, 250000)
print(f"Expected result: ATM has insufficient funds")
print(f"Actual result: {result}")
print(f"ATM machine balance after: {atm_machine.get_balance()}")
print("-------------------------")