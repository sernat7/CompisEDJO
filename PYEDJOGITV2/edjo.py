import ply.lex as lex
import sys

from program import Program
from quadruple import Quadruple
from virtual_machine import VirtualMachine



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
my_program = Program()

def p_inicio(p):
	'''program	:	START EDJO VAR_ID cmq_action cfd_action SEMICOLON Vars funciones Main
	'''

def p_cmq_action(p):
	'''cmq_action	: 
	'''
	quadruple = Quadruple(my_program.quadruple_number,'GOTO', 'MAIN', None, None)
	my_program.quadruple_list.append(quadruple)
	my_program.quadruple_number += 1

def p_cfd_action(p):
	'''cfd_action	: 
	'''
	my_program.global_scope = p[-2]
	my_program.current_scope = p[-2]
	my_program.function_directory.add_function(my_program.global_scope, 'void')
	
def p_Vars(p):
	'''Vars		:	Tipo VAR_ID mas_vars adv_action SEMICOLON Vars
			| 
	'''

def p_Tipo(p):
	'''Tipo		:	INT
			|	DECIMAL
			|	STRING
			|	CHAR
			|	BOOL
	'''
	p[0] = p[1]

def p_mas_vars(p):
	'''mas_vars	:	COMMA VAR_ID mas_vars
			| 
	'''
	if p[-1] is not None:
		variable_name = p[-1]
		my_program.temporal_variables.append(variable_name)

def p_adv_action(p):
	'''adv_action	: 
	'''
	variable_type = p[-3]
	my_program.temporal_variables.reverse()
	for variable in my_program.temporal_variables:
		variable_declared = my_program.function_directory.check_existing_variable(my_program.current_scope, variable)
		if not variable_declared:
			if my_program.current_scope == my_program.global_scope:
				variable_address = my_program.memory.request_global_address(variable_type)
			else:
				variable_address = my_program.memory.request_local_address(variable_type)			
			my_program.function_directory.add_variable_to_function(my_program.current_scope, variable_type, variable, variable_address)
	del my_program.temporal_variables[:]

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


def p_funciones(p):
	'''funciones	:	tipo_funcion VAR_ID LPAREN param RPAREN adf_action LBRACKET Vars reg_brack RBRACKET enp_action funciones
			| 
	''' 

def p_tipo_funcion(p):
	'''tipo_funcion	:	VOID
			|	Tipo
	'''
	p[0] = p[1]

def p_param(p):
	'''param	:	Tipo VAR_ID pos_commaf
			| 
	'''

def p_pos_commaf(p):
	'''pos_commaf	:	COMMA Tipo VAR_ID pos_commaf
			| 
	'''
	if p[-1] is not None:
		parameter_name = p[-1]
		parameter_type = p[-2]
		my_program.temporal_parameters_names.insert(0, parameter_name)
		my_program.temporal_parameters_types.insert(0, parameter_type)

def p_adf_action(p):
	'''adf_action	: 
	'''
	my_program.current_scope = p[-4]
	function_type = p[-5]
	parameter_address_list = []
	
	my_program.function_directory.add_function(my_program.current_scope, function_type)
	
	my_program.function_directory.set_function_quadruple_number(my_program.current_scope, my_program.quadruple_number)

	if function_type != 'void':
		function_address = my_program.memory.request_global_address(function_type)
		my_program.function_directory.set_function_address(my_program.current_scope, function_address)

	parameters = zip(my_program.temporal_parameters_names, my_program.temporal_parameters_types)
	
	for parameter_name, parameter_type in parameters:
		parameter_address = my_program.memory.request_local_address(parameter_type)
		parameter_address_list.append(parameter_address)
		my_program.function_directory.add_variable_to_function(my_program.current_scope, parameter_type, parameter_name, parameter_address)

	my_program.function_directory.add_parameter_to_function(my_program.current_scope, list(my_program.temporal_parameters_types), list(parameter_address_list))
	del my_program.temporal_parameters_names[:]
	del my_program.temporal_parameters_types[:]

	
def p_enp_action(p):
	'''enp_action	: 
	'''
	function_type = p[-10]
	
	if function_type == 'void' and my_program.return_flag:
		print('Function {0} of type {1} should not have return statement'.format(my_program.current_scope, function_type))
		sys.exit()
	elif function_type != 'void' and not my_program.return_flag:
		print('Function {0} of type {1} should have return statement'.format(my_program.current_scope, function_type))
		sys.exit()
	else:
		quadruple = Quadruple(my_program.quadruple_number, 'ENDPROC', None, None, None)
		my_program.quadruple_list.append(quadruple)
		
	if my_program.return_flag:
		while my_program.return_list:
			quadruple_number_to_fill = my_program.return_list.pop()
			my_program.quadruple_list[quadruple_number_to_fill - 1].fill_quadruple_jump(my_program.quadruple_number)
	my_program.quadruple_number += 1
	my_program.return_flag = False
	
	my_program.current_scope = my_program.global_scope
	my_program.memory.reset_temporal_memory()





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
	'''Main		:	MAIN LPAREN RPAREN LBRACKET Vars reg_brack RET ZERO SEMICOLON RBRACKET
	'''
#def p_Draw_o_espacio(p):
#	'''Draw_o_espacio	:	TurtleDraw
#				| 
#	'''
#def p_TurtleDraw(p):
#	'''TurtleDraw	:	IniciaTurtle
#	'''




import ply.yacc as yacc
import pprint
parser = yacc.yacc()
pp = pprint.PrettyPrinter(indent=4)

with open('prueba.txt','r') as f:
	input = f.read()
	pp.pprint(parser.parse(input))

	my_program.function_directory.print_directory()


