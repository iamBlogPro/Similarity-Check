# Keyword-Similarity-Check

A very simple experiment to implement `spacy` to remove contextually similar keywords from a list. 

# Install

1. Install spacy 

`pip install spacy`

2. Download a trained spacy model. Spacy currently has several models for several languages, as can be seen here - https://spacy.io/models/en

The code currently uses en_core_web_lg - https://spacy.io/models/en#en_core_web_lg - a 382 MB large language model.

To install `python -m spacy download en_core_web_lg`

If you decide to go with a different model, be sure to load it appropriately in line 9 of the script.

3. Add your keywords in a single column CSV file called `keywords.csv`

4. Let the script run, the output will be stores in `unique.csv`


# How it works

1. Uses spacy's `token.lemma_` to lemmatize the keywords (this is a trainable metric, so I need to play around with this - in it's present form it uses the default lemmatization)

2. Uses the `combination` function from `itertools`  to pair keywords - then makes them run a check against each others with similarity set to > 0.95

3. Reads file `keywords.csv` - removes contextually duplicate keywords and writes to file `unique.csv`
