from simbool.proposition import Prop
from simbool.simplify import simplify
import sys
def parseOr(expr):
    a=expr.split("|")
    result=Prop(False)
    for exp in a:
        result=result | parseAnd(exp)
    return result

def parseAnd(expr):
    expr=expr.replace("(","")
    expr=expr.replace(")","")
    a=expr.split("&")
    result=Prop(True)
    for exp in a:
        result=result & parseSingle(exp)

    return result

def parseSingle(exp):
    if (exp[0]=="~"):
        return ~ Prop(exp[1:])
    else:
        return Prop(exp)



f=open(sys.argv[1],'r')

expressions=f.readlines()
for expression in expressions:
    if(expression[0]=='#' or expression[0]=='*'):
        print(expression)
        continue
    if (len(expression)== 0 or  expression=='' or expression=='\n' or len(expression)== 1):
        continue
    if not (expression.find("False")==-1):
        continue
    if not (expression.find("abort")==-1): 
        print("abort")
        continue
    expression=expression.replace(" ","")

    print ('result',simplify(parseOr(expression)))

f.close()
