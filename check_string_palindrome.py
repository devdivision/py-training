# Check if a string is a palindrome

my_word = 'prorp'


# reversing approach
def opt1(word):
    reversed = word[::-1]
    if word == reversed:
        return True
    else:
        return False


print(opt1(my_word))


# two-pointer approach
def opt2(word):
    lp = 0
    rp = len(word)-1

    while lp < rp:
        if word[lp] != word[rp]:
            return False
        lp += 1
        rp -= 1

    return True


print(opt2(my_word))
