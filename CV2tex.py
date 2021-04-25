
# The ideal CV manifesto:
# It shouldn't rely on software that isn't very well supported.
# The data format should be standardized.
# It should be really easy to make changes.

# V2.0 KWC

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
mvPDF = 1         # TODO: platform independant pls

# Path information
yamlFile = "cooperCV2.yaml"
templateFile = "."
sectionFile = "/cooperCV2_sections.tex"
resultFile = "cooperCV2_2_w.tex"
resFile = "cooperCV_2_w2.tex" # These can be concatonated

yaml_contents = yaml.load(open(yamlFile, 'r')) # Read data

# Define Jinja2 envirement and load in the LaTeX templates
# Define new syntax for jinja code
env = Environment(loader=FileSystemLoader(templateFile),
  block_start_string='~{',block_end_string='}~',
  variable_start_string='~{{', variable_end_string='}}~')

def generate(): 
  body = ""
  for section in yaml_contents['order']: # Iteratavly generate sections TODO: multiple versions
    print(section)
    contents = yaml_contents[section[0]] # Append the section info to the 
    name = section[1].title()            # Used to select which section template to use
    body += env.get_template(sectionFile).render(
      name = name.upper(),
      contents = contents
    )
  # Generate the TeX wrapper and fill it with generated sections
  result = open(resultFile, 'w')
  result.write(env.get_template(resFile).render( body=body ))
  result.close()

generate() #finally, generate 

# Run the pdf2latex code to generate PDF
if generate_pdf:
  print('Building PDF (pdflatex)...') 
  cmd = 'pdflatex -output-directory=outFiles ' + resultFile
  os.system(cmd)
  os.system(cmd) # compile twice? 

# # move the PDF out of the result dir
# if mvPDF: 
#   os.system('mv outFiles/cooperCV.pdf cooperCV.pdf')


# date.today().strftime("%b %d, %Y")

# TODO: 
#   Add code for automatic versioning
#   Add code for formatting options (long short, graphs etc) -> compute multiple versions with each call
#   Add code for section order here? (Not just in the Yaml?)
#   Compute stats here? -> Add to either last page or seperate document
#   Create an automatic update log? 
# 	Add support for bibfile parsing? 

#   Support for google scholar / semantic scholar api for citations, etc? 

# 	What about a resume? Coverletter? ETC...

# If you need to access any of the YAML code in this script:
# result.write(env.get_template(resFile).render(
    # name = yaml_contents['name'], #.upper(),
