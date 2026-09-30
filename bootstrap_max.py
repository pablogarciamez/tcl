import random
import matplotlib.pyplot as plt

random.seed(42)

m = 6000
n = 30

realMaxNums = []

for _ in range(m):
    nums = [random.random() for _ in range(n)]
    maxNum = max(nums)
    realMaxNums.append(maxNum)

sample = [random.random() for _ in range(n)]
bootstrapMaxNums = []

for _ in range(m):
    nums = [random.choice(sample) for _ in range(n)]
    maxNum = max(nums)
    bootstrapMaxNums.append(maxNum)

meanRealMaxNums = sum(realMaxNums) / m
meanBootstrapMaxNums = sum(bootstrapMaxNums) / m
maxOfSample = max(sample)
distinctBootstrapMaxNums = len(set(bootstrapMaxNums))
numMaxOfSample = bootstrapMaxNums.count(maxOfSample)

print(f"meanRealMaxNums: {meanRealMaxNums}")
print(f"meanBootstrapMaxNums: {meanBootstrapMaxNums}")
print(f"maxOfSample: {maxOfSample}")
print(f"distinctBootstrapMaxNums: {distinctBootstrapMaxNums}")
print(f"numMaxOfSample: {numMaxOfSample}")

numBins = 200
borders = [(i - 0.5) / numBins for i in range(numBins + 2)]

plt.title("Comparison Real Max vs Bootstrap Max")
plt.xlabel("Max of 30 numbers between 0 and 1")
plt.ylabel("Number of maxes within bin")
plt.hist(realMaxNums, bins=borders, alpha=0.6, label="real")
plt.hist(bootstrapMaxNums, bins=borders, alpha=0.6, label="bootstrap")
plt.legend()

plt.savefig("max_real_vs_bootstrap.png")
plt.show()