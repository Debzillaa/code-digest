# Find the first circular tour that visits all petrol pump
def printTour(arr, n):
    # Consider first petrol pump as starting point
    start = 0
    s = 0 # Petrol available in the truck till now
    d = 0 # Deficit of petrol till visiting this petrol pump

    for i in range(n):
        s += arr[i][0] - arr[i][1]
        if s < 0:
            start = i + 1
            d += s
            s = 0
    return start if (s + d) >= 0 else -1

# Driver program to test above function
arr = [[6, 4], [3, 6], [7, 3]]
start = printTour(arr, 3)
if start == -1:
    print("No Solution Possible !!!")
else:
    print("Start = {}".format(start))
