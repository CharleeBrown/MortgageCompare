def main():
    def mortgageEstimate():
        print("Total Price of Home?")
        totalPrice = int(input())
        print("Mortgage- " + "${:,.2f}".format(totalPrice))
        print("Number Years of for Mortgage?")
        years = int(input())
        print("\n")
        downPayment = totalPrice / 10
        print("down payment would be " + "${:,.2f}".format(downPayment))
        netPrice = totalPrice - downPayment
        print("\n")
        print("With down payment applied, your total would be "  + "${:,.2f}".format(totalPrice - downPayment))

        while(years >30 ):
            print("Enter year less than 30")
            years = int(input())
        print("You chose a " + str(years) + "-year mortgage. " )
        mortgageMonths = years * 12
        print("\n")
        monthlyPrice = float(round(netPrice/mortgageMonths,2))

        print("The monthly rent would be $" + str(monthlyPrice))
        print("What is your current monthly rent?")
        rentPay = int(input())
        print("\n")
        percentage = round((monthlyPrice/rentPay)*100,2)
        print("You would pay " + str(percentage) + "% of the rent that you pay now\n")
        print("If you paid your current rent, you would own it in " + str(round((totalPrice / rentPay)/12,0)) + " years")
        return rentPay
    
    def PerCheck(price):
        _perCheck = round(price/2,2)
        print("For your rent, save $" + str(_perCheck) + " per check")
    mortgageEstimate()
    #PerCheck(mortgageEstimate())
  
if __name__ == "__main__":
    while True:
        main()

