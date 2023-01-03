def deleteColumns(strs):
    str_len = len(strs[0])

    answer = 0

    for col in range(0, str_len):
        for row in range(1, len(strs)):
            if (strs[row][col] < strs[row - 1][col]):
                answer += 1
                break
    return answer

