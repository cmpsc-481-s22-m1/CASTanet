# Team: BCM
# Members: Bailey Matrascia, Jordan Byrne, Pedro Carmo

# ------------------------------------------------------------------------------
# Grammar Rules:
#
# Statements can generate single statements or
# statements that lead into more statements.
#
# Single Statements can be identifiers(ID) set equal(EQUALS)
# to and expression or a print statement (PRINT) using parenthesis.
#
# Expressions can be numerical sums, subtractions, divisions, multiplications,
# modulo, or exponential.
# ------------------------------------------------------------------------------

from sly import Lexer, Parser

class MyLexer(Lexer):
    # Add tokens and definitions

    tokens = {
        ID,
        INT,
        EQ,
        NOTEQ,
        PRINT,
        ADDITION,
        SUBTRACTION,
        DIVISION,
        MULTIPLICATION,
        MODULO,
        POWER,
        LPAREN,
        RPAREN,
        PERCENTAGE,
        RANDOM,
        GREATERTN,
        LESSTN
    }

    # the ignore variable is used to tell
    # the parser to skip spaces

    ignore = ' \t'

    ID = r'[a-z_][0-9_]*'
    INT = r'[0-9]+'
    EQ = r'EQUALS'
    NOTEQ = r'DOES_NOT_EQUAL'
    ID['PRINT'] = PRINT

    # Mathematical operators defined
    ADDITION = r'PLUS'
    SUBTRACTION = r'MINUS'
    DIVISION = r'DIVIDED_BY'
    MULTIPLICATION = r'TIMES'
    MODULO = r'MODULO'
    POWER = r'TO_THE'
    PERCENTAGE = r'PERCENTAGE_OF'
    RANDOM = r'RANDOM_NUMBER'

    # Symbols defined
    LPAREN = r'\('
    RPAREN = r'\)'
    GREATERTN = r'GREATER_THAN'
    LESSTN = r'LESS_THAN'


    def INT(self, t):
        t.value = int(t.value)
        return t

class MyParser(Parser):
    tokens = MyLexer.tokens
    debugging_file = 'parser.out'

    # Add rules

    # Basic token rules.

    @_('expr')
    def statement(self, p):
        return [ p.expr ]

    @_('rval')
    def expr(self, p):
        return (p.rval)

    # expr -> Addition
    @_('ADDITION')
    def expr(self, p):
        return ('Add', p.ADDITION)

    # expr -> Subtraction
    @_('SUBTRACTION')
    def expr(self, p):
        return ('Subtract', p.SUBTRACTION)

    # expr -> Division
    @_('DIVISION')
    def expr(self, p):
        return ('Divide', p.DIVISION)

    # expr -> Multiplication
    @_('MULTIPLICATION')
    def expr(self, p):
        return ('Multiply', p.MULTIPLICATION)

    @_('ADDITION SUBTRACTION')
    def rval(self, p):
        return (p[1], p.PLUS, p.MINUS)

    # expr -> Modulo
    @_('MODULO')
    def expr(self, p):
        return ('Modulo', p.MODULO)

    # expr -> Power
    @_('POWER')
    def expr(self, p):
        return ('Power', p.POWER)

    # expr -> Percentage
    @_('PERCENTAGE')
    def expr(self, p):
        return ('Percentage', p.PERCENTAGE)

    # expr -> Random
    @_('RANDOM')
    def expr(self, p):
        return ('Random', p.RANDOM)

if __name__ == '__main__':
    lexer = MyLexer()
    parser = MyParser()

    for token in lexer.tokenize(input('INSERT FORMULA: \n' )):
        print('type=%r, value=%r' % (token.type, token.value))
