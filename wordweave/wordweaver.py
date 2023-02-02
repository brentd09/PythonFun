import urllib.request

def get_similar(word,word_list):
    similar_word_list = []
    desired_state = {'diff': 1 ,'same': word_size-1}
    for single_word in word_list:
        word_state = {'diff':0,'same':0}
        for indx in range(word_size): 
            if word[indx] == single_word[indx]:
                word_state['same'] += 1
            else:
                word_state['diff'] += 1  
        if word_state == desired_state:
            similar_word_list.append(single_word)
    return similar_word_list         

word_initial = input('Enter the initial word: ')
word_target = input('Enter the target word: ')
web_contents = urllib.request.urlopen('http://www.mieliestronk.com/corncob_lowercase.txt')
result = web_contents.readlines()
word_list = [x.decode("utf-8").replace('\r\n','') for x in result]
word_size = len(word_target)
filtered_word_list = [x for x in word_list if len(x) == word_size]

similar = get_similar(word_target,filtered_word_list)
print(similar)
for sim in similar:
    print(get_similar(sim,filtered_word_list))