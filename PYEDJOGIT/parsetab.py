
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASSIGN BOOL CHAR CIRCLE COMMA DECIMAL DIV DO EDJO ELSE EQ FALSE FOR FORWARD FROM GE GT IF IFELSE IMPORT INT LBRACKET LE LEFT LPAREN LT MAIN MINUS MINUSMINUS MULT NE PLUS PLUSPLUS POINT POS PRINT RBRACKET RET RETURN RIGHT RPAREN SEMICOLON SLBRACKET SRBRACKET START STRING TRUE TUR TURTLE VAR_CHAR VAR_DECIMAL VAR_ID VAR_INT VAR_STRING VOID WHILE ZEROprogram\t:\tSTART EDJO VAR_ID SEMICOLON LibreriaT vars_o_espacio tipo_funciones Main\n\tLibreriaT\t:\tFROM TUR IMPORT TURTLE SEMICOLON\n\tvars_o_espacio\t:\tVars vars_o_espacio\n\t\t\t\t| \n\tVars\t\t:\tTipo reglas_var SEMICOLON\n\tTipo\t\t:\tINT\n\t\t\t|\tDECIMAL\n\t\t\t|\tSTRING\n\t\t\t|\tCHAR\n\t\t\t|\tBOOL\n\treglas_var\t:\tVAR_ID pos_vec pos_comma\n\tpos_vec\t:\tSLBRACKET VAR_INT SRBRACKET\n\t\t\t| \n\tpos_comma\t:\tCOMMA reglas_var\n\t\t\t| \n\tExp\t\t:\tExpI pos_igual\n\tpos_igual\t:\tASSIGN ExpI\n\t\t\t| \n\tExpI\t\t:\tExpK pos_Operandos\n\tpos_Operandos\t:\tOperandos ExpI\n\t\t\t\t| \n\tOperandos\t:\tLT\n\t\t\t|\tGT\n\t\t\t|\tNE\n\t\t\t|\tLE\n\t\t\t|\tGE\n\t\t\t|\tEQ\n\tExpK\t\t:\tExpT pos_SUMRES\n\tpos_SUMRES\t:\tPLUS ExpK\n\t\t\t|\tMINUS ExpK\n\t\t\t| \n\tExpT\t\t:\tExpF pos_MULTDIV\n\tpos_MULTDIV\t:\tMULT ExpT\n\t\t\t|\tDIV ExpT\n\t\t\t| \n\tExpF\t\t:\tVAR_CTE\n\t\t\t|\tLPAREN Exp RPAREN\n\t\t\t|\tSLBRACKET Exp SRBRACKET\n\t\t\t|\tVAR_ID pos_parens\n\tVAR_CTE\t:\tVAR_INT\n\t\t\t|\tVAR_DECIMAL\n\tpos_parens\t:\tLPAREN Exp RPAREN\n\t\t\t|\tSLBRACKET Exp SRBRACKET\n\t\t\t| \n\ttipo_funciones\t:\tFuncs_void tipo_funciones\n\t\t\t\t| \n\tFuncs_void\t:\tVOID VAR_ID LPAREN reg_paren RPAREN LBRACKET vars_o_espacio reg_brack RBRACKET\n\treg_paren\t:\tparam\n\t\t\t|\n\tparam\t:\tTipo VAR_ID pos_commaf\n\tpos_commaf\t:\tCOMMA param\n\t\t\t| \n\treg_brack\t:\tEstatutos reg_brack\n\t\t\t| \n\tEstatutos\t:\tCondicion \n\t\t\t|\tCiclo  \n\t\t\t|\tReturn \n\t\t\t|\tExp SEMICOLON\n\t\t\t|\tPrint \n\t\t\t|\tLlamada_Func \n\t\t\t|\tTurtleMotion \n\tCondicion\t:\tIF LPAREN Exp RPAREN LBRACKET reg_brack RBRACKET pos_else\n\tpos_else\t:\tELSE LBRACKET reg_brack RBRACKET\n\t\t\t| \n\tReturn \t:\tRETURN Exp SEMICOLON\n\tPrint\t:\tPRINT LPAREN VAR_STRING RPAREN SEMICOLON\n\t\t\t|\tPRINT LPAREN Exp RPAREN SEMICOLON\n\tLlamada_Func\t:\tVAR_ID LPAREN paramLlam RPAREN SEMICOLON\n\tparamLlam\t:\tExp pos_commaLlam\n\tpos_commaLlam\t:\tCOMMA paramLlam\n\t\t\t\t| \n\tCiclo\t:\tFor\n\t\t\t|\tWhile\n\t\t\t|\tDoWhile\n\tWhile\t:\tWHILE LPAREN Exp RPAREN LBRACKET reg_brack RBRACKET\n\tDoWhile\t:\tDO LBRACKET reg_brack RBRACKET WHILE LPAREN Exp RPAREN SEMICOLON\n\tFor\t\t:\tFOR LPAREN VAR_ID ASSIGN Exp SEMICOLON Exp SEMICOLON VAR_ID Exp_ciclo RPAREN LBRACKET reg_brack RBRACKET\n\tExp_ciclo\t:\tPLUS VAR_INT\n\t\t\t|\tMINUS VAR_INT\n\t\t\t|\tMULT VAR_INT\n\t\t\t|\tDIV VAR_INT\n\t\t\t|\tPLUSPLUS\n\t\t\t|\tMINUSMINUS\n\tTurtleMotion\t:\tPosition\n\t\t\t|\tRight\n\t\t\t|\tLeft\n\t\t\t|\tForward\n\t\t\t|\tCircle\n\tPosition\t:\tVAR_ID POINT POS LPAREN RPAREN SEMICOLON\n\tForward\t:\tVAR_ID POINT FORWARD LPAREN Exp RPAREN SEMICOLON\n\tRight\t:\tVAR_ID POINT RIGHT LPAREN Exp RPAREN SEMICOLON\n\tLeft\t\t:\tVAR_ID POINT LEFT LPAREN Exp RPAREN SEMICOLON\n\tCircle\t:\tVAR_ID POINT CIRCLE LPAREN Exp RPAREN SEMICOLON\n\tMain\t\t:\tMAIN LPAREN RPAREN LBRACKET vars_o_espacio reg_brack RET ZERO SEMICOLON RBRACKET\n\t'
    
_lr_action_items = {'TURTLE':([17,],[24,]),'DO':([13,20,27,44,47,48,53,54,58,59,60,61,65,66,67,68,71,74,75,78,82,84,86,100,121,165,166,167,175,177,181,188,189,190,191,192,194,198,199,201,215,216,218,],[-4,-3,-5,-4,51,-4,-56,-72,-55,-84,-59,-88,-74,51,-86,-61,-73,-57,-60,-85,-87,51,51,-58,-65,-66,-67,51,-68,51,-89,-75,-91,-90,-93,-92,-64,-62,-76,51,-63,51,-77,]),'RETURN':([13,20,27,44,47,48,53,54,58,59,60,61,65,66,67,68,71,74,75,78,82,84,86,100,121,165,166,167,175,177,181,188,189,190,191,192,194,198,199,201,215,216,218,],[-4,-3,-5,-4,52,-4,-56,-72,-55,-84,-59,-88,-74,52,-86,-61,-73,-57,-60,-85,-87,52,52,-58,-65,-66,-67,52,-68,52,-89,-75,-91,-90,-93,-92,-64,-62,-76,52,-63,52,-77,]),'VOID':([7,13,14,20,22,27,32,144,],[-4,-4,23,-3,23,-5,-2,-47,]),'RET':([13,20,27,44,47,53,54,55,58,59,60,61,65,66,67,68,71,74,75,78,82,98,100,121,165,166,175,181,188,189,190,191,192,194,198,199,215,218,],[-4,-3,-5,-4,-54,-56,-72,89,-55,-84,-59,-88,-74,-54,-86,-61,-73,-57,-60,-85,-87,-53,-58,-65,-66,-67,-68,-89,-75,-91,-90,-93,-92,-64,-62,-76,-63,-77,]),'POS':([93,],[128,]),'CHAR':([7,13,27,32,37,44,48,50,],[11,11,-5,-2,11,11,11,11,]),'WHILE':([13,20,27,44,47,48,53,54,58,59,60,61,65,66,67,68,71,74,75,78,82,84,86,100,121,145,165,166,167,175,177,181,188,189,190,191,192,194,198,199,201,215,216,218,],[-4,-3,-5,-4,57,-4,-56,-72,-55,-84,-59,-88,-74,57,-86,-61,-73,-57,-60,-85,-87,57,57,-58,-65,163,-66,-67,57,-68,57,-89,-75,-91,-90,-93,-92,-64,-62,-76,57,-63,57,-77,]),'PRINT':([13,20,27,44,47,48,53,54,58,59,60,61,65,66,67,68,71,74,75,78,82,84,86,100,121,165,166,167,175,177,181,188,189,190,191,192,194,198,199,201,215,216,218,],[-4,-3,-5,-4,56,-4,-56,-72,-55,-84,-59,-88,-74,56,-86,-61,-73,-57,-60,-85,-87,56,56,-58,-65,-66,-67,56,-68,56,-89,-75,-91,-90,-93,-92,-64,-62,-76,56,-63,56,-77,]),'SRBRACKET':([33,62,64,70,79,80,81,83,87,94,96,103,106,113,117,126,134,136,138,139,140,141,142,143,151,159,],[38,-41,-18,-36,-40,-31,-21,-35,-44,-39,-16,138,-28,-19,-32,151,-17,-37,-38,-29,-30,-20,-34,-33,-43,-42,]),'DIV':([62,63,70,79,83,87,94,136,138,151,159,200,],[-41,-44,-36,-40,115,-44,-39,-37,-38,-43,-42,205,]),'MINUS':([62,63,70,79,80,83,87,94,117,136,138,142,143,151,159,200,],[-41,-44,-36,-40,105,-35,-44,-39,-32,-37,-38,-34,-33,-43,-42,206,]),'MULT':([62,63,70,79,83,87,94,136,138,151,159,200,],[-41,-44,-36,-40,116,-44,-39,-37,-38,-43,-42,208,]),'VAR_DECIMAL':([13,20,27,44,47,48,52,53,54,58,59,60,61,65,66,67,68,71,73,74,75,77,78,82,84,86,90,91,92,95,97,100,102,104,105,107,108,109,110,111,112,114,115,116,120,121,152,154,155,156,158,161,165,166,167,175,177,178,181,185,188,189,190,191,192,194,198,199,201,215,216,218,],[-4,-3,-5,-4,62,-4,62,-56,-72,-55,-84,-59,-88,-74,62,-86,-61,-73,62,-57,-60,62,-85,-87,62,62,62,62,62,62,62,-58,62,62,62,-25,-23,-26,62,-22,-24,-27,62,62,62,-65,62,62,62,62,62,62,-66,-67,62,-68,62,62,-89,62,-75,-91,-90,-93,-92,-64,-62,-76,62,-63,62,-77,]),'LE':([62,63,70,79,80,81,83,87,94,106,117,136,138,139,140,142,143,151,159,],[-41,-44,-36,-40,-31,107,-35,-44,-39,-28,-32,-37,-38,-29,-30,-34,-33,-43,-42,]),'RPAREN':([36,37,41,43,46,49,62,64,70,79,80,81,83,85,87,94,96,101,106,113,117,123,124,125,132,133,134,136,137,138,139,140,141,142,143,146,151,153,157,159,168,170,171,172,173,174,187,202,203,204,211,212,213,214,],[40,-49,45,-48,-52,-50,-41,-18,-36,-40,-31,-21,-35,-51,-44,-39,-16,136,-28,-19,-32,148,149,150,159,160,-17,-37,162,-38,-29,-30,-20,-34,-33,159,-43,169,-69,-42,180,182,183,184,-70,-71,195,-83,-82,210,-81,-79,-78,-80,]),'SEMICOLON':([4,18,19,24,26,35,38,39,62,63,64,70,72,79,80,81,83,87,88,94,96,106,113,117,122,134,136,138,139,140,141,142,143,148,149,151,159,160,169,176,180,182,183,184,193,195,],[5,-13,27,32,-15,-11,-12,-14,-41,-44,-18,-36,100,-40,-31,-21,-35,-44,121,-39,-16,-28,-19,-32,147,-17,-37,-38,-29,-30,-20,-34,-33,165,166,-43,-42,175,181,185,189,190,191,192,196,199,]),'POINT':([63,],[93,]),'VAR_ID':([3,9,10,11,12,13,15,16,20,23,27,34,42,44,47,48,52,53,54,58,59,60,61,65,66,67,68,71,73,74,75,77,78,82,84,86,90,91,92,95,97,99,100,102,104,105,107,108,109,110,111,112,114,115,116,120,121,152,154,155,156,158,161,165,166,167,175,177,178,181,185,188,189,190,191,192,194,196,198,199,201,215,216,218,],[4,18,-6,-9,-10,-4,-7,-8,-3,31,-5,18,46,-4,63,-4,87,-56,-72,-55,-84,-59,-88,-74,63,-86,-61,-73,87,-57,-60,87,-85,-87,63,63,87,87,87,87,87,135,-58,87,87,87,-25,-23,-26,87,-22,-24,-27,87,87,87,-65,87,87,87,87,87,87,-66,-67,63,-68,63,87,-89,87,-75,-91,-90,-93,-92,-64,200,-62,-76,63,-63,63,-77,]),'NE':([62,63,70,79,80,81,83,87,94,106,117,136,138,139,140,142,143,151,159,],[-41,-44,-36,-40,-31,112,-35,-44,-39,-28,-32,-37,-38,-29,-30,-34,-33,-43,-42,]),'PLUS':([62,63,70,79,80,83,87,94,117,136,138,142,143,151,159,200,],[-41,-44,-36,-40,104,-35,-44,-39,-32,-37,-38,-34,-33,-43,-42,207,]),'LT':([62,63,70,79,80,81,83,87,94,106,117,136,138,139,140,142,143,151,159,],[-41,-44,-36,-40,-31,111,-35,-44,-39,-28,-32,-37,-38,-29,-30,-34,-33,-43,-42,]),'COMMA':([18,26,38,46,62,64,70,79,80,81,83,87,94,96,106,113,117,132,134,136,138,139,140,141,142,143,151,159,174,],[-13,34,-12,50,-41,-18,-36,-40,-31,-21,-35,-44,-39,-16,-28,-19,-32,158,-17,-37,-38,-29,-30,-20,-34,-33,-43,-42,158,]),'IMPORT':([8,],[17,]),'DECIMAL':([7,13,27,32,37,44,48,50,],[15,15,-5,-2,15,15,15,15,]),'$end':([2,29,164,],[0,-1,-94,]),'GT':([62,63,70,79,80,81,83,87,94,106,117,136,138,139,140,142,143,151,159,],[-41,-44,-36,-40,-31,108,-35,-44,-39,-28,-32,-37,-38,-29,-30,-34,-33,-43,-42,]),'STRING':([7,13,27,32,37,44,48,50,],[16,16,-5,-2,16,16,16,16,]),'FOR':([13,20,27,44,47,48,53,54,58,59,60,61,65,66,67,68,71,74,75,78,82,84,86,100,121,165,166,167,175,177,181,188,189,190,191,192,194,198,199,201,215,216,218,],[-4,-3,-5,-4,69,-4,-56,-72,-55,-84,-59,-88,-74,69,-86,-61,-73,-57,-60,-85,-87,69,69,-58,-65,-66,-67,69,-68,69,-89,-75,-91,-90,-93,-92,-64,-62,-76,69,-63,69,-77,]),'PLUSPLUS':([200,],[203,]),'EDJO':([1,],[3,]),'VAR_STRING':([90,],[123,]),'ELSE':([194,],[197,]),'START':([0,],[1,]),'GE':([62,63,70,79,80,81,83,87,94,106,117,136,138,139,140,142,143,151,159,],[-41,-44,-36,-40,-31,109,-35,-44,-39,-28,-32,-37,-38,-29,-30,-34,-33,-43,-42,]),'LPAREN':([13,20,27,28,31,44,47,48,52,53,54,56,57,58,59,60,61,63,65,66,67,68,69,71,73,74,75,76,77,78,82,84,86,87,90,91,92,95,97,100,102,104,105,107,108,109,110,111,112,114,115,116,120,121,127,128,129,130,131,152,154,155,156,158,161,163,165,166,167,175,177,178,181,185,188,189,190,191,192,194,198,199,201,215,216,218,],[-4,-3,-5,36,37,-4,73,-4,73,-56,-72,90,91,-55,-84,-59,-88,95,-74,73,-86,-61,99,-73,73,-57,-60,102,73,-85,-87,73,73,120,73,73,73,73,73,-58,73,73,73,-25,-23,-26,73,-22,-24,-27,73,73,73,-65,152,153,154,155,156,73,73,73,73,73,73,178,-66,-67,73,-68,73,73,-89,73,-75,-91,-90,-93,-92,-64,-62,-76,73,-63,73,-77,]),'FORWARD':([93,],[129,]),'MINUSMINUS':([200,],[202,]),'EQ':([62,63,70,79,80,81,83,87,94,106,117,136,138,139,140,142,143,151,159,],[-41,-44,-36,-40,-31,114,-35,-44,-39,-28,-32,-37,-38,-29,-30,-34,-33,-43,-42,]),'CIRCLE':([93,],[130,]),'IF':([13,20,27,44,47,48,53,54,58,59,60,61,65,66,67,68,71,74,75,78,82,84,86,100,121,165,166,167,175,177,181,188,189,190,191,192,194,198,199,201,215,216,218,],[-4,-3,-5,-4,76,-4,-56,-72,-55,-84,-59,-88,-74,76,-86,-61,-73,-57,-60,-85,-87,76,76,-58,-65,-66,-67,76,-68,76,-89,-75,-91,-90,-93,-92,-64,-62,-76,76,-63,76,-77,]),'LBRACKET':([40,45,51,150,162,197,210,],[44,48,86,167,177,201,216,]),'SLBRACKET':([13,18,20,27,44,47,48,52,53,54,58,59,60,61,63,65,66,67,68,71,73,74,75,77,78,82,84,86,87,90,91,92,95,97,100,102,104,105,107,108,109,110,111,112,114,115,116,120,121,152,154,155,156,158,161,165,166,167,175,177,178,181,185,188,189,190,191,192,194,198,199,201,215,216,218,],[-4,25,-3,-5,-4,77,-4,77,-56,-72,-55,-84,-59,-88,92,-74,77,-86,-61,-73,77,-57,-60,77,-85,-87,77,77,92,77,77,77,77,77,-58,77,77,77,-25,-23,-26,77,-22,-24,-27,77,77,77,-65,77,77,77,77,77,77,-66,-67,77,-68,77,77,-89,77,-75,-91,-90,-93,-92,-64,-62,-76,77,-63,77,-77,]),'RIGHT':([93,],[127,]),'FROM':([5,],[6,]),'VAR_INT':([13,20,25,27,44,47,48,52,53,54,58,59,60,61,65,66,67,68,71,73,74,75,77,78,82,84,86,90,91,92,95,97,100,102,104,105,107,108,109,110,111,112,114,115,116,120,121,152,154,155,156,158,161,165,166,167,175,177,178,181,185,188,189,190,191,192,194,198,199,201,205,206,207,208,215,216,218,],[-4,-3,33,-5,-4,79,-4,79,-56,-72,-55,-84,-59,-88,-74,79,-86,-61,-73,79,-57,-60,79,-85,-87,79,79,79,79,79,79,79,-58,79,79,79,-25,-23,-26,79,-22,-24,-27,79,79,79,-65,79,79,79,79,79,79,-66,-67,79,-68,79,79,-89,79,-75,-91,-90,-93,-92,-64,-62,-76,79,211,212,213,214,-63,79,-77,]),'INT':([7,13,27,32,37,44,48,50,],[10,10,-5,-2,10,10,10,10,]),'TUR':([6,],[8,]),'ZERO':([89,],[122,]),'ASSIGN':([62,63,64,70,79,80,81,83,87,94,106,113,117,135,136,138,139,140,141,142,143,151,159,],[-41,-44,97,-36,-40,-31,-21,-35,-44,-39,-28,-19,-32,161,-37,-38,-29,-30,-20,-34,-33,-43,-42,]),'LEFT':([93,],[131,]),'BOOL':([7,13,27,32,37,44,48,50,],[12,12,-5,-2,12,12,12,12,]),'RBRACKET':([13,20,27,48,53,54,58,59,60,61,65,66,67,68,71,74,75,78,82,84,86,98,100,118,119,121,147,165,166,167,175,177,179,181,186,188,189,190,191,192,194,198,199,201,209,215,216,217,218,],[-4,-3,-5,-4,-56,-72,-55,-84,-59,-88,-74,-54,-86,-61,-73,-57,-60,-85,-87,-54,-54,-53,-58,144,145,-65,164,-66,-67,-54,-68,-54,188,-89,194,-75,-91,-90,-93,-92,-64,-62,-76,-54,215,-63,-54,218,-77,]),'MAIN':([7,13,14,20,21,22,27,30,32,144,],[-4,-4,-46,-3,28,-46,-5,-45,-2,-47,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Ciclo':([47,66,84,86,167,177,201,216,],[53,53,53,53,53,53,53,53,]),'Tipo':([7,13,37,44,48,50,],[9,9,42,9,9,42,]),'reg_brack':([47,66,84,86,167,177,201,216,],[55,98,118,119,179,186,209,217,]),'Operandos':([81,],[110,]),'pos_SUMRES':([80,],[106,]),'VAR_CTE':([47,52,66,73,77,84,86,90,91,92,95,97,102,104,105,110,115,116,120,152,154,155,156,158,161,167,177,178,185,201,216,],[70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,]),'Exp_ciclo':([200,],[204,]),'tipo_funciones':([14,22,],[21,30,]),'Condicion':([47,66,84,86,167,177,201,216,],[58,58,58,58,58,58,58,58,]),'Forward':([47,66,84,86,167,177,201,216,],[82,82,82,82,82,82,82,82,]),'Circle':([47,66,84,86,167,177,201,216,],[61,61,61,61,61,61,61,61,]),'Main':([21,],[29,]),'pos_MULTDIV':([83,],[117,]),'Return':([47,66,84,86,167,177,201,216,],[74,74,74,74,74,74,74,74,]),'For':([47,66,84,86,167,177,201,216,],[54,54,54,54,54,54,54,54,]),'pos_igual':([64,],[96,]),'Print':([47,66,84,86,167,177,201,216,],[60,60,60,60,60,60,60,60,]),'ExpI':([47,52,66,73,77,84,86,90,91,92,95,97,102,110,120,152,154,155,156,158,161,167,177,178,185,201,216,],[64,64,64,64,64,64,64,64,64,64,64,134,64,141,64,64,64,64,64,64,64,64,64,64,64,64,64,]),'param':([37,50,],[43,85,]),'DoWhile':([47,66,84,86,167,177,201,216,],[65,65,65,65,65,65,65,65,]),'program':([0,],[2,]),'LibreriaT':([5,],[7,]),'pos_vec':([18,],[26,]),'reg_paren':([37,],[41,]),'TurtleMotion':([47,66,84,86,167,177,201,216,],[68,68,68,68,68,68,68,68,]),'pos_parens':([63,87,],[94,94,]),'Estatutos':([47,66,84,86,167,177,201,216,],[66,66,66,66,66,66,66,66,]),'vars_o_espacio':([7,13,44,48,],[14,20,47,84,]),'pos_commaLlam':([132,174,],[157,157,]),'pos_commaf':([46,],[49,]),'Right':([47,66,84,86,167,177,201,216,],[78,78,78,78,78,78,78,78,]),'Funcs_void':([14,22,],[22,22,]),'Exp':([47,52,66,73,77,84,86,90,91,92,95,102,120,152,154,155,156,158,161,167,177,178,185,201,216,],[72,88,72,101,103,72,72,124,125,126,132,137,146,168,170,171,172,174,176,72,72,187,193,72,72,]),'Position':([47,66,84,86,167,177,201,216,],[59,59,59,59,59,59,59,59,]),'Llamada_Func':([47,66,84,86,167,177,201,216,],[75,75,75,75,75,75,75,75,]),'Left':([47,66,84,86,167,177,201,216,],[67,67,67,67,67,67,67,67,]),'pos_comma':([26,],[35,]),'paramLlam':([95,158,],[133,173,]),'Vars':([7,13,44,48,],[13,13,13,13,]),'pos_Operandos':([81,],[113,]),'While':([47,66,84,86,167,177,201,216,],[71,71,71,71,71,71,71,71,]),'ExpT':([47,52,66,73,77,84,86,90,91,92,95,97,102,104,105,110,115,116,120,152,154,155,156,158,161,167,177,178,185,201,216,],[80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,142,143,80,80,80,80,80,80,80,80,80,80,80,80,80,]),'ExpK':([47,52,66,73,77,84,86,90,91,92,95,97,102,104,105,110,120,152,154,155,156,158,161,167,177,178,185,201,216,],[81,81,81,81,81,81,81,81,81,81,81,81,81,139,140,81,81,81,81,81,81,81,81,81,81,81,81,81,81,]),'reglas_var':([9,34,],[19,39,]),'pos_else':([194,],[198,]),'ExpF':([47,52,66,73,77,84,86,90,91,92,95,97,102,104,105,110,115,116,120,152,154,155,156,158,161,167,177,178,185,201,216,],[83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> START EDJO VAR_ID SEMICOLON LibreriaT vars_o_espacio tipo_funciones Main','program',8,'p_inicio','bien.py',187),
  ('LibreriaT -> FROM TUR IMPORT TURTLE SEMICOLON','LibreriaT',5,'p_LibreriaT','bien.py',190),
  ('vars_o_espacio -> Vars vars_o_espacio','vars_o_espacio',2,'p_vars_o_espacio','bien.py',194),
  ('vars_o_espacio -> <empty>','vars_o_espacio',0,'p_vars_o_espacio','bien.py',195),
  ('Vars -> Tipo reglas_var SEMICOLON','Vars',3,'p_Vars','bien.py',199),
  ('Tipo -> INT','Tipo',1,'p_Tipo','bien.py',203),
  ('Tipo -> DECIMAL','Tipo',1,'p_Tipo','bien.py',204),
  ('Tipo -> STRING','Tipo',1,'p_Tipo','bien.py',205),
  ('Tipo -> CHAR','Tipo',1,'p_Tipo','bien.py',206),
  ('Tipo -> BOOL','Tipo',1,'p_Tipo','bien.py',207),
  ('reglas_var -> VAR_ID pos_vec pos_comma','reglas_var',3,'p_reglas_var','bien.py',211),
  ('pos_vec -> SLBRACKET VAR_INT SRBRACKET','pos_vec',3,'p_pos_vec','bien.py',215),
  ('pos_vec -> <empty>','pos_vec',0,'p_pos_vec','bien.py',216),
  ('pos_comma -> COMMA reglas_var','pos_comma',2,'p_pos_comma','bien.py',220),
  ('pos_comma -> <empty>','pos_comma',0,'p_pos_comma','bien.py',221),
  ('Exp -> ExpI pos_igual','Exp',2,'p_Exp','bien.py',225),
  ('pos_igual -> ASSIGN ExpI','pos_igual',2,'p_pos_igual','bien.py',229),
  ('pos_igual -> <empty>','pos_igual',0,'p_pos_igual','bien.py',230),
  ('ExpI -> ExpK pos_Operandos','ExpI',2,'p_ExpI','bien.py',234),
  ('pos_Operandos -> Operandos ExpI','pos_Operandos',2,'p_pos_Operandos','bien.py',238),
  ('pos_Operandos -> <empty>','pos_Operandos',0,'p_pos_Operandos','bien.py',239),
  ('Operandos -> LT','Operandos',1,'p_Operandos','bien.py',243),
  ('Operandos -> GT','Operandos',1,'p_Operandos','bien.py',244),
  ('Operandos -> NE','Operandos',1,'p_Operandos','bien.py',245),
  ('Operandos -> LE','Operandos',1,'p_Operandos','bien.py',246),
  ('Operandos -> GE','Operandos',1,'p_Operandos','bien.py',247),
  ('Operandos -> EQ','Operandos',1,'p_Operandos','bien.py',248),
  ('ExpK -> ExpT pos_SUMRES','ExpK',2,'p_ExpK','bien.py',252),
  ('pos_SUMRES -> PLUS ExpK','pos_SUMRES',2,'p_pos_SUMRES','bien.py',256),
  ('pos_SUMRES -> MINUS ExpK','pos_SUMRES',2,'p_pos_SUMRES','bien.py',257),
  ('pos_SUMRES -> <empty>','pos_SUMRES',0,'p_pos_SUMRES','bien.py',258),
  ('ExpT -> ExpF pos_MULTDIV','ExpT',2,'p_ExpT','bien.py',262),
  ('pos_MULTDIV -> MULT ExpT','pos_MULTDIV',2,'p_pos_MULTDIV','bien.py',266),
  ('pos_MULTDIV -> DIV ExpT','pos_MULTDIV',2,'p_pos_MULTDIV','bien.py',267),
  ('pos_MULTDIV -> <empty>','pos_MULTDIV',0,'p_pos_MULTDIV','bien.py',268),
  ('ExpF -> VAR_CTE','ExpF',1,'p_ExpF','bien.py',272),
  ('ExpF -> LPAREN Exp RPAREN','ExpF',3,'p_ExpF','bien.py',273),
  ('ExpF -> SLBRACKET Exp SRBRACKET','ExpF',3,'p_ExpF','bien.py',274),
  ('ExpF -> VAR_ID pos_parens','ExpF',2,'p_ExpF','bien.py',275),
  ('VAR_CTE -> VAR_INT','VAR_CTE',1,'p_VAR_CTE','bien.py',278),
  ('VAR_CTE -> VAR_DECIMAL','VAR_CTE',1,'p_VAR_CTE','bien.py',279),
  ('pos_parens -> LPAREN Exp RPAREN','pos_parens',3,'p_pos_parens','bien.py',283),
  ('pos_parens -> SLBRACKET Exp SRBRACKET','pos_parens',3,'p_pos_parens','bien.py',284),
  ('pos_parens -> <empty>','pos_parens',0,'p_pos_parens','bien.py',285),
  ('tipo_funciones -> Funcs_void tipo_funciones','tipo_funciones',2,'p_tipo_funciones','bien.py',289),
  ('tipo_funciones -> <empty>','tipo_funciones',0,'p_tipo_funciones','bien.py',290),
  ('Funcs_void -> VOID VAR_ID LPAREN reg_paren RPAREN LBRACKET vars_o_espacio reg_brack RBRACKET','Funcs_void',9,'p_Funcs_void','bien.py',293),
  ('reg_paren -> param','reg_paren',1,'p_reg_paren','bien.py',297),
  ('reg_paren -> <empty>','reg_paren',0,'p_reg_paren','bien.py',298),
  ('param -> Tipo VAR_ID pos_commaf','param',3,'p_param','bien.py',302),
  ('pos_commaf -> COMMA param','pos_commaf',2,'p_pos_commaf','bien.py',305),
  ('pos_commaf -> <empty>','pos_commaf',0,'p_pos_commaf','bien.py',306),
  ('reg_brack -> Estatutos reg_brack','reg_brack',2,'p_reg_brack','bien.py',310),
  ('reg_brack -> <empty>','reg_brack',0,'p_reg_brack','bien.py',311),
  ('Estatutos -> Condicion','Estatutos',1,'p_Estatutos','bien.py',314),
  ('Estatutos -> Ciclo','Estatutos',1,'p_Estatutos','bien.py',315),
  ('Estatutos -> Return','Estatutos',1,'p_Estatutos','bien.py',316),
  ('Estatutos -> Exp SEMICOLON','Estatutos',2,'p_Estatutos','bien.py',317),
  ('Estatutos -> Print','Estatutos',1,'p_Estatutos','bien.py',318),
  ('Estatutos -> Llamada_Func','Estatutos',1,'p_Estatutos','bien.py',319),
  ('Estatutos -> TurtleMotion','Estatutos',1,'p_Estatutos','bien.py',320),
  ('Condicion -> IF LPAREN Exp RPAREN LBRACKET reg_brack RBRACKET pos_else','Condicion',8,'p_Condicion','bien.py',323),
  ('pos_else -> ELSE LBRACKET reg_brack RBRACKET','pos_else',4,'p_pos_else','bien.py',327),
  ('pos_else -> <empty>','pos_else',0,'p_pos_else','bien.py',328),
  ('Return -> RETURN Exp SEMICOLON','Return',3,'p_Return','bien.py',331),
  ('Print -> PRINT LPAREN VAR_STRING RPAREN SEMICOLON','Print',5,'p_Print','bien.py',334),
  ('Print -> PRINT LPAREN Exp RPAREN SEMICOLON','Print',5,'p_Print','bien.py',335),
  ('Llamada_Func -> VAR_ID LPAREN paramLlam RPAREN SEMICOLON','Llamada_Func',5,'p_Llamada_Func','bien.py',339),
  ('paramLlam -> Exp pos_commaLlam','paramLlam',2,'p_paramLlam','bien.py',343),
  ('pos_commaLlam -> COMMA paramLlam','pos_commaLlam',2,'p_pos_commaLlam','bien.py',347),
  ('pos_commaLlam -> <empty>','pos_commaLlam',0,'p_pos_commaLlam','bien.py',348),
  ('Ciclo -> For','Ciclo',1,'p_Ciclo','bien.py',351),
  ('Ciclo -> While','Ciclo',1,'p_Ciclo','bien.py',352),
  ('Ciclo -> DoWhile','Ciclo',1,'p_Ciclo','bien.py',353),
  ('While -> WHILE LPAREN Exp RPAREN LBRACKET reg_brack RBRACKET','While',7,'p_While','bien.py',356),
  ('DoWhile -> DO LBRACKET reg_brack RBRACKET WHILE LPAREN Exp RPAREN SEMICOLON','DoWhile',9,'p_DoWhile','bien.py',360),
  ('For -> FOR LPAREN VAR_ID ASSIGN Exp SEMICOLON Exp SEMICOLON VAR_ID Exp_ciclo RPAREN LBRACKET reg_brack RBRACKET','For',14,'p_For','bien.py',364),
  ('Exp_ciclo -> PLUS VAR_INT','Exp_ciclo',2,'p_Exp_ciclo','bien.py',368),
  ('Exp_ciclo -> MINUS VAR_INT','Exp_ciclo',2,'p_Exp_ciclo','bien.py',369),
  ('Exp_ciclo -> MULT VAR_INT','Exp_ciclo',2,'p_Exp_ciclo','bien.py',370),
  ('Exp_ciclo -> DIV VAR_INT','Exp_ciclo',2,'p_Exp_ciclo','bien.py',371),
  ('Exp_ciclo -> PLUSPLUS','Exp_ciclo',1,'p_Exp_ciclo','bien.py',372),
  ('Exp_ciclo -> MINUSMINUS','Exp_ciclo',1,'p_Exp_ciclo','bien.py',373),
  ('TurtleMotion -> Position','TurtleMotion',1,'p_TurtleMotion','bien.py',377),
  ('TurtleMotion -> Right','TurtleMotion',1,'p_TurtleMotion','bien.py',378),
  ('TurtleMotion -> Left','TurtleMotion',1,'p_TurtleMotion','bien.py',379),
  ('TurtleMotion -> Forward','TurtleMotion',1,'p_TurtleMotion','bien.py',380),
  ('TurtleMotion -> Circle','TurtleMotion',1,'p_TurtleMotion','bien.py',381),
  ('Position -> VAR_ID POINT POS LPAREN RPAREN SEMICOLON','Position',6,'p_Position','bien.py',384),
  ('Forward -> VAR_ID POINT FORWARD LPAREN Exp RPAREN SEMICOLON','Forward',7,'p_Forward','bien.py',387),
  ('Right -> VAR_ID POINT RIGHT LPAREN Exp RPAREN SEMICOLON','Right',7,'p_Right','bien.py',390),
  ('Left -> VAR_ID POINT LEFT LPAREN Exp RPAREN SEMICOLON','Left',7,'p_Left','bien.py',393),
  ('Circle -> VAR_ID POINT CIRCLE LPAREN Exp RPAREN SEMICOLON','Circle',7,'p_Circle','bien.py',396),
  ('Main -> MAIN LPAREN RPAREN LBRACKET vars_o_espacio reg_brack RET ZERO SEMICOLON RBRACKET','Main',10,'p_Main','bien.py',400),
]