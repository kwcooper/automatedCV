


author_alias = ['Cooper, K. W.', 'Keiland Cooper', 'Keiland W. Cooper.', 'Cooper, K.W.', 
				'Cooper. K. W.,', 'Cooper K. W.', 'Cooper K. W.', 'Cooper K. W.', 'Cooper K. W.', 
				'Cooper, K. W']

def bold_author(authors):
	for tag in author_alias:
		if tag in authors:
			x = authors.replace(tag, f'\\textbf{{{tag}}}')
			return x
		
	print(f'>>> Name not found for {authors}')
	return authors


mentee_alias = ["Pan, C. J."]

def star_author(authors):
	for tag in mentee_alias:
		if tag in authors:
			x = authors.replace(tag, f'***{tag}')
			return x
	else:
		return authors


def format_authors(authors):

	boldAuthors = bold_author(authors)
	boldMenteeAuthors = star_author(boldAuthors)

	return boldMenteeAuthors