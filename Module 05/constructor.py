class Phone:
    manufactured = 'china'
    
    # constructor
    def __init__(self, owner, brand, price):
        self.owner = owner
        self.brand = brand
        self.price = price
        
    
    def send_sms(self, phone, sms):
        text = f'sending to: {phone} {sms}'
        print(text)
        
my_phone = Phone('munim', 'Oppo', 9800)
print(my_phone.owner, my_phone.brand, my_phone.price)

her_phone = Phone('she', 'iphone', 120000)
print(her_phone.owner, her_phone.brand, her_phone.price)

my_phone.send_sms(131231, 'hey, how are you?')
her_phone.send_sms(313212, 'umm, should i block him?')

dad_phone = Phone('abbu', 'Nokia', 3000)
print(dad_phone.owner, dad_phone.brand, dad_phone.price, dad_phone.manufactured)