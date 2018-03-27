import ply.lex as lex
import sys

#Define global variables
varGlobal = {}
varLocal = {}
variableType = None
lastVarName = None
scope = 'global'
funcType = None
funcTypeNext = False
funcGlobal = {}
lastFuncName = None
funcArguments = []




#TOKENS#
tokens = (
'LT',
'EQ',
'GT',
'NE',
'LE',
'GE',
'ASSIGN',
'PLUSPLUS',
'MINUSMINUS',
'PLUS',
'MINUS',
'MULT',
'DIV',
'LPAREN',
'RPAREN',
'LBRACKET',
'RBRACKET',
'SLBRACKET',
'SRBRACKET',
'SEMICOLON',
'COMMA',
'IF',
'ELSE',
'IFELSE',
'INT',
'DECIMAL',
'STRING',
'CHAR',
'BOOL',
'PRINT',
'START',
'EDJO',
'VOID',
'RETURN',
'MAIN',
'FOR',
'VAR_ID',
'VAR_INT',
'VAR_DECIMAL',
'VAR_CHAR',
'VAR_STRING',
'TRUE',
'FALSE',
'DO',
'WHILE',
'FROM',
'IMPORT',
'POINT',
'POS',
'FORWARD',
'CIRCLE',
'LEFT',
'RIGHT',
'TUR',
'TURTLE',
'ZERO',
'RET'
)

#Palabras reservadas#
reserved = {
'if'		:	'IF',
'else'		:	'ELSE',
'for'		:	'FOR',
'int'		:	'INT',
'do'		:	'DO',
'while'		:	'WHILE',
'decimal'	:	'DECIMAL',
'string'	:	'STRING',
'char'		:	'CHAR',
'bool'		:	'BOOL',
'void'		:	'VOID',
'return'	:	'RETURN',
'main'		:	'MAIN',
'print'		:	'PRINT',
'start'		:	'START',
'EDJO'		:	'EDJO',
'ifelse'	:	'IFELSE',
'true'		:	'TRUE',
'false'		:	'FALSE',
'from'		:	'FROM',
'import'	:	'IMPORT',
'turtle'	:	'TUR',
'Turtle'	:	'TURTLE',
'pos'		:	'POS',
'forward'	:	'FORWARD',
'circle'	:	'CIRCLE',
'left'		:	'LEFT',
'right'		:	'RIGHT',
'zero'		:	'ZERO',
'Return'	:	'RET'
}

#Expresiones regulares para los tokens simples#
t_LT = r'<'
t_GT = r'>'
t_EQ = r'=='
t_NE = r'!='
t_LE = r'<='
t_GE = r'>='

t_ASSIGN = r'='
t_PLUSPLUS = r'\+\+'
t_MINUSMINUS = r'--'

t_PLUS = r'\+'
t_MINUS = r'-'
t_MULT = r'\*'
t_DIV = r'/'

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\{'
t_RBRACKET = r'\}'
t_SLBRACKET = r'\['
t_SRBRACKET = r'\]'


t_SEMICOLON = r';'
t_COMMA = r','
t_POINT = r'\.'

#ignora espacios y tabs
t_ignore = ' \t' 

#Expresiones regulares con reglas
def t_newline(t):
	r'\n+'
	t.lexer.lineno += t.value.count("\n")

def t_error(t):
	print("Illegal character '%s" % t.value[0])
	t.lexer.skip(1)

def t_TRUE(t):
	r'(true)'
	t.value = True
	return t

def t_FALSE(t):
	r'(false)'
	t.value = False
	return t

def t_VAR_DECIMAL(t):
	r'\d+\.\d+'
	t.value = float(t.value)
	return t

def t_VAR_INT(t):
	r'\d+'
	t.value = int(t.value)
	return t

def t_VAR_CHAR(t):
	r'\"(\\.|[^\\"])\"'
	t.value = t.value[1:-1]
	return t

def t_VAR_STRING(t):
	r'\"(\\.|[^\\"])*\"'
	t.value = t.value[1:-1]
	return t

def t_VAR_ID(t):
	r'[a-zA-Z](_?([a-zA-Z]|[0-9]))*'
	t.type = reserved.get(t.value,'VAR_ID') #checa for las palabras reservadas
	return t


lexer = lex.lex()
file = open('prueba.txt','r')
lexer.input(file.read())

#while True:
#	tok = lexer.token()
#	if not tok:
#		break
#	print(tok)

def p_inicio(p):
	'''program	:	START EDJO VAR_ID SEMICOLON LibreriaT vars_o_espacio tipo_funciones Main
	'''
def p_LibreriaT(p):
	'''LibreriaT	:	FROM TUR IMPORT TURTLE SEMICOLON
	'''
#posible quita libreriaT  
def p_vars_o_espacio(p):
	'''vars_o_espacio	:	Vars vars_o_espacio
				| 
	'''

def p_Vars(p):
	'''Vars		:	Tipo reglas_var SEMICOLON
	'''

def p_Tipo(p):
	'''Tipo		:	INT AgregaTipo
			|	DECIMAL AgregaTipo
			|	STRING AgregaTipo
			|	CHAR AgregaTipo
			|	BOOL AgregaTipo
	'''

def p_reglas_var(p):
	'''reglas_var	:	VAR_ID AgregaVariable pos_vec pos_comma
	'''

def p_pos_vec(p):
	'''pos_vec	:	SLBRACKET VAR_INT SRBRACKET
			| 
	'''

def p_pos_comma(p):
	'''pos_comma	:	COMMA reglas_var
			| 
	'''

def p_Exp(p):
	'''Exp		:	ExpI pos_igual
	'''

def p_pos_igual(p):
	'''pos_igual	:	ASSIGN ExpI
			| 
	'''

def p_ExpI(p):
	'''ExpI		:	ExpK pos_Operandos
	'''

def p_pos_Operandos(p):
	'''pos_Operandos	:	Operandos ExpI
				| 
	'''

def p_Operandos(p):
	'''Operandos	:	LT
			|	GT
			|	NE
			|	LE
			|	GE
			|	EQ
	'''

def p_ExpK(p):
	'''ExpK		:	ExpT pos_SUMRES
	'''

def p_pos_SUMRES(p):
	'''pos_SUMRES	:	PLUS ExpK
			|	MINUS ExpK
			| 
	'''

def p_ExpT(p):
	'''ExpT		:	ExpF pos_MULTDIV
	'''

def p_pos_MULTDIV(p):
	'''pos_MULTDIV	:	MULT ExpT
			|	DIV ExpT
			| 
	'''

def p_ExpF(p):
	'''ExpF		:	VAR_CTE
			|	LPAREN Exp RPAREN
			|	SLBRACKET Exp SRBRACKET
			|	VAR_ID pos_parens
	'''
def p_VAR_CTE(p):
	'''VAR_CTE	:	VAR_INT
			|	VAR_DECIMAL
	'''

def p_pos_parens(p):
	'''pos_parens	:	LPAREN Exp RPAREN
			|	SLBRACKET Exp SRBRACKET
			| 
	'''

def p_tipo_funciones(p):
	'''tipo_funciones	:	Funcs_void tipo_funciones
				| 
	'''
def p_Funcs_void(p):
	'''Funcs_void	:	CambiarALocal VOID saveFuncTypeVoid VAR_ID saveFuncName LPAREN reg_paren RPAREN LBRACKET vars_o_espacio reg_brack RBRACKET CambiarAGlobal
	'''
	global varLocal
	global funcArguments
	addFunction(lastFuncName, funcType, funcArguments)
	print('local vars: %s' % varLocal)
	varLocal = {}
	funcArguments = []

def p_reg_paren(p):
	'''reg_paren	:	param
			|
	'''

def p_param(p):
	'''param	:	Tipo VAR_ID addArgument pos_commaf
	'''
def p_pos_commaf(p):
	'''pos_commaf	:	COMMA param
			| 
	'''

def p_reg_brack(p):
	'''reg_brack	:	Estatutos reg_brack
			| 
	'''
def p_Estatutos(p):
	'''Estatutos	:	Condicion 
			|	Ciclo  
			|	Return 
			|	Exp SEMICOLON
			|	Print 
			|	Llamada_Func 
			|	TurtleMotion 
	'''
def p_Condicion(p):
	'''Condicion	:	IF LPAREN Exp RPAREN LBRACKET reg_brack RBRACKET pos_else
	'''

def p_pos_else(p):
	'''pos_else	:	ELSE LBRACKET reg_brack RBRACKET
			| 
	'''
def p_Return(p):
	'''Return 	:	RETURN Exp SEMICOLON
	'''
def p_Print(p):
	'''Print	:	PRINT LPAREN VAR_STRING RPAREN SEMICOLON
			|	PRINT LPAREN Exp RPAREN SEMICOLON
	'''

def p_Llamada_Func(p):
	'''Llamada_Func	:	VAR_ID LPAREN paramLlam RPAREN SEMICOLON
	'''

def p_paramLlam(p):
	'''paramLlam	:	Exp pos_commaLlam
	'''

def p_pos_commaLlam(p):
	'''pos_commaLlam	:	COMMA paramLlam
				| 
	'''
def p_Ciclo(p):
	'''Ciclo	:	For
			|	While
			|	DoWhile
	'''
def p_While(p):
	'''While	:	WHILE LPAREN Exp RPAREN LBRACKET reg_brack RBRACKET
	'''

def p_DoWhile(p):
	'''DoWhile	:	DO LBRACKET reg_brack RBRACKET WHILE LPAREN Exp RPAREN SEMICOLON
	'''

def p_For(p):
	'''For		:	FOR LPAREN VAR_ID ASSIGN Exp SEMICOLON Exp SEMICOLON VAR_ID Exp_ciclo RPAREN LBRACKET reg_brack RBRACKET
	'''

def p_Exp_ciclo(p):
	'''Exp_ciclo	:	PLUS VAR_INT
			|	MINUS VAR_INT
			|	MULT VAR_INT
			|	DIV VAR_INT
			|	PLUSPLUS
			|	MINUSMINUS
	'''

def p_TurtleMotion(p):
	'''TurtleMotion	:	Position
			|	Right
			|	Left
			|	Forward
			|	Circle
	'''
def p_Position(p):
	'''Position	:	VAR_ID POINT POS LPAREN RPAREN SEMICOLON
	'''
def p_Forward(p):
	'''Forward	:	VAR_ID POINT FORWARD LPAREN Exp RPAREN SEMICOLON
	'''
def p_Right(p):
	'''Right	:	VAR_ID POINT RIGHT LPAREN Exp RPAREN SEMICOLON
	'''
def p_Left(p):
	'''Left		:	VAR_ID POINT LEFT LPAREN Exp RPAREN SEMICOLON
	'''
def p_Circle(p):
	'''Circle	:	VAR_ID POINT CIRCLE LPAREN Exp RPAREN SEMICOLON
	'''

def p_Main(p):
	'''Main		:	MAIN LPAREN RPAREN LBRACKET CambiarALocal vars_o_espacio reg_brack RET ZERO SEMICOLON RBRACKET
	'''
	print('local vars: %s' % varLocal)
	print('global vars: %s' % varGlobal)
	print('functions: %s' % funcGlobal)

#def p_Draw_o_espacio(p):
#	'''Draw_o_espacio	:	TurtleDraw
#				| 
#	'''
#def p_TurtleDraw(p):
#	'''TurtleDraw	:	IniciaTurtle
#	'''


#Puntos neurales

def p_AgregaTipo(p):
	'''AgregaTipo	: 
	'''
	global variableType
	global funcTypeNext
	global funcType
	if funcTypeNext:
		funcType = typesValues[p[-1]]
	else:
		variableType = typesValues[p[-1]]
	funcTypeNext = False

def p_AgregaVariable(p):
	'''AgregaVariable	:
	'''
	global lastVarName
	lastVarName = p[-1]
	variableName = lastVarName
	addVariable(variableName, variableType)


def p_CambiarALocal(p):
	'''CambiarALocal	: 
	'''
	global scope
	scope = 'local'

def p_CambiarAGlobal(p):
	'''CambiarAGlobal	:
	'''
	global scope
	scope = 'global'

def p_saveFuncTypeVoid(p):
	'''saveFuncTypeVoid	: 
	'''
	global funcType
	funcType = typesValues['void']
	

def p_saveFuncName(p):
	'''saveFuncName		: 
	'''
	global lastFuncName
	lastFuncName = p[-1]

def p_addArgument(p):
	'''addArgument		: 
	'''
	global lastVarName
	global funcArguments
	lastVarName = p[-1]
	variableName = lastVarName
	addVariable(variableName, variableType)
	funcArguments.append(varLocal[variableName])



import ply.yacc as yacc
import pprint
parser = yacc.yacc()
pp = pprint.PrettyPrinter(indent=4)

#funciones
typesValues = {
		'void':0,
		'int':1,
		'decimal':2,
		'bool':3,
		'string':4,
		'char':5,
}

def addVariable(variable, varType):
	global varGlobal
	global varLocal
	if scope == 'global':
		if not variable in varGlobal.keys():
			varGlobal[variable] = {'name':variable, 'type':varType}
		else:
			print("Variable is already declared globally")
	else:
		if not variable in varLocal.keys():
			varLocal[variable] = {'name':variable, 'type':varType}
		else:
			print("Variable is already delcared locally")

def addFunction(name, funType, parameters):
	global funcGlobal
	if not name in funcGlobal.keys():
		funcGlobal[name] = {'name':name, 'type':funType, 'parameters':parameters}
	else:
		print("Functions is already declared")



with open('prueba.txt','r') as f:
	input = f.read()
	pp.pprint(parser.parse(input))




