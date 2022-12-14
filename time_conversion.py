# a function takes in a 12-hour time as a string and convert it to 24-hour
def timeConversion(s):
    s = s.split(":")
    if s[0] == "12" and s[2][2] == "A":
        s[0] = "00"
        s[2] = s[2][0:2]
        return ":".join(s)
    elif s[2][2] == "P":
        s[0] = str(int(s[0])+12)
        s[2] = s[2][0:2]
        return ":".join(s)
    else:
        s[2] = s[2][0:2]
        return ":".join(s)

#some examples
if __name__ == "__main__":
    print(timeConversion("12:00:00AM"))
    print(timeConversion("12:00:00PM"))
    print(timeConversion("09:40:30PM"))
    print(timeConversion("8:25:59PM"))
