import numpy as np
from numpy import mean, median
from numpy.fft import irfft, rfft

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
res1 = np.correlate(x, y, mode=1)
res0 = np.correlate(x, y, mode=0)
print(res0)
print(res1)

xcorr = lambda x,y : irfft(rfft(x)*rfft(y[::-1]))
z = xcorr(x,y)
print(z)
maxz  = max(z)
print(maxz)
#728

#meanz = mean(z)
#medianz = median(z)
#print(medianz)
#print(meanz)

A = [1, 2, 3, 4, 5, 6]
r0 = np.fft.ifft(np.abs(np.fft.fft(A)) ** 2).real
length = len(A)
len1 = length//2
r1 = r0[:len(A) // 2]
r2 = r0[:len(A) // len1]
#print(length)
#print(r0)


#[55. 45. 40. 40. 45.]
#40