class Bike:
    def __init__(self, description, condition, saleprice, costprice=0):#defualting CP
        self.Describe = description
        self.SP = saleprice
        self.Cond = condition
        self.CP = costprice
        self.sold = False# all other attributes are different for all instances but this is same
        print(f"Created new instance {self}")# use f-strings executed at run time {object}
        pass
    def update_SP(self):
        self.SP= self.CP + 0.2 * (self.CP)

    def sell(self):
        self.sold = True
        profit = self.SP - self.CP
        return profit

    def servicing(self):
        if self.Cond=='BAD':
            self.SP = self.update_SP()
        elif self.Cond=='GOOD':
            self.SP = self.SP *(1.1)
        else: self.SP = self.SP
        return self.SP

if __name__ == "__main__":
    my_bike = Bike("REI COOP","GOOD",1200,700)
    print(my_bike.sold)
    print(my_bike.servicing())
    print(my_bike.sell())
    profit = my_bike.sell()
    print(profit)
    #print(my_bike.CP)
    #print(my_bike.sold)
    #profit = my_bike.sell()
    print(f"profit is {profit.CP} dollars for my {my_bike.Describe}")


