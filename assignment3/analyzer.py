import os
import numpy as np
import pandas as pd
from scipy.fftpack import fft
import matplotlib.pyplot as plt
import sys

plt.rcParams['figure.dpi'] = 120
plt.rcParams['font.size'] = 15
# Import data using Pandas. Using report I XY data, this line should work
print(os.path.dirname(os.path.abspath(__file__)) + '\\' + sys.argv[1])
data = pd.read_csv(os.path.dirname(os.path.abspath(__file__)) + '\\' + sys.argv[1],
                   skiprows=5, header=None, delim_whitespace=True)
data = data.values
# Fast Fourier Transform
y = fft(data[:, int(sys.argv[2])])

# Absolute value
m = np.abs(y)
# Frequency
freq = np.linspace(0, 50, y.shape[0], endpoint=True)
# Plot
plt.grid()
plt.plot(freq[:25], m[:25], linewidth=2, color='firebrick')
plt.xlabel('Frequency (Hz)')
plt.ylabel('|FFT(y)|')
plt.show()
