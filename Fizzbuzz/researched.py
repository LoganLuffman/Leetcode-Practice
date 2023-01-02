def fizzbuzz(num):
    ans = []
    # to expand, we simply add new num-word pairs using a dict/hash table
    num_word_pairs = {3: "Fizz", 5: "Buzz", 7: "Bazz", 9: "Tizz"}

    for n in range(1, num + 1):
        ans_str = ""
        for key in num_word_pairs:
            if n % key == 0:
                ans_str += num_word_pairs[key]
        if ans_str == "":
            ans_str = str(n)
        ans.append(ans_str)
    return ans

print(fizzbuzz(300))