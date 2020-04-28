

# Task #1: Write code to determine if passed in string
#          argument is a palindrome
def is_palindrome(word):
    # todo: Put your code here for task #1
    left_postition = 0
    right_pos = len(word) - 1
    while right_pos >= left_postition:
        if not word[left_postition] == word[right_pos]:
            return False
        left_postition += 1
        right_pos -= 1
    return True


# Task #2: Write code to find all palindromes in the
#          given file, and add them to palindromes list
def find_palindromes(filename):
    palindromes = []
    with open('EX06-Palindromes-eliasdandouch\words.txt') as text:
        for line in text:
            line = line.strip()
            if line == line[::-1]:
                palindromes.append(line)
                print(palindromes)
        return str(palindromes)


# Task #3: Write code to save each element of a list
#          to a file, with each element on its own line
def write_list(filename, list):
    # todo: Put your code here for task #3
    palindromes = find_palindromes(filename)
    with open ('EX06-Palindromes-eliasdandouch\palindromes.txt','w') as output:
            output.write(str(palindromes))

if __name__ == '__main__':
    # Put some code here to test your code
    print(is_palindrome('bob'))
    print(find_palindromes("bobob"))
    print(write_list("bobobob",list))