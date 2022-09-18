import numpy as np

class NumInt:
    def __init__(self, Nstep, lower_bound, upper_bound):
        self.Nstep = Nstep
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

    def printNstep(self):
        print(self.Nstep)

    def printLowerBound(self):
        print(self.lower_bound)

    def printUpperBound(self):
        print(self.upper_bound)

    def integral(self, array):
        Is38 = 0.
        for i in range(0, len(array)-1, 1):
            if i % 3 == 0 and i < len(array)-3:
                Is38 += (array[i] + 3. * array[i+1] + 3. * array[i+2] + array[i+3]) / 8.
        return 3. * Is38

    def result_function(self, func_in, par_array):
        dx = (self.upper_bound - self.lower_bound) / self.Nstep
        func = []
        for i in range(0, self.Nstep, 1):
            x = self.lower_bound + i * dx
            func.append(func_in(x, par_array))
        return self.integral(func) * dx


class Fourier(NumInt):
    def fourier_integral(self, func_in, t, par_array):
        t1 = self.upper_bound
        t0 = self.lower_bound
        nstep = self.Nstep
        dx = (t1 - t0) / nstep
        func_real = []
        func_imag = []

        for i in range(0, nstep, 1):
            x = t0 + i * dx
            func_real.append(func_in(x, par_array) * np.cos(2. * np.pi * t * x))
            func_imag.append(func_in(x, par_array) * np.sin(2. * np.pi * t * x))

            #print(func_in(x, par_array) * np.cos(2. * np.pi * t * x))
        return self.integral(func_real) * dx, self.integral(func_imag) * dx

    def fourier_transform(self, func_in, par_array):
        t1 = self.upper_bound
        t0 = self.lower_bound
        nstep = self.Nstep
        dt = (t1 - t0) / nstep
        variable = []
        result_real = []
        result_imag = []

        for i in range(0, nstep, 1):
            t = t0 + i * dt
            real_part, imag_part = self.fourier_integral(func_in, t, par_array);
            variable.append(t)
            result_real.append(real_part)
            result_imag.append(imag_part)

        return variable, result_real, result_imag
