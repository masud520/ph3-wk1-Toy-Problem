def clock_converter(timestr):
    #remove "." in the time
    time=timestr.replace('.','')
    #handle 12am
    if time[:2]=="12"and time[-2:]=="am":
        return('00'+time[2:-2])
    #handle 12pm
    elif time[:2]=="12" and time[-2:]=="pm":
            return(time[0:-2])
    #handle am
    elif time[-2:]=="am":
        am_time=int(time.replace("am",""))
        #handle if hour is a single digit
