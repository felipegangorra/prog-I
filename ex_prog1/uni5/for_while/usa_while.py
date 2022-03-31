#!/bin/env python3
import sys
import ast

tree = ast.parse(open(sys.argv[1]).read())
tokens = set([type(tk) for tk in ast.walk(tree)])
summary = "." if ast.While in tokens else "D"
print(summary)
