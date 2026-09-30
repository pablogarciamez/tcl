import random
from math import sqrt

random.seed(42)

faces = [1, 1, 1, 1, 1, 6]
n = 30
m = 6000
trials = 10

true_mean = sum(faces) / len(faces)
true_sd = sqrt(sum((f - true_mean) ** 2 for f in faces) / len(faces))
true_sd_of_mean = true_sd / sqrt(n)
print(f"true_sd_of_mean: {true_sd_of_mean}")

for t in range(trials):
    sample = [random.choice(faces) for _ in range(n)]

    means = []
    for _ in range(m):
        resample = [random.choice(sample) for _ in range(n)]
        means.append(sum(resample) / n)

    mean_of_means = sum(means) / m
    bootstrap_sd = sqrt(sum((x - mean_of_means) ** 2 for x in means) / m)
    print(f"trial {t + 1}, bootstrap_sd: {bootstrap_sd}")