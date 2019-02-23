class Messange:

    def __init__(self, recipient, sender, receiving_time, message):
        self.recipient = recipient
        self.sender = sender
        self.receiving_time = receiving_time
        self.message = message

    def show_message(self):
        print ('messages:'+ self.recipient)
        pass

    def show_detail_message(self):
        print ('recipient:' + self.recipient)
        print ('sender:' + self.sender)
        print ('receiving time:'+ self.receiving_time)
        print('message:' + self.message)

    def sent_message(self,recipinet,message):
        pass
