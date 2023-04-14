n = int(input())
num = list(map(int, input().split()))
num.sort()

left, right = 0, n - 1
min_abs_sum = abs(num[left] + num[right])
result = (num[left], num[right])

while left < right:
    curr_sum = num[left] + num[right]
    curr_abs_sum = abs(curr_sum)
    if curr_abs_sum < min_abs_sum:
        min_abs_sum = curr_abs_sum
        result = (num[left], num[right])
    if curr_sum > 0:
        right -= 1
    elif curr_sum < 0:
        left += 1
    else:
        break

print(result[0], result[1])
