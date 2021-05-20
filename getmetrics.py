
# Grabs external academic metrics

from scholarly import scholarly
import pickle
from datetime import date

def fetch_scholar_author(gsID, fill=True):
	''' Queries google scholar for a given author
		Also fills all stats if fill is True (a bit slower)'''
	author = scholarly.search_author_id(gsID)
	if fill:
		author = scholarly.fill(author, sections=['publications', 'basics', 'indices', 'counts'])
	return author


def cache_scholar_author(author, fName): 
	''' Saves author object to a pickle '''
	cacheAuthor = {}
	cacheAuthor['date'] = date.today()
	cacheAuthor['author'] = author
	with open(fName+'.pickle', 'wb') as fp:
		pickle.dump(cacheAuthor, fp)


def load_scholar_author(gsID):

	fName = 'outFiles/author'

	try: # try to load in the chached author for speed
		with open(fName+'.pickle', 'rb') as fp:
			LoadAuthor = pickle.load(fp)
			
		# check if saved dates match, else search scholar again
		if LoadAuthor['date'] == date.today():
			author = LoadAuthor['author']
		else: 
			author = fetch_scholar_author(gsID)
			cache_scholar_author(author, fName)
		
	except:	# Save the computed author object to chache
		author = fetch_scholar_author(gsID)
		cache_scholar_author(author, fName)

	return author


def parse_gscholar_citations(gsID):
	''' Simple helper function to get scholar cites
		(will be depriciated soon)'''
	author = load_scholar_author(gsID)
	return author['citedby']


def print_gscholar_stats(gsID):

	author = load_scholar_author(gsID)

	print('Google Scholar Stats:')
	print("------------------------")
	print(author['name'])
	print(author['affiliation'])
	print("citedby:", author['citedby'])
	print("hindex:", author['hindex'])
	print("n publications:", len(author['publications']))


def grab_metrics(gsID=None):
	""" """

	if gsID != None:
		scholar_cites = parse_gscholar_citations(gsID)
	else:
		raise ValueError('No google scholar citations found!')
	# Package it all up
	metrics = {}
	metrics['gs_citations'] = scholar_cites

	return metrics