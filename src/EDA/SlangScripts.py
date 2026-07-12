import pandas as pd
import numpy as np
import math
import random
import re
import html
import unicodedata

# This code tokenizer code originally came from Hargun
# tokenize comments

def tokenize(text):
    """Basic tokenizer for comment text."""
    TOKEN_RE = re.compile(
        r"""
        (?<![a-z0-9])
        \#?
        (?:
            [a-z]+(?:['’‘ʼ`´＇-][a-z]+)*[a-z0-9]*
            |
            [a-z]*\d+[a-z0-9]*
        )
        (?![a-z0-9])
        """,
        re.I | re.VERBOSE
    )
    
    URL_RE = re.compile(r"https?://\S+|www\.\S+")
    TIME_RE = re.compile(r"\b\d{1,2}:\d{2}(?::\d{2})?\b")
    
    APOSTROPHE_TRANSLATION = str.maketrans({
        "’": "'",
        "‘": "'",
        "ʼ": "'",
        "`": "'",
        "´": "'",
        "＇": "'"
    })

    text = html.unescape(str(text))
    text = unicodedata.normalize("NFKC", text)
    text = text.translate(APOSTROPHE_TRANSLATION)
    text = text.lower()
    text = URL_RE.sub(" ", text)
    text = TIME_RE.sub(" ", text)

    return [m.group(0).lstrip("#") for m in TOKEN_RE.finditer(text)]

def removeWords(df): #df is a dataframe of statistics of words in particular weeks. Requires 'word' and 'count' columns, which are strings and integers respectively
    #code made by Hargun
    # remove common/non-informative words
    stopwords = set("""
    a about above after again against all am an and any are as at be because been before being below between both but by
    can cannot could did do does doing down during each few for from further had has have having he her here hers herself
    him himself his how i if in into is it its itself just me more most my myself no nor not of off on once only or other
    our ours ourselves out over own same she should so some such than that the their theirs them themselves then there
    these they this those through to too under until up very was we were what when where which while who whom why will
    with you your yours yourself yourselves
    """.split())
    
    # Contractions and common variants.
    stopwords |= {
        "i'm", "it's", "that's", "don't", "you're", "he's", "she's", "we're", "they're",
        "i've", "you've", "we've", "they've", "i'll", "you'll", "we'll", "they'll",
        "isn't", "aren't", "wasn't", "weren't", "can't", "couldn't", "wouldn't",
        "shouldn't", "won't", "didn't", "doesn't", "haven't", "hasn't", "hadn't",
        "there's", "what's", "who's", "where's", "when's", "why's", "how's",
        "im", "ive", "dont", "cant", "wont", "youre", "thats", "theres", "whats",
        "hes", "shes", "were", "theyre", "ll", "re", "ve", "ur", "amp"
    }
    
    # Extra ordinary/common words that appeared in earlier top predictions.
    # This is project-specific cleanup.
    extra_common_words = {
        "would", "one", "get", "even", "video", "go", "know", "never", "got", "good",
        "make", "made", "see", "think", "really", "still", "also", "much", "going",
        "people", "bro", "man", "guys", "time", "way", "back", "first", "last",
        "like", "game", "person", "now", "years", "guy", "kid", "thing", "stuff",
        "day", "watch", "look", "looks", "say", "said", "right", "actually"
    }
    
    stopwords |= extra_common_words
    
    dftemp = df[
        df["word"].map(
            lambda w: (w not in stopwords) and (len(w) >= 2 or w in {"w", "l"})
        )
    ].copy()

    # Rare-word filter:
    # Keep a word if it appears in at least 5 comments in at least one week.
    max_by_word = dftemp.groupby("word").agg(max_count=("count", "max")).reset_index()
    keep_words = max_by_word.loc[max_by_word["max_count"] >= 5, "word"]
    
    return dftemp[dftemp["word"].isin(keep_words)].copy()

def TrainTestSplit(df,testweeks = 5, testwordproportion = 0.2, seed = None):
    #df is a dataframe of words during different weeks, we assume it contains the columns 'word' and 'time_id'
    #testweeks is an integer and is the number of weeks to be held for the time test set, these will be the last weeks
    #testwordproportion is a float and is the proportion of words to be held for the word test set
    #seed is an integer that seeds the RNG
    if seed != None:
        random.seed(seed)
    testwords = np.choice(df.word.unique(),math.ceil(testwordproportion*df.word.nunique()),replace=False) #randomly determines which words to hold for the test set
    dftesttime = df.loc[df.word.map(lambda word: word not in testwords)].copy()
    dftestwords = df.loc[df.word.map(lambda word: word in testwords)].copy()
    dftrain = dftesttime.loc[df.time_id<=df.time_id.max()-testweeks].copy()
    return dftrain, dftesttime, dftestwords