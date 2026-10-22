def large_ele(arr, n):
    # Step 1: Find Largest
    largest = arr[0]
    for i in range(1, n):
        if arr[i] > largest:
            largest = arr[i]
    print("Largest:", largest)

    # Step 2: Find Second Largest
    slargest = float('-inf')
    for j in range(0, n):
        if arr[j] > slargest and arr[j] != largest:
            slargest = arr[j]
    print("Second Largest:", slargest if slargest != float('-inf') else "Not Found")

    # Step 3: Find Smallest
    smallest = arr[0]
    for i in range(1, n):
        if arr[i] < smallest:
            smallest = arr[i]
    print("Smallest:", smallest)

    # Step 4: Find Second Smallest
    ssmallest = float('inf')
    for j in range(0, n):
        if arr[j] < ssmallest and arr[j] != smallest:
            ssmallest = arr[j]
    print("Second Smallest:", ssmallest if ssmallest != float('inf') else "Not Found")

    return arr

# Test
arr = [3, 2, 1, 5, 4]
n = len(arr)
res = large_ele(arr, n)
