import learning_package.mod1 as mod1

def soma_horas(time1,time2,return_day):
    hh1 = mod1.horas(time1)
    hh2 = mod1.horas(time2)
    hh = (hh1+hh2)%24
    dd = (hh1+hh2)//24
    
    if return_day:
        return hh, dd
    else:
        return hh
    

def soma_minutos(time1,time2,return_hour):
    mm1 = mod1.minutos(time1)
    mm2 = mod1.minutos(time2)
    mm = (mm1+mm2)%60
    hh = (mm1+mm2)//60
    
    if return_hour:
        return mm, hh
    else:
        return mm
    
    
def soma_segundos(time1,time2,return_minutos):
    ss1 = mod1.segundos(time1)
    ss2 = mod1.segundos(time2)
    ss = (ss1+ss2)%60
    mm = (ss1+ss2)//60
    
    if return_minutos:
        return ss, mm
    else:
       return ss
    
    
