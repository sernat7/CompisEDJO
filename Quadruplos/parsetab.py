
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'LT EQ GT NE LE GE ASSIGN PLUSPLUS MINUSMINUS PLUS MINUS MULT DIV LPAREN RPAREN LBRACKET RBRACKET SLBRACKET SRBRACKET SEMICOLON COMMA IF ELSE IFELSE INT DECIMAL STRING CHAR BOOL PRINT START EDJO VOID RETURN MAIN FOR VAR_ID VAR_INT VAR_DECIMAL VAR_CHAR VAR_STRING TRUE FALSE DO WHILE FROM IMPORT POINT POS FORWARD CIRCLE LEFT RIGHT TUR TURTLE ZERO RET FUNCprogram\t:\tSTART EDJO VAR_ID crea_primer_quadruple crea_funcion_global SEMICOLON Vars funciones Main\n\tcrea_primer_quadruple\t: \n\tcrea_funcion_global\t: \n\tVars\t\t:\tTipo VAR_ID mas_vars agrega_var_funcion SEMICOLON Vars\n\t\t\t| \n\tTipo\t\t:\tINT\n\t\t\t|\tDECIMAL\n\t\t\t|\tSTRING\n\t\t\t|\tCHAR\n\t\t\t|\tBOOL\n\tmas_vars\t:\tCOMMA VAR_ID mas_vars\n\t\t\t| \n\tagrega_var_funcion\t: \n\tAsignacion\t:\tVAR_ID push_var_PilaOperandos ASSIGN push_operador_PilaOperadores ExpI SEMICOLON resuelve_asignacion\n\tpush_var_PilaOperandos\t: \n\tpush_operador_PilaOperadores\t: \n\tresuelve_asignacion\t: \n\tExpI\t\t:\tExpK resuelve_operadores_relacionales \n\t\t\t|\tExpK Operandos push_operador_PilaOperadores ExpK resuelve_operadores_relacionales\n\tOperandos\t:\tLT\n\t\t\t|\tGT\n\t\t\t|\tNE\n\t\t\t|\tLE\n\t\t\t|\tGE\n\t\t\t|\tEQ\n\tresuelve_operadores_relacionales\t: \n\tExpK\t\t:\tExpT resuelve_termino \n\t\t\t|\tExpT resuelve_termino pos_SUMRES push_operador_PilaOperadores ExpK\n\tresuelve_termino\t: \n\tpos_SUMRES\t:\tPLUS \n\t\t\t|\tMINUS \n\tExpT\t\t:\tExpF resuelve_factor \n\t\t\t|\tExpF resuelve_factor pos_MULTDIV push_operador_PilaOperadores ExpT\n\tresuelve_factor\t: \n\tpos_MULTDIV\t:\tMULT \n\t\t\t|\tDIV \n\tExpF\t\t:\tVAR_CTE\n\t\t\t|\tLPAREN agrega_falso ExpI RPAREN quita_falso\n\t\t\t|\tVAR_ID push_var_PilaOperandos pos_arreglo\n\t\t\t|\tllama_funcion \n\tVAR_CTE\t:\tVAR_INT push_int_PilaOperandos\n\t\t\t|\tVAR_DECIMAL push_decimal_PilaOperandos\n\tpush_int_PilaOperandos\t:\n\tpush_decimal_PilaOperandos\t: \n\tagrega_falso\t: \n\tquita_falso\t: \n\tllama_funcion\t:\tVAR_ID LPAREN agrega_falso checa_funcion_si_existe argumentos RPAREN quita_falso resuelve_llamada_funcion guarda_resultado_funcion\n\tcheca_funcion_si_existe\t: \n\targumentos\t:\tExpI resuelve_argumentos mas_argumentos\n\t\t\t| \n\tmas_argumentos\t: \tCOMMA ExpI resuelve_argumentos mas_argumentos\n\t\t\t\t| \n\tresuelve_argumentos\t: \n\tresuelve_llamada_funcion\t: \n\tguarda_resultado_funcion\t: \n\tpos_arreglo\t:\tSLBRACKET ExpI SRBRACKET\n\t\t\t| \n\tfunciones\t:\tFUNC tipo_funcion VAR_ID LPAREN param RPAREN agrega_funcion LBRACKET Vars reg_brack RBRACKET fin_func_quad funciones\n\t\t\t| \n\ttipo_funcion\t:\tVOID\n\t\t\t|\tTipo\n\tparam\t:\tTipo VAR_ID pos_commaf\n\t\t\t| \n\tpos_commaf\t:\tCOMMA Tipo VAR_ID pos_commaf\n\t\t\t| \n\tagrega_funcion\t: \n\tfin_func_quad\t: \n\treg_brack\t:\tEstatutos reg_brack\n\t\t\t| \n\tEstatutos\t:\tCondicion \n\t\t\t|\tCiclo  \n\t\t\t|\tReturn \n\t\t\t|\tAsignacion\n\t\t\t|\tPrint \n\t\t\t|\tLlamada_Func \n\t\t\t|\tTurtleMotion \n\tCondicion\t:\tIF LPAREN ExpI RPAREN crea_GOTOF LBRACKET reg_brack RBRACKET pos_else llena_cuadruplo_if\n\tcrea_GOTOF\t: \n\tllena_cuadruplo_if\t: \n\tpos_else\t:\tELSE crea_else_cuadruplo LBRACKET reg_brack RBRACKET\n\t\t\t| \n\tcrea_else_cuadruplo\t: \n\tReturn \t:\tRETURN ExpI SEMICOLON resuelve_return\n\tresuelve_return\t: \n\tPrint\t:\tPRINT LPAREN VAR_STRING RPAREN SEMICOLON\n\t\t\t|\tPRINT LPAREN ExpI RPAREN SEMICOLON crea_print\n\tcrea_print\t: \n\tLlamada_Func\t:\tVAR_ID LPAREN agrega_falso checa_funcion_si_existe argumentos RPAREN quita_falso resuelve_llamada_funcion SEMICOLON vtc_action\n\tvtc_action\t: \n\tCiclo\t:\tFor\n\t\t\t|\tWhile\n\t\t\t|\tDoWhile\n\tWhile\t:\tWHILE guarda_numero_cuadruplo LPAREN ExpI RPAREN crea_GOTOF LBRACKET reg_brack RBRACKET regresa_inicio_while\n\tguarda_numero_cuadruplo\t: \n\tregresa_inicio_while\t: \n\tDoWhile\t:\tDO LBRACKET reg_brack RBRACKET WHILE LPAREN ExpI RPAREN SEMICOLON\n\tFor\t\t:\tFOR LPAREN VAR_ID ASSIGN ExpI SEMICOLON ExpI SEMICOLON VAR_ID Exp_ciclo RPAREN LBRACKET reg_brack RBRACKET\n\tExp_ciclo\t:\tPLUS VAR_INT\n\t\t\t|\tMINUS VAR_INT\n\t\t\t|\tMULT VAR_INT\n\t\t\t|\tDIV VAR_INT\n\t\t\t|\tPLUSPLUS\n\t\t\t|\tMINUSMINUS\n\tTurtleMotion\t:\tPosition\n\t\t\t|\tRight\n\t\t\t|\tLeft\n\t\t\t|\tForward\n\t\t\t|\tCircle\n\tPosition\t:\tVAR_ID POINT POS LPAREN RPAREN SEMICOLON\n\tForward\t:\tVAR_ID POINT FORWARD LPAREN ExpI RPAREN SEMICOLON\n\tRight\t:\tVAR_ID POINT RIGHT LPAREN ExpI RPAREN SEMICOLON\n\tLeft\t\t:\tVAR_ID POINT LEFT LPAREN ExpI RPAREN SEMICOLON\n\tCircle\t:\tVAR_ID POINT CIRCLE LPAREN ExpI RPAREN SEMICOLON\n\tMain\t\t:\tMAIN agrega_main_funcion LPAREN RPAREN LBRACKET Vars reg_brack RET ZERO SEMICOLON RBRACKET\n\tagrega_main_funcion\t: \n\t'
    
_lr_action_items = {'FOR':([32,36,39,43,45,46,47,48,49,50,51,52,54,55,56,58,59,60,67,68,69,71,74,115,142,152,153,174,176,189,190,195,198,199,200,201,202,207,213,214,216,219,221,223,232,234,241,242,244,],[-5,-4,-5,63,-5,-108,-75,-92,-90,-91,63,-74,-105,-107,-71,-72,-106,-73,-70,-104,-76,63,63,-84,-83,-85,-87,-86,63,-109,-17,63,-110,-112,-113,-111,-14,-81,-96,-79,-95,-89,-77,-93,-88,63,63,-80,-97,]),'RBRACKET':([32,36,45,46,47,48,49,50,51,52,54,55,56,58,59,60,67,68,69,71,72,74,93,96,115,142,143,152,153,174,176,189,190,194,195,198,199,200,201,202,207,208,213,214,216,219,221,223,232,234,240,241,242,243,244,],[-5,-4,-5,-108,-75,-92,-90,-91,-69,-74,-105,-107,-71,-72,-106,-73,-70,-104,-76,-69,-68,-69,124,127,-84,-83,164,-85,-87,-86,-69,-109,-17,207,-69,-110,-112,-113,-111,-14,-81,216,-96,-79,-95,-89,-77,-93,-88,-69,242,-69,-80,244,-97,]),'BOOL':([7,15,29,32,39,41,45,],[11,11,11,11,11,11,11,]),'MULT':([80,82,83,84,85,86,110,111,113,114,140,160,181,184,197,210,217,218,231,],[-37,-34,-43,-40,-15,-44,137,-41,-57,-42,-39,-46,-38,-56,-46,-54,226,-55,-47,]),'INT':([7,15,29,32,39,41,45,],[9,9,9,9,9,9,9,]),'PLUS':([79,80,82,83,84,85,86,108,110,111,113,114,140,160,181,182,184,197,210,217,218,231,],[-29,-37,-34,-43,-40,-15,-44,134,-32,-41,-57,-42,-39,-46,-38,-33,-56,-46,-54,229,-55,-47,]),'DECIMAL':([7,15,29,32,39,41,45,],[8,8,8,8,8,8,8,]),'FUNC':([7,10,32,36,124,151,],[-5,15,-5,-4,-67,15,]),'GT':([78,79,80,82,83,84,85,86,108,110,111,113,114,140,160,180,181,182,184,197,210,218,231,],[103,-29,-37,-34,-43,-40,-15,-44,-27,-32,-41,-57,-42,-39,-46,-28,-38,-33,-56,-46,-54,-55,-47,]),'VAR_STRING':([73,],[94,]),'VOID':([15,],[20,]),'GE':([78,79,80,82,83,84,85,86,108,110,111,113,114,140,160,180,181,182,184,197,210,218,231,],[104,-29,-37,-34,-43,-40,-15,-44,-27,-32,-41,-57,-42,-39,-46,-28,-38,-33,-56,-46,-54,-55,-47,]),'PRINT':([32,36,39,43,45,46,47,48,49,50,51,52,54,55,56,58,59,60,67,68,69,71,74,115,142,152,153,174,176,189,190,195,198,199,200,201,202,207,213,214,216,219,221,223,232,234,241,242,244,],[-5,-4,-5,53,-5,-108,-75,-92,-90,-91,53,-74,-105,-107,-71,-72,-106,-73,-70,-104,-76,53,53,-84,-83,-85,-87,-86,53,-109,-17,53,-110,-112,-113,-111,-14,-81,-96,-79,-95,-89,-77,-93,-88,53,53,-80,-97,]),'LEFT':([89,],[118,]),'LBRACKET':([35,38,42,57,128,155,156,177,215,222,237,],[39,-66,45,74,-78,176,-78,195,-82,234,241,]),'STRING':([7,15,29,32,39,41,45,],[13,13,13,13,13,13,13,]),'$end':([2,21,164,],[0,-1,-114,]),'START':([0,],[1,]),'MINUSMINUS':([217,],[225,]),'ZERO':([88,],[116,]),'ASSIGN':([66,90,99,],[-15,122,130,]),'SEMICOLON':([4,5,6,17,24,27,28,31,78,79,80,82,83,84,85,86,87,100,108,110,111,113,114,116,125,126,140,157,158,160,169,170,179,180,181,182,184,185,186,187,188,191,196,197,203,206,210,211,218,231,],[-2,-3,7,-12,-13,-12,32,-11,-26,-29,-37,-34,-43,-40,-15,-44,115,-18,-27,-32,-41,-57,-42,143,152,153,-39,178,-26,-46,189,190,-19,-28,-38,-33,-56,198,199,200,201,-46,209,-46,-54,213,-54,219,-55,-47,]),'PLUSPLUS':([217,],[227,]),'SRBRACKET':([78,79,80,82,83,84,85,86,100,108,110,111,113,114,140,158,160,163,179,180,181,182,184,197,210,218,231,],[-26,-29,-37,-34,-43,-40,-15,-44,-18,-27,-32,-41,-57,-42,-39,-26,-46,184,-19,-28,-38,-33,-56,-46,-54,-55,-47,]),'COMMA':([17,27,37,70,78,79,80,82,83,84,85,86,100,108,110,111,113,114,140,158,160,172,179,180,181,182,184,192,197,210,212,218,220,231,],[23,23,41,41,-26,-29,-37,-34,-43,-40,-15,-44,-18,-27,-32,-41,-57,-42,-39,-26,-46,-53,-19,-28,-38,-33,-56,204,-46,-54,-53,-55,204,-47,]),'SLBRACKET':([85,113,],[-15,141,]),'DO':([32,36,39,43,45,46,47,48,49,50,51,52,54,55,56,58,59,60,67,68,69,71,74,115,142,152,153,174,176,189,190,195,198,199,200,201,202,207,213,214,216,219,221,223,232,234,241,242,244,],[-5,-4,-5,57,-5,-108,-75,-92,-90,-91,57,-74,-105,-107,-71,-72,-106,-73,-70,-104,-76,57,57,-84,-83,-85,-87,-86,57,-109,-17,57,-110,-112,-113,-111,-14,-81,-96,-79,-95,-89,-77,-93,-88,57,57,-80,-97,]),'LE':([78,79,80,82,83,84,85,86,108,110,111,113,114,140,160,180,181,182,184,197,210,218,231,],[106,-29,-37,-34,-43,-40,-15,-44,-27,-32,-41,-57,-42,-39,-46,-28,-38,-33,-56,-46,-54,-55,-47,]),'NE':([78,79,80,82,83,84,85,86,108,110,111,113,114,140,160,180,181,182,184,197,210,218,231,],[107,-29,-37,-34,-43,-40,-15,-44,-27,-32,-41,-57,-42,-39,-46,-28,-38,-33,-56,-46,-54,-55,-47,]),'RET':([32,36,39,43,46,47,48,49,50,51,52,54,55,56,58,59,60,65,67,68,69,72,115,142,152,153,174,189,190,198,199,200,201,202,207,213,214,216,219,221,223,232,242,244,],[-5,-4,-5,-69,-108,-75,-92,-90,-91,-69,-74,-105,-107,-71,-72,-106,-73,88,-70,-104,-76,-68,-84,-83,-85,-87,-86,-109,-17,-110,-112,-113,-111,-14,-81,-96,-79,-95,-89,-77,-93,-88,-80,-97,]),'LPAREN':([22,25,26,53,61,62,63,64,66,73,75,76,81,85,91,98,101,102,103,104,105,106,107,109,112,117,118,119,120,121,122,123,130,131,132,133,134,136,137,138,139,141,144,145,146,147,149,150,154,159,161,162,175,178,204,],[-115,29,30,73,75,-94,77,81,91,81,81,98,-45,112,-45,81,-20,-16,-21,-24,-25,-23,-22,81,-45,144,145,146,147,148,-16,-48,81,81,-16,-31,-30,-36,-35,-16,-48,81,81,81,81,81,81,81,175,81,81,81,81,81,81,]),'RPAREN':([29,30,34,37,40,70,78,79,80,82,83,84,85,86,91,92,94,95,97,100,108,110,111,112,113,114,123,129,135,139,140,148,150,158,160,162,165,166,167,168,171,172,179,180,181,182,183,184,192,193,197,205,210,212,218,220,225,227,228,231,233,235,236,238,239,],[-63,35,38,-65,-62,-65,-26,-29,-37,-34,-43,-40,-15,-44,-45,-64,125,126,128,-18,-27,-32,-41,-45,-57,-42,-48,156,160,-48,-39,169,-50,-26,-46,-50,185,186,187,188,191,-53,-19,-28,-38,-33,197,-56,-52,206,-46,-49,-54,-53,-55,-52,-103,-102,237,-47,-51,-101,-100,-98,-99,]),'MAIN':([7,10,16,32,36,124,151,173,],[-5,-59,22,-5,-4,-67,-59,-58,]),'DIV':([80,82,83,84,85,86,110,111,113,114,140,160,181,184,197,210,217,218,231,],[-37,-34,-43,-40,-15,-44,136,-41,-57,-42,-39,-46,-38,-56,-46,-54,224,-55,-47,]),'VAR_DECIMAL':([64,73,75,81,91,98,101,102,103,104,105,106,107,109,112,122,123,130,131,132,133,134,136,137,138,139,141,144,145,146,147,149,150,159,161,162,175,178,204,],[86,86,86,-45,-45,86,-20,-16,-21,-24,-25,-23,-22,86,-45,-16,-48,86,86,-16,-31,-30,-36,-35,-16,-48,86,86,86,86,86,86,86,86,86,86,86,86,86,]),'IF':([32,36,39,43,45,46,47,48,49,50,51,52,54,55,56,58,59,60,67,68,69,71,74,115,142,152,153,174,176,189,190,195,198,199,200,201,202,207,213,214,216,219,221,223,232,234,241,242,244,],[-5,-4,-5,61,-5,-108,-75,-92,-90,-91,61,-74,-105,-107,-71,-72,-106,-73,-70,-104,-76,61,61,-84,-83,-85,-87,-86,61,-109,-17,61,-110,-112,-113,-111,-14,-81,-96,-79,-95,-89,-77,-93,-88,61,61,-80,-97,]),'EQ':([78,79,80,82,83,84,85,86,108,110,111,113,114,140,160,180,181,182,184,197,210,218,231,],[105,-29,-37,-34,-43,-40,-15,-44,-27,-32,-41,-57,-42,-39,-46,-28,-38,-33,-56,-46,-54,-55,-47,]),'LT':([78,79,80,82,83,84,85,86,108,110,111,113,114,140,160,180,181,182,184,197,210,218,231,],[101,-29,-37,-34,-43,-40,-15,-44,-27,-32,-41,-57,-42,-39,-46,-28,-38,-33,-56,-46,-54,-55,-47,]),'VAR_INT':([64,73,75,81,91,98,101,102,103,104,105,106,107,109,112,122,123,130,131,132,133,134,136,137,138,139,141,144,145,146,147,149,150,159,161,162,175,178,204,224,226,229,230,],[83,83,83,-45,-45,83,-20,-16,-21,-24,-25,-23,-22,83,-45,-16,-48,83,83,-16,-31,-30,-36,-35,-16,-48,83,83,83,83,83,83,83,83,83,83,83,83,83,235,236,238,239,]),'CIRCLE':([89,],[119,]),'RETURN':([32,36,39,43,45,46,47,48,49,50,51,52,54,55,56,58,59,60,67,68,69,71,74,115,142,152,153,174,176,189,190,195,198,199,200,201,202,207,213,214,216,219,221,223,232,234,241,242,244,],[-5,-4,-5,64,-5,-108,-75,-92,-90,-91,64,-74,-105,-107,-71,-72,-106,-73,-70,-104,-76,64,64,-84,-83,-85,-87,-86,64,-109,-17,64,-110,-112,-113,-111,-14,-81,-96,-79,-95,-89,-77,-93,-88,64,64,-80,-97,]),'POINT':([66,],[89,]),'CHAR':([7,15,29,32,39,41,45,],[12,12,12,12,12,12,12,]),'FORWARD':([89,],[117,]),'VAR_ID':([3,8,9,11,12,13,14,18,19,20,23,32,33,36,39,43,44,45,46,47,48,49,50,51,52,54,55,56,58,59,60,64,67,68,69,71,73,74,75,77,81,91,98,101,102,103,104,105,106,107,109,112,115,122,123,130,131,132,133,134,136,137,138,139,141,142,144,145,146,147,149,150,152,153,159,161,162,174,175,176,178,189,190,195,198,199,200,201,202,204,207,209,213,214,216,219,221,223,232,234,241,242,244,],[4,-7,-6,-10,-9,-8,17,-61,25,-60,27,-5,37,-4,-5,66,70,-5,-108,-75,-92,-90,-91,66,-74,-105,-107,-71,-72,-106,-73,85,-70,-104,-76,66,85,66,85,99,-45,-45,85,-20,-16,-21,-24,-25,-23,-22,85,-45,-84,-16,-48,85,85,-16,-31,-30,-36,-35,-16,-48,85,-83,85,85,85,85,85,85,-85,-87,85,85,85,-86,85,66,85,-109,-17,66,-110,-112,-113,-111,-14,85,-81,217,-96,-79,-95,-89,-77,-93,-88,66,66,-80,-97,]),'RIGHT':([89,],[120,]),'ELSE':([207,],[215,]),'EDJO':([1,],[3,]),'WHILE':([32,36,39,43,45,46,47,48,49,50,51,52,54,55,56,58,59,60,67,68,69,71,74,115,127,142,152,153,174,176,189,190,195,198,199,200,201,202,207,213,214,216,219,221,223,232,234,241,242,244,],[-5,-4,-5,62,-5,-108,-75,-92,-90,-91,62,-74,-105,-107,-71,-72,-106,-73,-70,-104,-76,62,62,-84,154,-83,-85,-87,-86,62,-109,-17,62,-110,-112,-113,-111,-14,-81,-96,-79,-95,-89,-77,-93,-88,62,62,-80,-97,]),'MINUS':([79,80,82,83,84,85,86,108,110,111,113,114,140,160,181,182,184,197,210,217,218,231,],[-29,-37,-34,-43,-40,-15,-44,133,-32,-41,-57,-42,-39,-46,-38,-33,-56,-46,-54,230,-55,-47,]),'POS':([89,],[121,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'pos_arreglo':([113,],[140,]),'Llamada_Func':([43,51,71,74,176,195,234,241,],[47,47,47,47,47,47,47,47,]),'mas_vars':([17,27,],[24,31,]),'ExpK':([64,73,75,98,109,130,131,141,144,145,146,147,149,150,159,162,175,178,204,],[78,78,78,78,78,78,158,78,78,78,78,78,78,78,180,78,78,78,78,]),'resuelve_operadores_relacionales':([78,158,],[100,179,]),'param':([29,],[34,]),'agrega_falso':([81,91,112,],[109,123,139,]),'Main':([16,],[21,]),'crea_funcion_global':([5,],[6,]),'crea_else_cuadruplo':([215,],[222,]),'DoWhile':([43,51,71,74,176,195,234,241,],[48,48,48,48,48,48,48,48,]),'push_decimal_PilaOperandos':([86,],[114,]),'For':([43,51,71,74,176,195,234,241,],[49,49,49,49,49,49,49,49,]),'pos_MULTDIV':([110,],[138,]),'resuelve_termino':([79,],[108,]),'push_operador_PilaOperadores':([102,122,132,138,],[131,149,159,161,]),'pos_SUMRES':([108,],[132,]),'guarda_resultado_funcion':([218,],[231,]),'tipo_funcion':([15,],[19,]),'While':([43,51,71,74,176,195,234,241,],[50,50,50,50,50,50,50,50,]),'resuelve_return':([115,],[142,]),'funciones':([10,151,],[16,173,]),'crea_print':([153,],[174,]),'push_int_PilaOperandos':([83,],[111,]),'Estatutos':([43,51,71,74,176,195,234,241,],[51,51,51,51,51,51,51,51,]),'guarda_numero_cuadruplo':([62,],[76,]),'Condicion':([43,51,71,74,176,195,234,241,],[67,67,67,67,67,67,67,67,]),'crea_GOTOF':([128,156,],[155,177,]),'push_var_PilaOperandos':([66,85,],[90,113,]),'agrega_funcion':([38,],[42,]),'fin_func_quad':([124,],[151,]),'resuelve_factor':([82,],[110,]),'Right':([43,51,71,74,176,195,234,241,],[54,54,54,54,54,54,54,54,]),'crea_primer_quadruple':([4,],[5,]),'Forward':([43,51,71,74,176,195,234,241,],[55,55,55,55,55,55,55,55,]),'llama_funcion':([64,73,75,98,109,130,131,141,144,145,146,147,149,150,159,161,162,175,178,204,],[84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,]),'Ciclo':([43,51,71,74,176,195,234,241,],[56,56,56,56,56,56,56,56,]),'ExpT':([64,73,75,98,109,130,131,141,144,145,146,147,149,150,159,161,162,175,178,204,],[79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,182,79,79,79,79,]),'Return':([43,51,71,74,176,195,234,241,],[58,58,58,58,58,58,58,58,]),'checa_funcion_si_existe':([123,139,],[150,162,]),'agrega_var_funcion':([24,],[28,]),'Exp_ciclo':([217,],[228,]),'Left':([43,51,71,74,176,195,234,241,],[59,59,59,59,59,59,59,59,]),'Operandos':([78,],[102,]),'Circle':([43,51,71,74,176,195,234,241,],[46,46,46,46,46,46,46,46,]),'Asignacion':([43,51,71,74,176,195,234,241,],[60,60,60,60,60,60,60,60,]),'llena_cuadruplo_if':([214,],[221,]),'vtc_action':([219,],[232,]),'ExpF':([64,73,75,98,109,130,131,141,144,145,146,147,149,150,159,161,162,175,178,204,],[82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,]),'Print':([43,51,71,74,176,195,234,241,],[52,52,52,52,52,52,52,52,]),'agrega_main_funcion':([22,],[26,]),'VAR_CTE':([64,73,75,98,109,130,131,141,144,145,146,147,149,150,159,161,162,175,178,204,],[80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,]),'program':([0,],[2,]),'pos_else':([207,],[214,]),'pos_commaf':([37,70,],[40,92,]),'regresa_inicio_while':([216,],[223,]),'Vars':([7,32,39,45,],[10,36,43,71,]),'quita_falso':([160,191,197,],[181,203,210,]),'ExpI':([64,73,75,98,109,130,141,144,145,146,147,149,150,162,175,178,204,],[87,95,97,129,135,157,163,165,166,167,168,170,172,172,193,196,212,]),'argumentos':([150,162,],[171,183,]),'reg_brack':([43,51,71,74,176,195,234,241,],[65,72,93,96,194,208,240,243,]),'mas_argumentos':([192,220,],[205,233,]),'Position':([43,51,71,74,176,195,234,241,],[68,68,68,68,68,68,68,68,]),'resuelve_llamada_funcion':([203,210,],[211,218,]),'resuelve_asignacion':([190,],[202,]),'resuelve_argumentos':([172,212,],[192,220,]),'TurtleMotion':([43,51,71,74,176,195,234,241,],[69,69,69,69,69,69,69,69,]),'Tipo':([7,15,29,32,39,41,45,],[14,18,33,14,14,44,14,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> START EDJO VAR_ID crea_primer_quadruple crea_funcion_global SEMICOLON Vars funciones Main','program',9,'p_inicio','edjo.py',196),
  ('crea_primer_quadruple -> <empty>','crea_primer_quadruple',0,'p_crea_primer_quadruple','edjo.py',201),
  ('crea_funcion_global -> <empty>','crea_funcion_global',0,'p_crea_funcion_global','edjo.py',209),
  ('Vars -> Tipo VAR_ID mas_vars agrega_var_funcion SEMICOLON Vars','Vars',6,'p_Vars','edjo.py',216),
  ('Vars -> <empty>','Vars',0,'p_Vars','edjo.py',217),
  ('Tipo -> INT','Tipo',1,'p_Tipo','edjo.py',221),
  ('Tipo -> DECIMAL','Tipo',1,'p_Tipo','edjo.py',222),
  ('Tipo -> STRING','Tipo',1,'p_Tipo','edjo.py',223),
  ('Tipo -> CHAR','Tipo',1,'p_Tipo','edjo.py',224),
  ('Tipo -> BOOL','Tipo',1,'p_Tipo','edjo.py',225),
  ('mas_vars -> COMMA VAR_ID mas_vars','mas_vars',3,'p_mas_vars','edjo.py',230),
  ('mas_vars -> <empty>','mas_vars',0,'p_mas_vars','edjo.py',231),
  ('agrega_var_funcion -> <empty>','agrega_var_funcion',0,'p_agrega_var_funcion','edjo.py',239),
  ('Asignacion -> VAR_ID push_var_PilaOperandos ASSIGN push_operador_PilaOperadores ExpI SEMICOLON resuelve_asignacion','Asignacion',7,'p_Asignacion','edjo.py',254),
  ('push_var_PilaOperandos -> <empty>','push_var_PilaOperandos',0,'p_push_var_PilaOperandos','edjo.py',259),
  ('push_operador_PilaOperadores -> <empty>','push_operador_PilaOperadores',0,'p_push_operador_PilaOperadores','edjo.py',276),
  ('resuelve_asignacion -> <empty>','resuelve_asignacion',0,'p_resuelve_asignacion','edjo.py',282),
  ('ExpI -> ExpK resuelve_operadores_relacionales','ExpI',2,'p_ExpI','edjo.py',301),
  ('ExpI -> ExpK Operandos push_operador_PilaOperadores ExpK resuelve_operadores_relacionales','ExpI',5,'p_ExpI','edjo.py',302),
  ('Operandos -> LT','Operandos',1,'p_Operandos','edjo.py',306),
  ('Operandos -> GT','Operandos',1,'p_Operandos','edjo.py',307),
  ('Operandos -> NE','Operandos',1,'p_Operandos','edjo.py',308),
  ('Operandos -> LE','Operandos',1,'p_Operandos','edjo.py',309),
  ('Operandos -> GE','Operandos',1,'p_Operandos','edjo.py',310),
  ('Operandos -> EQ','Operandos',1,'p_Operandos','edjo.py',311),
  ('resuelve_operadores_relacionales -> <empty>','resuelve_operadores_relacionales',0,'p_resuelve_operadores_relacionales','edjo.py',317),
  ('ExpK -> ExpT resuelve_termino','ExpK',2,'p_ExpK','edjo.py',344),
  ('ExpK -> ExpT resuelve_termino pos_SUMRES push_operador_PilaOperadores ExpK','ExpK',5,'p_ExpK','edjo.py',345),
  ('resuelve_termino -> <empty>','resuelve_termino',0,'p_resuelve_termino','edjo.py',350),
  ('pos_SUMRES -> PLUS','pos_SUMRES',1,'p_pos_SUMRES','edjo.py',358),
  ('pos_SUMRES -> MINUS','pos_SUMRES',1,'p_pos_SUMRES','edjo.py',359),
  ('ExpT -> ExpF resuelve_factor','ExpT',2,'p_ExpT','edjo.py',364),
  ('ExpT -> ExpF resuelve_factor pos_MULTDIV push_operador_PilaOperadores ExpT','ExpT',5,'p_ExpT','edjo.py',365),
  ('resuelve_factor -> <empty>','resuelve_factor',0,'p_resuelve_factor','edjo.py',369),
  ('pos_MULTDIV -> MULT','pos_MULTDIV',1,'p_pos_MULTDIV','edjo.py',377),
  ('pos_MULTDIV -> DIV','pos_MULTDIV',1,'p_pos_MULTDIV','edjo.py',378),
  ('ExpF -> VAR_CTE','ExpF',1,'p_ExpF','edjo.py',383),
  ('ExpF -> LPAREN agrega_falso ExpI RPAREN quita_falso','ExpF',5,'p_ExpF','edjo.py',384),
  ('ExpF -> VAR_ID push_var_PilaOperandos pos_arreglo','ExpF',3,'p_ExpF','edjo.py',385),
  ('ExpF -> llama_funcion','ExpF',1,'p_ExpF','edjo.py',386),
  ('VAR_CTE -> VAR_INT push_int_PilaOperandos','VAR_CTE',2,'p_VAR_CTE','edjo.py',391),
  ('VAR_CTE -> VAR_DECIMAL push_decimal_PilaOperandos','VAR_CTE',2,'p_VAR_CTE','edjo.py',392),
  ('push_int_PilaOperandos -> <empty>','push_int_PilaOperandos',0,'p_push_int_PilaOperandos','edjo.py',397),
  ('push_decimal_PilaOperandos -> <empty>','push_decimal_PilaOperandos',0,'p_push_decimal_PilaOperandos','edjo.py',407),
  ('agrega_falso -> <empty>','agrega_falso',0,'p_agrega_falso','edjo.py',418),
  ('quita_falso -> <empty>','quita_falso',0,'p_quita_falso','edjo.py',424),
  ('llama_funcion -> VAR_ID LPAREN agrega_falso checa_funcion_si_existe argumentos RPAREN quita_falso resuelve_llamada_funcion guarda_resultado_funcion','llama_funcion',9,'p_llama_funcion','edjo.py',429),
  ('checa_funcion_si_existe -> <empty>','checa_funcion_si_existe',0,'p_checa_funcion_si_existe','edjo.py',434),
  ('argumentos -> ExpI resuelve_argumentos mas_argumentos','argumentos',3,'p_argumentos','edjo.py',449),
  ('argumentos -> <empty>','argumentos',0,'p_argumentos','edjo.py',450),
  ('mas_argumentos -> COMMA ExpI resuelve_argumentos mas_argumentos','mas_argumentos',4,'p_mas_argumentos','edjo.py',454),
  ('mas_argumentos -> <empty>','mas_argumentos',0,'p_mas_argumentos','edjo.py',455),
  ('resuelve_argumentos -> <empty>','resuelve_argumentos',0,'p_resuelve_argumentos','edjo.py',460),
  ('resuelve_llamada_funcion -> <empty>','resuelve_llamada_funcion',0,'p_resuelve_llamada_funcion','edjo.py',479),
  ('guarda_resultado_funcion -> <empty>','guarda_resultado_funcion',0,'p_guarda_resultado_funcion','edjo.py',493),
  ('pos_arreglo -> SLBRACKET ExpI SRBRACKET','pos_arreglo',3,'p_pos_arreglo','edjo.py',509),
  ('pos_arreglo -> <empty>','pos_arreglo',0,'p_pos_arreglo','edjo.py',510),
  ('funciones -> FUNC tipo_funcion VAR_ID LPAREN param RPAREN agrega_funcion LBRACKET Vars reg_brack RBRACKET fin_func_quad funciones','funciones',13,'p_funciones','edjo.py',515),
  ('funciones -> <empty>','funciones',0,'p_funciones','edjo.py',516),
  ('tipo_funcion -> VOID','tipo_funcion',1,'p_tipo_funcion','edjo.py',520),
  ('tipo_funcion -> Tipo','tipo_funcion',1,'p_tipo_funcion','edjo.py',521),
  ('param -> Tipo VAR_ID pos_commaf','param',3,'p_param','edjo.py',526),
  ('param -> <empty>','param',0,'p_param','edjo.py',527),
  ('pos_commaf -> COMMA Tipo VAR_ID pos_commaf','pos_commaf',4,'p_pos_commaf','edjo.py',531),
  ('pos_commaf -> <empty>','pos_commaf',0,'p_pos_commaf','edjo.py',532),
  ('agrega_funcion -> <empty>','agrega_funcion',0,'p_agrega_funcion','edjo.py',542),
  ('fin_func_quad -> <empty>','fin_func_quad',0,'p_fin_func_quad','edjo.py',563),
  ('reg_brack -> Estatutos reg_brack','reg_brack',2,'p_reg_brack','edjo.py',586),
  ('reg_brack -> <empty>','reg_brack',0,'p_reg_brack','edjo.py',587),
  ('Estatutos -> Condicion','Estatutos',1,'p_Estatutos','edjo.py',590),
  ('Estatutos -> Ciclo','Estatutos',1,'p_Estatutos','edjo.py',591),
  ('Estatutos -> Return','Estatutos',1,'p_Estatutos','edjo.py',592),
  ('Estatutos -> Asignacion','Estatutos',1,'p_Estatutos','edjo.py',593),
  ('Estatutos -> Print','Estatutos',1,'p_Estatutos','edjo.py',594),
  ('Estatutos -> Llamada_Func','Estatutos',1,'p_Estatutos','edjo.py',595),
  ('Estatutos -> TurtleMotion','Estatutos',1,'p_Estatutos','edjo.py',596),
  ('Condicion -> IF LPAREN ExpI RPAREN crea_GOTOF LBRACKET reg_brack RBRACKET pos_else llena_cuadruplo_if','Condicion',10,'p_Condicion','edjo.py',599),
  ('crea_GOTOF -> <empty>','crea_GOTOF',0,'p_crea_GOTOF','edjo.py',603),
  ('llena_cuadruplo_if -> <empty>','llena_cuadruplo_if',0,'p_llena_cuadruplo_if','edjo.py',620),
  ('pos_else -> ELSE crea_else_cuadruplo LBRACKET reg_brack RBRACKET','pos_else',5,'p_pos_else','edjo.py',628),
  ('pos_else -> <empty>','pos_else',0,'p_pos_else','edjo.py',629),
  ('crea_else_cuadruplo -> <empty>','crea_else_cuadruplo',0,'p_crea_else_cuadruplo','edjo.py',633),
  ('Return -> RETURN ExpI SEMICOLON resuelve_return','Return',4,'p_Return','edjo.py',645),
  ('resuelve_return -> <empty>','resuelve_return',0,'p_resuelve_return','edjo.py',650),
  ('Print -> PRINT LPAREN VAR_STRING RPAREN SEMICOLON','Print',5,'p_Print','edjo.py',671),
  ('Print -> PRINT LPAREN ExpI RPAREN SEMICOLON crea_print','Print',6,'p_Print','edjo.py',672),
  ('crea_print -> <empty>','crea_print',0,'p_crea_print','edjo.py',676),
  ('Llamada_Func -> VAR_ID LPAREN agrega_falso checa_funcion_si_existe argumentos RPAREN quita_falso resuelve_llamada_funcion SEMICOLON vtc_action','Llamada_Func',10,'p_Llamada_Func','edjo.py',685),
  ('vtc_action -> <empty>','vtc_action',0,'p_vtc_action','edjo.py',689),
  ('Ciclo -> For','Ciclo',1,'p_Ciclo','edjo.py',698),
  ('Ciclo -> While','Ciclo',1,'p_Ciclo','edjo.py',699),
  ('Ciclo -> DoWhile','Ciclo',1,'p_Ciclo','edjo.py',700),
  ('While -> WHILE guarda_numero_cuadruplo LPAREN ExpI RPAREN crea_GOTOF LBRACKET reg_brack RBRACKET regresa_inicio_while','While',10,'p_While','edjo.py',704),
  ('guarda_numero_cuadruplo -> <empty>','guarda_numero_cuadruplo',0,'p_guarda_numero_cuadruplo','edjo.py',708),
  ('regresa_inicio_while -> <empty>','regresa_inicio_while',0,'p_regresa_inicio_while','edjo.py',713),
  ('DoWhile -> DO LBRACKET reg_brack RBRACKET WHILE LPAREN ExpI RPAREN SEMICOLON','DoWhile',9,'p_DoWhile','edjo.py',725),
  ('For -> FOR LPAREN VAR_ID ASSIGN ExpI SEMICOLON ExpI SEMICOLON VAR_ID Exp_ciclo RPAREN LBRACKET reg_brack RBRACKET','For',14,'p_For','edjo.py',729),
  ('Exp_ciclo -> PLUS VAR_INT','Exp_ciclo',2,'p_Exp_ciclo','edjo.py',733),
  ('Exp_ciclo -> MINUS VAR_INT','Exp_ciclo',2,'p_Exp_ciclo','edjo.py',734),
  ('Exp_ciclo -> MULT VAR_INT','Exp_ciclo',2,'p_Exp_ciclo','edjo.py',735),
  ('Exp_ciclo -> DIV VAR_INT','Exp_ciclo',2,'p_Exp_ciclo','edjo.py',736),
  ('Exp_ciclo -> PLUSPLUS','Exp_ciclo',1,'p_Exp_ciclo','edjo.py',737),
  ('Exp_ciclo -> MINUSMINUS','Exp_ciclo',1,'p_Exp_ciclo','edjo.py',738),
  ('TurtleMotion -> Position','TurtleMotion',1,'p_TurtleMotion','edjo.py',742),
  ('TurtleMotion -> Right','TurtleMotion',1,'p_TurtleMotion','edjo.py',743),
  ('TurtleMotion -> Left','TurtleMotion',1,'p_TurtleMotion','edjo.py',744),
  ('TurtleMotion -> Forward','TurtleMotion',1,'p_TurtleMotion','edjo.py',745),
  ('TurtleMotion -> Circle','TurtleMotion',1,'p_TurtleMotion','edjo.py',746),
  ('Position -> VAR_ID POINT POS LPAREN RPAREN SEMICOLON','Position',6,'p_Position','edjo.py',749),
  ('Forward -> VAR_ID POINT FORWARD LPAREN ExpI RPAREN SEMICOLON','Forward',7,'p_Forward','edjo.py',752),
  ('Right -> VAR_ID POINT RIGHT LPAREN ExpI RPAREN SEMICOLON','Right',7,'p_Right','edjo.py',755),
  ('Left -> VAR_ID POINT LEFT LPAREN ExpI RPAREN SEMICOLON','Left',7,'p_Left','edjo.py',758),
  ('Circle -> VAR_ID POINT CIRCLE LPAREN ExpI RPAREN SEMICOLON','Circle',7,'p_Circle','edjo.py',761),
  ('Main -> MAIN agrega_main_funcion LPAREN RPAREN LBRACKET Vars reg_brack RET ZERO SEMICOLON RBRACKET','Main',11,'p_Main','edjo.py',765),
  ('agrega_main_funcion -> <empty>','agrega_main_funcion',0,'p_agrega_main_funcion','edjo.py',769),
]