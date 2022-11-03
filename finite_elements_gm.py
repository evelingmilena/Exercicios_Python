import numpy as np
import matplotlib.pyplot as plt
import time #remove later, just for debugging
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
    def __init__(self, metric, lmax, Npoints_x=10000, xmin=-100, xmax=100,
                 t_step = 10/10000 , m=0, initial_value = None,
                 initial_velocity = None, initial_spread = 2, initial_distance=0):
        #initialize constant atributes
        self.metric = metric
        self.lmax = lmax
        self.Npoints_x = Npoints_x
        self.xmin = xmin
        self.xmax = xmax
        self.x_step = (xmax - xmin)/Npoints_x
        self.m = m
        if t_step >= self.x_step:
            print("WARNING: time step is greater than the spatial step. \
                  Von Neumann conditions may not be satisfied")
        self.t_step = t_step
        
        #populate integration grid
        self.Xtilde = np.linspace(self.xmin, self.xmax, self.Npoints_x)
        self.X = self.metric.inverse_turtle_coord(self.Xtilde)
        
        #initialize A, B and b matrices
        self.A = np.zeros((lmax,lmax,Npoints_x), dtype=float)
        self.b = np.zeros((lmax,lmax,Npoints_x), dtype=float)
        self.B = np.zeros((lmax,lmax,Npoints_x), dtype=float)

        #populating these matrices
        for l in range(lmax):
            for k in range(lmax):
                for i, x in enumerate(self.X):
                    self.A[l,k,i] = self.Norm(l,k)*quad(self.a_prod,-1,1,args=(x,l,k))[0]
                    self.b[l,k,i] = self.Norm(l,k)*quad(self.b_prod,-1,1,args=(x,l,k))[0]
                    self.B[l,k,i] = ((x - 1)/(x + 1)**3) \
                        *(self.A[l,k,i]*self.Veff(l,x) + (self.m**2)*self.b[l,k,i])
        
        #initial conditions:
        self.Psi = np.zeros((lmax,self.Npoints_x,self.Npoints_x//2))
            
        if initial_value:
            self.Psi[:,:,0] = np.array(initial_value, dtype=float)
        else:
            self.Psi[:,:,0] = np.zeros((self.lmax, self.Npoints_x))
            self.Psi[0,:,0] += np.ones(self.Npoints_x)*np.exp(-(self.Xtilde-initial_distance)**2/initial_spread)
            
        if initial_velocity:
            self.initial_velocity = np.array(initial_velocity, dtype=float)
        else:
            self.initial_velocity = np.zeros((self.lmax, self.Npoints_x))

        if initial_value:
            pass
        else:
            f_dobleline = np.zeros((self.lmax,self.Npoints_x))
            f_dobleline[0,:] = (2/initial_spread)*((2/initial_spread)*self.Xtilde - 1) \
                *np.exp(-self.Xtilde**2/initial_spread)
            self.Psi[:,:,1] += np.einsum('ijk,jk->ik'
                    , (np.tensordot(np.eye(self.lmax),np.ones(self.Npoints_x),0) \
                       - (self.t_step**2/2)*self.B),
                    self.Psi[:,:,0]) #contracts the matrix B with F for each value of x
            self.Psi[:,:,1] += self.t_step*self.initial_velocity
            self.Psi[:,:,1] += (self.t_step**2/2)*np.einsum('ijk,jk->ik', self.A,
                    f_dobleline)

                    
    def Norm(self,l,k):
        return 1/(np.sqrt(((2*l+1)/(4*np.pi))*((np.math.factorial(l-self.m))/ \
                                     (np.math.factorial(l+self.m)))) * \
            np.sqrt(((2*l+1)/(4*np.pi))*((np.math.factorial(k-self.m))/ \
                                 (np.math.factorial(k+self.m)))))
    
    def a_prod(self,y,x,l,k):
        return self.metric.ratio_fg(y,x)*lpmv(self.m,l,y)*lpmv(self.m,k,y)
        
    def b_prod(self,y,x,l,k):
        return self.metric.b_integrand(y,x)*lpmv(self.m,l,y)*lpmv(self.m,k,y)
    
    def Veff(self,l,x):
        return np.array(l*(l+1) + 2/(x+1))
    
    def step(self,i_t):
        self.Psi[:,:,i_t] = -self.Psi[:,:,i_t-2] + 2*self.Psi[:,:,i_t - 1]
        self.Psi[:,:,i_t] += -self.t_step**2 * np.einsum('ijk,jk->ik', \
                                            self.B, self.Psi[:,:,i_t - 1])
        D2Psi = np.zeros((self.lmax, self.Npoints_x))
        for i_x in range(i_t, self.Npoints_x - i_t - 1):
            D2Psi[:,i_x] = self.Psi[:,i_x - 1,i_t] - 2*self.Psi[:,i_x,i_t] \
                + self.Psi[:,i_x + 1,i_t]
        self.Psi[:,:,i_t] += (self.t_step**2 / self.x_step) \
            * np.einsum('ijk,jk->ik', self.A, D2Psi)
    
    def solve(self):
        for i_t in range(2,self.Npoints_x//2):
            self.step(i_t)


def test_initialization(alpha, lmax):
    metric = Metric(alpha)
    solver = Solver(metric, lmax, Npoints_x=100, t_step=1/10)
    
    plt.figure(0)
    plt.plot(solver.Xtilde, solver.A[0,0,:], 'r')
    plt.plot(solver.Xtilde, solver.A[1,1,:], 'b')
    plt.plot(solver.Xtilde, solver.A[2,2,:], 'y')
    plt.show()
    
    plt.figure(1)
    plt.plot(solver.Xtilde, solver.B[0,0,:], 'r')
    plt.plot(solver.Xtilde, solver.B[1,1,:], 'b')
    plt.plot(solver.Xtilde, solver.B[2,2,:], 'y')
    plt.show()
    
    plt.figure(2)
    plt.plot(solver.Xtilde, solver.B[1,0,:], 'r')
    plt.plot(solver.Xtilde, solver.B[2,0,:], 'b')
    plt.plot(solver.Xtilde, solver.B[3,0,:], 'y')
    plt.plot(solver.Xtilde, solver.B[4,0,:], 'g')
    
    plt.figure(3)
    plt.plot(solver.Xtilde, solver.Psi[0,:,0], 'r')
    plt.plot(solver.Xtilde, solver.Psi[1,:,0], 'b')
    plt.plot(solver.Xtilde, solver.Psi[2,:,0], 'y')
    plt.plot(solver.Xtilde, solver.Psi[3,:,0], 'g')
    plt.plot(solver.Xtilde, solver.Psi[4,:,0], 'k')
    plt.show()
    
    plt.figure(4)
    plt.plot(solver.Xtilde, solver.Psi[0,:,1], 'r')
    plt.plot(solver.Xtilde, solver.Psi[1,:,1], 'b')
    plt.plot(solver.Xtilde, solver.Psi[2,:,1], 'y')
    plt.plot(solver.Xtilde, solver.Psi[3,:,1], 'g')
    plt.plot(solver.Xtilde, solver.Psi[4,:,1], 'k')
    plt.show()
    
    return metric, solver
    
    
start = time.time()
m, s = test_initialization(0.1, 5)
stop = time.time()
print("initialization time: %s seconds" % (stop - start))

# start = time.time()
# s.step(2)
# stop = time.time()
# print("step time: %s seconds" % (stop - start))

s.solve()
plt.plot(s.Xtilde, s.Psi[0,:,-1])
