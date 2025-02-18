import ast

class Analiz_Cody(ast.NodeVisitor):
    def __init__(self):
        self.funkcii = []
        self.rahynok_ifok = 0
        self.rahynok_forok = 0
        self.rahynok_while = 0
        self.rahynok_operatoriv_prusvoennya = 0

    def visit_FunctionDef(self, node):
        func_name = node.name
        args = [arg.arg for arg in node.args.args]
        self.funkcii.append((func_name, args))
        self.generic_visit(node)


    def visit_If(self, node):
        self.rahynok_ifok += 1
        self.generic_visit(node)

    def visit_For(self, node):
        self.rahynok_forok += 1
        self.generic_visit(node)

    def visit_While(self, node):
        self.rahynok_while += 1
        self.generic_visit(node)

    def visit_Assign(self, node):
        self.rahynok_operatoriv_prusvoennya += 1
        self.generic_visit(node)

def analyze_code(code):
    tree = ast.parse(code)
    analiz = Analiz_Cody()
    analiz.visit(tree)
    print("Функції та їх аргументи:")
    for funciya_name, args in analiz.funkcii:
        print(f"Функція: {funciya_name}, Аргументи: {args}")

    print("\nКількість умовних операторів (if):", analiz.rahynok_ifok)
    print("Кількість циклів for:", analiz.rahynok_forok)
    print("Кількість циклів while:", analiz.rahynok_while)
    print("Кількість операторів `=` :", analiz.rahynok_operatoriv_prusvoennya)

cod = """
def funciya(a, b):
    x = 10
    if a > b:
        print("a більше b")
    else:
        print("b більше а")

    for i in range(10):
        print(i)

    while x > 0:
        x -= 1

def insha_funciya(c):
    y = c * 2
    return y
"""

analyze_code(cod)