import math
import random
import timeit
import matplotlib.pyplot as plt


def make_array(n, seed=None, low=0, high=100):
    # function makes two arrays with size n and a seed of random numbers of integers from 1-100
    random.seed(seed)
    a = [random.randint(low, high - 1) for _ in range(n)]
    b = [random.randint(low, high - 1) for _ in range(n)]
    return a, b


def main(size=1000000):
    j = 2
    a, b = make_array(size, 10) # set arrays to
    n = len(a)
    Sum = 0
    # outer loop we estimate as n /log n
    while j < n:
        k = j
        # inner loop we estimate as log log n
        while k < n:
            Sum += a[k] * b[k]
            k = k * k

        j += int(math.log(k, 2))
    return Sum


if __name__ == '__main__':
    # our experimental values of 1000, 10000, 100000, 1000000
    values_of_n = [10**3, 10**4, 10**5, 10**6]
    ex_results = []
    # our big-o estimation of n * log log n /log n
    theo_results = [v * math.log2(math.log2(v)) / math.log2(v) for v in values_of_n]
    for x in values_of_n:
        # calculating the time of the main function
        elapsed = timeit.timeit(lambda: main(x), number=1)
        ex_results.append(elapsed)

    # Normalize experimental results so they scale like the theoretical results
    scaling_factor = theo_results[0] / ex_results[0]
    ex_results_normalized = [val * scaling_factor for val in ex_results]

    print(ex_results_normalized)
    print(ex_results)
    print(theo_results)
    # Creating the plot graphs
    plt.plot(values_of_n, ex_results_normalized, label="Experimental Results Normalized", marker="o")
    plt.plot(values_of_n, theo_results, label="Theoretical Results", marker="s")
    plt.title("Time Complexity")
    plt.legend()
    plt.grid(True)
    plt.show()

