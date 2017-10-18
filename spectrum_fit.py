#!/usr/bin/env python
#Script to fit spectrum with gamma function
import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np

#spectrum and energy bins in binned format
Ebins=[0,0.125,0.25,0.375,0.5,0.625,0.75,0.875,1,1.125,1.25,1.375,1.5,1.625,1.75,1.875,2,2.125,2.25,2.375,2.5,2.625,2.75,2.875,3,3.125,3.25,3.375,3.5,3.625,3.75,3.875,4,4.125,4.25,4.375,4.5,4.625,4.75,4.875,5,5.125,5.25,5.375,5.5,5.625,5.75,5.875,6,6.125,6.25,6.375,6.5,6.625,6.75,6.875,7,7.125,7.25,7.375,7.5,7.625,7.75,7.875,8]
y=[1e-9,0.0186176,0.0865335,0.735213,156.83,401.622,425.576,547.128,671.816,737.864,831.819,859.423,888.056,911.318,940.432,958.79,963.343,985.975,974.608,995.774,979.917,941.153,907.552,865.736,797.247,729.36,659.869,582.71,519.115,\
    455.485,401.686,351.107,297.258,258.408,220.897,188.965,167.309,143.047,122.778,109.995,100.715,89.8686,80.9079,71.9916,65.7639,62.5326,55.6679,52.9838,48.7261,46.6036,43.136,42.8935,41.0557,38.3422,37.0935,36.9174,36.254,35.7731,34.8589,34.7187,33.8421,34.8576,33.4684,33.24]


#convert to list form
data=[]
for i in range(len(Ebins)-1):
    e=(Ebins[i]+Ebins[i+1])/2
    n=int(round(y[i]))
    data += ([e] * n)

#print(data)

fit_alpha, fit_loc, fit_beta=stats.gamma.fit(data)
print("alpha=%f, loc=%f, beta=%f" %(fit_alpha, fit_loc, fit_beta))

fig, ax = plt.subplots(1, 1)
x = np.linspace(stats.gamma.ppf(0.01, fit_alpha),stats.gamma.ppf(0.99, fit_alpha), 100)
ax.plot(x, stats.gamma.pdf(x, fit_alpha, fit_loc, fit_beta),'r-', lw=5, alpha=0.6, label='gamma pdf')
ax.plot(x, stats.gamma.pdf(x, fit_alpha, 0, fit_beta),'r-', lw=5, alpha=0.6, label='gamma pdf, loc=0')
ax.hist(data, normed=True, alpha=0.2, label='DUNE $\\nu_\\mu$ Spectrum')
ax.legend(loc='best', frameon=False)
plt.show()
