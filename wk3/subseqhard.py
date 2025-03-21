

def subseqhard(arr, n):
    prefix_sum_count = {0: 1}
    current_sum = 0
    count = 0

    for num in arr:
        current_sum += num
        if (current_sum - 47) in prefix_sum_count:
            count += prefix_sum_count[current_sum - 47]

        prefix_sum_count[current_sum] = prefix_sum_count.get(current_sum, 0) + 1

    return count

n = int(input())

for i in range(0, n):
    _input = input()
    if _input == '\n':
        continue
    len = int(_input)
    arr = input().split(' ')
    arr = list(map(int, arr))

    print(subseqhard(arr, len))