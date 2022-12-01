import numpy as np
import matplotlib.pyplot as plt
import time #remove later, just for debugging
from scipy.integrate import quad
from scipy.special import lpmv, lambertw
from scipy.optimize import curve_fit

class Metric:
    def __init__(self,alpha):
        self.alpha = alpha
    
    def turtule_coord(self,x):
        return x + 2*np.ln(x-1)
    
    def inverse_turtle_coord(self, xtilde):
        return np.array(2*lambertw(np.exp((xtilde-1)/2)/2)+1, dtype=np.double)
    
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
    def __init__(self, metric, lmax, Npoints_x=10000, Npoints_t=20000, xmin=-100, xmax=100,
                 t_step = 10/10000 , m=0, initial_value = None, li=0,
                 initial_velocity = None, initial_spread = 2, initial_distance=0):
        #initialize constant atributes
        self.metric = metric
        self.lmax = lmax
        self.Npoints_x = Npoints_x
        self.Npoints_t = Npoints_t
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
        self.A = np.zeros((self.lmax,self.lmax,self.Npoints_x), dtype=float)
        self.b = np.zeros((self.lmax,self.lmax,self.Npoints_x), dtype=float)
        self.B = np.zeros((self.lmax,self.lmax,self.Npoints_x), dtype=float)

        #populating these matrices
        for l in range(lmax):
            for k in range(lmax):
                for i, x in enumerate(self.X):
                    self.A[l,k,i] = self.Norm(l,k)*quad(self.a_prod,-1,1,args=(x,l,k))[0]
                    self.b[l,k,i] = self.Norm(l,k)*quad(self.b_prod,-1,1,args=(x,l,k))[0]
                    self.B[l,k,i] = ((x - 1)/(x + 1)**3) \
                        *(self.A[l,k,i]*self.Veff(l,x) + (self.m**2)*self.b[l,k,i])
        
        #initial conditions:
        self.Psi = np.zeros((lmax,self.Npoints_x,self.Npoints_t))
            
        if initial_value:
            self.Psi[:,:,0] = np.array(initial_value, dtype=float)
        else:
            self.Psi[:,:,0] = np.zeros((self.lmax, self.Npoints_x))
            self.Psi[li,:,0] += np.ones(self.Npoints_x)*np.exp(-(self.Xtilde-initial_distance)**2/initial_spread)
            
        if initial_velocity:
            self.initial_velocity = np.array(initial_velocity, dtype=float)
        else:
            self.initial_velocity = np.zeros((self.lmax, self.Npoints_x))

        if initial_value:
            pass
        else:
            f_dobleline = np.zeros((self.lmax,self.Npoints_x))
            f_dobleline[li,:] = (2/initial_spread)*((2/initial_spread)*self.Xtilde - 1) \
                *np.exp(-self.Xtilde**2/initial_spread)
            self.Psi[:,:,1] += np.einsum('ijk,jk->ik'
                    , (np.tensordot(np.eye(self.lmax),np.ones(self.Npoints_x),0) \
                       - (self.t_step**2/2)*self.B),
                    self.Psi[:,:,0]) #contracts the matrix B with F for each value of x
            self.Psi[:,:,1] += self.t_step*self.initial_velocity
            self.Psi[:,:,1] += (self.t_step**2/2)*np.einsum('ijk,jk->ik', self.A,
                    f_dobleline)
            
    def times(self,x_point):
        tmax = (self.Npoints_x - x_point) if x_point >= self.Npoints_x//2 else x_point
        return np.linspace(0, tmax*self.t_step,tmax)

                    
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
        #implement 4th order, implement borders
        self.Psi[:,:,i_t] = -self.Psi[:,:,i_t-2] + 2*self.Psi[:,:,i_t - 1]
        self.Psi[:,:,i_t] += -self.t_step**2 * np.einsum('ijk,jk->ik', \
                                            self.B, self.Psi[:,:,i_t - 1])
            
        D2Psi = np.zeros((self.lmax, self.Npoints_x))
        D2Psi[:,0] = (35*self.Psi[:,0,i_t-1] - 104*self.Psi[:,1,i_t-1]
        + 114*self.Psi[:,2,i_t-1] - 56*self.Psi[:,3,i_t-1] + 11*self.Psi[:,4,i_t-1])/12
        D2Psi[:,1] = (11*self.Psi[:,0,i_t-1] - 20*self.Psi[:,1,i_t-1]
        + 6*self.Psi[:,2,i_t-1] + 4*self.Psi[:,3,i_t-1] - 1*self.Psi[:,4,i_t-1])/12
        D2Psi[:,-1] = (35*self.Psi[:,-1,i_t-1] - 104*self.Psi[:,-2,i_t-1]
        +114*self.Psi[:,-3,i_t-1] - 56*self.Psi[:,-4,i_t-1] + 11*self.Psi[:,-5,i_t-1])
        D2Psi[:,-2] = (11*self.Psi[:,-1,i_t-1] - 20*self.Psi[:,-2,i_t-1]
        + 6*self.Psi[:,-3,i_t-1] + 4*self.Psi[:,-4,i_t-1] - 1*self.Psi[:,-5,i_t-1])/12
        
        for i_x in range(3, self.Npoints_x-2):
            D2Psi[:,i_x] = -self.Psi[:,i_x - 2,i_t] +  16*self.Psi[:,i_x - 1,i_t] \
                - 30*self.Psi[:,i_x,i_t] \
                + 16*self.Psi[:,i_x + 1,i_t] - self.Psi[:,i_x + 2,i_t]
        self.Psi[:,:,i_t] += (self.t_step**2 / self.x_step**2) \
            * np.einsum('ijk,jk->ik', self.A, D2Psi)/12
    
    def solve(self):
        #implement 4th order, increase the initial time
        for i_t in range(2,self.Npoints_t):
            self.step(i_t)
            
    def energy(self,i_t):
        pass


def test_initialization(alpha, lmax, linit):
    metric = Metric(alpha)
    solver = Solver(metric, lmax=5, xmin=-50, xmax=550, Npoints_x=10000,
                    t_step=1/200, li=linit, initial_distance=100)
    
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
    plt.show()
    
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
    
    

class Tester():
    def __init__(self, **init_params):
        #arrumar
        self.metric_params = init_params['metric'] if 'metric' in init_params else {'alpha':0.1}
        self.solver_params = init_params['solver'] if 'solver' in init_params else {'lmax':5,
                'xmin':-50, 'xmax':550, 'Npoints_x':10000, 't_step':1/200, 'li':0,
                'initial_distance':100}
        self.noplots = init_params['No_plots'] if 'No_plots' in init_params else False
        self.test_point = init_params['test_point'] if 'test_point' in init_params else 100
        self.test_point_index = ipoint = np.where(self.solver.Xtilde >= self.test_point)[0][0]
        self.test_point_tmax = ( self.solver_params['Npoints_x'] - self.test_point_index-1) \
            if self.test_point_index>= self.solver_params['Npoints_x']//2 else self.test_point_index
    
    def _initialize(self):
        self.metric = Metric(self.metric_params['alpha'])
        self.solver = Solver(self.metric, **self.solver_params)
     
        
    def _fit(self, ipoint, tmax):
        params, params_cov = curve_fit(self.expsin, self.sover.times(ipoint),
                            self.sover.Psi[self.solver_params['li'],ipoint,:tmax], p0=[-0.5,0.5,0])
        self.fitted_params = params

    
    def timed_tests(self):
        start = time.time()
        self.metric = Metric(self.metric_params['alpha'])
        self.solver = Solver(self.metric, **self.solver_params)
        stop = time.time()
        initialization_time = stop - start
        print('initialization time: %f' % initialization_time)
        
        start = time.time()
        self.solver.solve()
        stop = time.time()
        solving_time = stop - start
        print('Solving time: %f' % solving_time)
        
        start = time.time()
        self._fit(self.test_point_index, self.test_point_tmax)
        stop = time.time()
        fitting_time = stop - start
        print('Fitting time: %f' % fitting_time)
    
        return initialization_time, solving_time, fitting_time
    
    def test_initialization(self):
        if not self.noplots:
            plt.figure(0)
            plt.plot(self.solver.Xtilde, self.solver.A[0,0,:], 'r')
            plt.plot(self.solver.Xtilde, self.solver.A[1,1,:], 'b')
            plt.plot(self.solver.Xtilde, self.solver.A[2,2,:], 'y')
            plt.show()
            
            plt.figure(1)
            plt.plot(self.solver.Xtilde, self.solver.B[0,0,:], 'r')
            plt.plot(self.solver.Xtilde, self.solver.B[1,1,:], 'b')
            plt.plot(self.solver.Xtilde, self.solver.B[2,2,:], 'y')
            plt.show()
            
            plt.figure(2)
            plt.plot(self.solver.Xtilde, self.solver.B[1,0,:], 'r')
            plt.plot(self.solver.Xtilde, self.solver.B[2,0,:], 'b')
            plt.plot(self.solver.Xtilde, self.solver.B[3,0,:], 'y')
            plt.plot(self.solver.Xtilde, self.solver.B[4,0,:], 'g')
            plt.show()
            
            plt.figure(3)
            plt.plot(self.solver.Xtilde, self.solver.Psi[0,:,0], 'r')
            plt.plot(self.solver.Xtilde, self.solver.Psi[1,:,0], 'b')
            plt.plot(self.solver.Xtilde, self.solver.Psi[2,:,0], 'y')
            plt.plot(self.solver.Xtilde, self.solver.Psi[3,:,0], 'g')
            plt.plot(self.solver.Xtilde, self.solver.Psi[4,:,0], 'k')
            plt.show()
            
            plt.figure(4)
            plt.plot(self.solver.Xtilde, self.solver.Psi[0,:,1], 'r')
            plt.plot(self.solver.Xtilde, self.solver.Psi[1,:,1], 'b')
            plt.plot(self.solver.Xtilde, self.solver.Psi[2,:,1], 'y')
            plt.plot(self.solver.Xtilde, self.solver.Psi[3,:,1], 'g')
            plt.plot(self.solver.Xtilde, self.solver.Psi[4,:,1], 'k')
            plt.show()
    
    
    def test_solving(self, ipoint, tmax):
        plt.figure()
        for l in range(self.solver.lmax):
            plt.plot(self.solver.times(ipoint), self.solver.Psi[l,ipoint,:tmax])
        plt.plot(self.solver.times(ipoint), np.exp(self.fitted_params[0]*self.solver.times(ipoint)), '--')
        plt.plot(self.solver.times(ipoint), -np.exp(self.fitted_params[0]*self.solver.times(ipoint)), '--')
        plt.plot(self.solver.times(ipoint), -np.zeros(ipoint), '--')
        plt.plot(self.solver.times(ipoint), self.expsin(self.solver.times(ipoint)
        ,self.fitted_params[0],self.fitted_params[1],self.fitted_params[2]), '--')
        plt.title('alpha = %f; Exitation Mode: %d; Time evolution at x = %02f' % (self.metric.alpha, self.solver_params['li'], self.solver.X[ipoint]))
        plt.xlabel('t [s]')  
        plt.ylabel('phi')
        plt.legend(range(self.solver.lmax))
        plt.show()
    
    
    def _expsin(x,lamb,w,phi):
        return np.exp(x*lamb)*np.cos(w*x+phi)
    
    
met = Metric(0.5)
s = Solver(met, 5, m=0, Npoints_x = 5000, t_step=1/100, xmin = -1400,
           xmax = 1400, initial_distance=-300, Npoints_t=20000, li=0)
s.solve()

fig, ax = plt.subplots(1,1)
img = ax.imshow(np.log(np.square(s.Psi[0,:,:])+1e-19), extent=[0,200,1400,-1400],aspect=0.02)
fig.colorbar(img)
plt.xlabel('time');
plt.ylabel(r'$\tilde{x}$ position');
plt.title('wave propagation')
plt.show()

plt.figure()
plt.plot(np.log(np.abs(s.Psi[0,3000,:])+1e-19))
plt.title(r'Field Intensity at $\tilde{x} = %f$' % s.X[3000])
plt.xlabel('Time')
plt.ylabel('Field Intensity')

# fig, ax = plt.subplots(1,1)
# img = ax.imshow(np.log(np.square(s.Psi[1,:,:])+1e-19))
# ax.set_yticklabels(s.X)
# fig.colorbar(img)
# plt.show()

# fig, ax = plt.subplots(1,1)
# img = ax.imshow(np.log(np.square(s.Psi[2,:,:])+1e-19))
# ax.set_yticklabels(s.X)
# fig.colorbar(img)
# plt.show()

# fig, ax = plt.subplots(1,1)
# img = ax.imshow(np.log(np.square(s.Psi[3,:,:])+1e-19))
# ax.set_yticklabels(s.X)
# fig.colorbar(img)
# plt.show()

# fig, ax = plt.subplots(1,1)
# img = ax.imshow(np.log(np.square(s.Psi[4,:,:])+1e-19))
# ax.set_yticklabels(s.X)
# fig.colorbar(img)
# plt.show()
