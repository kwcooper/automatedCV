
# The ideal CV manifesto:
# - It shouldn't rely on software that isn't very well supported.
# - The data format should be standardized.
# - It should be really easy to make changes.
# - It should provide more than just a list of your past life

# V2.0 KWC

# Requires pdflatex to compile the .tex output 
# ------------------------------------------------------------------------------

import re
import yaml
import sys
import os

from datetime import date
from jinja2 import Environment, FileSystemLoader

from getmetrics import grab_metrics, print_stats
from utils import format_authors

# General Params
generate_pdf = True
engine = 'XeTeX' # pdflatex
mvPDF = False         # TODO: platform independant pls
compileTwice = True

# Path information
yamlFile = "cooperCV2.yaml"              # The text database
templateFile = "."                       # templating directory
sectionFile = "/cooperCV2_sections.tex"  # CV section logic
resFile = "cooperCV2_.tex"               # Latex structure
resultFile = "cooperCV.tex"              # Final built file 

yaml_contents = yaml.safe_load(open(yamlFile, 'r')) # Read data (updated to safe_load)

# Define Jinja2 envirement and load in the LaTeX templates
# Define new syntax for jinja code
env = Environment(loader=FileSystemLoader(templateFile),
  block_start_string='~{',block_end_string='}~',
  variable_start_string='~{{', variable_end_string='}}~')


# Grab the academic metrics for cv stats
print('Computing metrics... Please wait')
gsID = 'nCEUdSoAAAAJ'
ssID = 89510954
metrics = grab_metrics(gsID=gsID, ssID=ssID)

def generate(): 
  body = ""
  for section in yaml_contents['order']: # iterate and generate sections TODO: multiple versions
    print(section)
    contents = yaml_contents[section[0]] # Append the section info to the 
    name = section[1].title()            # Used to select which section template to use
    body += env.get_template(sectionFile).render(
      name = name.upper(),
      contents = contents,
      metrics = metrics,
      format_authors = format_authors
    )
  # Generate the TeX wrapper and fill it with generated sections
  result = open(resultFile, 'w')
  result.write(env.get_template(resFile).render( body=body ))
  result.close()

generate() #finally, generate 

# Run the pdf2latex code to generate PDF
# TODO: update to add support for LuaTeX
if generate_pdf:

  if engine == 'pdflatex':
    cmd = f'pdflatex -output-directory=outFiles {resultFile}'
  elif engine == 'XeTeX': 
    # Note, batchmode supresses output, but that also means you don't see warnings... 
    # Check cooperCV.log in outfiles to get a better view
    cmd = f'xelatex --interaction=batchmode --halt-on-error --output-directory=outFiles {resultFile} '

  print(f'Building PDF ({engine})...') 
  os.system(cmd)
  if compileTwice: os.system(cmd) # compile twice? 

# move the PDF out of the result dir
if mvPDF: 
  # if something breaks, this will throw an error since there will be no PDF to move
  os.system('mv outFiles/cooperCV.pdf cooperCV.pdf')

# Just so we can get a bit of insight since we're 
# thinking about all of this stuff
print_stats(gsID, ssID)

# date.today().strftime("%b %d, %Y")

# TODO: 
#   Add code for automatic versioning
#   Add code for formatting options (long short, graphs etc) -> compute multiple versions with each call
#   Add code for section order here? (Not just in the Yaml?)
#   Compute stats here? -> Add to either last page or seperate document
#   Create an automatic update log? 
# 	Add support for bibfile parsing? 

#   Support for google scholar / semantic scholar api for citations, etc? -> working!

# 	What about a resume? Coverletter? ETC...

# If you need to access any of the YAML code in this script:
# result.write(env.get_template(resFile).render(
    # name = yaml_contents['name'], #.upper(),


# inspired by:
# https://github.com/qutebits
# https://github.com/bamos/cv
# https://github.com/craffel/craffel.github.io/blob/master/src/compile.py
# https://timsainburg.com/curriculum-vitae-in-python-html-jinja.html


