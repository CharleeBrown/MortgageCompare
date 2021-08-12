def main():
    def mortgageEstimate():
        print("Total Price of Home?")
        totalPrice = int(input())
        print("Years of Mortgage?")
        years = int(input())
        while(years >30 ):
            print("Enter year less than 30")
            years = int(input())
        monthlyPrice = float(round(totalPrice/(years*12),2))
        print("The monthly rent would be $" + str(monthlyPrice))
        print("What is your current monthly rent?")
        rentPay = int(input())
        percentage = round((monthlyPrice/rentPay)*100,2)
        print("You would pay " + str(percentage) + "% of the rent that you pay now")
        return rentPay
    
    def PerCheck(price):
        _perCheck = round(price /2,2)
        print("For your rent, save $" + str(_perCheck) + " per check")
    


    PerCheck(mortgageEstimate())
  
        

if __name__ == "__main__":
    main()

