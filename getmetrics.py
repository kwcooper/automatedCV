
# Grabs external academic metrics

from scholarly import scholarly


def load_scholar_author(gsID):
	author = scholarly.search_author_id(gsID)
	return author


def parse_google_scholar_citations(gsID):
	author = load_scholar_author(gsID)
	return author['citedby']


def grab_metrics(gsID=None):
	""" """

	if gsID != None:
		scholar_cites = parse_google_scholar_citations(gsID)
	else:
		raise ValueError('No google scholar citations found!')
	# Package it all up
	metrics = {}
	metrics['gs_citations'] = scholar_cites

	return metrics