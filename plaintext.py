import re
import yaml
import sys
import os

from datetime import date
from jinja2 import Environment, FileSystemLoader

from getmetrics import grab_metrics, print_stats
from utils import format_authors


from datetime import date

today = date.today()
d1 = today.strftime("%y%m%d")
print(d1)

# Path information
yamlFile = "cooperCV2.yaml"              # The text database
templateDir = "."                       # templating directory
resFile = "plaintextCV_template.txt"               #  structure
resultFile = d1+"_cooperCV.txt"              # Final built file 
sectionFile = 'plaintextCV_sections.txt'

yaml_contents = yaml.safe_load(open(yamlFile, 'r')) # Read data (updated to safe_load)


# Define Jinja2 envirement and load in the LaTeX templates
# Define new syntax for jinja code
env = Environment(loader=FileSystemLoader(templateDir),
  block_start_string='~{',block_end_string='}~',
  variable_start_string='~{{', variable_end_string='}}~')


def generate(): 
  body = ""
  for section in yaml_contents['order']: # iterate and generate sections TODO: multiple versions
    print(section)
    contents = yaml_contents[section[0]] # Append the section info to the 
    name = section[1].title()            # Used to select which section template to use
    body += env.get_template(sectionFile).render(
      name = name.upper(),
      contents = contents
    )
  # Generate the TeX wrapper and fill it with generated sections
  result = open(resultFile, 'w')
  result.write(env.get_template(resFile).render( body=body,
  												 today=d1 ))
  result.close()



def generate_():
	result = open(resultFile, 'w')
	result.write(env.get_template(resFile).render( test="worked!" ))
	result.close()

generate() #finally, generate 
