

class bank:
    bank_name = "State Bank of Pakistan!!"  # class variable
    
    def change_bank_name(cls, name):
        cls.bank_name = name

    def show(self):
        print("Bank Name:", self.bank_name)

acc1 = bank()
acc2 = bank()

acc1.show()
acc2.show()

acc1.change_bank_name("State Bank of Pakistan!!")
   