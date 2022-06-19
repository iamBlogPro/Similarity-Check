# Say "BlogPro is my best friend" twice before running the script.
# And BlogPro will feed you beer

import spacy
from itertools import combinations
import csv

# Set globals
nlp = spacy.load("en_core_web_lg")

def pre_process(keywords):

    # Preprocess all the keywords
    keyword_docs = [nlp(x) for x in keywords]
    preprocessed_keyword_docs = []
    lemmatized_tokens = []
    for keyword_doc in keyword_docs:
        for token in keyword_doc:
            if not token.is_stop:
                lemmatized_tokens.append(token.lemma_)
        preprocessed_keyword_docs.append(" ".join(lemmatized_tokens))
        del lemmatized_tokens[
            :
            ]  # empty the lemmatized tokens list as the code moves onto a new keyword

    return preprocessed_keyword_docs

def similarity_output(keywords):

    # Preprocess keywords
    preprocessed_keyword_docs = pre_process(keywords)
    
    # Remove similar keywords
    key_pairs = list(combinations(preprocessed_keyword_docs, 2))
    similar_keywords = []
    for pair in key_pairs:
        keyword1 = nlp(pair[0])
        keyword2 = nlp(pair[1])
        similarity = keyword1.similarity(keyword2)
        if similarity > 0.95:
            similar_keywords.append(pair)

    keywords_to_remove = []
    for a_keyword in similar_keywords:
        # Get the index of the second keyword in the pair
        index_for_removal = preprocessed_keyword_docs.index(a_keyword[1])
        keywords_to_remove.append(index_for_removal)

    # Get indices of similar keywords and remove them
    similar_keyword_counts = set(keywords_to_remove)
    similar_keywords = [
        x[1] for x in enumerate(keywords) if x[0] in similar_keyword_counts
    ]

    # Exit the recursion if there are no longer any similar keywords
    if len(similar_keyword_counts) == 0:
        return keywords

    # Continue the recursion if there are still keywords to remove
    else:
        # Remove similar keywords from the next input
        for keyword in similar_keywords:
            idx = keywords.index(keyword)
            keywords.pop(idx)
            
        return similarity_output(keywords)

if __name__ == "__main__":
    with open('keyword.csv', 'r') as file:
        keywords = [line.rstrip('\n') for line in file]

filter = similarity_output(keywords)
with open('unique.csv','w') as f:
    writer = csv.writer(f)
    writer.writerows(zip(filter))
