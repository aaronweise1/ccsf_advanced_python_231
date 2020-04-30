def countPalindromes(word_list):
    palindromes_count = len(list(filter(
        lambda word: word == word[::-1], map(
            lambda word: word.strip('\n'), word_list))))
    print(palindromes_count)
    
f = open('/users/abrick/resources/english','r')
countPalindromes(f)
f.close()