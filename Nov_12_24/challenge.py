def format(time):
    removeSpaces = time.split(" ")
    out = ""
    for i in removeSpaces:
        if "am" in i or "pm" in i:
            out += " " + i
        else:
            out += i
    if (out[out.index(":")+1] == " "):
        out = out.replace(":",":00")
    return out

def convertTime(time):
    try:
        if ("am" in time):
            out = format(str(int(time.split("am")[0].strip()[0:time.index(":"):1])%12)+time.split("am")[0].strip()[time.index(":")::])
        elif("pm" in time):
            out = format(str(int(time.split("pm")[0].strip()[0:time.index(":"):1])+12)+time.split("pm")[0].strip()[time.index(":")::])
        elif(int(time[0:time.index(":"):1]) > 12):
            out = format(str(int(time[0:time.index(":"):1])%12)+time[time.index(":")::].strip()+" pm")
        else:
            out = format(time+" am")
        return out
    except:
        return "error, make sure your entering a time and make sure its a string"

testCases = ["12:00 am", "6:20 pm", "21:00", "5:05", "12:", "23:      21", "9:00 pm", "5: 0 5 am"]
correct = ["0:00", "18:20", "9:00 pm", "5:05 am", "12:00 am", "11:21 pm", "21:00", "5:05"]
for i in range(len(testCases)):
    print(convertTime(testCases[i]), end=" ")
    if convertTime(testCases[i]) == correct[i]:
        print("Correct")
    else:
        print("Wrong")