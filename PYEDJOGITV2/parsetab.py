
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'LT EQ GT NE LE GE ASSIGN PLUSPLUS MINUSMINUS PLUS MINUS MULT DIV LPAREN RPAREN LBRACKET RBRACKET SLBRACKET SRBRACKET SEMICOLON COMMA IF ELSE IFELSE INT DECIMAL STRING CHAR BOOL PRINT START EDJO VOID RETURN MAIN FOR VAR_ID VAR_INT VAR_DECIMAL VAR_CHAR VAR_STRING TRUE FALSE DO WHILE FROM IMPORT POINT POS FORWARD CIRCLE LEFT RIGHT TUR TURTLE ZERO RETprogram\t:\tSTART EDJO VAR_ID cmq_action cfd_action SEMICOLON Vars funciones Main\n\tcmq_action\t: \n\tcfd_action\t: \n\tVars\t\t:\tTipo VAR_ID mas_vars adv_action SEMICOLON Vars\n\t\t\t| \n\tTipo\t\t:\tINT\n\t\t\t|\tDECIMAL\n\t\t\t|\tSTRING\n\t\t\t|\tCHAR\n\t\t\t|\tBOOL\n\tmas_vars\t:\tCOMMA VAR_ID mas_vars\n\t\t\t| \n\tadv_action\t: \n\tExp\t\t:\tExpI pos_igual\n\tpos_igual\t:\tASSIGN ExpI\n\t\t\t| \n\tExpI\t\t:\tExpK pos_Operandos\n\tpos_Operandos\t:\tOperandos ExpI\n\t\t\t\t| \n\tOperandos\t:\tLT\n\t\t\t|\tGT\n\t\t\t|\tNE\n\t\t\t|\tLE\n\t\t\t|\tGE\n\t\t\t|\tEQ\n\tExpK\t\t:\tExpT pos_SUMRES\n\tpos_SUMRES\t:\tPLUS ExpK\n\t\t\t|\tMINUS ExpK\n\t\t\t| \n\tExpT\t\t:\tExpF pos_MULTDIV\n\tpos_MULTDIV\t:\tMULT ExpT\n\t\t\t|\tDIV ExpT\n\t\t\t| \n\tExpF\t\t:\tVAR_CTE\n\t\t\t|\tLPAREN Exp RPAREN\n\t\t\t|\tSLBRACKET Exp SRBRACKET\n\t\t\t|\tVAR_ID pos_parens\n\tVAR_CTE\t:\tVAR_INT\n\t\t\t|\tVAR_DECIMAL\n\tpos_parens\t:\tLPAREN Exp RPAREN\n\t\t\t|\tSLBRACKET Exp SRBRACKET\n\t\t\t| \n\tfunciones\t:\ttipo_funcion VAR_ID LPAREN param RPAREN adf_action LBRACKET Vars reg_brack RBRACKET enp_action funciones\n\t\t\t| \n\ttipo_funcion\t:\tVOID\n\t\t\t|\tTipo\n\tparam\t:\tTipo VAR_ID pos_commaf\n\t\t\t| \n\tpos_commaf\t:\tCOMMA Tipo VAR_ID pos_commaf\n\t\t\t| \n\tadf_action\t: \n\tenp_action\t: \n\treg_brack\t:\tEstatutos reg_brack\n\t\t\t| \n\tEstatutos\t:\tCondicion \n\t\t\t|\tCiclo  \n\t\t\t|\tReturn \n\t\t\t|\tExp SEMICOLON\n\t\t\t|\tPrint \n\t\t\t|\tLlamada_Func \n\t\t\t|\tTurtleMotion \n\tCondicion\t:\tIF LPAREN Exp RPAREN LBRACKET reg_brack RBRACKET pos_else\n\tpos_else\t:\tELSE LBRACKET reg_brack RBRACKET\n\t\t\t| \n\tReturn \t:\tRETURN Exp SEMICOLON\n\tPrint\t:\tPRINT LPAREN VAR_STRING RPAREN SEMICOLON\n\t\t\t|\tPRINT LPAREN Exp RPAREN SEMICOLON\n\tLlamada_Func\t:\tVAR_ID LPAREN paramLlam RPAREN SEMICOLON\n\tparamLlam\t:\tExp pos_commaLlam\n\tpos_commaLlam\t:\tCOMMA paramLlam\n\t\t\t\t| \n\tCiclo\t:\tFor\n\t\t\t|\tWhile\n\t\t\t|\tDoWhile\n\tWhile\t:\tWHILE LPAREN Exp RPAREN LBRACKET reg_brack RBRACKET\n\tDoWhile\t:\tDO LBRACKET reg_brack RBRACKET WHILE LPAREN Exp RPAREN SEMICOLON\n\tFor\t\t:\tFOR LPAREN VAR_ID ASSIGN Exp SEMICOLON Exp SEMICOLON VAR_ID Exp_ciclo RPAREN LBRACKET reg_brack RBRACKET\n\tExp_ciclo\t:\tPLUS VAR_INT\n\t\t\t|\tMINUS VAR_INT\n\t\t\t|\tMULT VAR_INT\n\t\t\t|\tDIV VAR_INT\n\t\t\t|\tPLUSPLUS\n\t\t\t|\tMINUSMINUS\n\tTurtleMotion\t:\tPosition\n\t\t\t|\tRight\n\t\t\t|\tLeft\n\t\t\t|\tForward\n\t\t\t|\tCircle\n\tPosition\t:\tVAR_ID POINT POS LPAREN RPAREN SEMICOLON\n\tForward\t:\tVAR_ID POINT FORWARD LPAREN Exp RPAREN SEMICOLON\n\tRight\t:\tVAR_ID POINT RIGHT LPAREN Exp RPAREN SEMICOLON\n\tLeft\t\t:\tVAR_ID POINT LEFT LPAREN Exp RPAREN SEMICOLON\n\tCircle\t:\tVAR_ID POINT CIRCLE LPAREN Exp RPAREN SEMICOLON\n\tMain\t\t:\tMAIN LPAREN RPAREN LBRACKET Vars reg_brack RET ZERO SEMICOLON RBRACKET\n\t'
    
_lr_action_items = {'DO':([29,34,37,41,42,45,46,50,51,53,54,56,60,61,63,66,69,71,72,76,77,79,108,131,160,168,169,170,171,178,184,185,186,187,188,189,192,195,196,206,212,214,],[-5,-4,-5,44,-5,-60,-85,-88,44,-72,-59,-56,-87,-74,-84,-61,-73,-86,-55,-57,44,44,-58,-65,-68,44,-67,-66,44,-89,-92,-93,-91,-90,-64,-75,-62,-76,44,-63,44,-77,]),'LEFT':([87,],[119,]),'GT':([49,52,55,58,62,67,75,85,90,94,97,125,126,129,130,135,137,141,143,],[-38,-39,-42,-33,-29,100,-34,-37,-30,-26,-42,-31,-32,-27,-28,-36,-35,-41,-40,]),'SLBRACKET':([29,34,37,41,42,45,46,50,51,53,54,55,56,60,61,63,64,66,68,69,71,72,74,76,77,79,81,84,86,88,89,91,92,93,95,97,98,99,100,101,102,104,105,106,108,131,132,145,146,147,148,150,156,160,168,169,170,171,174,178,182,184,185,186,187,188,189,192,195,196,206,212,214,],[-5,-4,-5,68,-5,-60,-85,-88,68,-72,-59,84,-56,-87,-74,-84,68,-61,68,-73,-86,-55,68,-57,68,68,68,68,68,68,68,68,68,68,68,84,68,-24,-21,-20,-22,68,-25,-23,-58,-65,68,68,68,68,68,68,68,-68,68,-67,-66,68,68,-89,68,-92,-93,-91,-90,-64,-75,-62,-76,68,-63,68,-77,]),'RIGHT':([87,],[121,]),'VAR_INT':([29,34,37,41,42,45,46,50,51,53,54,56,60,61,63,64,66,68,69,71,72,74,76,77,79,81,84,86,88,89,91,92,93,95,98,99,100,101,102,104,105,106,108,131,132,145,146,147,148,150,156,160,168,169,170,171,174,178,182,184,185,186,187,188,189,192,195,196,199,200,203,204,206,212,214,],[-5,-4,-5,49,-5,-60,-85,-88,49,-72,-59,-56,-87,-74,-84,49,-61,49,-73,-86,-55,49,-57,49,49,49,49,49,49,49,49,49,49,49,49,-24,-21,-20,-22,49,-25,-23,-58,-65,49,49,49,49,49,49,49,-68,49,-67,-66,49,49,-89,49,-92,-93,-91,-90,-64,-75,-62,-76,49,207,208,210,211,-63,49,-77,]),'PLUS':([49,52,55,58,62,75,85,90,97,125,126,135,137,141,143,197,],[-38,-39,-42,-33,93,-34,-37,-30,-42,-31,-32,-36,-35,-41,-40,203,]),'VAR_STRING':([92,],[128,]),'POINT':([55,],[87,]),'DIV':([49,52,55,58,75,85,97,135,137,141,143,197,],[-38,-39,-42,91,-34,-37,-42,-36,-35,-41,-40,204,]),'BOOL':([7,12,27,29,34,37,39,42,138,157,],[8,8,8,8,-4,8,8,8,-52,8,]),'MULT':([49,52,55,58,75,85,97,135,137,141,143,197,],[-38,-39,-42,89,-34,-37,-42,-36,-35,-41,-40,199,]),'NE':([49,52,55,58,62,67,75,85,90,94,97,125,126,129,130,135,137,141,143,],[-38,-39,-42,-33,-29,102,-34,-37,-30,-26,-42,-31,-32,-27,-28,-36,-35,-41,-40,]),'FORWARD':([87,],[123,]),'CHAR':([7,12,27,29,34,37,39,42,138,157,],[10,10,10,10,-4,10,10,10,-52,10,]),'EDJO':([2,],[3,]),'LBRACKET':([33,35,38,44,151,155,193,209,],[37,-51,42,79,168,171,196,212,]),'VAR_ID':([3,8,9,10,11,13,14,16,17,18,21,29,32,34,37,41,42,43,45,46,50,51,53,54,56,60,61,63,64,66,68,69,71,72,74,76,77,79,81,84,86,88,89,91,92,93,95,98,99,100,101,102,104,105,106,108,109,131,132,145,146,147,148,150,156,160,168,169,170,171,174,178,182,184,185,186,187,188,189,192,194,195,196,206,212,214,],[4,-10,-7,-9,15,-6,-8,-46,-45,22,26,-5,36,-4,-5,55,-5,78,-60,-85,-88,55,-72,-59,-56,-87,-74,-84,97,-61,97,-73,-86,-55,97,-57,55,55,97,97,97,97,97,97,97,97,97,97,-24,-21,-20,-22,97,-25,-23,-58,136,-65,97,97,97,97,97,97,97,-68,55,-67,-66,55,97,-89,97,-92,-93,-91,-90,-64,-75,-62,197,-76,55,-63,55,-77,]),'ELSE':([188,],[193,]),'INT':([7,12,27,29,34,37,39,42,138,157,],[13,13,13,13,-4,13,13,13,-52,13,]),'IF':([29,34,37,41,42,45,46,50,51,53,54,56,60,61,63,66,69,71,72,76,77,79,108,131,160,168,169,170,171,178,184,185,186,187,188,189,192,195,196,206,212,214,],[-5,-4,-5,57,-5,-60,-85,-88,57,-72,-59,-56,-87,-74,-84,-61,-73,-86,-55,-57,57,57,-58,-65,-68,57,-67,-66,57,-89,-92,-93,-91,-90,-64,-75,-62,-76,57,-63,57,-77,]),'RBRACKET':([29,34,42,45,46,50,51,53,54,56,60,61,63,66,69,71,72,76,77,79,83,108,111,113,131,140,160,168,169,170,171,178,180,181,184,185,186,187,188,189,192,195,196,198,206,212,213,214,],[-5,-4,-5,-60,-85,-88,-54,-72,-59,-56,-87,-74,-84,-61,-73,-86,-55,-57,-54,-54,-53,-58,138,139,-65,159,-68,-54,-67,-66,-54,-89,188,189,-92,-93,-91,-90,-64,-75,-62,-76,-54,206,-63,-54,214,-77,]),'PRINT':([29,34,37,41,42,45,46,50,51,53,54,56,60,61,63,66,69,71,72,76,77,79,108,131,160,168,169,170,171,178,184,185,186,187,188,189,192,195,196,206,212,214,],[-5,-4,-5,59,-5,-60,-85,-88,59,-72,-59,-56,-87,-74,-84,-61,-73,-86,-55,-57,59,59,-58,-65,-68,59,-67,-66,59,-89,-92,-93,-91,-90,-64,-75,-62,-76,59,-63,59,-77,]),'VAR_DECIMAL':([29,34,37,41,42,45,46,50,51,53,54,56,60,61,63,64,66,68,69,71,72,74,76,77,79,81,84,86,88,89,91,92,93,95,98,99,100,101,102,104,105,106,108,131,132,145,146,147,148,150,156,160,168,169,170,171,174,178,182,184,185,186,187,188,189,192,195,196,206,212,214,],[-5,-4,-5,52,-5,-60,-85,-88,52,-72,-59,-56,-87,-74,-84,52,-61,52,-73,-86,-55,52,-57,52,52,52,52,52,52,52,52,52,52,52,52,-24,-21,-20,-22,52,-25,-23,-58,-65,52,52,52,52,52,52,52,-68,52,-67,-66,52,52,-89,52,-92,-93,-91,-90,-64,-75,-62,-76,52,-63,52,-77,]),'COMMA':([15,26,36,47,49,52,58,62,67,75,78,80,85,90,94,97,103,114,118,125,126,129,130,134,135,137,141,143,162,],[21,21,39,-16,-38,-39,-33,-29,-19,-34,39,-14,-37,-30,-26,-42,-17,-15,145,-31,-32,-27,-28,-18,-36,-35,-41,-40,145,]),'DECIMAL':([7,12,27,29,34,37,39,42,138,157,],[9,9,9,9,-4,9,9,9,-52,9,]),'SRBRACKET':([47,49,52,58,62,67,75,80,85,90,94,97,103,107,114,116,125,126,129,130,134,135,137,141,143,],[-16,-38,-39,-33,-29,-19,-34,-14,-37,-30,-26,-42,-17,135,-15,141,-31,-32,-27,-28,-18,-36,-35,-41,-40,]),'MINUSMINUS':([197,],[202,]),'ZERO':([82,],[115,]),'SEMICOLON':([4,5,6,15,20,25,26,30,47,49,52,55,58,62,67,70,75,80,85,90,94,96,97,103,114,115,125,126,129,130,134,135,137,141,142,143,152,153,166,172,175,176,177,179,190,191,],[-2,-3,7,-12,-13,29,-12,-11,-16,-38,-39,-42,-33,-29,-19,108,-34,-14,-37,-30,-26,131,-42,-17,-15,140,-31,-32,-27,-28,-18,-36,-35,-41,160,-40,169,170,178,182,184,185,186,187,194,195,]),'RET':([29,34,37,41,45,46,48,50,51,53,54,56,60,61,63,66,69,71,72,76,83,108,131,160,169,170,178,184,185,186,187,188,189,192,195,206,214,],[-5,-4,-5,-54,-60,-85,82,-88,-54,-72,-59,-56,-87,-74,-84,-61,-73,-86,-55,-57,-53,-58,-65,-68,-67,-66,-89,-92,-93,-91,-90,-64,-75,-62,-76,-63,-77,]),'LT':([49,52,55,58,62,67,75,85,90,94,97,125,126,129,130,135,137,141,143,],[-38,-39,-42,-33,-29,101,-34,-37,-30,-26,-42,-31,-32,-27,-28,-36,-35,-41,-40,]),'WHILE':([29,34,37,41,42,45,46,50,51,53,54,56,60,61,63,66,69,71,72,76,77,79,108,131,139,160,168,169,170,171,178,184,185,186,187,188,189,192,195,196,206,212,214,],[-5,-4,-5,65,-5,-60,-85,-88,65,-72,-59,-56,-87,-74,-84,-61,-73,-86,-55,-57,65,65,-58,-65,158,-68,65,-67,-66,65,-89,-92,-93,-91,-90,-64,-75,-62,-76,65,-63,65,-77,]),'VOID':([7,12,29,34,138,157,],[-5,17,-5,-4,-52,17,]),'CIRCLE':([87,],[120,]),'RPAREN':([27,28,31,36,40,47,49,52,58,62,67,75,78,80,85,90,94,97,103,110,112,114,117,118,124,125,126,127,128,129,130,133,134,135,137,141,143,144,149,154,161,162,163,164,165,167,183,201,202,205,207,208,210,211,],[-48,33,35,-50,-47,-16,-38,-39,-33,-29,-19,-34,-50,-14,-37,-30,-26,-42,-17,137,-49,-15,142,143,151,-31,-32,152,153,-27,-28,155,-18,-36,-35,-41,-40,-69,166,143,-70,-71,175,176,177,179,191,209,-83,-82,-80,-79,-78,-81,]),'MAIN':([7,12,19,29,34,138,157,173,],[-5,-44,23,-5,-4,-52,-44,-43,]),'MINUS':([49,52,55,58,62,75,85,90,97,125,126,135,137,141,143,197,],[-38,-39,-42,-33,95,-34,-37,-30,-42,-31,-32,-36,-35,-41,-40,200,]),'START':([0,],[2,]),'PLUSPLUS':([197,],[205,]),'FOR':([29,34,37,41,42,45,46,50,51,53,54,56,60,61,63,66,69,71,72,76,77,79,108,131,160,168,169,170,171,178,184,185,186,187,188,189,192,195,196,206,212,214,],[-5,-4,-5,73,-5,-60,-85,-88,73,-72,-59,-56,-87,-74,-84,-61,-73,-86,-55,-57,73,73,-58,-65,-68,73,-67,-66,73,-89,-92,-93,-91,-90,-64,-75,-62,-76,73,-63,73,-77,]),'RETURN':([29,34,37,41,42,45,46,50,51,53,54,56,60,61,63,66,69,71,72,76,77,79,108,131,160,168,169,170,171,178,184,185,186,187,188,189,192,195,196,206,212,214,],[-5,-4,-5,64,-5,-60,-85,-88,64,-72,-59,-56,-87,-74,-84,-61,-73,-86,-55,-57,64,64,-58,-65,-68,64,-67,-66,64,-89,-92,-93,-91,-90,-64,-75,-62,-76,64,-63,64,-77,]),'LPAREN':([22,23,29,34,37,41,42,45,46,50,51,53,54,55,56,57,59,60,61,63,64,65,66,68,69,71,72,73,74,76,77,79,81,84,86,88,89,91,92,93,95,97,98,99,100,101,102,104,105,106,108,119,120,121,122,123,131,132,145,146,147,148,150,156,158,160,168,169,170,171,174,178,182,184,185,186,187,188,189,192,195,196,206,212,214,],[27,28,-5,-4,-5,74,-5,-60,-85,-88,74,-72,-59,86,-56,88,92,-87,-74,-84,74,98,-61,74,-73,-86,-55,109,74,-57,74,74,74,74,74,74,74,74,74,74,74,132,74,-24,-21,-20,-22,74,-25,-23,-58,146,147,148,149,150,-65,74,74,74,74,74,74,74,174,-68,74,-67,-66,74,74,-89,74,-92,-93,-91,-90,-64,-75,-62,-76,74,-63,74,-77,]),'STRING':([7,12,27,29,34,37,39,42,138,157,],[14,14,14,14,-4,14,14,14,-52,14,]),'GE':([49,52,55,58,62,67,75,85,90,94,97,125,126,129,130,135,137,141,143,],[-38,-39,-42,-33,-29,99,-34,-37,-30,-26,-42,-31,-32,-27,-28,-36,-35,-41,-40,]),'ASSIGN':([47,49,52,55,58,62,67,75,85,90,94,97,103,125,126,129,130,134,135,136,137,141,143,],[81,-38,-39,-42,-33,-29,-19,-34,-37,-30,-26,-42,-17,-31,-32,-27,-28,-18,-36,156,-35,-41,-40,]),'LE':([49,52,55,58,62,67,75,85,90,94,97,125,126,129,130,135,137,141,143,],[-38,-39,-42,-33,-29,106,-34,-37,-30,-26,-42,-31,-32,-27,-28,-36,-35,-41,-40,]),'POS':([87,],[122,]),'EQ':([49,52,55,58,62,67,75,85,90,94,97,125,126,129,130,135,137,141,143,],[-38,-39,-42,-33,-29,105,-34,-37,-30,-26,-42,-31,-32,-27,-28,-36,-35,-41,-40,]),'$end':([1,24,159,],[0,-1,-94,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'mas_vars':([15,26,],[20,30,]),'Llamada_Func':([41,51,77,79,168,171,196,212,],[45,45,45,45,45,45,45,45,]),'Right':([41,51,77,79,168,171,196,212,],[46,46,46,46,46,46,46,46,]),'ExpT':([41,51,64,68,74,77,79,81,84,86,88,89,91,92,93,95,98,104,132,145,146,147,148,150,156,168,171,174,182,196,212,],[62,62,62,62,62,62,62,62,62,62,62,125,126,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,]),'program':([0,],[1,]),'Operandos':([67,],[104,]),'Tipo':([7,12,27,29,37,39,42,157,],[11,16,32,11,11,43,11,16,]),'Vars':([7,29,37,42,],[12,34,41,77,]),'cmq_action':([4,],[5,]),'While':([41,51,77,79,168,171,196,212,],[69,69,69,69,69,69,69,69,]),'VAR_CTE':([41,51,64,68,74,77,79,81,84,86,88,89,91,92,93,95,98,104,132,145,146,147,148,150,156,168,171,174,182,196,212,],[75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,]),'Circle':([41,51,77,79,168,171,196,212,],[50,50,50,50,50,50,50,50,]),'adf_action':([35,],[38,]),'Estatutos':([41,51,77,79,168,171,196,212,],[51,51,51,51,51,51,51,51,]),'tipo_funcion':([12,157,],[18,18,]),'funciones':([12,157,],[19,173,]),'pos_igual':([47,],[80,]),'pos_commaLlam':([118,162,],[144,144,]),'paramLlam':([86,145,],[117,161,]),'pos_commaf':([36,78,],[40,112,]),'For':([41,51,77,79,168,171,196,212,],[53,53,53,53,53,53,53,53,]),'cfd_action':([5,],[6,]),'Ciclo':([41,51,77,79,168,171,196,212,],[56,56,56,56,56,56,56,56,]),'ExpF':([41,51,64,68,74,77,79,81,84,86,88,89,91,92,93,95,98,104,132,145,146,147,148,150,156,168,171,174,182,196,212,],[58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,]),'Forward':([41,51,77,79,168,171,196,212,],[60,60,60,60,60,60,60,60,]),'DoWhile':([41,51,77,79,168,171,196,212,],[61,61,61,61,61,61,61,61,]),'adv_action':([20,],[25,]),'Position':([41,51,77,79,168,171,196,212,],[63,63,63,63,63,63,63,63,]),'param':([27,],[31,]),'pos_MULTDIV':([58,],[90,]),'enp_action':([138,],[157,]),'TurtleMotion':([41,51,77,79,168,171,196,212,],[66,66,66,66,66,66,66,66,]),'ExpK':([41,51,64,68,74,77,79,81,84,86,88,92,93,95,98,104,132,145,146,147,148,150,156,168,171,174,182,196,212,],[67,67,67,67,67,67,67,67,67,67,67,67,129,130,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,]),'ExpI':([41,51,64,68,74,77,79,81,84,86,88,92,98,104,132,145,146,147,148,150,156,168,171,174,182,196,212,],[47,47,47,47,47,47,47,114,47,47,47,47,47,134,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'reg_brack':([41,51,77,79,168,171,196,212,],[48,83,111,113,180,181,198,213,]),'Exp':([41,51,64,68,74,77,79,84,86,88,92,98,132,145,146,147,148,150,156,168,171,174,182,196,212,],[70,70,96,107,110,70,70,116,118,124,127,133,154,162,163,164,165,167,172,70,70,183,190,70,70,]),'pos_parens':([55,97,],[85,85,]),'pos_else':([188,],[192,]),'Left':([41,51,77,79,168,171,196,212,],[71,71,71,71,71,71,71,71,]),'Condicion':([41,51,77,79,168,171,196,212,],[72,72,72,72,72,72,72,72,]),'pos_SUMRES':([62,],[94,]),'Print':([41,51,77,79,168,171,196,212,],[54,54,54,54,54,54,54,54,]),'pos_Operandos':([67,],[103,]),'Main':([19,],[24,]),'Exp_ciclo':([197,],[201,]),'Return':([41,51,77,79,168,171,196,212,],[76,76,76,76,76,76,76,76,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> START EDJO VAR_ID cmq_action cfd_action SEMICOLON Vars funciones Main','program',9,'p_inicio','edjo.py',194),
  ('cmq_action -> <empty>','cmq_action',0,'p_cmq_action','edjo.py',198),
  ('cfd_action -> <empty>','cfd_action',0,'p_cfd_action','edjo.py',205),
  ('Vars -> Tipo VAR_ID mas_vars adv_action SEMICOLON Vars','Vars',6,'p_Vars','edjo.py',212),
  ('Vars -> <empty>','Vars',0,'p_Vars','edjo.py',213),
  ('Tipo -> INT','Tipo',1,'p_Tipo','edjo.py',217),
  ('Tipo -> DECIMAL','Tipo',1,'p_Tipo','edjo.py',218),
  ('Tipo -> STRING','Tipo',1,'p_Tipo','edjo.py',219),
  ('Tipo -> CHAR','Tipo',1,'p_Tipo','edjo.py',220),
  ('Tipo -> BOOL','Tipo',1,'p_Tipo','edjo.py',221),
  ('mas_vars -> COMMA VAR_ID mas_vars','mas_vars',3,'p_mas_vars','edjo.py',226),
  ('mas_vars -> <empty>','mas_vars',0,'p_mas_vars','edjo.py',227),
  ('adv_action -> <empty>','adv_action',0,'p_adv_action','edjo.py',234),
  ('Exp -> ExpI pos_igual','Exp',2,'p_Exp','edjo.py',249),
  ('pos_igual -> ASSIGN ExpI','pos_igual',2,'p_pos_igual','edjo.py',253),
  ('pos_igual -> <empty>','pos_igual',0,'p_pos_igual','edjo.py',254),
  ('ExpI -> ExpK pos_Operandos','ExpI',2,'p_ExpI','edjo.py',258),
  ('pos_Operandos -> Operandos ExpI','pos_Operandos',2,'p_pos_Operandos','edjo.py',262),
  ('pos_Operandos -> <empty>','pos_Operandos',0,'p_pos_Operandos','edjo.py',263),
  ('Operandos -> LT','Operandos',1,'p_Operandos','edjo.py',267),
  ('Operandos -> GT','Operandos',1,'p_Operandos','edjo.py',268),
  ('Operandos -> NE','Operandos',1,'p_Operandos','edjo.py',269),
  ('Operandos -> LE','Operandos',1,'p_Operandos','edjo.py',270),
  ('Operandos -> GE','Operandos',1,'p_Operandos','edjo.py',271),
  ('Operandos -> EQ','Operandos',1,'p_Operandos','edjo.py',272),
  ('ExpK -> ExpT pos_SUMRES','ExpK',2,'p_ExpK','edjo.py',276),
  ('pos_SUMRES -> PLUS ExpK','pos_SUMRES',2,'p_pos_SUMRES','edjo.py',280),
  ('pos_SUMRES -> MINUS ExpK','pos_SUMRES',2,'p_pos_SUMRES','edjo.py',281),
  ('pos_SUMRES -> <empty>','pos_SUMRES',0,'p_pos_SUMRES','edjo.py',282),
  ('ExpT -> ExpF pos_MULTDIV','ExpT',2,'p_ExpT','edjo.py',286),
  ('pos_MULTDIV -> MULT ExpT','pos_MULTDIV',2,'p_pos_MULTDIV','edjo.py',290),
  ('pos_MULTDIV -> DIV ExpT','pos_MULTDIV',2,'p_pos_MULTDIV','edjo.py',291),
  ('pos_MULTDIV -> <empty>','pos_MULTDIV',0,'p_pos_MULTDIV','edjo.py',292),
  ('ExpF -> VAR_CTE','ExpF',1,'p_ExpF','edjo.py',296),
  ('ExpF -> LPAREN Exp RPAREN','ExpF',3,'p_ExpF','edjo.py',297),
  ('ExpF -> SLBRACKET Exp SRBRACKET','ExpF',3,'p_ExpF','edjo.py',298),
  ('ExpF -> VAR_ID pos_parens','ExpF',2,'p_ExpF','edjo.py',299),
  ('VAR_CTE -> VAR_INT','VAR_CTE',1,'p_VAR_CTE','edjo.py',302),
  ('VAR_CTE -> VAR_DECIMAL','VAR_CTE',1,'p_VAR_CTE','edjo.py',303),
  ('pos_parens -> LPAREN Exp RPAREN','pos_parens',3,'p_pos_parens','edjo.py',307),
  ('pos_parens -> SLBRACKET Exp SRBRACKET','pos_parens',3,'p_pos_parens','edjo.py',308),
  ('pos_parens -> <empty>','pos_parens',0,'p_pos_parens','edjo.py',309),
  ('funciones -> tipo_funcion VAR_ID LPAREN param RPAREN adf_action LBRACKET Vars reg_brack RBRACKET enp_action funciones','funciones',12,'p_funciones','edjo.py',314),
  ('funciones -> <empty>','funciones',0,'p_funciones','edjo.py',315),
  ('tipo_funcion -> VOID','tipo_funcion',1,'p_tipo_funcion','edjo.py',319),
  ('tipo_funcion -> Tipo','tipo_funcion',1,'p_tipo_funcion','edjo.py',320),
  ('param -> Tipo VAR_ID pos_commaf','param',3,'p_param','edjo.py',325),
  ('param -> <empty>','param',0,'p_param','edjo.py',326),
  ('pos_commaf -> COMMA Tipo VAR_ID pos_commaf','pos_commaf',4,'p_pos_commaf','edjo.py',330),
  ('pos_commaf -> <empty>','pos_commaf',0,'p_pos_commaf','edjo.py',331),
  ('adf_action -> <empty>','adf_action',0,'p_adf_action','edjo.py',340),
  ('enp_action -> <empty>','enp_action',0,'p_enp_action','edjo.py',367),
  ('reg_brack -> Estatutos reg_brack','reg_brack',2,'p_reg_brack','edjo.py',396),
  ('reg_brack -> <empty>','reg_brack',0,'p_reg_brack','edjo.py',397),
  ('Estatutos -> Condicion','Estatutos',1,'p_Estatutos','edjo.py',400),
  ('Estatutos -> Ciclo','Estatutos',1,'p_Estatutos','edjo.py',401),
  ('Estatutos -> Return','Estatutos',1,'p_Estatutos','edjo.py',402),
  ('Estatutos -> Exp SEMICOLON','Estatutos',2,'p_Estatutos','edjo.py',403),
  ('Estatutos -> Print','Estatutos',1,'p_Estatutos','edjo.py',404),
  ('Estatutos -> Llamada_Func','Estatutos',1,'p_Estatutos','edjo.py',405),
  ('Estatutos -> TurtleMotion','Estatutos',1,'p_Estatutos','edjo.py',406),
  ('Condicion -> IF LPAREN Exp RPAREN LBRACKET reg_brack RBRACKET pos_else','Condicion',8,'p_Condicion','edjo.py',409),
  ('pos_else -> ELSE LBRACKET reg_brack RBRACKET','pos_else',4,'p_pos_else','edjo.py',413),
  ('pos_else -> <empty>','pos_else',0,'p_pos_else','edjo.py',414),
  ('Return -> RETURN Exp SEMICOLON','Return',3,'p_Return','edjo.py',417),
  ('Print -> PRINT LPAREN VAR_STRING RPAREN SEMICOLON','Print',5,'p_Print','edjo.py',420),
  ('Print -> PRINT LPAREN Exp RPAREN SEMICOLON','Print',5,'p_Print','edjo.py',421),
  ('Llamada_Func -> VAR_ID LPAREN paramLlam RPAREN SEMICOLON','Llamada_Func',5,'p_Llamada_Func','edjo.py',425),
  ('paramLlam -> Exp pos_commaLlam','paramLlam',2,'p_paramLlam','edjo.py',429),
  ('pos_commaLlam -> COMMA paramLlam','pos_commaLlam',2,'p_pos_commaLlam','edjo.py',433),
  ('pos_commaLlam -> <empty>','pos_commaLlam',0,'p_pos_commaLlam','edjo.py',434),
  ('Ciclo -> For','Ciclo',1,'p_Ciclo','edjo.py',437),
  ('Ciclo -> While','Ciclo',1,'p_Ciclo','edjo.py',438),
  ('Ciclo -> DoWhile','Ciclo',1,'p_Ciclo','edjo.py',439),
  ('While -> WHILE LPAREN Exp RPAREN LBRACKET reg_brack RBRACKET','While',7,'p_While','edjo.py',442),
  ('DoWhile -> DO LBRACKET reg_brack RBRACKET WHILE LPAREN Exp RPAREN SEMICOLON','DoWhile',9,'p_DoWhile','edjo.py',446),
  ('For -> FOR LPAREN VAR_ID ASSIGN Exp SEMICOLON Exp SEMICOLON VAR_ID Exp_ciclo RPAREN LBRACKET reg_brack RBRACKET','For',14,'p_For','edjo.py',450),
  ('Exp_ciclo -> PLUS VAR_INT','Exp_ciclo',2,'p_Exp_ciclo','edjo.py',454),
  ('Exp_ciclo -> MINUS VAR_INT','Exp_ciclo',2,'p_Exp_ciclo','edjo.py',455),
  ('Exp_ciclo -> MULT VAR_INT','Exp_ciclo',2,'p_Exp_ciclo','edjo.py',456),
  ('Exp_ciclo -> DIV VAR_INT','Exp_ciclo',2,'p_Exp_ciclo','edjo.py',457),
  ('Exp_ciclo -> PLUSPLUS','Exp_ciclo',1,'p_Exp_ciclo','edjo.py',458),
  ('Exp_ciclo -> MINUSMINUS','Exp_ciclo',1,'p_Exp_ciclo','edjo.py',459),
  ('TurtleMotion -> Position','TurtleMotion',1,'p_TurtleMotion','edjo.py',463),
  ('TurtleMotion -> Right','TurtleMotion',1,'p_TurtleMotion','edjo.py',464),
  ('TurtleMotion -> Left','TurtleMotion',1,'p_TurtleMotion','edjo.py',465),
  ('TurtleMotion -> Forward','TurtleMotion',1,'p_TurtleMotion','edjo.py',466),
  ('TurtleMotion -> Circle','TurtleMotion',1,'p_TurtleMotion','edjo.py',467),
  ('Position -> VAR_ID POINT POS LPAREN RPAREN SEMICOLON','Position',6,'p_Position','edjo.py',470),
  ('Forward -> VAR_ID POINT FORWARD LPAREN Exp RPAREN SEMICOLON','Forward',7,'p_Forward','edjo.py',473),
  ('Right -> VAR_ID POINT RIGHT LPAREN Exp RPAREN SEMICOLON','Right',7,'p_Right','edjo.py',476),
  ('Left -> VAR_ID POINT LEFT LPAREN Exp RPAREN SEMICOLON','Left',7,'p_Left','edjo.py',479),
  ('Circle -> VAR_ID POINT CIRCLE LPAREN Exp RPAREN SEMICOLON','Circle',7,'p_Circle','edjo.py',482),
  ('Main -> MAIN LPAREN RPAREN LBRACKET Vars reg_brack RET ZERO SEMICOLON RBRACKET','Main',10,'p_Main','edjo.py',486),
]