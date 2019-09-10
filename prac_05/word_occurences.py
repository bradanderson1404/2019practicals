count_of_all_words = {}

string = input("Enter a string: ")
words = string.split(" ")

for word in words:
    amount_of_word = count_of_all_words.get(word, 0)
    count_of_all_words[word] = amount_of_word + 1

longest_word = max(len(word) for word in words)
words = list(count_of_all_words.keys())
words.sort()
for word in words:
    print("{:{}} : {}".format(word, longest_word, count_of_all_words[word]))
