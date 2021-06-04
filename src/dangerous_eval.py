import sys
import ast

def non_conformant_1(c):
    command = 'os.system("%s")' % c#23
    # expect finding: dangerous eval
    eval(command)

def non_conformant_2(command):
    # expect finding: dangerous eval
    eval(command)

def non_conformant_3():
    c = input()
    # expect finding: dangerous eval
    eval(c)

def non_conformant_4():
    c = sys.argv[0]
    # expect finding: dangerous eval
    eval(c)

def non_conformant_5():
    with open('file.txt') as f:
        for line in f:
            # expect finding: dangerous eval
            eval(line)

def conformant_1():
    c = '1 + 2'
    eval(c)

def conformant_3():
    c = input()
    ast.literal_eval(c)

def conformant_4():
    # expect finding: resource leak
    f = open('file.txt')
    command = f.read()
    ast.literal_eval(command)
