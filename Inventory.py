months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
mon_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # Represents the days in each months
stock = {}
Revenue = {}
Output = {}
name = {}

# In this we take the input from a text file and write the output into another text file.
# Input is in the form of {'start_year': , 'start_stock':,'start_revenue':}
'''
In AU_INV_START.txt took a inputs
start_year 2000
start_stock 1000
start_revenue 705
'''


def read_data():
    f = open('AU_INV_START.txt', 'r')  # open the text fine and 'r' is to read the file
    for line in f.readlines():  # Complete the loop till each line is read
        a = line.split()
        name[a[0]] = a[1]

    return name


read_data()
value = read_data()

start_year = int(value['start_year'])
start_stock = int(value['start_stock'])
start_revenue = int(value['start_revenue'])


def ap_year(first, last, difference):  # After the first Global crisis, each crisis comes after every 11 years
    ap = [first]  # After 2009 it is following a pattern as mathematical Arithmetic progression(AP)
    while first + difference < last:
        first = first + difference
        ap.append(first)
    return ap


ap1 = ap_year(2009, start_year, 11)  # Global crisis starts after 9years of the start year and continue two years
ap2 = ap_year(2010, start_year, 11)  # continued first year
ap3 = ap_year(2011, start_year, 11)  # continued second year


def cal_revenue(initial_revenue):  # calculating the complete revenue
    for year in range(2000, start_year + 1):
        year1 = []

        for i in range(12):  # 12 indicates the indexes of months with month_days
            if year in ap1:
                initial_revenue = (initial_revenue * 1.1)  # 10% increase for global crisis
                CEU = initial_revenue  # CEU = cost of each umbrella
            elif year in ap2:
                initial_revenue = (initial_revenue * 1.05)  # 5% increase for global crisis
                CEU = initial_revenue
            elif year in ap3:
                initial_revenue = (initial_revenue * 1.03)  # 3% increase for global crisis
                CEU = initial_revenue
            elif i in (0, 1):
                CEU = initial_revenue


            elif i in (2, 3, 4, 5):
                initial_revenue = (initial_revenue / 1.2)  # cost decreased by 20% (Original cost with out peek)
                CEU = initial_revenue


            elif i in (6, 7, 8, 9):
                initial_revenue = (initial_revenue * 1.05)  # cost increases by 5%
                CEU = initial_revenue


            elif i in (10, 11):
                initial_revenue = (initial_revenue * 1.2)  # cost increased by 20% peak
                CEU = initial_revenue

            if year % 4 == 0:   # Condition for leap year and the feb date will be updated
                mon_days[1] = 29

            for j in range(mon_days[i]):
                if i in (0, 1, 10, 11):
                    TD = 36 * mon_days[i]   # TD = Total Distribution
                else:
                    TD = 26 * mon_days[i]
                CDU = 0.8 * CEU             # CDU = cost of defective umbrella
                DEF = 0.05 * TD             # DEF = Total defective umbrella
                NDEF = TD - DEF             # NDEF = Non defective
                TC = round((CEU * NDEF) + (CDU * DEF), 2)

            year1.append(TC)
        Total = round(sum(year1), 2)
        Revenue[year] = Total
    return Revenue


cal_revenue(start_revenue)
R = Revenue


def cal_stock_revenue(initial_stock):  # Calculate stock
    for year in range(2000, start_year + 1):
        year1 = []
        for i in range(12):             # 12 indicates the indexes of months with month_days
            if i in (0, 1, 10, 11):
                if year in ap1:
                    d = int(0.8 * 36)   # 20% decrease in the distribution Global crisis at peak season
                elif year in ap2:
                    d = int(0.9 * 28)   # 10% decrease in the distribution Global crisis at peak season
                elif year in ap3:
                    d = int(0.95 * 25)  # 5% decrease in the distribution Global crisis at peak season
                else:
                    d = 36              # Distribution at peak season
            else:
                if year in ap1:
                    d = int((0.8 * 36) / 1.35)  # 20% decrease in the distribution Global crisis at normal season
                elif year in ap2:
                    d = int((0.9 * 28) / 1.35)  # 20% decrease in the distribution Global crisis at normal season
                elif year in ap3:
                    d = int((0.95 * 25) / 1.35)  # 20% decrease in the distribution Global crisis at normal season
                else:
                    d = 26      # Distribution at Normal season
            if i in (6,):
                initial_stock = initial_stock * (1 + 0.1)  # 10% increase in supply every financial year
            if year % 4 == 0:  # Condition for leap year and the feb date will be updated
                mon_days[1] = 29
            for j in range(mon_days[i]):
                initial_stock = initial_stock - d
                if initial_stock < 400:
                    initial_stock = initial_stock + 600
                    initial_stock = int(initial_stock)
        year1.append(initial_stock)
        stock[year] = year1
    return stock
    return Revenue


cal_stock_revenue(start_stock)
Y = stock


def write_data(result):
    k = Y[start_year]
    end_stock = int(str(k).strip('[]'))
    Output["end-year"] = start_year + 1
    Output["end_stock"] = end_stock
    Output["end_revenue"] = R[start_year]
    f = open('AU_INV_END.txt', 'w')  # open the text fine and 'w' is to write the file
    f.write(str(result))


write_data(Output)
print(Output)
