#!/usr/bin/env pipenv
import re

my_pattern = r"It's such a lovely day today."
my_regex = re.compile(my_pattern)
match = re.search("Some weather we're having today, huh?",my_pattern)
print(match)