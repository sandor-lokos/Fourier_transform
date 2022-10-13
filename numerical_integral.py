import function_definitions as funcs
import numpy as np
import matplotlib.pyplot as plt


def test_func(x, par_array):
    A = par_array[0]
    B = par_array[1]
    C = par_array[2]

    return A * x + B + C


parameters = [1, 1, 0]

integral = funcs.NumInt(10000, 0, 1)
result = integral.result_function(test_func, parameters)


def Gauss(x, par_array):
    A = par_array[0]
    s = par_array[1]

    return A * np.exp(-x*x/s/s)


fourier_array = [1., 1.5]

fourier = funcs.Fourier(2000, -10, 10)

result_fourier = fourier.fourier_transform(Gauss, fourier_array)

gauss_array = []
i = -10
while i < 9.99:
    gauss_array.append(Gauss(i, fourier_array))
    i += 0.01

fig, ax = plt.subplots()
ax.plot(result_fourier[0], result_fourier[1])
ax.plot(result_fourier[0], gauss_array)

ax.set(xlabel='variable', ylabel='value',
       title='Fourier transformation - demonstration')
ax.grid()

fig.savefig("test.png")
plt.show()