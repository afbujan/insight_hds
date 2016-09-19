from __future__ import division
import numpy as np
import praw
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer,TfidfVectorizer





def get_tf(X, with_names=True,**kwargs):
    tf_vec = CountVectorizer(**kwargs)
    tf_vec.fit(X)
    if with_names:
        return tf_vec.transform(X), tf_vec.get_feature_names()
    else:
        return tf_vec.transform(X)


def get_tfidf(X, with_names=True,**kwargs):
    """ Transforms a list of texts into a list of tf-idf vectors
	Parameters:
	----------
	- X, list of strings
		list of input texts

	Returns:
	- tfidf_list, list
		list of tf-idf vectors
    """
    tfidf_vec = TfidfVectorizer(**kwargs)
    tfidf_vec.fit(X)
    if with_names:
        return tfidf_vec.transform(X), tfidf_vec.get_feature_names()
    else:
        return tfidf_tra.transform(X)


def scrape_comments(subreddit_list,verbose=True):
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
    return X, np.array(y).astype('int')
