import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

N = 100
data = np.random.randn(N)

# We got to arrange the data and get its percentiles to plot cdf
X = np.sort(data)
print("Sorted Data:", X)
Y = np.arange(N) / float(N)
print("Cumulative Probability:", Y)

#pdf for the above data
pdf = norm.pdf(X,X.mean(),X.std())
logpdf = norm.logpdf(X,X.mean(),X.std())
sf = norm.sf(X,X.mean(),X.std())
print("Probablity density function:",pdf)

# Create the plots

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.hist(X, bins=20, density=True, alpha=0.6, color='g', label="Histogram (PDF Approx.)")
plt.plot(X, pdf, 'r', label="Theoretical PDF")
plt.plot(X, Y, label="Empirical CDF")
plt.plot(X, sf, 'b', label="Theoretical PDF")
plt.grid(True)

plt.tight_layout()
plt.show()