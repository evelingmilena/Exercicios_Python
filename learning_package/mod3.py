import learning_package.mod2 as mod2

def soma_times(time1, time2):

    return_minutos = True
    ss, mm0 = mod2.soma_segundos(time1,time2,return_minutos)
    
    return_hour = True
    mm, hh0 = mod2.soma_minutos(time1,time2,return_hour)
    mm = mm + mm0
    
    return_day = False
    hh = mod2.soma_horas(time1,time2,return_day)
    hh = hh + hh0
    
    time3 = [hh,mm,ss]
    
    return time3
