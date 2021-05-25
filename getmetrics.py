
# Grabs external academic metrics

from scholarly import scholarly
import semanticscholar as sch
import pickle
from datetime import date

# -------------------------------------------
# Google Scholar Functions
#--------------------------------------------
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

	fName = 'outFiles/gs_author'

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
	''' pretty print function for scholar stats'''
	author = load_scholar_author(gsID)

	print('\nGoogle Scholar Stats:')
	print("------------------------")
	print(author['name'])
	print(author['affiliation'])
	print("citedby:", author['citedby'])
	print("hindex:", author['hindex'])
	print("n publications:", len(author['publications']))



# -------------------------------------------
# Semantic Scholar Functions
#--------------------------------------------

def fetch_semantic_papers(author):
    filled_papers = []
    for pi in range(len(author['papers'])):
        paper_link = author['papers'][pi]['paperId']
        paper = sch.paper(paper_link, timeout=2)
        filled_papers.append(paper)
    return filled_papers


def fetch_semantic_author(ssID, fillpapers=True):
	''' Queries semantic scholar for a given author
		Also fills all papers if fillpapers is True (a bit slower)'''
	author = sch.author(ssID, timeout=2)

	if fillpapers:
		filledpapers = fetch_semantic_papers(author)
		author['filledpapers'] = filledpapers
	return author


def cache_semantic_author(author, fName): 
	''' Saves author object to a pickle '''
	cacheAuthor = {}
	cacheAuthor['date'] = date.today()
	cacheAuthor['author'] = author
	with open(fName+'.pickle', 'wb') as fp:
		pickle.dump(cacheAuthor, fp)


def load_semantic_author(ssID):

	fName = 'outFiles/ss_author'

	try: # try to load in the chached author for speed
		with open(fName+'.pickle', 'rb') as fp:
			LoadAuthor = pickle.load(fp)
			
		# check if saved dates match, else search scholar again
		if LoadAuthor['date'] == date.today():
			author = LoadAuthor['author']
		else: 
			author = fetch_semantic_author(ssID)
			cache_semantic_author(author, fName)
		
	except:	# Save the computed author object to chache
		author = fetch_semantic_author(ssID)
		cache_semantic_author(author, fName)

	return author

def parse_semantic_citations(ssID):
    """ Compute the total number of citations
    for a filled semantic scholar author """
    author = load_semantic_author(ssID)
    try:
        total_citations = 0
        for pi in range(len(author['filledpapers'])):
            total_citations += author['filledpapers'][pi]['numCitedBy']
        return total_citations
    except KeyError:
        print('Need to fill papers')
        # TODO: add logic to fill papers if needed



# -------------------------------------------
# General Functions
#--------------------------------------------

def grab_metrics(gsID=None, ssID=None):
	""" grabs all metrics of interest and packages them in a dict 
		Top level function"""

	# Google Scholar
	if gsID != None:
		scholar_cites = parse_gscholar_citations(gsID)
	else:
		raise ValueError('No google scholar citations found!')

	# Semantic Scholar
	if ssID != None:
		semantic_cites = parse_semantic_citations(ssID)
	else:
		raise ValueError('No semantic scholar citations found!')

	# Package it all up
	metrics = {}
	metrics['gs_citations'] = scholar_cites
	metrics['ss_citations'] = semantic_cites

	return metrics