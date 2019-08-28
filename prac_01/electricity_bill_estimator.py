TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

def main():
    print("Electricity Bill Estimator")
    tariff = int(input("Are you using Tariff 11 or 31? "))
    while tariff != 11 and tariff != 31:
        print("Invalid selection.")
        tariff = int(input("Are you using Tariff 11 or 31? "))
    if tariff == 11:
        price = TARIFF_11
    else:
        price = TARIFF_31
    usage = float(input("Enter daily usage in kWh "))
    days = int(input("Enter number of billed days "))
    total = price * usage * days
    print("Estimated bill: ${:.2f}".format(total))


main()
