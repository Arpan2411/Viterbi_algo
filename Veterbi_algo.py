# parts of speech 
POS = ['Noun', 'Pronoun', 'Adjective', 'Adverb', 'Preposition', 'Conjunction', 'Interjection', 'Article']
# User given sentence
sentence = "the quick brown fox jumps over the lazy dog"
# spliting the sentence into words
words = sentence.split()
# define the start dictionary for the Viterbi algorithm
start_prob = {'Noun': 0.2, 'Pronoun': 0.1, 'Adjective': 0.3, 'Adverb': 0.1, 'Preposition': 0.1, 'Conjunction': 0.05, 'Interjection': 0.05, 'Article': 0.1}
# define the transition probabilities between parts of speech
transition_prob = {
    'Noun': {'Noun': 0.1, 'Pronoun': 0.1, 'Adjective': 0.3, 'Adverb': 0.1, 'Preposition': 0.1, 'Conjunction': 0.05, 'Interjection': 0.05, 'Article': 0.1},
    'Pronoun': {'Noun': 0.1, 'Pronoun': 0.1, 'Adjective': 0.2, 'Adverb': 0.1, 'Preposition': 0.1, 'Conjunction': 0.1, 'Interjection': 0.1, 'Article': 0.2},
    'Adjective': {'Noun': 0.4, 'Pronoun': 0.1, 'Adjective': 0.1, 'Adverb': 0.1, 'Preposition': 0.1, 'Conjunction': 0.05, 'Interjection': 0.05, 'Article': 0.1},
    'Adverb': {'Noun': 0.1, 'Pronoun': 0.1, 'Adjective': 0.1, 'Adverb': 0.1, 'Preposition': 0.1, 'Conjunction': 0.1, 'Interjection': 0.1, 'Article': 0.2},
    'Preposition': {'Noun': 0.1, 'Pronoun': 0.1, 'Adjective': 0.1, 'Adverb': 0.1, 'Preposition': 0.1, 'Conjunction': 0.1, 'Interjection': 0.1, 'Article': 0.2},
    'Conjunction': {'Noun': 0.1, 'Pronoun': 0.1, 'Adjective': 0.1, 'Adverb': 0.1, 'Preposition': 0.1, 'Conjunction': 0.1, 'Interjection': 0.1, 'Article': 0.2},  
    'Interjection': {'Noun': 0.1, 'Pronoun': 0.1, 'Adjective': 0.1, 'Adverb': 0.1, 'Preposition': 0.1, 'Conjunction': 0.1, 'Interjection': 0.1, 'Article': 0.2},
    'Article': {'Noun': 0.4, 'Pronoun': 0.1, 'Adjective': 0.1, 'Adverb': 0.1, 'Preposition': 0.1, 'Conjunction': 0.05, 'Interjection': 0.05, 'Article': 0.1}
}
# define the emission probabilities for each word given a part of speech
emission_prob = {
    'Noun': {'the': 0.1, 'quick': 0.1, 'brown': 0.1, 'fox': 0.2, 'jumps': 0.1, 'over': 0.1, 'lazy': 0.1, 'dog': 0.2},
    'Pronoun': {'the': 0.1, 'quick': 0.1, 'brown': 0.1, 'fox': 0.1, 'jumps': 0.1, 'over': 0.1, 'lazy': 0.1, 'dog': 0.1},
    'Adjective': {'the': 0.1, 'quick': 0.3, 'brown': 0.3, 'fox': 0.1, 'jumps': 0.1, 'over': 0.1, 'lazy': 0.1, 'dog': 0.1},
    'Adverb': {'the': 0.1, 'quick': 0.1, 'brown': 0.1, 'fox': 0.1, 'jumps': 0.1, 'over': 0.1, 'lazy': 0.1, 'dog': 0.1},
    'Preposition': {'the': 0.1, 'quick': 0.1, 'brown': 0.1, 'fox': 0.1, 'jumps': 0.1, 'over': 0.3, 'lazy': 0.1, 'dog': 0.1},
    'Conjunction': {'the': 0.1, 'quick': 0.1, 'brown': 0.1, 'fox': 0.1, 'jumps': 0.1, 'over': 0.1, 'lazy': 0.1, 'dog': 0.1},
    'Interjection': {'the': 0.1, 'quick': 0.1, 'brown': 0.1, 'fox': 0.1, 'jumps': 0.1, 'over': 0.1, 'lazy': 0.1, 'dog': 0.1},
    'Article': {'the': 0.4, 'quick': 0.1, 'brown': 0.1, 'fox': 0.1, 'jumps': 0.1, 'over': 0.1, 'lazy': 0.1, 'dog': 0.1}
}
# Viterbi algorithm implementation
V = [{}]
path = {}
# this loop is for calculating probability of the 1st word starts with perticular POS
for pos in POS:
    word = words[0]
    emit = emission_prob[pos].get(word, 0.0000001) # very small prob for new words
    V[0][pos] = start_prob[pos] * emit
    path[pos] = [pos]

# this loop does the actual thing , calculating probability for each case by multiplying with transition and emission and the previous probability and then checks the max prob value and then append it in dp table
for t in range(1, len(words)):
    V.append({})
    new_path = {}
    for cur_pos in POS:
        max_prob = -1
        last_max_prob = None
        for prev_pos in POS:
            emit = emission_prob[cur_pos].get(words[t], 0.0000001) 
            prob = V[t-1][prev_pos] * transition_prob[prev_pos][cur_pos] * emit  #calculating the prob for each nodes/phase
            if prob > max_prob:
                max_prob = prob
                last_max_prob = prev_pos
        V[t][cur_pos] = max_prob
        new_path[cur_pos] = path[last_max_prob] + [cur_pos]
    path = new_path

final_state = max(V[-1], key=V[-1].get)
best_path = path[final_state]

print('sentence:', sentence)
print('best path:', best_path)
print('probability of the best path:', V[-1][final_state])