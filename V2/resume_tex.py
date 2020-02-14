# Converts my Resume from YAML to TeX.
# Requires pdflatex 
# ------------------------------------------------------------------------------
# inspired by work of:
#  Aleksandr Mattal <https://github.com/qutebits>
#  Brandon Amos <https://github.com/bamos/cv>
# https://github.com/craffel/craffel.github.io/blob/master/src/compile.py

import re
import yaml
import sys

from datetime import date
from jinja2 import Environment, FileSystemLoader

yaml_contents = yaml.load(open("resume.yaml", 'r')) #read data

env = Environment(loader=FileSystemLoader("template"),
  block_start_string='~{',block_end_string='}~',
  variable_start_string='~{{', variable_end_string='}}~')

this_loc = len(open("resume_tex.py", 'r').readlines()) #lets keep it at 42

def generate():
  body = ""
  for section in yaml_contents['order']: #generate sections 1 by 1
    contents = yaml_contents[section[0]]
    name = section[1].title()
    body += env.get_template("resume-section.tmpl.tex").render(
      name = name.upper(),
      contents = contents
    )
  #and then generate the TeX wrapper and fill it with generated sections
  result = open("result/resume.tex", 'w')
  result.write(env.get_template("resume.tmpl.tex").render(
    name = yaml_contents['name'].upper(),
    email = yaml_contents['email'],
    loc = this_loc, #lines of code in this very script :)
    body = body,
    today = date.today().strftime("%B %d, %Y") #generation date
  ))
  result.close()

generate() #finally, generate this beauty