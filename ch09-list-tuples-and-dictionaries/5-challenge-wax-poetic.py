import random

nouns = ['fossil', 'horse', 'aardvark', 'judge', 'chef', 'mango', 'extrovert', 'gorilla']
verbs = ['kicks', 'jingles', 'bounces', 'slurps', 'meows', 'explodes', 'curdles']
adjectives = ['furry', 'balding', 'incredulous', 'fragant', 'exuberant', 'glistening']
prepositions = ['againts', 'after', 'into', 'beneath', 'upon', 'for', 'in', 'like', 'over', 'within']
adverbs = ['curiously', 'extravagantly', 'tantalizingly', 'furiously', 'sensuously']



def make_poem():
    # Three nouns
    noun1 = random.choice(nouns)
    noun2 = random.choice(nouns)
    while noun1 == noun2:
        noun2 = random.choice(nouns)
    noun3 = random.choice(nouns)
    while noun1 == noun3 or noun2 == noun3:
        noun3 = random.choice(nouns)
    # Three verbs
    verb1 = random.choice(verbs)
    verb2 = random.choice(verbs)
    while verb1 == verb2:
        verb2 = random.choice(verbs)
    verb3 = random.choice(verbs)
    while verb1 == verb3 or verb2 == verb3:
        verb3 = random.choice(verbs)
    # Three adjectives
    adj1 = random.choice(adjectives)
    adj2 = random.choice(adjectives)
    while adj1 == adj2:
        adj2 = random.choice(adjectives)
    adj3 = random.choice(adjectives)
    while adj1 == adj3 or adj2 == adj3:
        adj3 = random.choice(adjectives)
    # Two prepositions
    prep1 = random.choice(prepositions)
    prep2 = random.choice(prepositions)
    while prep1 == prep2:
        prep2 = random.choice(prepositions)
    # One adverb
    adverb1 = random.choice(adverbs)

    if adj1[0] in ('a', 'e', 'i', 'o', 'u'):
        article = 'An'
    else:
        article = 'A'
    # Create the poem
    poem = f"""
    {article} {adj1} {noun1}

    {article} {adj1} {noun1} {verb1} {prep1} the {adj2} {noun2}
    {adverb1}, the {noun1} {verb2}
    the {noun3} {verb3} {prep2} a {adj3} {noun3}
    """

    return poem

if __name__ == '__main__':
    poem = make_poem()
    print(poem)