import re 

def check_similarity_new(correct_sentence, wrong_sentence):
    overall_percentage = 0
    
    def extract_words(input_string):
        words = re.findall(r'\b\w+\b', input_string)
        return words
    
    def count_letters(input_string):
        letter_counts = {}
        for letter in input_string:
            letter = letter.lower()
            letter_counts[letter] = letter_counts.get(letter, 0) + 1
        return letter_counts
    
    def word_similarity_check(dic1, dic2):
        word_similarity_score = 0
        
        if len(dic1) >= len(dic2):
            for letter in dic1.keys():
                if letter in dic2.keys():
                    if dic1[letter] >= dic2[letter]:
                        word_similarity_score = word_similarity_score + ((dic2[letter] / dic1[letter]) * 100)
                    if dic1[letter] < dic2[letter]:
                        word_similarity_score = word_similarity_score + ((dic1[letter] / dic2[letter]) * 100)
            return word_similarity_score / len(dic1)
        
        if len(dic1) < len(dic2):
            for letter in dic2.keys():
                if letter in dic1.keys():
                    if dic1[letter] >= dic2[letter]:
                        word_similarity_score = word_similarity_score + ((dic2[letter] / dic1[letter]) * 100)
                    if dic1[letter] < dic2[letter]:
                        word_similarity_score = word_similarity_score + ((dic1[letter] / dic2[letter]) * 100)
            return word_similarity_score / len(dic2)
    for correct_word, wrong_word in zip(extract_words(correct_sentence), extract_words(wrong_sentence)):
        overall_percentage = overall_percentage + word_similarity_check(count_letters(correct_word), count_letters(wrong_word))
    
    if extract_words(correct_sentence) >= extract_words(wrong_sentence):
        divider = len(extract_words(correct_sentence))
    elif extract_words(correct_sentence) < extract_words(wrong_sentence):
        divider = len(extract_words(wrong_sentence))        
        
    return overall_percentage / divider

string1 = "this is a test text"
string2 = "this is a test"
check_similarity_new(string1, string2)
