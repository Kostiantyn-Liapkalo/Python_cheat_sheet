from collections import UserList


class AmountPaymentList(UserList):

    def amount_payment(self):

        self.sum = 0
        for payment in self.data:
            if payment > 0:
                self.sum += payment
        return self.sum
