### Python Stop words if find the given occurance of words count

from timeit import repeat


def stop_words(input_word,k):
    input_words = input_word.split()
    words_count = dict()
    for word in input_words:
        if word not in words_count:
            words_count[word]=1
        else:
            words_count[word]+=1
    for word,repeated_word in words_count.items():
        if repeated_word == k:
            print(word)
    
    print(words_count)




sentence = input("Enter Your Sentence:")
k = int(input("Occurance of Words Count:"))
stop_words(sentence,k)
