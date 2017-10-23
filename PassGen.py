from time import time, sleep
import random
import matplotlib.pyplot as plt
import numpy as np
import string

lst = string.ascii_letters + '0123456789?%'

def get_bit():
    sleep(0.001)
    a = '{0:.9f}'.format(time())
    return int(a[-1]) % 2

def get_psd(length):
    psd = ''
    for i in range(length):
        index = 0
        for i in range(6):
            index = index * 2 + get_bit()
        psd += lst[index]
    return psd

if __name__ == "__main__":
    '''y = np.random.randn(1000)
    print(lst)
    plt.hist(lst)
    plt.show()'''
    print(get_psd(15))

