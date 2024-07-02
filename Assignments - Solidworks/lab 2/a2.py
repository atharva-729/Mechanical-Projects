import numpy as np
import matplotlib.pyplot as plt


# defining cy+ky'+my"=0
def g(y, z, t, m, k, c):
    return   -(k/m)*z-y*c/m


def euler_method(y0, z0, num_steps, tf, m , k , c ,alpha):
    t_values = np.linspace(0, tf, num=num_steps+1)
    delta_t = tf/num_steps


    y_values = np.zeros(num_steps+1)
    z_values = np.zeros(num_steps+1)


    z_prime_values = np.zeros(num_steps+1)
    y_values[0] = y0
    z_values[0] = z0

    z_prime_values[0]=g(y_values[0], z_values[0],t_values[0], m, k,c)

    for i in range(1, num_steps+1):
        y_values[i] = y_values[i-1]+delta_t*z_values[i-1]+(1 - alpha) * delta_t**2 / 2 * z_values[i-1]
        z_values[i] = z_values[i-1]+delta_t* delta_t * (1 - alpha) * z_prime_values[i-1]
        z_prime_values[i] =  g(y_values[i-1], z_values[i-1],t_values[i-1], m, k,c)
    
    return t_values , y_values
m=int(input("Enter m :"))
k=int(input("Enter k :"))
c=int(input("Enter c :"))
y0=int(input("Enter y0 :"))
z0=int(input("Enter z0 :"))
alpha=float(input("Enter the value of alpha :"))

num_steps=int(input("Enter the number of steps : "))

tf=int(input("Enter stopping time : "))

t , y = euler_method(y0,z0,num_steps,tf, m , k ,c, alpha)


plt.plot(t,y)

#1plt.plot(t,np.exp(t))
plt.show()