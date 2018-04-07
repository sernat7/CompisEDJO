
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'LT EQ GT NE LE GE ASSIGN PLUSPLUS MINUSMINUS PLUS MINUS MULT DIV LPAREN RPAREN LBRACKET RBRACKET SLBRACKET SRBRACKET SEMICOLON COMMA IF ELSE IFELSE INT DECIMAL STRING CHAR BOOL PRINT START EDJO VOID RETURN MAIN FOR VAR_ID VAR_INT VAR_DECIMAL VAR_CHAR VAR_STRING TRUE FALSE DO WHILE FROM IMPORT POINT POS FORWARD CIRCLE LEFT RIGHT TUR TURTLE ZERO RET FUNC FINISHprogram\t:\tSTART EDJO VAR_ID crea_primer_quadruple crea_funcion_global SEMICOLON Vars funciones Main\n\tcrea_primer_quadruple\t: \n\tcrea_funcion_global\t: \n\tVars\t\t:\tTipo VAR_ID mas_vars agrega_var_funcion SEMICOLON Vars\n\t\t\t| \n\tTipo\t\t:\tINT\n\t\t\t|\tDECIMAL\n\t\t\t|\tSTRING\n\t\t\t|\tCHAR\n\t\t\t|\tBOOL\n\tmas_vars\t:\tCOMMA VAR_ID mas_vars\n\t\t\t| \n\tagrega_var_funcion\t: \n\tAsignacion\t:\tVAR_ID push_var_PilaOperandos ASSIGN push_operador_PilaOperadores ExpI SEMICOLON resuelve_asignacion\n\tpush_var_PilaOperandos\t: \n\tpush_operador_PilaOperadores\t: \n\tresuelve_asignacion\t: \n\tExpI\t\t:\tExpK resuelve_operadores_relacionales \n\t\t\t|\tExpK Operandos push_operador_PilaOperadores ExpK resuelve_operadores_relacionales\n\tOperandos\t:\tLT\n\t\t\t|\tGT\n\t\t\t|\tNE\n\t\t\t|\tLE\n\t\t\t|\tGE\n\t\t\t|\tEQ\n\tresuelve_operadores_relacionales\t: \n\tExpK\t\t:\tExpT resuelve_termino \n\t\t\t|\tExpT resuelve_termino pos_SUMRES push_operador_PilaOperadores ExpK\n\tresuelve_termino\t: \n\tpos_SUMRES\t:\tPLUS \n\t\t\t|\tMINUS \n\tExpT\t\t:\tExpF resuelve_factor \n\t\t\t|\tExpF resuelve_factor pos_MULTDIV push_operador_PilaOperadores ExpT\n\tresuelve_factor\t: \n\tpos_MULTDIV\t:\tMULT \n\t\t\t|\tDIV \n\tExpF\t\t:\tVAR_CTE\n\t\t\t|\tLPAREN agrega_falso ExpI RPAREN quita_falso\n\t\t\t|\tVAR_ID push_var_PilaOperandos pos_arreglo\n\t\t\t|\tllama_funcion \n\tVAR_CTE\t:\tVAR_INT push_int_PilaOperandos\n\t\t\t|\tVAR_DECIMAL push_decimal_PilaOperandos\n\tpush_int_PilaOperandos\t:\n\tpush_decimal_PilaOperandos\t: \n\tagrega_falso\t: \n\tquita_falso\t: \n\tllama_funcion\t:\tVAR_ID LPAREN agrega_falso checa_funcion_si_existe argumentos RPAREN quita_falso resuelve_llamada_funcion guarda_resultado_funcion\n\tcheca_funcion_si_existe\t: \n\targumentos\t:\tExpI resuelve_argumentos mas_argumentos\n\t\t\t| \n\tmas_argumentos\t: \tCOMMA ExpI resuelve_argumentos mas_argumentos\n\t\t\t\t| \n\tresuelve_argumentos\t: \n\tresuelve_llamada_funcion\t: \n\tguarda_resultado_funcion\t: \n\tpos_arreglo\t:\tSLBRACKET ExpI SRBRACKET\n\t\t\t| \n\tfunciones\t:\tFUNC tipo_funcion VAR_ID LPAREN param RPAREN agrega_funcion LBRACKET Vars reg_brack RBRACKET fin_func_quad funciones\n\t\t\t| \n\ttipo_funcion\t:\tVOID\n\t\t\t|\tTipo\n\tparam\t:\tTipo VAR_ID pos_commaf\n\t\t\t| \n\tpos_commaf\t:\tCOMMA Tipo VAR_ID pos_commaf\n\t\t\t| \n\tagrega_funcion\t: \n\tfin_func_quad\t: \n\treg_brack\t:\tEstatutos reg_brack\n\t\t\t| \n\tEstatutos\t:\tCondicion \n\t\t\t|\tCiclo  \n\t\t\t|\tReturn \n\t\t\t|\tAsignacion\n\t\t\t|\tPrint \n\t\t\t|\tLlamada_Func \n\t\t\t|\tTurtleMotion \n\tCondicion\t:\tIF LPAREN ExpI RPAREN crea_GOTOF LBRACKET reg_brack RBRACKET pos_else llena_cuadruplo_if\n\tcrea_GOTOF\t: \n\tllena_cuadruplo_if\t: \n\tpos_else\t:\tELSE crea_else_cuadruplo LBRACKET reg_brack RBRACKET\n\t\t\t| \n\tcrea_else_cuadruplo\t: \n\tReturn \t:\tRETURN ExpI SEMICOLON resuelve_return\n\tresuelve_return\t: \n\tPrint\t:\tPRINT LPAREN VAR_STRING RPAREN SEMICOLON\n\t\t\t|\tPRINT LPAREN ExpI RPAREN SEMICOLON crea_print\n\tcrea_print\t: \n\tLlamada_Func\t:\tVAR_ID LPAREN agrega_falso checa_funcion_si_existe argumentos RPAREN quita_falso resuelve_llamada_funcion SEMICOLON vtc_action\n\tvtc_action\t: \n\tCiclo\t:\tFor\n\t\t\t|\tWhile\n\t\t\t|\tDoWhile\n\tWhile\t:\tWHILE guarda_numero_cuadruplo LPAREN ExpI RPAREN crea_GOTOF LBRACKET reg_brack RBRACKET regresa_inicio_while\n\tguarda_numero_cuadruplo\t: \n\tregresa_inicio_while\t: \n\tcrea_GOTOV\t: \n\tDoWhile\t:\tDO guarda_numero_cuadruplo LBRACKET reg_brack RBRACKET WHILE LPAREN ExpI RPAREN crea_GOTOV SEMICOLON\n\tFor\t\t:\tFOR LPAREN VAR_ID ASSIGN ExpI SEMICOLON ExpI SEMICOLON VAR_ID Exp_ciclo RPAREN LBRACKET reg_brack RBRACKET\n\tExp_ciclo\t:\tPLUS VAR_INT\n\t\t\t|\tMINUS VAR_INT\n\t\t\t|\tMULT VAR_INT\n\t\t\t|\tDIV VAR_INT\n\t\t\t|\tPLUSPLUS\n\t\t\t|\tMINUSMINUS\n\tTurtleMotion\t:\tPosition\n\t\t\t|\tRight\n\t\t\t|\tLeft\n\t\t\t|\tForward\n\t\t\t|\tCircle\n\t\t\t|\tIniciaTurtle\n\t\t\t|\tTerminaTurtle\n\tPosition\t:\tTUR POINT POS LPAREN ExpI COMMA ExpI RPAREN SEMICOLON pfc_set_position\n\tpfc_set_position\t: \n\tForward\t:\tTUR POINT FORWARD LPAREN ExpI RPAREN SEMICOLON pfc_move_forward\n\tpfc_move_forward\t: \n\tRight\t:\tTUR POINT RIGHT LPAREN ExpI RPAREN SEMICOLON pfc_turn_right\n\tpfc_turn_right\t: \n\tLeft\t\t:\tTUR POINT LEFT LPAREN ExpI RPAREN SEMICOLON pfc_turn_left\n\tpfc_turn_left\t: \n\tCircle\t:\tTUR POINT CIRCLE LPAREN ExpI RPAREN SEMICOLON pfc_draw_circle\n\tpfc_draw_circle\t: \n\tIniciaTurtle\t:\tTUR POINT TURTLE LPAREN RPAREN SEMICOLON pfc_create_turtle\n\tpfc_create_turtle\t: \n\tTerminaTurtle\t:\tTUR POINT FINISH LPAREN RPAREN SEMICOLON pfc_finish_drawing\n\tpfc_finish_drawing\t: \n\tMain\t\t:\tMAIN agrega_main_funcion LPAREN RPAREN LBRACKET Vars reg_brack RET ZERO SEMICOLON RBRACKET\n\tagrega_main_funcion\t: \n\t'
    
_lr_action_items = {'START':([0,],[2,]),'$end':([1,18,158,],[0,-1,-126,]),'EDJO':([2,],[3,]),'VAR_ID':([3,9,10,11,12,13,14,20,21,22,24,31,35,36,37,40,45,46,47,48,49,50,51,52,54,55,56,57,60,61,62,63,64,65,66,71,72,75,81,87,88,89,93,97,99,100,101,102,103,104,105,108,110,113,114,118,119,131,132,133,134,135,136,137,138,141,142,143,144,147,150,151,152,153,154,161,162,165,169,170,182,189,192,193,196,201,202,206,209,211,212,214,215,216,217,218,219,220,224,228,229,230,231,232,235,238,240,241,244,253,255,256,262,264,265,267,],[4,17,-6,-7,-8,-9,-10,26,-60,-61,28,-5,39,-4,-5,58,58,-70,-71,-72,-73,-74,-75,-76,-90,-91,-92,82,-105,-106,-107,-108,-109,-110,-111,-5,94,82,-45,-45,82,117,58,-84,-16,-20,-21,-22,-23,-24,-25,82,-45,-16,-48,82,58,-83,82,-16,-30,-31,-16,-35,-36,82,-48,82,82,82,82,82,82,82,82,82,82,82,-85,-87,58,-17,-86,82,82,-123,-125,-14,82,58,82,-117,-119,-115,-121,-122,-124,-81,237,-116,-118,-114,-120,-79,-89,-95,-113,-77,-88,-93,-112,58,-97,58,-80,-98,]),'SEMICOLON':([4,5,6,17,23,27,28,32,76,77,78,79,80,82,83,84,85,95,98,106,107,109,111,112,140,145,146,160,163,166,171,179,180,183,184,185,186,187,190,197,198,199,200,205,207,210,221,222,227,234,239,243,254,],[-2,-3,7,-12,-13,31,-12,-11,97,-26,-29,-34,-37,-15,-40,-43,-44,129,-18,-27,-32,-57,-41,-42,-39,169,170,-26,-46,189,193,201,202,-19,-28,-33,-38,-56,-46,214,215,216,217,-46,-54,224,-54,235,240,-55,-96,-47,262,]),'FUNC':([7,8,31,36,157,181,],[-5,16,-5,-4,-67,16,]),'MAIN':([7,8,15,31,36,157,181,203,],[-5,-59,19,-5,-4,-67,-59,-58,]),'INT':([7,16,30,31,37,43,71,],[10,10,10,10,10,10,10,]),'DECIMAL':([7,16,30,31,37,43,71,],[11,11,11,11,11,11,11,]),'STRING':([7,16,30,31,37,43,71,],[12,12,12,12,12,12,12,]),'CHAR':([7,16,30,31,37,43,71,],[13,13,13,13,13,13,13,]),'BOOL':([7,16,30,31,37,43,71,],[14,14,14,14,14,14,14,]),'VOID':([16,],[21,]),'COMMA':([17,28,39,77,78,79,80,82,83,84,85,94,98,106,107,109,111,112,140,160,163,168,174,183,184,185,186,187,191,205,221,223,234,236,243,],[24,24,43,-26,-29,-34,-37,-15,-40,-43,-44,43,-18,-27,-32,-57,-41,-42,-39,-26,-46,-53,196,-19,-28,-33,-38,-56,209,-46,-54,-53,-55,209,-47,]),'LPAREN':([19,25,26,53,57,58,59,67,68,75,81,82,87,88,90,99,100,101,102,103,104,105,108,110,113,114,118,120,121,122,123,124,125,126,132,133,134,135,136,137,138,141,142,143,144,147,150,151,152,153,154,161,162,165,193,195,196,209,212,],[-127,29,30,75,81,87,88,89,-94,81,-45,110,-45,81,118,-16,-20,-21,-22,-23,-24,-25,81,-45,-16,-48,81,150,151,152,153,154,155,156,81,-16,-30,-31,-16,-35,-36,81,-48,81,81,81,81,81,81,81,81,81,81,81,81,212,81,81,81,]),'RPAREN':([29,30,34,39,42,77,78,79,80,82,83,84,85,87,94,96,98,106,107,109,110,111,112,114,115,116,128,139,140,142,144,148,155,156,160,163,165,167,168,175,176,177,178,183,184,185,186,187,188,191,205,208,213,221,223,226,234,236,243,245,246,251,252,258,259,260,261,],[33,-63,38,-65,-62,-26,-29,-34,-37,-15,-40,-43,-44,-45,-65,130,-18,-27,-32,-57,-45,-41,-42,-48,145,146,-64,163,-39,-48,-50,172,179,180,-26,-46,-50,190,-53,197,198,199,200,-19,-28,-33,-38,-56,205,-52,-46,-49,227,-54,-53,239,-55,-52,-47,-51,257,-103,-104,-99,-100,-101,-102,]),'IF':([31,36,37,40,45,46,47,48,49,50,51,52,54,55,56,60,61,62,63,64,65,66,71,93,97,119,131,169,170,182,189,192,201,202,206,211,214,215,216,217,218,219,220,228,229,230,231,232,235,238,240,241,244,253,255,256,262,264,265,267,],[-5,-4,-5,53,53,-70,-71,-72,-73,-74,-75,-76,-90,-91,-92,-105,-106,-107,-108,-109,-110,-111,-5,53,-84,53,-83,-85,-87,53,-17,-86,-123,-125,-14,53,-117,-119,-115,-121,-122,-124,-81,-116,-118,-114,-120,-79,-89,-95,-113,-77,-88,-93,-112,53,-97,53,-80,-98,]),'RETURN':([31,36,37,40,45,46,47,48,49,50,51,52,54,55,56,60,61,62,63,64,65,66,71,93,97,119,131,169,170,182,189,192,201,202,206,211,214,215,216,217,218,219,220,228,229,230,231,232,235,238,240,241,244,253,255,256,262,264,265,267,],[-5,-4,-5,57,57,-70,-71,-72,-73,-74,-75,-76,-90,-91,-92,-105,-106,-107,-108,-109,-110,-111,-5,57,-84,57,-83,-85,-87,57,-17,-86,-123,-125,-14,57,-117,-119,-115,-121,-122,-124,-81,-116,-118,-114,-120,-79,-89,-95,-113,-77,-88,-93,-112,57,-97,57,-80,-98,]),'PRINT':([31,36,37,40,45,46,47,48,49,50,51,52,54,55,56,60,61,62,63,64,65,66,71,93,97,119,131,169,170,182,189,192,201,202,206,211,214,215,216,217,218,219,220,228,229,230,231,232,235,238,240,241,244,253,255,256,262,264,265,267,],[-5,-4,-5,59,59,-70,-71,-72,-73,-74,-75,-76,-90,-91,-92,-105,-106,-107,-108,-109,-110,-111,-5,59,-84,59,-83,-85,-87,59,-17,-86,-123,-125,-14,59,-117,-119,-115,-121,-122,-124,-81,-116,-118,-114,-120,-79,-89,-95,-113,-77,-88,-93,-112,59,-97,59,-80,-98,]),'FOR':([31,36,37,40,45,46,47,48,49,50,51,52,54,55,56,60,61,62,63,64,65,66,71,93,97,119,131,169,170,182,189,192,201,202,206,211,214,215,216,217,218,219,220,228,229,230,231,232,235,238,240,241,244,253,255,256,262,264,265,267,],[-5,-4,-5,67,67,-70,-71,-72,-73,-74,-75,-76,-90,-91,-92,-105,-106,-107,-108,-109,-110,-111,-5,67,-84,67,-83,-85,-87,67,-17,-86,-123,-125,-14,67,-117,-119,-115,-121,-122,-124,-81,-116,-118,-114,-120,-79,-89,-95,-113,-77,-88,-93,-112,67,-97,67,-80,-98,]),'WHILE':([31,36,37,40,45,46,47,48,49,50,51,52,54,55,56,60,61,62,63,64,65,66,71,93,97,119,131,169,170,173,182,189,192,201,202,206,211,214,215,216,217,218,219,220,228,229,230,231,232,235,238,240,241,244,253,255,256,262,264,265,267,],[-5,-4,-5,68,68,-70,-71,-72,-73,-74,-75,-76,-90,-91,-92,-105,-106,-107,-108,-109,-110,-111,-5,68,-84,68,-83,-85,-87,195,68,-17,-86,-123,-125,-14,68,-117,-119,-115,-121,-122,-124,-81,-116,-118,-114,-120,-79,-89,-95,-113,-77,-88,-93,-112,68,-97,68,-80,-98,]),'DO':([31,36,37,40,45,46,47,48,49,50,51,52,54,55,56,60,61,62,63,64,65,66,71,93,97,119,131,169,170,182,189,192,201,202,206,211,214,215,216,217,218,219,220,228,229,230,231,232,235,238,240,241,244,253,255,256,262,264,265,267,],[-5,-4,-5,69,69,-70,-71,-72,-73,-74,-75,-76,-90,-91,-92,-105,-106,-107,-108,-109,-110,-111,-5,69,-84,69,-83,-85,-87,69,-17,-86,-123,-125,-14,69,-117,-119,-115,-121,-122,-124,-81,-116,-118,-114,-120,-79,-89,-95,-113,-77,-88,-93,-112,69,-97,69,-80,-98,]),'TUR':([31,36,37,40,45,46,47,48,49,50,51,52,54,55,56,60,61,62,63,64,65,66,71,93,97,119,131,169,170,182,189,192,201,202,206,211,214,215,216,217,218,219,220,228,229,230,231,232,235,238,240,241,244,253,255,256,262,264,265,267,],[-5,-4,-5,70,70,-70,-71,-72,-73,-74,-75,-76,-90,-91,-92,-105,-106,-107,-108,-109,-110,-111,-5,70,-84,70,-83,-85,-87,70,-17,-86,-123,-125,-14,70,-117,-119,-115,-121,-122,-124,-81,-116,-118,-114,-120,-79,-89,-95,-113,-77,-88,-93,-112,70,-97,70,-80,-98,]),'RET':([31,36,37,40,44,45,46,47,48,49,50,51,52,54,55,56,60,61,62,63,64,65,66,74,97,131,169,170,189,192,201,202,206,214,215,216,217,218,219,220,228,229,230,231,232,235,238,240,241,244,253,255,262,265,267,],[-5,-4,-5,-69,73,-69,-70,-71,-72,-73,-74,-75,-76,-90,-91,-92,-105,-106,-107,-108,-109,-110,-111,-68,-84,-83,-85,-87,-17,-86,-123,-125,-14,-117,-119,-115,-121,-122,-124,-81,-116,-118,-114,-120,-79,-89,-95,-113,-77,-88,-93,-112,-97,-80,-98,]),'RBRACKET':([31,36,45,46,47,48,49,50,51,52,54,55,56,60,61,62,63,64,65,66,71,74,93,97,119,127,129,131,149,169,170,182,189,192,201,202,204,206,211,214,215,216,217,218,219,220,225,228,229,230,231,232,235,238,240,241,244,253,255,256,262,263,264,265,266,267,],[-5,-4,-69,-70,-71,-72,-73,-74,-75,-76,-90,-91,-92,-105,-106,-107,-108,-109,-110,-111,-5,-68,-69,-84,-69,157,158,-83,173,-85,-87,-69,-17,-86,-123,-125,220,-14,-69,-117,-119,-115,-121,-122,-124,-81,238,-116,-118,-114,-120,-79,-89,-95,-113,-77,-88,-93,-112,-69,-97,265,-69,-80,267,-98,]),'LBRACKET':([33,38,41,69,91,130,159,172,194,233,242,257,],[37,-66,71,-94,119,-78,182,-78,211,-82,256,264,]),'VAR_INT':([57,75,81,87,88,99,100,101,102,103,104,105,108,110,113,114,118,132,133,134,135,136,137,138,141,142,143,144,147,150,151,152,153,154,161,162,165,193,196,209,212,247,248,249,250,],[84,84,-45,-45,84,-16,-20,-21,-22,-23,-24,-25,84,-45,-16,-48,84,84,-16,-30,-31,-16,-35,-36,84,-48,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,258,259,260,261,]),'VAR_DECIMAL':([57,75,81,87,88,99,100,101,102,103,104,105,108,110,113,114,118,132,133,134,135,136,137,138,141,142,143,144,147,150,151,152,153,154,161,162,165,193,196,209,212,],[85,85,-45,-45,85,-16,-20,-21,-22,-23,-24,-25,85,-45,-16,-48,85,85,-16,-30,-31,-16,-35,-36,85,-48,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,]),'ASSIGN':([58,86,117,],[-15,113,147,]),'POINT':([70,],[92,]),'ZERO':([73,],[95,]),'SRBRACKET':([77,78,79,80,82,83,84,85,98,106,107,109,111,112,140,160,163,164,183,184,185,186,187,205,221,234,243,],[-26,-29,-34,-37,-15,-40,-43,-44,-18,-27,-32,-57,-41,-42,-39,-26,-46,187,-19,-28,-33,-38,-56,-46,-54,-55,-47,]),'LT':([77,78,79,80,82,83,84,85,106,107,109,111,112,140,163,184,185,186,187,205,221,234,243,],[100,-29,-34,-37,-15,-40,-43,-44,-27,-32,-57,-41,-42,-39,-46,-28,-33,-38,-56,-46,-54,-55,-47,]),'GT':([77,78,79,80,82,83,84,85,106,107,109,111,112,140,163,184,185,186,187,205,221,234,243,],[101,-29,-34,-37,-15,-40,-43,-44,-27,-32,-57,-41,-42,-39,-46,-28,-33,-38,-56,-46,-54,-55,-47,]),'NE':([77,78,79,80,82,83,84,85,106,107,109,111,112,140,163,184,185,186,187,205,221,234,243,],[102,-29,-34,-37,-15,-40,-43,-44,-27,-32,-57,-41,-42,-39,-46,-28,-33,-38,-56,-46,-54,-55,-47,]),'LE':([77,78,79,80,82,83,84,85,106,107,109,111,112,140,163,184,185,186,187,205,221,234,243,],[103,-29,-34,-37,-15,-40,-43,-44,-27,-32,-57,-41,-42,-39,-46,-28,-33,-38,-56,-46,-54,-55,-47,]),'GE':([77,78,79,80,82,83,84,85,106,107,109,111,112,140,163,184,185,186,187,205,221,234,243,],[104,-29,-34,-37,-15,-40,-43,-44,-27,-32,-57,-41,-42,-39,-46,-28,-33,-38,-56,-46,-54,-55,-47,]),'EQ':([77,78,79,80,82,83,84,85,106,107,109,111,112,140,163,184,185,186,187,205,221,234,243,],[105,-29,-34,-37,-15,-40,-43,-44,-27,-32,-57,-41,-42,-39,-46,-28,-33,-38,-56,-46,-54,-55,-47,]),'PLUS':([78,79,80,82,83,84,85,106,107,109,111,112,140,163,185,186,187,205,221,234,237,243,],[-29,-34,-37,-15,-40,-43,-44,134,-32,-57,-41,-42,-39,-46,-33,-38,-56,-46,-54,-55,247,-47,]),'MINUS':([78,79,80,82,83,84,85,106,107,109,111,112,140,163,185,186,187,205,221,234,237,243,],[-29,-34,-37,-15,-40,-43,-44,135,-32,-57,-41,-42,-39,-46,-33,-38,-56,-46,-54,-55,248,-47,]),'MULT':([79,80,82,83,84,85,107,109,111,112,140,163,186,187,205,221,234,237,243,],[-34,-37,-15,-40,-43,-44,137,-57,-41,-42,-39,-46,-38,-56,-46,-54,-55,249,-47,]),'DIV':([79,80,82,83,84,85,107,109,111,112,140,163,186,187,205,221,234,237,243,],[-34,-37,-15,-40,-43,-44,138,-57,-41,-42,-39,-46,-38,-56,-46,-54,-55,250,-47,]),'SLBRACKET':([82,109,],[-15,141,]),'VAR_STRING':([88,],[115,]),'POS':([92,],[120,]),'RIGHT':([92,],[121,]),'LEFT':([92,],[122,]),'FORWARD':([92,],[123,]),'CIRCLE':([92,],[124,]),'TURTLE':([92,],[125,]),'FINISH':([92,],[126,]),'ELSE':([220,],[233,]),'PLUSPLUS':([237,],[251,]),'MINUSMINUS':([237,],[252,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'crea_primer_quadruple':([4,],[5,]),'crea_funcion_global':([5,],[6,]),'Vars':([7,31,37,71,],[8,36,40,93,]),'Tipo':([7,16,30,31,37,43,71,],[9,22,35,9,9,72,9,]),'funciones':([8,181,],[15,203,]),'Main':([15,],[18,]),'tipo_funcion':([16,],[20,]),'mas_vars':([17,28,],[23,32,]),'agrega_main_funcion':([19,],[25,]),'agrega_var_funcion':([23,],[27,]),'param':([30,],[34,]),'agrega_funcion':([38,],[41,]),'pos_commaf':([39,94,],[42,128,]),'reg_brack':([40,45,93,119,182,211,256,264,],[44,74,127,149,204,225,263,266,]),'Estatutos':([40,45,93,119,182,211,256,264,],[45,45,45,45,45,45,45,45,]),'Condicion':([40,45,93,119,182,211,256,264,],[46,46,46,46,46,46,46,46,]),'Ciclo':([40,45,93,119,182,211,256,264,],[47,47,47,47,47,47,47,47,]),'Return':([40,45,93,119,182,211,256,264,],[48,48,48,48,48,48,48,48,]),'Asignacion':([40,45,93,119,182,211,256,264,],[49,49,49,49,49,49,49,49,]),'Print':([40,45,93,119,182,211,256,264,],[50,50,50,50,50,50,50,50,]),'Llamada_Func':([40,45,93,119,182,211,256,264,],[51,51,51,51,51,51,51,51,]),'TurtleMotion':([40,45,93,119,182,211,256,264,],[52,52,52,52,52,52,52,52,]),'For':([40,45,93,119,182,211,256,264,],[54,54,54,54,54,54,54,54,]),'While':([40,45,93,119,182,211,256,264,],[55,55,55,55,55,55,55,55,]),'DoWhile':([40,45,93,119,182,211,256,264,],[56,56,56,56,56,56,56,56,]),'Position':([40,45,93,119,182,211,256,264,],[60,60,60,60,60,60,60,60,]),'Right':([40,45,93,119,182,211,256,264,],[61,61,61,61,61,61,61,61,]),'Left':([40,45,93,119,182,211,256,264,],[62,62,62,62,62,62,62,62,]),'Forward':([40,45,93,119,182,211,256,264,],[63,63,63,63,63,63,63,63,]),'Circle':([40,45,93,119,182,211,256,264,],[64,64,64,64,64,64,64,64,]),'IniciaTurtle':([40,45,93,119,182,211,256,264,],[65,65,65,65,65,65,65,65,]),'TerminaTurtle':([40,45,93,119,182,211,256,264,],[66,66,66,66,66,66,66,66,]),'ExpI':([57,75,88,108,118,141,143,144,147,150,151,152,153,154,165,193,196,209,212,],[76,96,116,139,148,164,166,168,171,174,175,176,177,178,168,210,213,223,226,]),'ExpK':([57,75,88,108,118,132,141,143,144,147,150,151,152,153,154,161,165,193,196,209,212,],[77,77,77,77,77,160,77,77,77,77,77,77,77,77,77,184,77,77,77,77,77,]),'ExpT':([57,75,88,108,118,132,141,143,144,147,150,151,152,153,154,161,162,165,193,196,209,212,],[78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,185,78,78,78,78,78,]),'ExpF':([57,75,88,108,118,132,141,143,144,147,150,151,152,153,154,161,162,165,193,196,209,212,],[79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,]),'VAR_CTE':([57,75,88,108,118,132,141,143,144,147,150,151,152,153,154,161,162,165,193,196,209,212,],[80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,]),'llama_funcion':([57,75,88,108,118,132,141,143,144,147,150,151,152,153,154,161,162,165,193,196,209,212,],[83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,]),'push_var_PilaOperandos':([58,82,],[86,109,]),'guarda_numero_cuadruplo':([68,69,],[90,91,]),'resuelve_operadores_relacionales':([77,160,],[98,183,]),'Operandos':([77,],[99,]),'resuelve_termino':([78,],[106,]),'resuelve_factor':([79,],[107,]),'agrega_falso':([81,87,110,],[108,114,142,]),'push_int_PilaOperandos':([84,],[111,]),'push_decimal_PilaOperandos':([85,],[112,]),'resuelve_return':([97,],[131,]),'push_operador_PilaOperadores':([99,113,133,136,],[132,143,161,162,]),'pos_SUMRES':([106,],[133,]),'pos_MULTDIV':([107,],[136,]),'pos_arreglo':([109,],[140,]),'checa_funcion_si_existe':([114,142,],[144,165,]),'crea_GOTOF':([130,172,],[159,194,]),'argumentos':([144,165,],[167,188,]),'fin_func_quad':([157,],[181,]),'quita_falso':([163,190,205,],[186,207,221,]),'resuelve_argumentos':([168,223,],[191,236,]),'crea_print':([170,],[192,]),'resuelve_asignacion':([189,],[206,]),'mas_argumentos':([191,236,],[208,245,]),'pfc_create_turtle':([201,],[218,]),'pfc_finish_drawing':([202,],[219,]),'resuelve_llamada_funcion':([207,221,],[222,234,]),'pfc_turn_right':([214,],[228,]),'pfc_turn_left':([215,],[229,]),'pfc_move_forward':([216,],[230,]),'pfc_draw_circle':([217,],[231,]),'pos_else':([220,],[232,]),'llena_cuadruplo_if':([232,],[241,]),'crea_else_cuadruplo':([233,],[242,]),'guarda_resultado_funcion':([234,],[243,]),'vtc_action':([235,],[244,]),'Exp_ciclo':([237,],[246,]),'regresa_inicio_while':([238,],[253,]),'crea_GOTOV':([239,],[254,]),'pfc_set_position':([240,],[255,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> START EDJO VAR_ID crea_primer_quadruple crea_funcion_global SEMICOLON Vars funciones Main','program',9,'p_inicio','edjo.py',198),
  ('crea_primer_quadruple -> <empty>','crea_primer_quadruple',0,'p_crea_primer_quadruple','edjo.py',203),
  ('crea_funcion_global -> <empty>','crea_funcion_global',0,'p_crea_funcion_global','edjo.py',211),
  ('Vars -> Tipo VAR_ID mas_vars agrega_var_funcion SEMICOLON Vars','Vars',6,'p_Vars','edjo.py',218),
  ('Vars -> <empty>','Vars',0,'p_Vars','edjo.py',219),
  ('Tipo -> INT','Tipo',1,'p_Tipo','edjo.py',223),
  ('Tipo -> DECIMAL','Tipo',1,'p_Tipo','edjo.py',224),
  ('Tipo -> STRING','Tipo',1,'p_Tipo','edjo.py',225),
  ('Tipo -> CHAR','Tipo',1,'p_Tipo','edjo.py',226),
  ('Tipo -> BOOL','Tipo',1,'p_Tipo','edjo.py',227),
  ('mas_vars -> COMMA VAR_ID mas_vars','mas_vars',3,'p_mas_vars','edjo.py',232),
  ('mas_vars -> <empty>','mas_vars',0,'p_mas_vars','edjo.py',233),
  ('agrega_var_funcion -> <empty>','agrega_var_funcion',0,'p_agrega_var_funcion','edjo.py',241),
  ('Asignacion -> VAR_ID push_var_PilaOperandos ASSIGN push_operador_PilaOperadores ExpI SEMICOLON resuelve_asignacion','Asignacion',7,'p_Asignacion','edjo.py',256),
  ('push_var_PilaOperandos -> <empty>','push_var_PilaOperandos',0,'p_push_var_PilaOperandos','edjo.py',261),
  ('push_operador_PilaOperadores -> <empty>','push_operador_PilaOperadores',0,'p_push_operador_PilaOperadores','edjo.py',278),
  ('resuelve_asignacion -> <empty>','resuelve_asignacion',0,'p_resuelve_asignacion','edjo.py',284),
  ('ExpI -> ExpK resuelve_operadores_relacionales','ExpI',2,'p_ExpI','edjo.py',303),
  ('ExpI -> ExpK Operandos push_operador_PilaOperadores ExpK resuelve_operadores_relacionales','ExpI',5,'p_ExpI','edjo.py',304),
  ('Operandos -> LT','Operandos',1,'p_Operandos','edjo.py',308),
  ('Operandos -> GT','Operandos',1,'p_Operandos','edjo.py',309),
  ('Operandos -> NE','Operandos',1,'p_Operandos','edjo.py',310),
  ('Operandos -> LE','Operandos',1,'p_Operandos','edjo.py',311),
  ('Operandos -> GE','Operandos',1,'p_Operandos','edjo.py',312),
  ('Operandos -> EQ','Operandos',1,'p_Operandos','edjo.py',313),
  ('resuelve_operadores_relacionales -> <empty>','resuelve_operadores_relacionales',0,'p_resuelve_operadores_relacionales','edjo.py',319),
  ('ExpK -> ExpT resuelve_termino','ExpK',2,'p_ExpK','edjo.py',346),
  ('ExpK -> ExpT resuelve_termino pos_SUMRES push_operador_PilaOperadores ExpK','ExpK',5,'p_ExpK','edjo.py',347),
  ('resuelve_termino -> <empty>','resuelve_termino',0,'p_resuelve_termino','edjo.py',352),
  ('pos_SUMRES -> PLUS','pos_SUMRES',1,'p_pos_SUMRES','edjo.py',360),
  ('pos_SUMRES -> MINUS','pos_SUMRES',1,'p_pos_SUMRES','edjo.py',361),
  ('ExpT -> ExpF resuelve_factor','ExpT',2,'p_ExpT','edjo.py',366),
  ('ExpT -> ExpF resuelve_factor pos_MULTDIV push_operador_PilaOperadores ExpT','ExpT',5,'p_ExpT','edjo.py',367),
  ('resuelve_factor -> <empty>','resuelve_factor',0,'p_resuelve_factor','edjo.py',371),
  ('pos_MULTDIV -> MULT','pos_MULTDIV',1,'p_pos_MULTDIV','edjo.py',379),
  ('pos_MULTDIV -> DIV','pos_MULTDIV',1,'p_pos_MULTDIV','edjo.py',380),
  ('ExpF -> VAR_CTE','ExpF',1,'p_ExpF','edjo.py',385),
  ('ExpF -> LPAREN agrega_falso ExpI RPAREN quita_falso','ExpF',5,'p_ExpF','edjo.py',386),
  ('ExpF -> VAR_ID push_var_PilaOperandos pos_arreglo','ExpF',3,'p_ExpF','edjo.py',387),
  ('ExpF -> llama_funcion','ExpF',1,'p_ExpF','edjo.py',388),
  ('VAR_CTE -> VAR_INT push_int_PilaOperandos','VAR_CTE',2,'p_VAR_CTE','edjo.py',393),
  ('VAR_CTE -> VAR_DECIMAL push_decimal_PilaOperandos','VAR_CTE',2,'p_VAR_CTE','edjo.py',394),
  ('push_int_PilaOperandos -> <empty>','push_int_PilaOperandos',0,'p_push_int_PilaOperandos','edjo.py',399),
  ('push_decimal_PilaOperandos -> <empty>','push_decimal_PilaOperandos',0,'p_push_decimal_PilaOperandos','edjo.py',409),
  ('agrega_falso -> <empty>','agrega_falso',0,'p_agrega_falso','edjo.py',420),
  ('quita_falso -> <empty>','quita_falso',0,'p_quita_falso','edjo.py',426),
  ('llama_funcion -> VAR_ID LPAREN agrega_falso checa_funcion_si_existe argumentos RPAREN quita_falso resuelve_llamada_funcion guarda_resultado_funcion','llama_funcion',9,'p_llama_funcion','edjo.py',431),
  ('checa_funcion_si_existe -> <empty>','checa_funcion_si_existe',0,'p_checa_funcion_si_existe','edjo.py',436),
  ('argumentos -> ExpI resuelve_argumentos mas_argumentos','argumentos',3,'p_argumentos','edjo.py',451),
  ('argumentos -> <empty>','argumentos',0,'p_argumentos','edjo.py',452),
  ('mas_argumentos -> COMMA ExpI resuelve_argumentos mas_argumentos','mas_argumentos',4,'p_mas_argumentos','edjo.py',456),
  ('mas_argumentos -> <empty>','mas_argumentos',0,'p_mas_argumentos','edjo.py',457),
  ('resuelve_argumentos -> <empty>','resuelve_argumentos',0,'p_resuelve_argumentos','edjo.py',462),
  ('resuelve_llamada_funcion -> <empty>','resuelve_llamada_funcion',0,'p_resuelve_llamada_funcion','edjo.py',481),
  ('guarda_resultado_funcion -> <empty>','guarda_resultado_funcion',0,'p_guarda_resultado_funcion','edjo.py',495),
  ('pos_arreglo -> SLBRACKET ExpI SRBRACKET','pos_arreglo',3,'p_pos_arreglo','edjo.py',511),
  ('pos_arreglo -> <empty>','pos_arreglo',0,'p_pos_arreglo','edjo.py',512),
  ('funciones -> FUNC tipo_funcion VAR_ID LPAREN param RPAREN agrega_funcion LBRACKET Vars reg_brack RBRACKET fin_func_quad funciones','funciones',13,'p_funciones','edjo.py',517),
  ('funciones -> <empty>','funciones',0,'p_funciones','edjo.py',518),
  ('tipo_funcion -> VOID','tipo_funcion',1,'p_tipo_funcion','edjo.py',522),
  ('tipo_funcion -> Tipo','tipo_funcion',1,'p_tipo_funcion','edjo.py',523),
  ('param -> Tipo VAR_ID pos_commaf','param',3,'p_param','edjo.py',528),
  ('param -> <empty>','param',0,'p_param','edjo.py',529),
  ('pos_commaf -> COMMA Tipo VAR_ID pos_commaf','pos_commaf',4,'p_pos_commaf','edjo.py',533),
  ('pos_commaf -> <empty>','pos_commaf',0,'p_pos_commaf','edjo.py',534),
  ('agrega_funcion -> <empty>','agrega_funcion',0,'p_agrega_funcion','edjo.py',544),
  ('fin_func_quad -> <empty>','fin_func_quad',0,'p_fin_func_quad','edjo.py',565),
  ('reg_brack -> Estatutos reg_brack','reg_brack',2,'p_reg_brack','edjo.py',588),
  ('reg_brack -> <empty>','reg_brack',0,'p_reg_brack','edjo.py',589),
  ('Estatutos -> Condicion','Estatutos',1,'p_Estatutos','edjo.py',592),
  ('Estatutos -> Ciclo','Estatutos',1,'p_Estatutos','edjo.py',593),
  ('Estatutos -> Return','Estatutos',1,'p_Estatutos','edjo.py',594),
  ('Estatutos -> Asignacion','Estatutos',1,'p_Estatutos','edjo.py',595),
  ('Estatutos -> Print','Estatutos',1,'p_Estatutos','edjo.py',596),
  ('Estatutos -> Llamada_Func','Estatutos',1,'p_Estatutos','edjo.py',597),
  ('Estatutos -> TurtleMotion','Estatutos',1,'p_Estatutos','edjo.py',598),
  ('Condicion -> IF LPAREN ExpI RPAREN crea_GOTOF LBRACKET reg_brack RBRACKET pos_else llena_cuadruplo_if','Condicion',10,'p_Condicion','edjo.py',601),
  ('crea_GOTOF -> <empty>','crea_GOTOF',0,'p_crea_GOTOF','edjo.py',605),
  ('llena_cuadruplo_if -> <empty>','llena_cuadruplo_if',0,'p_llena_cuadruplo_if','edjo.py',622),
  ('pos_else -> ELSE crea_else_cuadruplo LBRACKET reg_brack RBRACKET','pos_else',5,'p_pos_else','edjo.py',630),
  ('pos_else -> <empty>','pos_else',0,'p_pos_else','edjo.py',631),
  ('crea_else_cuadruplo -> <empty>','crea_else_cuadruplo',0,'p_crea_else_cuadruplo','edjo.py',635),
  ('Return -> RETURN ExpI SEMICOLON resuelve_return','Return',4,'p_Return','edjo.py',647),
  ('resuelve_return -> <empty>','resuelve_return',0,'p_resuelve_return','edjo.py',652),
  ('Print -> PRINT LPAREN VAR_STRING RPAREN SEMICOLON','Print',5,'p_Print','edjo.py',673),
  ('Print -> PRINT LPAREN ExpI RPAREN SEMICOLON crea_print','Print',6,'p_Print','edjo.py',674),
  ('crea_print -> <empty>','crea_print',0,'p_crea_print','edjo.py',678),
  ('Llamada_Func -> VAR_ID LPAREN agrega_falso checa_funcion_si_existe argumentos RPAREN quita_falso resuelve_llamada_funcion SEMICOLON vtc_action','Llamada_Func',10,'p_Llamada_Func','edjo.py',687),
  ('vtc_action -> <empty>','vtc_action',0,'p_vtc_action','edjo.py',691),
  ('Ciclo -> For','Ciclo',1,'p_Ciclo','edjo.py',700),
  ('Ciclo -> While','Ciclo',1,'p_Ciclo','edjo.py',701),
  ('Ciclo -> DoWhile','Ciclo',1,'p_Ciclo','edjo.py',702),
  ('While -> WHILE guarda_numero_cuadruplo LPAREN ExpI RPAREN crea_GOTOF LBRACKET reg_brack RBRACKET regresa_inicio_while','While',10,'p_While','edjo.py',706),
  ('guarda_numero_cuadruplo -> <empty>','guarda_numero_cuadruplo',0,'p_guarda_numero_cuadruplo','edjo.py',710),
  ('regresa_inicio_while -> <empty>','regresa_inicio_while',0,'p_regresa_inicio_while','edjo.py',716),
  ('crea_GOTOV -> <empty>','crea_GOTOV',0,'p_crea_GOTOV','edjo.py',728),
  ('DoWhile -> DO guarda_numero_cuadruplo LBRACKET reg_brack RBRACKET WHILE LPAREN ExpI RPAREN crea_GOTOV SEMICOLON','DoWhile',11,'p_DoWhile','edjo.py',748),
  ('For -> FOR LPAREN VAR_ID ASSIGN ExpI SEMICOLON ExpI SEMICOLON VAR_ID Exp_ciclo RPAREN LBRACKET reg_brack RBRACKET','For',14,'p_For','edjo.py',753),
  ('Exp_ciclo -> PLUS VAR_INT','Exp_ciclo',2,'p_Exp_ciclo','edjo.py',757),
  ('Exp_ciclo -> MINUS VAR_INT','Exp_ciclo',2,'p_Exp_ciclo','edjo.py',758),
  ('Exp_ciclo -> MULT VAR_INT','Exp_ciclo',2,'p_Exp_ciclo','edjo.py',759),
  ('Exp_ciclo -> DIV VAR_INT','Exp_ciclo',2,'p_Exp_ciclo','edjo.py',760),
  ('Exp_ciclo -> PLUSPLUS','Exp_ciclo',1,'p_Exp_ciclo','edjo.py',761),
  ('Exp_ciclo -> MINUSMINUS','Exp_ciclo',1,'p_Exp_ciclo','edjo.py',762),
  ('TurtleMotion -> Position','TurtleMotion',1,'p_TurtleMotion','edjo.py',766),
  ('TurtleMotion -> Right','TurtleMotion',1,'p_TurtleMotion','edjo.py',767),
  ('TurtleMotion -> Left','TurtleMotion',1,'p_TurtleMotion','edjo.py',768),
  ('TurtleMotion -> Forward','TurtleMotion',1,'p_TurtleMotion','edjo.py',769),
  ('TurtleMotion -> Circle','TurtleMotion',1,'p_TurtleMotion','edjo.py',770),
  ('TurtleMotion -> IniciaTurtle','TurtleMotion',1,'p_TurtleMotion','edjo.py',771),
  ('TurtleMotion -> TerminaTurtle','TurtleMotion',1,'p_TurtleMotion','edjo.py',772),
  ('Position -> TUR POINT POS LPAREN ExpI COMMA ExpI RPAREN SEMICOLON pfc_set_position','Position',10,'p_Position','edjo.py',775),
  ('pfc_set_position -> <empty>','pfc_set_position',0,'p_pfc_set_position','edjo.py',779),
  ('Forward -> TUR POINT FORWARD LPAREN ExpI RPAREN SEMICOLON pfc_move_forward','Forward',8,'p_Forward','edjo.py',788),
  ('pfc_move_forward -> <empty>','pfc_move_forward',0,'p_pfc_move_forward','edjo.py',792),
  ('Right -> TUR POINT RIGHT LPAREN ExpI RPAREN SEMICOLON pfc_turn_right','Right',8,'p_Right','edjo.py',800),
  ('pfc_turn_right -> <empty>','pfc_turn_right',0,'p_pfc_turn_right','edjo.py',804),
  ('Left -> TUR POINT LEFT LPAREN ExpI RPAREN SEMICOLON pfc_turn_left','Left',8,'p_Left','edjo.py',812),
  ('pfc_turn_left -> <empty>','pfc_turn_left',0,'p_pfc_turn_left','edjo.py',816),
  ('Circle -> TUR POINT CIRCLE LPAREN ExpI RPAREN SEMICOLON pfc_draw_circle','Circle',8,'p_Circle','edjo.py',824),
  ('pfc_draw_circle -> <empty>','pfc_draw_circle',0,'p_pfc_draw_circle','edjo.py',828),
  ('IniciaTurtle -> TUR POINT TURTLE LPAREN RPAREN SEMICOLON pfc_create_turtle','IniciaTurtle',7,'p_IniciaTurtle','edjo.py',837),
  ('pfc_create_turtle -> <empty>','pfc_create_turtle',0,'p_pfc_create_turtle','edjo.py',841),
  ('TerminaTurtle -> TUR POINT FINISH LPAREN RPAREN SEMICOLON pfc_finish_drawing','TerminaTurtle',7,'p_TerminaTurtle','edjo.py',848),
  ('pfc_finish_drawing -> <empty>','pfc_finish_drawing',0,'p_pfc_finish_drawing','edjo.py',852),
  ('Main -> MAIN agrega_main_funcion LPAREN RPAREN LBRACKET Vars reg_brack RET ZERO SEMICOLON RBRACKET','Main',11,'p_Main','edjo.py',859),
  ('agrega_main_funcion -> <empty>','agrega_main_funcion',0,'p_agrega_main_funcion','edjo.py',863),
]
