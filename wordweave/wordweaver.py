import urllib.request, difflib

def get_character_diff(test_word,target_word):
    char_diff = 0
    w1_len = len(test_word)
    w2_len = len(target_word)
    if w1_len != w2_len:
        return -1
    for x in range(w1_len):
        char_diff += 1 if test_word[x] != target_word[x] else 0
    return char_diff    

def get_character_same(test_word,target_word):
    char_same = 0
    w1_len = len(test_word)
    w2_len = len(target_word)
    if w1_len != w2_len:
        return -1
    for x in range(w1_len):
        char_same += 1 if test_word[x] == target_word[x] else 0
    return char_same 

def closest_matching(list1_words, list2_words):
    best_same = 0
    best_words = []
    for word1 in list1_words:
        for word2 in list2_words:
            same = get_character_same(word1, word2)
            if same > best_same:
                best_same = same
                best_words = [[word1, word2, same]]
            elif same == best_same:
                best_words.append([word1, word2, same])      
    return best_words         
       

def one_letter_diff(word, word_list):
    words_one_ltr_dif = []
    for single_word in word_list:
        if get_character_diff(single_word,word) == 1:
            words_one_ltr_dif.append(single_word)
    return words_one_ltr_dif         

def unique_words(words):
    return sorted(list(set(words)))    


word_initial = input('Enter the initial word: ')
word_target = input('Enter the target word: ')
web_contents = urllib.request.urlopen('http://www.mieliestronk.com/corncob_lowercase.txt')
all_words = [x.decode("utf-8").replace('\r\n','') for x in web_contents.readlines()]
same_len_words = [x for x in all_words if len(x) == len(word_target)]

word_list = one_letter_diff(word_initial,same_len_words)
print(word_list)

all_words = []
for i in word_list:
    new_list = one_letter_diff(i,same_len_words)
    print ('all= ',all_words)
    print([x for x in new_list if x not in word_list and x not in all_words])
    all_words = unique_words(all_words + new_list)



# get init and target words - complete
# get list of same length words - complete
# get a starting list of words that are 1 letter different from the target word - complete
# get a starting list of words that are 1 letter different from the initial word - complete
# work toward the middle of the chain by comparing the two lists and identifying words with greater similarity
# work with similar content first to find a word ladder 
# repeat this until a matching word is found in both top and bottom lists

