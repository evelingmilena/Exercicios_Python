import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.special import lpmv, lambertw

class Metric:
    def __init__(self,alpha):
        self.alpha = alpha
    
    def turtule_coord(self,x):
        return x + 2*np.ln(x-1)
    
    def inverse_turtle_coord(self, xtilde):
        return np.array(2*lambertw(np.sqrt(np.exp(xtilde-1))/2)+1, dtype=float)
    
    def ratio_fg(self,y,x):
        #correct one is ratio_fg = ((1+self.alpha**2)*(x**2-y**2))**8/ \
        #(((x**2)-(y**2) + (self.alpha**2)*(x**2-1))**2 \
        #    - 4*(self.alpha**2)*(y**2)*(x**2-1))**4
        return 1 + self.alpha**2 * y**2/(1+x**2)
    
    def g2(self,y,x):
        #correct one
        return 1 + self.alpha**2 *(1- y**2)*y**2/(1+x**2)
    
    def f(self,y,x):
        pass
    
    def b_integrand(self,y,x):
        return (self.g2(y, x) - 1)*self.ratio_fg(y, x)/(1-y**2)
    

class Solver:
    def __init__(self, metric, lmax, Npoints=1000, xmin=-30, xmax=30, m=0):
        #initialize constant atributes
        self.metric = metric
        self.lmax = lmax
        self.Npoints = Npoints
        self.xmin = xmin
        self.xmax = xmax
        self.m = m
        
        #populate integration grid
        self.Xtilde = np.linspace(self.xmin, self.xmax, self.Npoints)
        self.X = self.metric.inverse_turtle_coord(self.Xtilde)
        
        #initialize A, B and b matrices
        self.A = np.zeros((lmax,lmax,Npoints), dtype=float)
        self.b = np.zeros((lmax,lmax,Npoints), dtype=float)
        self.B = np.zeros((lmax,lmax,Npoints), dtype=float)

        #populating these matrices
        for l in range(lmax):
            for k in range(lmax):
                for i, x in enumerate(self.X):
                    self.A[l,k,i] = self.Norm(l,k)*quad(self.a_prod,-1,1,args=(x,l,k))[0]
                    self.b[l,k,i] = self.Norm(l,k)*quad(self.b_prod,-1,1,args=(x,l,k))[0]
                    self.B[l,k,i] = self.A[l,k,i]*self.Veff(l,x) + self.b[l,k,i]
                    
    def Norm(self,l,k):
        return np.sqrt(((2*l+1)/(4*np.pi))*((np.math.factorial(l-self.m))/ \
                                     (np.math.factorial(l+self.m)))) * \
            np.sqrt(((2*l+1)/(4*np.pi))*((np.math.factorial(k-self.m))/ \
                                 (np.math.factorial(k+self.m))))
    
    def a_prod(self,y,x,l,k):
        return self.metric.ratio_fg(y,x)*lpmv(self.m,l,y)*lpmv(self.m,k,y)
        
    def b_prod(self,y,x,l,k):
        return self.metric.b_integrand(y,x)*lpmv(self.m,l,y)*lpmv(self.m,k,y)
    
    def Veff(self,l,x):
        return l*(l+1) + 2/(x+1)


def test_script(alpha):
    metric = Metric(alpha)
    solver = Solver(metric, 2)
    
    plt.figure(0)
    plt.plot(solver.Xtilde, solver.A[0,0,:])
    plt.plot(solver.Xtilde, solver.A[0,1,:])
    plt.plot(solver.Xtilde, solver.A[1,0,:])
    plt.plot(solver.Xtilde, solver.A[1,1,:])
    plt.show()
    
    plt.figure(1)
    plt.plot(solver.Xtilde, solver.B[0,0,:])
    plt.plot(solver.Xtilde, solver.B[0,1,:])
    plt.plot(solver.Xtilde, solver.B[1,0,:])
    plt.plot(solver.Xtilde, solver.B[1,1,:])
    plt.show()
    
test_script(0.1)

def matrix_A_element(y, x, l, k, m, alpha):
    pass

def matrix_b_element(y, x, l, k, m, alpha):
    pass

def matrix_B_element(y, x, l, k, m, alpha):
    pass

