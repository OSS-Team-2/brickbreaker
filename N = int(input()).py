n = int(input())

ans, current_sum, top_pointer, bot_pointer = 1, 1, 1, 1

while top_pointer != n:
    if current_sum == n:
        ans = 1
        current_sum = bot_pointer
        bot_pointer = 1

    elif current_sum > n:
        current_sum = bot_pointer
        bot_pointer = 1

    elif current_sum < n:
        current_sum = top_pointer
        top_pointer = 1

print(ans)
