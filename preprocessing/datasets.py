from __future__ import division
import numpy as np
import praw
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer


def get_tfidf(X):
    """ Transforms a list of texts into a list of tf-idf vectors
	Parameters:
	----------
	- X, list of strings
		list of input texts

	Returns:
	- tfidf_list, list
		list of tf-idf vectors
    """
    count_vect = CountVectorizer()
    tfidf_transformer = TfidfTransformer()
    tfidf_list = tfidf_transformer.fit_transform(count_vect.fit_transform(X))
    return tfidf_list

def scrape_comments(subreddit_list,tfidf=True,verbose=True):
    """This function scrapes comments from different subreddits

    Parameters:
    ----------
    - subreddit_list, list of strings
      list of target subreddit names to scrape the data

    Returns:
    -------
    - X, list of strings
      list of comments
    - y, array of integers
      subreddit labels (integers starting from 1)
    """
    r = praw.Reddit('Test by u/_Daimon_')
    X = []
    y = []
    for i, subreddit in enumerate(subreddit_list):
        comments = r.get_subreddit(subreddit).get_comments(limit=None)
        count=0
        for c in comments:
   	    X.append(c.body) 
	    y.append(i+1)
	    count+=1
	if verbose:
            print '\n%i comments from subreddit: %s fetched!'%(count,subreddit)
    y = np.array(y).astype('int')
    if tfidf:
        X = get_tfidf(X)	
    return X, y

