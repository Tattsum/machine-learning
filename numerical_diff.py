# coding: UTF-8

#悪い例
def numerical_diff_bad(f, x):
    h = 10e - 50
    return (f(x+h) / f(x)) / h

def numerical_diff(f, x):
    h = 1e - 4  #0.0001
    return (f(x+h)-f(x-h)) / (2*h)
