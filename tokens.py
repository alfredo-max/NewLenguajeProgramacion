import ply.lex as lex
from main import salida
palabrasReservadas = {
    "imprimir": "IMPRIMIR",
    "leer": "LEER",
    "numerico": "NUMERICO",
    "falso": "ESTADO",
    "verdadero": "ESTADO",
    "cadena": "CADENA",
    "caracter": "CARACTER",
    "si": "SI",
    "no": "NO",
    "mientras": "MIENTRAS",
    "para": "PARA",
    "haz":"HAZ"
}
ERROR2 = ""
# lista de tokens

tokens = (

    # Palabras Reservadas
    'NUMERICO',
    'ESTADO',
    'CADENA',
    'CARACTER',
    'SI',
    'NO',
    'IMPRIMIR',
    'LEER',
    'PARA',
    'MIENTRAS',
    'HAZ',
    # Symbolos
    'MAS',  # +
    'MENOS',  # -
    'MULTIPLICAR',  # *
    'DIVIDIR',  # /
    'MENOR',  # <
    'MENORIGUAL',  # <=
    'MAYOR',  # >
    'MAYORIGUAL',  # >=
    'ASIGNAR',  # =
    'IGUALDAD',  # ==
    'DISTINTO',  # !=
    'PUNTOYCOMA',  # ;
    'DOSPUNTOS',  #:
    'LPAREN',  # (
    'RPAREN',  # )
    'LBLOCK',  # {
    'RBLOCK',  # }
    'COMILLA',  # "
    'COMILLASIMPLE',  # '

    # Otros
    'ID',
    'COMENTARIOS'
)

# Reglas de Expresiones Regualres para token de Contexto simple
t_CADENA = r'\"[\w*\t*\n*\ *]+\"'
t_CARACTER = r"\'[a-zA-Z_0-9]\'"
t_NUMERICO = r'[0-9]+([.][0-9]+)?'

t_MAS = r'\+'
t_MENOS = r'-'
t_MULTIPLICAR = r'\*'
t_DIVIDIR = r'/'
t_ASIGNAR = r'='
t_MENOR = r'<'
t_MAYOR = r'>'
t_MENORIGUAL = r'<='
t_MAYORIGUAL = r'>='
t_IGUALDAD = r'=='
t_PUNTOYCOMA = '\;'
t_DOSPUNTOS = r'\:'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBLOCK = r'{'
t_RBLOCK = r'}'
t_ESTADO = r'verdadero|falso'
t_PARA = r'PARA'
t_MIENTRAS = r'MIENTRAS'
t_HAZ = r'HAZ'
t_COMENTARIOS = r'\*\*[\w*\t*\n*\ *[:punct:]*]+\*\*'
t_COMILLA = r'\"'
t_COMILLASIMPLE = r"\'"


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if (t.value in palabrasReservadas):
        t.type = palabrasReservadas[t.value]
    return t


t_IMPRIMIR = r'imprimir'
t_LEER = r'leer'
t_SI = r'SI'
t_NO = r'NO'
t_ignore = ' \t'  # Para ignorar los espacios


def t_error(t):
    print(f'Caracter ilegal {t.value[0]!r}')
    # return (f'Caracter ilegal {t.value[0]!r}')
    t.lexer.skip(1)

