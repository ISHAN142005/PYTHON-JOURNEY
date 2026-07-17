"""
Importing Modules
Python provides built-in and third-party modules.

Two Types of of modules in python :
-Build in modules
-External Modules
 Lists:http://docs.python.org/3/py-modindex.html
"""

import math
import os
import mymodule  # -->Creating your own module
import requests

print(math.sqrt(16))  # -->4(output)
mymodule.hello()
print(mymodule.greet("Alice"))  # Output: Hello, Alice!
r = requests.get("https://www.google.com")
print(r.text)

# You can search request module on browser to see this external modules pip
