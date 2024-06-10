def count_words(s: str) -> int:
   
    words = s.split()
   
    return len(words)

input_string = input()

print(count_words(input_string))