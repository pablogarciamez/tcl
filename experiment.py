import random
from math import sqrt, exp, pi
import matplotlib.pyplot as plt

random.seed(42)

cases = [1, 2, 5, 10, 30, 100]
faces = [1, 1, 1, 1, 1, 6]
true_mean = sum(faces) / len(faces)
standard_deviation_n_equals_1 = sqrt(sum((face - true_mean) ** 2 for face in faces) / len(faces))


for n in cases:
    means = []
    m = 50000

    for _ in range(m):
        cur_mean = sum(random.choice(faces) for _ in range(n)) / n
        means.append(cur_mean)

    expected_standard_deviation = standard_deviation_n_equals_1 / sqrt(n)
    mean_of_means = sum(means) / m
    standard_deviation = sqrt(sum((mean - mean_of_means) ** 2 for mean in means) / m)
    pct_less_than_1_standard_deviation = 100 * sum(1 if abs(true_mean - mean) < expected_standard_deviation else 0 for mean in means) / m
    pct_less_than_2_standard_deviation = 100 * sum(1 if abs(true_mean - mean) < 2 * expected_standard_deviation else 0 for mean in means) / m

    print(f"n: {n}")
    print(f"mean_of_means: {mean_of_means}")
    print(f"standard_deviation: {standard_deviation}")
    print(f"expected_standard_deviation: {expected_standard_deviation}")
    print(f"pct_less_than_1_standard_deviation: {pct_less_than_1_standard_deviation}%")
    print(f"pct_less_than_2_standard_deviation: {pct_less_than_2_standard_deviation}%")

    borders = [1 + (5 * i - 2.5) / n for i in range(n + 2)]
    l = 200
    s = expected_standard_deviation
    xs = [1 + i * (max(faces) - min(faces)) / (l - 1) for i in range(l)]
    ys = [exp(-(x - true_mean) ** 2 / (2 * s ** 2)) / (s * sqrt(2 * pi)) for x in xs]

    plt.title(f"Means, n: {n}")
    plt.hist(means, bins=borders, density=True)
    plt.plot(xs, ys)
    plt.show()