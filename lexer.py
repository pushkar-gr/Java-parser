import ply.lex as lex

reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'for': 'FOR',
    'while': 'WHILE',
    'return': 'RETURN',
    'int': 'INT',
    'void': 'VOID',
    'private': 'PRIVATE',
    'public' : 'PUBLIC',
    'static' : 'STATIC',
    'new' : 'NEW',
    'enum': 'ENUM',
}

tokens = [
    'ID',
    'NUMBER',
    'ASSIGN',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'SEMICOLON',
    'COMPARE',
    'ALG',
    'AND',
    'OR',
    'COMMA',
    'LBRACKET',
    'RBRACKET'
] + list(reserved.values())

t_ASSIGN = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMICOLON = r';'
t_AND = '&&'
t_OR = r'\|\|'
t_COMMA = r'\,'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_COMPARE(t):
    r'== | <= | >= | != | > | <'
    return t

def t_ALG(t):
    r'\+|\-|\*|\/'
    return t

t_ignore = ' \t\n'


def t_error(t):
    print(f"Illegal character {t.value[0]}")
    t.lexer.skip(1)


lexer = lex.lex()

