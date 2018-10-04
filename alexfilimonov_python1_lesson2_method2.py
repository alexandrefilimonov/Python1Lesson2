import num2word
d = "02.11.2013"
digit = int(d[0:2])
def twodigit_tomonth(argument):
    switcher = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    return switcher.get(argument, "nothing") 
print("Date: ", num2word.to_card(digit), twodigit_tomonth(int(d[3:5])), d[6:], "year")
 