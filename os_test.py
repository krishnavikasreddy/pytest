import os
import re

fd = open('os_test.py', 'r')
file_contents = fd.read()
fd.close()

import_statement = re.compile('^import')

print import_statement.findall(file_contents)
