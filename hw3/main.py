import matplotlib.pyplot as plt
import numpy as np

# The code for part 1 was modified from Dr. Mario's code

class European_Call_Payoff:

    def __init__(self, strike):
        self.strike = strike

    def get_payoff(self, stock_price):
        if stock_price > self.strike:
            return stock_price - self.strike
        else:
            return 0


class BetaMotion:

    def simulate_paths(self):
        while(self.T - self.dt > 0):
            dWt = np.random.beta(14, 6) - .65  # Beta motion with shift to left of .65
            dYt = self.drift*self.dt + self.volatility*dWt  # Change in price
            # print("Change in price: {0}", dYt)
            self.current_price += dYt  # Add the change to the current price
            self.prices.append(self.current_price)  # Append new price to series
            self.T -= self.dt  # Accound for the step in time

    def __init__(self, initial_price, drift, volatility, dt, T):
        self.current_price = initial_price
        self.initial_price = initial_price
        self.drift = drift
        self.volatility = volatility
        self.dt = dt
        self.T = T
        self.prices = []
        self.simulate_paths()


if __name__ == "__main__":
    print("Executing part 1...")

    # Model Parameters
    paths = 5000
    initial_price = 100
    drift = .01
    volatility = 0.7
    dt = 1/365
    T = 1
    price_paths = []

    # Generate a set of sample paths
    for i in range(0, paths):
        price_paths.append(BetaMotion(initial_price, drift, volatility, dt, T).prices)

    call_payoffs = []
    final_prices = []
    ec = European_Call_Payoff(100)
    risk_free_rate = .01
    for price_path in price_paths:
        call_payoffs.append(ec.get_payoff(price_path[-1])/(1 + risk_free_rate))  # We get the last stock price in the series generated to determine the payoff and discount it by one year
        final_prices.append(price_path[-1])

    # Plot the set of generated sample paths
    for price_path in price_paths:
        plt.plot(price_path)
    plt.xlabel('Days')
    plt.ylabel('Price')
    plt.title("Simulations of Stock Price Based on Normal Distribution")
    plt.show()

    print(f"Average stock price after {int(1 / dt) * T} days: $", np.average(final_prices))
    print("\nAverage payoff(option block of 100): $", np.average(call_payoffs)*100)  # Options are in blocks of 100
    print("Cost of option: $", np.average(call_payoffs))

    print("Part 1 finished")

    print("Executing part 2")
