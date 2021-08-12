def main():
    def mortgageEstimate():
        print("Total Price of Home?")
        totalPrice = int(input())
        print("Mortgage- " + "${:,.2f}".format(totalPrice))
        print("Number Years of for Mortgage?")
        years = int(input())
        downPayment = totalPrice / 10
        print(" your down payment would be" + str(downPayment))
        netPrice = totalPrice - downPayment
        print("With down payment applied, your total would be"  + "${:,.2f}".format(totalPrice - downPayment))

        while(years >30 ):
            print("Enter year less than 30")
            years = int(input())
        print(str(years) + "-year" )
        mortgageMonths = years * 12
        monthlyPrice = float(round(netPrice/mortgageMonths,2))

        print("The monthly rent would be $" + str(monthlyPrice))

        print("What is your current monthly rent?")
        rentPay = int(input())
        percentage = round((monthlyPrice/rentPay)*100,2)
        print("You would pay " + str(percentage) + "% of the rent that you pay now")
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

