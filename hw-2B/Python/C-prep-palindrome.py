def prep_palindrome(word):

    if word == word[::-1]:  # if the word is already palindrome
        return 0

    ans = 0
    if len(word) % 2 == 0:
        r = len(word) // 2
        l = r - 1
    else:
        r = len(word) // 2 + 1
        l = r - 2
    while l >= 0:
        if word[l] != word[r]:
            ans += 1
        l -= 1
        r += 1
    return ans


if __name__ == '__main__':

    """Calculate the cost of palindrome preparing from word: 
       we can change 1 letter in the word with the cost 1"""

    word = input()
    res = prep_palindrome(word)
    print(res)
