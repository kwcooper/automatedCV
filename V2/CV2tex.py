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

generate_pdf = True

yaml_contents = yaml.load(open("resume.yaml", 'r')) #read data

env = Environment(loader=FileSystemLoader("template3"),
  block_start_string='~{',block_end_string='}~',
  variable_start_string='~{{', variable_end_string='}}~')

this_loc = len(open("CV2tex.py", 'r').readlines()) #lets keep it at 42

def generate():
  body = ""
  for section in yaml_contents['order']: #generate sections 1 by 1
    contents = yaml_contents[section[0]]
    name = section[1].title()
    body += env.get_template("cooperCV-sections.tex").render(
      name = name.upper(),
      contents = contents
    )
  #and then generate the TeX wrapper and fill it with generated sections
  result = open("result/cooperCV-res.tex", 'w')
  result.write(env.get_template("cooperCV.tex").render(
    name = yaml_contents['name'], #.upper(),
    lastName = yaml_contents['lastName'], #.upper(),
    email = yaml_contents['email'],
    loc = this_loc, #lines of code in this very script :)
    body = body,
    today = date.today().strftime("%b %d, %Y") #generation date
  ))
  result.close()

generate() #finally, generate this beauty

# Run the pdf2latex code to generate PDF
if generate_pdf:
  print('Building PDF (pdflatex)...') 
  cmd = 'pdflatex result/cooperCV-res.tex'
  os.system(cmd)

