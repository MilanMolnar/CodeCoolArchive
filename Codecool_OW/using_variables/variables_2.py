
def interval_in_day(hourprompt1, minuteprompt1, secondprompt1, hourprompt2, minuteprompt2, secondprompt2):
    while True:
        try:
            hour = int(input(hourprompt1))
            minute = int(input(minuteprompt1))
            second = int(input(secondprompt1))
            hour2 = int(input(hourprompt2))
            minute2 = int(input(minuteprompt2))
            second2 = int(input(secondprompt2))
        except ValueError:
            print("Egész számot adj meg!")
            continue
        if isinstance(hour, int) and isinstance(minute, int) and isinstance(second, int) and isinstance(hour2, int) and isinstance(minute2, int) and isinstance(second2, int):
            break
    hour_in_sec1 = hour * 3600
    minute_in_sec1 = minute * 60
    hour_in_sec2 = hour2 * 3600
    minute_in_sec2 = minute2 * 60
    time1 = second + hour_in_sec1 + minute_in_sec1
    time2 = second2 + hour_in_sec2 + minute_in_sec2
    x = time1 - time2
    return x


result = interval_in_day("Ird be az első órát: ", "Ird be az első percet: ", "Ird be az első másodpercet: ",
                "Ird be az masodik orat: ", "Ird be a masodik percet: ", "Ird be a masodik masodpercet: ")
print("A két idő közötti különbség: " +   str(result) + " másodperc")