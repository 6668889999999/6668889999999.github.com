### 这个程序用来生成正弦信号
import numpy as np
import matplotlib.pyplot as plt


def generate_sinusoid(N,A,f0,fs,phi):
    '''
    :param N(int): number of samples
    :param A(float): amplitude
    :param f0(float): frequency
    :param fs(float): sample rate
    :param phi(float): initial phase
    :return: x(numpy array): sinusoid signal which length is M
    '''
    T = 1/fs
    n = np.arange(N)
    x = A * np.cos(2*f0*np.pi*n*T+phi)

    return x

def generate_sinusoid_2(t,A,f0,fs,phi):
    '''
    :param t(float): the time of generated signal
    :param A(float): amplitude
    :param f0(float): frequency
    :param fs(float): sample rate
    :param phi(float): initial phase
    :return: x(numpy array): sinusoid signal which length is M
    '''
    T = 1.0/fs
    N = t/T

    return generate_sinusoid(N,A,f0,fs,phi)

if __name__ == "__main__":
    N = 511
    A = 1
    f0 = 440
    fs = 44100
    t = 0.02

    n = np.arange(0,0.02,1/fs)

    phi = 0
    x = generate_sinusoid(N,A,f0,fs,phi)
    x2 = generate_sinusoid_2(t,A,f0,fs,phi)
   # plt.figure()
    #plt.plot(x)
    #plt.xlabel('Number')
    #plt.ylabel('amplitude')
    #plt.title('sin wave')
    plt.figure()
    plt.plot(n,x2)
    plt.xlabel('time/s')
    plt.ylabel('amplitude')
    plt.title('sin wave')
    plt.show()

    t=np.linspace(0,2*np.pi,100)
    x=np.sin(t)
    plt.figure()
    plt.plot(t,x)
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title('Discreat Signal')
    plt.show()

























