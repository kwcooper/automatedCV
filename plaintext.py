import re
import yaml
import sys
import os

from datetime import date
from jinja2 import Environment, FileSystemLoader

from getmetrics import grab_metrics, print_stats
from utils import format_authors


# Path information
yamlFile = "cooperCV2.yaml"              # The text database
templateFile = "."                       # templating directory

yaml_contents = yaml.safe_load(open(yamlFile, 'r')) # Read data (updated to safe_load)


# Define Jinja2 envirement and load in the LaTeX templates
# Define new syntax for jinja code
env = Environment(loader=FileSystemLoader(templateFile),
  block_start_string='~{',block_end_string='}~',
  variable_start_string='~{{', variable_end_string='}}~')



 