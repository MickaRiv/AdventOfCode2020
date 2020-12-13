import numpy as np
import sys

data = np.loadtxt("input",dtype=str)
timestamp = int(data[0])
ids = np.array([int(num) for num in data[1].split(",") if num != "x"])
waitingTimes = ids-np.mod(timestamp,ids)
bestInd = np.argmin(waitingTimes)
print(waitingTimes[bestInd]*ids[bestInd])

nums = np.array([[i,int(val)] for i,val in enumerate(data[1].split(",")) if val != "x"], dtype=np.int64)
cumProd = 1
c = 0
for k in range(1,nums.shape[0]):
    a = 0
    cumProd *= nums[k-1,1]
    reste = np.mod(c, nums[k,1])
    while reste != np.mod(nums[k,1]-nums[k,0],nums[k,1]):
        a += 1
        reste = np.mod(reste + cumProd, nums[k,1])
    c += a*cumProd
print(c)