from tokens import *
from ply.yacc import yacc

a = ' a = 67+(97+5); para(a=(678+8); a<=68;  a\n=a+1; ){ **soy un comentario \n multilinea** a=67; haz {c = c+1;} mientras(c <= 67);}'
lexer = lex.lex()
lexer.input(a)

for tok in lexer:
    print(tok)


def p_statements_multiple(p):
    '''
    statements : statements statement
               | statements sentencia
               | sentencia
    '''


def p_statements_single(p):
    '''
    statements : statement
    '''


def p_asignamiento_statements(p):
    '''
    statement : asignacion
    '''
def p_comentario_statements(p):
    '''
    statement : COMENTARIOS
    '''

def p_asignar(p):
    '''
        asignacion : ID ASIGNAR expr PUNTOYCOMA
    '''


def p_tipodato(p):
    '''
    tipodato : NUMERICO
             | CARACTER
             | ESTADO
             | CADENA
    '''


def p_leer_statement(p):
    '''
    statement : LEER DOSPUNTOS expr
    '''


def p_imprimir_statement(p):
    '''
    statement : IMPRIMIR DOSPUNTOS expr
    '''


def p_expr_name(p):
    '''
    expr : ID
    '''

def p_expr_numerico(p):
    '''
    expr : NUMERICO
    '''


def p_expr_cadena(p):
    '''
    expr : CADENA
    '''


def p_expr_caracter(p):
    '''
    expr : CARACTER
    '''


def p_expr_estado(p):
    '''
    expr : ESTADO
    '''

def p_expr_opbin(p):
    '''
    expr : expr MAS expr
        | NUMERICO MULTIPLICAR NUMERICO
        | NUMERICO DIVIDIR NUMERICO
        | NUMERICO MENOS NUMERICO
    '''


def p_expr_group(p):
    '''
    expr : LPAREN expr RPAREN
    '''


def p_condiciones(p):
    '''
    condiciones : MENOR
                | MENORIGUAL
                | MAYOR
                | MAYORIGUAL
                | ASIGNAR
                | IGUALDAD
                | DISTINTO
    '''


def p_condicion(p):
    "condicion : expr condiciones expr"


def p_sentencia_si(p):
    """sentencia_si : SI LPAREN condicion RPAREN LBLOCK lista_sentencia RBLOCK
                    | SI LPAREN condicion RPAREN LBLOCK lista_sentencia RBLOCK NO  LBLOCK lista_sentencia RBLOCK
                    """


def p_sentencia_mientras(p):
    """
        sentencia_mientras : MIENTRAS LPAREN condicion RPAREN LBLOCK lista_sentencia RBLOCK
                          | HAZ LBLOCK lista_sentencia  RBLOCK MIENTRAS LPAREN condicion RPAREN PUNTOYCOMA
    """

def p_sentencia_para(p):
    "sentencia_para : PARA LPAREN asignacion condicion PUNTOYCOMA asignacion RPAREN LBLOCK lista_sentencia RBLOCK"



def p_sentencia(p):
    """sentencia :   sentencia_si
                    | sentencia_mientras
                    | sentencia_para
                    | statement
    """


def p_lista_sentencia(p):
    """lista_sentencia : lista_sentencia sentencia
                    | sentencia
    """


parser = yacc()
result = parser.parse(a)

print(result)