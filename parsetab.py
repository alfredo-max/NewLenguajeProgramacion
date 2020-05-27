
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASIGNAR CADENA CARACTER COMENTARIOS COMILLA COMILLASIMPLE DISTINTO DIVIDIR DOSPUNTOS ESTADO HAZ ID IGUALDAD IMPRIMIR LBLOCK LEER LPAREN MAS MAYOR MAYORIGUAL MENOR MENORIGUAL MENOS MIENTRAS MULTIPLICAR NO NUMERICO PARA PUNTOYCOMA RBLOCK RPAREN SALTODELINEA SI\n        statements : statements statement\n                | statements sentencia\n                | sentencia\n        \n        statements : statement\n        \n        statement : asignacion\n        \n        statement : COMENTARIOS\n        \n            asignacion : ID ASIGNAR expr PUNTOYCOMA\n        \n        tipodato : NUMERICO\n                | CARACTER\n                | ESTADO\n                | CADENA\n        \n        statement : LEER DOSPUNTOS expr\n        \n        statement : IMPRIMIR DOSPUNTOS expr PUNTOYCOMA\n        \n        expr : ID\n        \n        expr : NUMERICO\n        \n        expr : CADENA\n        \n        expr : CARACTER\n        \n        expr : ESTADO\n        \n        expr : NUMERICO MAS NUMERICO\n            | NUMERICO MULTIPLICAR NUMERICO\n            | NUMERICO DIVIDIR NUMERICO\n            | NUMERICO MENOS NUMERICO\n            | ID MAS NUMERICO\n            | NUMERICO MAS ID\n            | ID MAS ID\n        \n        expr : LPAREN expr RPAREN\n        \n        condiciones : MENOR\n                    | MENORIGUAL\n                    | MAYOR\n                    | MAYORIGUAL\n                    | ASIGNAR\n                    | IGUALDAD\n                    | DISTINTO\n        condicion : expr condiciones exprsentencia_si : SI LPAREN condicion RPAREN LBLOCK lista_sentencia RBLOCK\n                        | SI LPAREN condicion RPAREN LBLOCK lista_sentencia RBLOCK NO  LBLOCK lista_sentencia RBLOCK\n        \n            sentencia_mientras : MIENTRAS LPAREN condicion RPAREN LBLOCK lista_sentencia RBLOCK\n                            | HAZ LBLOCK lista_sentencia  RBLOCK MIENTRAS LPAREN condicion RPAREN PUNTOYCOMA\n        sentencia_para : PARA LPAREN asignacion condicion PUNTOYCOMA asignacion RPAREN LBLOCK lista_sentencia RBLOCKsentencia :   sentencia_si\n                        | sentencia_mientras\n                        | sentencia_para\n                        | statement\n        lista_sentencia : lista_sentencia sentencia\n                        | sentencia\n        '
    
_lr_action_items = {'COMENTARIOS':([0,1,2,3,4,5,6,7,8,16,17,22,25,26,27,28,29,30,36,37,38,47,59,61,62,63,64,65,66,67,68,69,70,72,75,76,79,80,85,86,87,88,89,90,91,],[8,8,-4,-3,-40,-41,-42,-5,-6,-1,-2,8,-12,-14,-15,-16,-17,-18,8,-45,-43,-13,-44,-7,-25,-23,-19,-24,-20,-21,-22,-26,8,8,8,8,-35,-37,8,8,-38,8,8,-39,-36,]),'LEER':([0,1,2,3,4,5,6,7,8,16,17,22,25,26,27,28,29,30,36,37,38,47,59,61,62,63,64,65,66,67,68,69,70,72,75,76,79,80,85,86,87,88,89,90,91,],[9,9,-4,-3,-40,-41,-42,-5,-6,-1,-2,9,-12,-14,-15,-16,-17,-18,9,-45,-43,-13,-44,-7,-25,-23,-19,-24,-20,-21,-22,-26,9,9,9,9,-35,-37,9,9,-38,9,9,-39,-36,]),'IMPRIMIR':([0,1,2,3,4,5,6,7,8,16,17,22,25,26,27,28,29,30,36,37,38,47,59,61,62,63,64,65,66,67,68,69,70,72,75,76,79,80,85,86,87,88,89,90,91,],[10,10,-4,-3,-40,-41,-42,-5,-6,-1,-2,10,-12,-14,-15,-16,-17,-18,10,-45,-43,-13,-44,-7,-25,-23,-19,-24,-20,-21,-22,-26,10,10,10,10,-35,-37,10,10,-38,10,10,-39,-36,]),'SI':([0,1,2,3,4,5,6,7,8,16,17,22,25,26,27,28,29,30,36,37,38,47,59,61,62,63,64,65,66,67,68,69,70,72,75,76,79,80,85,86,87,88,89,90,91,],[11,11,-4,-3,-40,-41,-42,-5,-6,-1,-2,11,-12,-14,-15,-16,-17,-18,11,-45,-43,-13,-44,-7,-25,-23,-19,-24,-20,-21,-22,-26,11,11,11,11,-35,-37,11,11,-38,11,11,-39,-36,]),'MIENTRAS':([0,1,2,3,4,5,6,7,8,16,17,22,25,26,27,28,29,30,36,37,38,47,58,59,61,62,63,64,65,66,67,68,69,70,72,75,76,79,80,85,86,87,88,89,90,91,],[12,12,-4,-3,-40,-41,-42,-5,-6,-1,-2,12,-12,-14,-15,-16,-17,-18,12,-45,-43,-13,73,-44,-7,-25,-23,-19,-24,-20,-21,-22,-26,12,12,12,12,-35,-37,12,12,-38,12,12,-39,-36,]),'HAZ':([0,1,2,3,4,5,6,7,8,16,17,22,25,26,27,28,29,30,36,37,38,47,59,61,62,63,64,65,66,67,68,69,70,72,75,76,79,80,85,86,87,88,89,90,91,],[13,13,-4,-3,-40,-41,-42,-5,-6,-1,-2,13,-12,-14,-15,-16,-17,-18,13,-45,-43,-13,-44,-7,-25,-23,-19,-24,-20,-21,-22,-26,13,13,13,13,-35,-37,13,13,-38,13,13,-39,-36,]),'PARA':([0,1,2,3,4,5,6,7,8,16,17,22,25,26,27,28,29,30,36,37,38,47,59,61,62,63,64,65,66,67,68,69,70,72,75,76,79,80,85,86,87,88,89,90,91,],[14,14,-4,-3,-40,-41,-42,-5,-6,-1,-2,14,-12,-14,-15,-16,-17,-18,14,-45,-43,-13,-44,-7,-25,-23,-19,-24,-20,-21,-22,-26,14,14,14,14,-35,-37,14,14,-38,14,14,-39,-36,]),'ID':([0,1,2,3,4,5,6,7,8,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,36,37,38,39,41,42,47,49,50,51,52,53,54,55,56,59,61,62,63,64,65,66,67,68,69,70,72,74,75,76,77,79,80,85,86,87,88,89,90,91,],[15,15,-4,-3,-40,-41,-42,-5,-6,-1,-2,26,26,26,26,15,15,26,-12,-14,-15,-16,-17,-18,26,15,-45,-43,26,62,65,-13,26,-27,-28,-29,-30,-31,-32,-33,-44,-7,-25,-23,-19,-24,-20,-21,-22,-26,15,15,15,15,15,26,-35,-37,15,15,-38,15,15,-39,-36,]),'$end':([1,2,3,4,5,6,7,8,16,17,25,26,27,28,29,30,47,61,62,63,64,65,66,67,68,69,79,80,87,90,91,],[0,-4,-3,-40,-41,-42,-5,-6,-1,-2,-12,-14,-15,-16,-17,-18,-13,-7,-25,-23,-19,-24,-20,-21,-22,-26,-35,-37,-38,-39,-36,]),'RBLOCK':([4,5,6,7,8,25,26,27,28,29,30,36,37,38,47,59,61,62,63,64,65,66,67,68,69,75,76,79,80,87,88,89,90,91,],[-40,-41,-42,-5,-6,-12,-14,-15,-16,-17,-18,58,-45,-43,-13,-44,-7,-25,-23,-19,-24,-20,-21,-22,-26,79,80,-35,-37,-38,90,91,-39,-36,]),'DOSPUNTOS':([9,10,],[18,19,]),'LPAREN':([11,12,14,18,19,20,21,24,31,39,49,50,51,52,53,54,55,56,61,73,77,],[20,21,23,31,31,31,31,31,31,31,31,-27,-28,-29,-30,-31,-32,-33,-7,77,31,]),'LBLOCK':([13,48,57,82,83,],[22,70,72,85,86,]),'ASIGNAR':([15,26,27,28,29,30,34,62,63,64,65,66,67,68,69,],[24,-14,-15,-16,-17,-18,54,-25,-23,-19,-24,-20,-21,-22,-26,]),'NUMERICO':([18,19,20,21,24,31,39,41,42,43,44,45,49,50,51,52,53,54,55,56,61,77,],[27,27,27,27,27,27,27,63,64,66,67,68,27,-27,-28,-29,-30,-31,-32,-33,-7,27,]),'CADENA':([18,19,20,21,24,31,39,49,50,51,52,53,54,55,56,61,77,],[28,28,28,28,28,28,28,28,-27,-28,-29,-30,-31,-32,-33,-7,28,]),'CARACTER':([18,19,20,21,24,31,39,49,50,51,52,53,54,55,56,61,77,],[29,29,29,29,29,29,29,29,-27,-28,-29,-30,-31,-32,-33,-7,29,]),'ESTADO':([18,19,20,21,24,31,39,49,50,51,52,53,54,55,56,61,77,],[30,30,30,30,30,30,30,30,-27,-28,-29,-30,-31,-32,-33,-7,30,]),'PUNTOYCOMA':([26,27,28,29,30,32,40,60,62,63,64,65,66,67,68,69,71,84,],[-14,-15,-16,-17,-18,47,61,74,-25,-23,-19,-24,-20,-21,-22,-26,-34,87,]),'MENOR':([26,27,28,29,30,34,62,63,64,65,66,67,68,69,],[-14,-15,-16,-17,-18,50,-25,-23,-19,-24,-20,-21,-22,-26,]),'MENORIGUAL':([26,27,28,29,30,34,62,63,64,65,66,67,68,69,],[-14,-15,-16,-17,-18,51,-25,-23,-19,-24,-20,-21,-22,-26,]),'MAYOR':([26,27,28,29,30,34,62,63,64,65,66,67,68,69,],[-14,-15,-16,-17,-18,52,-25,-23,-19,-24,-20,-21,-22,-26,]),'MAYORIGUAL':([26,27,28,29,30,34,62,63,64,65,66,67,68,69,],[-14,-15,-16,-17,-18,53,-25,-23,-19,-24,-20,-21,-22,-26,]),'IGUALDAD':([26,27,28,29,30,34,62,63,64,65,66,67,68,69,],[-14,-15,-16,-17,-18,55,-25,-23,-19,-24,-20,-21,-22,-26,]),'DISTINTO':([26,27,28,29,30,34,62,63,64,65,66,67,68,69,],[-14,-15,-16,-17,-18,56,-25,-23,-19,-24,-20,-21,-22,-26,]),'RPAREN':([26,27,28,29,30,33,35,46,61,62,63,64,65,66,67,68,69,71,78,81,],[-14,-15,-16,-17,-18,48,57,69,-7,-25,-23,-19,-24,-20,-21,-22,-26,-34,82,84,]),'MAS':([26,27,],[41,42,]),'MULTIPLICAR':([27,],[43,]),'DIVIDIR':([27,],[44,]),'MENOS':([27,],[45,]),'NO':([79,],[83,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statements':([0,],[1,]),'statement':([0,1,22,36,70,72,75,76,85,86,88,89,],[2,16,38,38,38,38,38,38,38,38,38,38,]),'sentencia':([0,1,22,36,70,72,75,76,85,86,88,89,],[3,17,37,59,37,37,59,59,37,37,59,59,]),'sentencia_si':([0,1,22,36,70,72,75,76,85,86,88,89,],[4,4,4,4,4,4,4,4,4,4,4,4,]),'sentencia_mientras':([0,1,22,36,70,72,75,76,85,86,88,89,],[5,5,5,5,5,5,5,5,5,5,5,5,]),'sentencia_para':([0,1,22,36,70,72,75,76,85,86,88,89,],[6,6,6,6,6,6,6,6,6,6,6,6,]),'asignacion':([0,1,22,23,36,70,72,74,75,76,85,86,88,89,],[7,7,7,39,7,7,7,78,7,7,7,7,7,7,]),'expr':([18,19,20,21,24,31,39,49,77,],[25,32,34,34,40,46,34,71,34,]),'condicion':([20,21,39,77,],[33,35,60,81,]),'lista_sentencia':([22,70,72,85,86,],[36,75,76,88,89,]),'condiciones':([34,],[49,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statements","S'",1,None,None,None),
  ('statements -> statements statement','statements',2,'p_statements_multiple','grammar.py',18),
  ('statements -> statements sentencia','statements',2,'p_statements_multiple','grammar.py',19),
  ('statements -> sentencia','statements',1,'p_statements_multiple','grammar.py',20),
  ('statements -> statement','statements',1,'p_statements_single','grammar.py',30),
  ('statement -> asignacion','statement',1,'p_asignamiento_statements','grammar.py',37),
  ('statement -> COMENTARIOS','statement',1,'p_comentario_statements','grammar.py',44),
  ('asignacion -> ID ASIGNAR expr PUNTOYCOMA','asignacion',4,'p_asignar','grammar.py',50),
  ('tipodato -> NUMERICO','tipodato',1,'p_tipodato','grammar.py',58),
  ('tipodato -> CARACTER','tipodato',1,'p_tipodato','grammar.py',59),
  ('tipodato -> ESTADO','tipodato',1,'p_tipodato','grammar.py',60),
  ('tipodato -> CADENA','tipodato',1,'p_tipodato','grammar.py',61),
  ('statement -> LEER DOSPUNTOS expr','statement',3,'p_leer_statement','grammar.py',67),
  ('statement -> IMPRIMIR DOSPUNTOS expr PUNTOYCOMA','statement',4,'p_imprimir_statement','grammar.py',74),
  ('expr -> ID','expr',1,'p_expr_name','grammar.py',82),
  ('expr -> NUMERICO','expr',1,'p_expr_numerico','grammar.py',88),
  ('expr -> CADENA','expr',1,'p_expr_cadena','grammar.py',94),
  ('expr -> CARACTER','expr',1,'p_expr_caracter','grammar.py',100),
  ('expr -> ESTADO','expr',1,'p_expr_estado','grammar.py',106),
  ('expr -> NUMERICO MAS NUMERICO','expr',3,'p_expr_opbin','grammar.py',112),
  ('expr -> NUMERICO MULTIPLICAR NUMERICO','expr',3,'p_expr_opbin','grammar.py',113),
  ('expr -> NUMERICO DIVIDIR NUMERICO','expr',3,'p_expr_opbin','grammar.py',114),
  ('expr -> NUMERICO MENOS NUMERICO','expr',3,'p_expr_opbin','grammar.py',115),
  ('expr -> ID MAS NUMERICO','expr',3,'p_expr_opbin','grammar.py',116),
  ('expr -> NUMERICO MAS ID','expr',3,'p_expr_opbin','grammar.py',117),
  ('expr -> ID MAS ID','expr',3,'p_expr_opbin','grammar.py',118),
  ('expr -> LPAREN expr RPAREN','expr',3,'p_expr_group','grammar.py',127),
  ('condiciones -> MENOR','condiciones',1,'p_condiciones','grammar.py',134),
  ('condiciones -> MENORIGUAL','condiciones',1,'p_condiciones','grammar.py',135),
  ('condiciones -> MAYOR','condiciones',1,'p_condiciones','grammar.py',136),
  ('condiciones -> MAYORIGUAL','condiciones',1,'p_condiciones','grammar.py',137),
  ('condiciones -> ASIGNAR','condiciones',1,'p_condiciones','grammar.py',138),
  ('condiciones -> IGUALDAD','condiciones',1,'p_condiciones','grammar.py',139),
  ('condiciones -> DISTINTO','condiciones',1,'p_condiciones','grammar.py',140),
  ('condicion -> expr condiciones expr','condicion',3,'p_condicion','grammar.py',152),
  ('sentencia_si -> SI LPAREN condicion RPAREN LBLOCK lista_sentencia RBLOCK','sentencia_si',7,'p_sentencia_si','grammar.py',162),
  ('sentencia_si -> SI LPAREN condicion RPAREN LBLOCK lista_sentencia RBLOCK NO LBLOCK lista_sentencia RBLOCK','sentencia_si',11,'p_sentencia_si','grammar.py',163),
  ('sentencia_mientras -> MIENTRAS LPAREN condicion RPAREN LBLOCK lista_sentencia RBLOCK','sentencia_mientras',7,'p_sentencia_mientras','grammar.py',181),
  ('sentencia_mientras -> HAZ LBLOCK lista_sentencia RBLOCK MIENTRAS LPAREN condicion RPAREN PUNTOYCOMA','sentencia_mientras',9,'p_sentencia_mientras','grammar.py',182),
  ('sentencia_para -> PARA LPAREN asignacion condicion PUNTOYCOMA asignacion RPAREN LBLOCK lista_sentencia RBLOCK','sentencia_para',10,'p_sentencia_para','grammar.py',188),
  ('sentencia -> sentencia_si','sentencia',1,'p_sentencia','grammar.py',202),
  ('sentencia -> sentencia_mientras','sentencia',1,'p_sentencia','grammar.py',203),
  ('sentencia -> sentencia_para','sentencia',1,'p_sentencia','grammar.py',204),
  ('sentencia -> statement','sentencia',1,'p_sentencia','grammar.py',205),
  ('lista_sentencia -> lista_sentencia sentencia','lista_sentencia',2,'p_lista_sentencia','grammar.py',210),
  ('lista_sentencia -> sentencia','lista_sentencia',1,'p_lista_sentencia','grammar.py',211),
]
