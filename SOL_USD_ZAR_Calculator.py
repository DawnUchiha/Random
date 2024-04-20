
zar_usd = 20
sol_usd = 170

def main():
    
    print("Sol = 0     Usd = $0     Zar = R0")
    print(f"Convertion Rates: \nUSD to ZAR = R{zar_usd} \nSOL to USD = R{sol_usd} \nSOL to ZAR = R{zar_usd*sol_usd}")
    rate = input("Change Rates(Y/N)?")
    if rate == "Y":
        print("Changing Rates")
        zar = input("ZAR/USD = ")
        usd = input("USD/SOL = ")
        
        while True: 
            if zar.isdigit:
                zar = int(zar)
                zarusd = zar
                break
            else: 
                return zarusd
            
        while True:
            if usd.isdigit:
                usd = int(usd)
                solusd = usd
                break
            else: 
                return solusd
            
    elif rate == "y":
        print("Changing Rates")
        zar = input("ZAR/USD = ")
        usd = input("USD/SOL = ")
        
        while True: 
            if zar.isdigit:
                zar = int(zar)
                zarusd = zar
                break
            else: 
                return zarusd
            
        while True:
            if usd.isdigit:
                usd = int(usd)
                solusd = usd
                break
            else: 
                return solusd
                
    elif rate == "N":
        print("Keeping Rates")
        zarusd = zar_usd
        solusd = sol_usd
    elif rate == "n":
        print("Keeping Rates")
        zarusd = zar_usd
        solusd = sol_usd
    
    cur = input("What currency are you converting?(SOL? USD? ZAR?): ")
    
    if cur == "SOL":
        print("SOL Selected")
    elif cur == "USD":
        print("USD Selected")
    elif cur == "ZAR":
        print("ZAR Selected")
    else:
        print("That is not one of the options")
        main()
    
    c_amount_in = input(f"How much {cur} do you want to convert?: ")
    
    if c_amount_in.isdigit():
        c_amount = int(c_amount_in)
        calculate(c_amount, cur, zarusd, solusd)
        


def calculate(number, cur, zarusd, solusd):
 
    zar = 0
    usd = 0
    sol = 0
    num = int(number)
    
    if cur == "ZAR":
        usd = num / zarusd
        sol = usd / solusd 
        zar = num
    elif cur == "USD":
        zar = num * zarusd
        sol = num / solusd
        usd = num
    elif cur == "SOL":
        usd = num * solusd
        zar = usd * zarusd
        sol = num
        
    print(f"Sol = {sol}     Usd = ${usd}     Zar = R{zar}")
            

    
run = True    
while(run):
        
        if input("Ready to Calculate?") == "":
            main()  
        
        break