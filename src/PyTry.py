def main():
    import locale
    locale.setlocale(locale.LC_ALL,'')
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



    mortgageEstimate()

if __name__ == "__main__":
    main()

