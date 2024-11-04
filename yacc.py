import ply.yacc as yacc
from lexer import tokens

def p_start(p): #start state
    """statement : expression
    | conditional_statements
    | function
    | forloops
    | whileloops
    """
    p[0] = p[1]

def p_empty(p):
    """empty :"""
    # p[0] = " "
    pass

def p_type(p): #data types
    """type : INT"""
    p[0] = p[1]

def p_expression(p): #expression for variable declaration (used in loops)
    """expression : type ID ASSIGN NUMBER SEMICOLON"""
    p[0] = f"{p[1]} {p[2]} {p[3]} {p[4]};"

def p_idornumber(p):
    """idornumber : ID
    | NUMBER
    """
    p[0] = p[1]

def p_condition(p): #conditinos for if statements (assuming an expression will result either true or false)
    """condition : condition COMPARE condition
    | condition AND condition
    | condition OR condition
    | idornumber
    | idornumber ALG idornumber
    """
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = f"{p[1]} {p[2]} {p[3]}"

def p_blabla(p): #random string for body of conditional statements/function/loops
    """blabla : ID blabla 
    | ID
    """
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = f"{p[1]}{p[2]}"

def p_blablablank(p):
    """blablablank : blabla
    | empty
    """
    if len(p) == 1:
        p[0] = ""
    else:
        p[0] = p[1]

def p_conditional_statements(p): #if statements
    """conditional_statements : IF LPAREN condition RPAREN LBRACE blabla RBRACE else"""
    p[0] = f"{p[1]} ({p[3]}) {p[5]}{p[6]}{p[7]} \n{p[8]}"

def p_else(p): #else and else if statements if required
    """else : ELSE conditional_statements 
    | ELSE LBRACE blabla RBRACE 
    | 
    """
    if len(p) == 1:
        p[0] = ""
    elif len(p) == 2:
        p[0] = p[1]
    elif len(p) == 3:
        p[0] = f"{p[1]} {p[2]}"
    else:
        p[0] = f"{p[1]} {p[2]}{p[3]}{p[4]}"

def p_parameters(p): #parameters for function
    """parameters : parameters COMMA parameters
    | blabla
    | 
    """
    if len(p) == 1:
        p[0] = ""
    elif len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = f"{p[1]}, {p[3]}"

def p_priv_pub_stat(p):
    """priv_pub_stat : PRIVATE STATIC
    | PUBLIC STATIC
    | PRIVATE
    | PUBLIC
    | STATIC
    | empty
    """
    if len(p) == 3:
        p[0] = f"{p[1]} {p[2]}"
    elif len(p) == 2:
        p[0] = f"private {p[1]}"
    else:
        p[0] = "private"

def p_function(p): #function (datatype name(parameters){body})
    """function : priv_pub_stat type blabla LPAREN parameters RPAREN LBRACE blablablank RETURN blabla RBRACE"""
    p[0] = f"{p[1]} {p[2]} {p[3]} ({p[5]})\n{p[7]}\n{p[8]}\n{p[9]} {p[10]}\n{p[11]}"


def p_exp(p):
    """exp : ID ASSIGN exp_"""
    p[0] = f"{p[1]} = {p[3]}"

def p_exp_(p):
    """exp_ : exp_ ALG exp_
    | idornumber
    """
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = f"{p[1]} {p[2]} {p[3]}"

def p_forloops(p):
    """forloops : FOR LPAREN expression condition SEMICOLON exp RPAREN LBRACE blablablank RBRACE"""
    p[0] = f"for ({p[3]}; {p[4]}; {p[6]})\n{p[8]} {p[9]} {p[10]}"

def p_whileloops(p):
    """whileloops : WHILE LPAREN condition RPAREN LBRACE blablablank RBRACE"""
    p[0] = f"while ({p[3]})\n{p[5]} {p[6]} {p[7]}"

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()

while True:
    try:
        data = input("Enter java expression: ")
    except EOFError:
        break

    if not data:
        continue

    result = parser.parse(data)
    print(result)
