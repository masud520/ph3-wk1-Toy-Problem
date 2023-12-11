def clock_converter(timestr):
    #remove "." in the time
    time=timestr.replace('.','')
    #handle 12am
    if time[:2]=="12"and time[-2:]=="am":
        return('00'+time[2:-2])
