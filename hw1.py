# Hocam çalışması için numpy ve scipy kütüphanelerini indirmeyi unutmayınız.

import numpy as np
import scipy.stats as stats

def test_distributions(data):

    distributions = ['norm', 'uniform', 'expon', 'gamma', 'lognorm', 'beta', 't']

    results = {}

    for distribution in distributions:
        dist = getattr(stats, distribution)
        params = dist.fit(data)
        D, p_value = stats.kstest(data, distribution, args=params)
        percentage_fit = (1 - D) * 100
        results[distribution] = percentage_fit
    return results


# Example usage:
data = np.random.normal(0, 1, 1000)

fit_results = test_distributions(data)

print("Fitness of data to various distributions:")
for dist, fit in fit_results.items():
    print(f"{dist}: {fit:.2f}%")