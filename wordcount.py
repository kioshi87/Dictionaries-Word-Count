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
        words_count[word] = counter
        if words_count[word] == words_count[word]:
            counter += 0
        else:
            counter += 1
        print(words_count)
for word, counter in words_count.items():
    print(f'{word}: {counter}')
       # if words_count[word]:
            #counter = test
            # counter += 1
    #print(words_count)