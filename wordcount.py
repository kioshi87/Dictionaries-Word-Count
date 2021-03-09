#open the file
test_file = open("test.txt") 

#count how many times each space-separated word occurs in 'test_file'

#create the dictionary
words_count = {}
counter = 0
#start looping through each line in the file
for line in test_file:
    separated_words = line.split(' ')       #separate each word by a space
    for word in separated_words:
        counter += 1
        words_count[word] = counter
    print(words_count) 