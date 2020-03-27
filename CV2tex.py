# The ideal CV:
# It shouldn't rely on software that isn't very well supported.
# The data format should be standardized.
# It should be really easy to make changes.

# Requires pdflatex to compile the .tex output -> TODO: create function for this
# ------------------------------------------------------------------------------
# inspired by:
# https://github.com/qutebits
# https://github.com/bamos/cv
# https://github.com/craffel/craffel.github.io/blob/master/src/compile.py
# https://timsainburg.com/curriculum-vitae-in-python-html-jinja.html

import re
import yaml
import sys
import os

from datetime import date
from jinja2 import Environment, FileSystemLoader

# General Params
generate_pdf = 1
mvPDF = 1

# Path information
yamlFile = "cooperCV.yaml"
templateFile = "template3"
sectionFile = "cooperCV-sections.tex"
resultFile = "outFiles/cooperCV.tex"
resFile = "cooperCV.tex" # These can be concatonated

yaml_contents = yaml.load(open(yamlFile, 'r')) # Read data

env = Environment(loader=FileSystemLoader(templateFile),
  block_start_string='~{',block_end_string='}~',
  variable_start_string='~{{', variable_end_string='}}~')

def generate():
  body = ""
  for section in yaml_contents['order']: # Iteratavly generate sections
    contents = yaml_contents[section[0]]
    name = section[1].title()
    body += env.get_template(sectionFile).render(
      name = name.upper(),
      contents = contents
    )
  # Generate the TeX wrapper and fill it with generated sections
  result = open(resultFile, 'w')
  result.write(env.get_template(resFile).render(
    name = yaml_contents['name'], #.upper(),
    lastName = yaml_contents['lastName'], #.upper(),
    email = yaml_contents['email'],
    body = body,
    today = date.today().strftime("%b %d, %Y") #generation date (could move to LaTeX)
  ))
  result.close()

generate() #finally, generate 

# Run the pdf2latex code to generate PDF
if generate_pdf:
  print('Building PDF (pdflatex)...') 
  cmd = 'pdflatex -output-directory=outFiles ' + resultFile
  os.system(cmd)

# move the PDF out of the result dir
if mvPDF: 
  os.system('mv outFiles/cooperCV.pdf cooperCV.pdf')

# TODO: 
#   Add code for automatic versioning
#   Add code for formatting options (long short, graphs etc) -> compute multiple versions with each call
#   Add code for section order here? (Not just in the Yaml?)
#   Compute stats here? 
#   Create an automatic update log? 