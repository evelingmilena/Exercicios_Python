def e_psi(x,y,alpha):
 
    a = (x-1)/(x+1)
    b = (x**2-y**2+alpha**2*(x**2-1))**2
    c = 4*alpha**2*x**2*(1-y**2)
    d = (x**2-y**2+alpha**2*(x-1)**2)**2
    e = 4*alpha**2*x**2*(1-y**2)
    f = (b+c)/(d-e)
    
    epsi = a*f**2
    return x,y
    
def x_y(x,y,r,k):
    x = 1/(2*k)*(sqrt(r**2+(z+k)**2)+sqrt(r**2+(z-k)**2))
    y = 1/(2*k)*(sqrt(r**2+(z+k)**2)-sqrt(r**2+(z-k)**2)) 
    
    z=0
    
    return y,y

