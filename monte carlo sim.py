import random
import math
import matplotlib.pyplot as plt

days_per_year = 365

def gbm_sim(initial, mu, sigma, T_days):
    prices = [initial]
    dt = 1  
    for _ in range(T_days):
        S_t = prices[-1]
        z = random.gauss(0, 1)
        dS = S_t * (mu * dt + sigma * math.sqrt(dt) * z)
        prices.append(S_t + dS)
    return prices

initial = int(input("initial value ($): "))
volatility = float(input("volatility (% per year): ")) / 100
d_return = float(input("expected return (% per year): ")) / 100
years = int(input("Time (Years): "))
sims = int(input("Number of simulations: "))
total_days = years * days_per_year

# Simulations
for _ in range(sims):
    result = gbm_sim(initial, d_return / days_per_year, volatility /
                      math.sqrt(days_per_year), total_days)
    plt.plot(result)

plt.xlabel("Days")
plt.ylabel("Stock Price")
plt.grid(True)
plt.show()
