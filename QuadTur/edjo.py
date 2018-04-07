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
'RET',
'FUNC',
'FINISH'
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
'Return'	:	'RET',
'func'		:	'FUNC',
'finish'	:	'FINISH'
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
edjo = Program()

def p_inicio(p):
	'''program	:	START EDJO VAR_ID crea_primer_quadruple crea_funcion_global SEMICOLON Vars funciones Main
	'''

#Crea primer Quadruple
def p_crea_primer_quadruple(p):
	'''crea_primer_quadruple	: 
	'''
	quadruple = Quadruple(edjo.quadruple_number,'GOTO', 'MAIN', None, None)
	edjo.quadruple_list.append(quadruple)
	edjo.quadruple_number += 1

#Crea funcion global
def p_crea_funcion_global(p):
	'''crea_funcion_global	: 
	'''
	edjo.global_scope = p[-2]
	edjo.current_scope = p[-2]
	edjo.function_directory.add_function(edjo.global_scope, 'void')
	
def p_Vars(p):
	'''Vars		:	Tipo VAR_ID mas_vars agrega_var_funcion SEMICOLON Vars
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
		edjo.temporal_variables.append(variable_name)

#Agrega la variable a la funcion actual ya sea global o local
def p_agrega_var_funcion(p):
	'''agrega_var_funcion	: 
	'''
	variable_type = p[-3]
	edjo.temporal_variables.reverse()
	for variable in edjo.temporal_variables:
		variable_declared = edjo.function_directory.check_existing_variable(edjo.current_scope, variable)
		if not variable_declared:
			if edjo.current_scope == edjo.global_scope:
				variable_address = edjo.memory.request_global_address(variable_type)
			else:
				variable_address = edjo.memory.request_local_address(variable_type)			
			edjo.function_directory.add_variable_to_function(edjo.current_scope, variable_type, variable, variable_address)
	del edjo.temporal_variables[:]

def p_Asignacion(p):
	'''Asignacion	:	VAR_ID push_var_PilaOperandos ASSIGN push_operador_PilaOperadores ExpI SEMICOLON resuelve_asignacion
	'''

#Push el id a la pila operandos 
def p_push_var_PilaOperandos(p):
	'''push_var_PilaOperandos	: 
	'''
	variable = edjo.function_directory.get_function_variable(edjo.current_scope, p[-1])
	if variable is None:
		variable = edjo.function_directory.get_function_variable(edjo.global_scope, p[-1])
		if variable is None:
			print("The variable " + p[-1] + " has not been declared")
			sys.exit()
		else:
			edjo.operand_stack.append(variable['memory_adress'])
			edjo.type_stack.append(variable['type'])
	else:
		edjo.operand_stack.append(variable['memory_adress'])
		edjo.type_stack.append(variable['type'])

#Push el operador al pila operadores
def p_push_operador_PilaOperadores(p):
	'''push_operador_PilaOperadores	: 
	'''
	edjo.operator_stack.append(p[-1])

#Resuelve la asignacion
def p_resuelve_asignacion(p):
	'''resuelve_asignacion	: 
	'''
	operator = edjo.operator_stack.pop()
	if operator == '=':
		right_operand = edjo.operand_stack.pop()
		right_type = edjo.type_stack.pop()
		left_operand = edjo.operand_stack.pop()
		left_type = edjo.type_stack.pop()
		result_type = edjo.semantic_cube.get_semantic_type(left_type, right_type, operator)
		if result_type != 'error':
			quadruple = Quadruple(edjo.quadruple_number, operator, right_operand, None, left_operand)
			edjo.quadruple_list.append(quadruple)
			edjo.quadruple_number += 1
		else:
			print('Operation type mismatch at {0}'.format(p.lexer.lineno))
			sys.exit()


def p_ExpI(p):
	'''ExpI		:	ExpK resuelve_operadores_relacionales 
			|	ExpK Operandos push_operador_PilaOperadores ExpK resuelve_operadores_relacionales
	'''

def p_Operandos(p):
	'''Operandos	:	LT
			|	GT
			|	NE
			|	LE
			|	GE
			|	EQ
	'''
	p[0] = p[1]

#Resuelve operadores relacionales
def p_resuelve_operadores_relacionales(p):
	'''resuelve_operadores_relacionales	: 
	'''
	if len(edjo.operator_stack) > 0 and len(edjo.operand_stack) > 1:
		if edjo.operator_stack[-1] in edjo.relational_operations:
			resuelve_operacion(p)

#Resuelve operacion
def resuelve_operacion(p):
	right_operand = edjo.operand_stack.pop()
	right_type = edjo.type_stack.pop()
	left_operand = edjo.operand_stack.pop()
	left_type = edjo.type_stack.pop()
	operator = edjo.operator_stack.pop()
	result_type = edjo.semantic_cube.get_semantic_type(left_type, right_type, operator)
	if result_type != 'error':
		temporal_variable_address = edjo.memory.request_temporal_address(result_type)
		edjo.function_directory.add_temporal_to_function(edjo.current_scope, result_type)
		quadruple = Quadruple(edjo.quadruple_number, operator, left_operand, right_operand, temporal_variable_address)
		edjo.quadruple_list.append(quadruple)
		edjo.quadruple_number += 1
		edjo.operand_stack.append(temporal_variable_address)
		edjo.type_stack.append(result_type)
	else:
		print('Operation type mismatch at {0}'.format(p.lexer.lineno))
		sys.exit()
	
def p_ExpK(p):
	'''ExpK		:	ExpT resuelve_termino 
			|	ExpT resuelve_termino pos_SUMRES push_operador_PilaOperadores ExpK
	'''

#Resuelve termino
def p_resuelve_termino(p):
	'''resuelve_termino	: 
	'''
	if len(edjo.operator_stack) > 0 and len(edjo.operand_stack) > 1:
		if edjo.operator_stack[-1] == '+' or edjo.operator_stack[-1] == '-':
			resuelve_operacion(p)


def p_pos_SUMRES(p):
	'''pos_SUMRES	:	PLUS 
			|	MINUS 
	'''
	p[0] = p[1]

def p_ExpT(p):
	'''ExpT		:	ExpF resuelve_factor 
			|	ExpF resuelve_factor pos_MULTDIV push_operador_PilaOperadores ExpT
	'''
#Resuelve factor
def p_resuelve_factor(p):
	'''resuelve_factor	: 
	'''
	if len(edjo.operator_stack) > 0 and len(edjo.operand_stack) > 1:
		if edjo.operator_stack[-1] == '*' or edjo.operator_stack[-1] == '/':
			resuelve_operacion(p)


def p_pos_MULTDIV(p):
	'''pos_MULTDIV	:	MULT 
			|	DIV 
	'''
	p[0] = p[1]

def p_ExpF(p):
	'''ExpF		:	VAR_CTE
			|	LPAREN agrega_falso ExpI RPAREN quita_falso
			|	VAR_ID push_var_PilaOperandos pos_arreglo
			|	llama_funcion 
	'''
	#falta arreglos

def p_VAR_CTE(p):
	'''VAR_CTE	:	VAR_INT push_int_PilaOperandos
			|	VAR_DECIMAL push_decimal_PilaOperandos
	'''

#Push int pila operandos
def p_push_int_PilaOperandos(p):
	'''push_int_PilaOperandos	:
	'''
	constant_address = edjo.memory.check_existing_constant_value('int', int(p[-1]))
	if constant_address is None:
		constant_address = edjo.memory.request_constant_address('int', int(p[-1]))
	edjo.operand_stack.append(constant_address)
	edjo.type_stack.append('int')
		
#Push decimal pila operandos
def p_push_decimal_PilaOperandos(p):
	'''push_decimal_PilaOperandos	: 
	'''
	constant_address = edjo.memory.check_existing_constant_value('decimal', float(p[-1]))
	if constant_address is None:
		constant_address = edjo.memory.request_constant_address('decimal', float(p[-1]))
	edjo.operand_stack.append(constant_address)
	edjo.type_stack.append('decimal')
	

#Crea la marca falsa 
def p_agrega_falso(p):
	'''agrega_falso	: 
	'''
	edjo.operator_stack.append('()')

#Elimina la marca falsa
def p_quita_falso(p):
	'''quita_falso	: 
	'''
	edjo.operator_stack.pop()

def p_llama_funcion(p):
	'''llama_funcion	:	VAR_ID LPAREN agrega_falso checa_funcion_si_existe argumentos RPAREN quita_falso resuelve_llamada_funcion guarda_resultado_funcion
	'''

#Checa si la funcion existe
def p_checa_funcion_si_existe(p):
	'''checa_funcion_si_existe	: 
	'''
	function = p[-3]
	if edjo.function_directory.has_function(function):
		quadruple = Quadruple(edjo.quadruple_number, 'ERA', function, None, None)
		edjo.quadruple_list.append(quadruple)
		edjo.quadruple_number += 1
		parameters = edjo.function_directory.get_function_parameters(function)
		edjo.temporal_arguments_types = list(parameters['types'])
	else:
		print("The function " +  function + " doesn't exist")
		sys.exit()


def p_argumentos(p):
	'''argumentos	:	ExpI resuelve_argumentos mas_argumentos
			| 
	'''

def p_mas_argumentos(p):
	'''mas_argumentos	: 	COMMA ExpI resuelve_argumentos mas_argumentos
				| 
	'''

#Resuelve argumentos
def p_resuelve_argumentos(p):
	'''resuelve_argumentos	: 
	'''
	if edjo.temporal_arguments_types:
		argument = edjo.operand_stack.pop()
		argument_type = edjo.type_stack.pop()
		parameter_type = edjo.temporal_arguments_types.pop(0)
		if argument_type == parameter_type:
			quadruple = Quadruple(edjo.quadruple_number, 'PARAMETER', argument, None, None)
			edjo.quadruple_list.append(quadruple)
			edjo.quadruple_number += 1
		else:
			print('Argument type mismatch at {0} lines'.format(p.lexer.lineno))
			sys.exit()
	else:
		print('Argument number mismatch at {0} lines'.format(p.lexer.lineno))
		sys.exit()

#Resuelve llamada funcion
def p_resuelve_llamada_funcion(p):
	'''resuelve_llamada_funcion	: 
	'''
	if not edjo.temporal_arguments_types:
		function = p[-7]
		function_quadruple_number = edjo.function_directory.get_function_quadruple_number(function)
		quadruple = Quadruple(edjo.quadruple_number, 'GOSUB', function, None, function_quadruple_number)
		edjo.quadruple_list.append(quadruple)
		edjo.quadruple_number += 1
	else:
		print('Argument number mismatch at {0} line '.format(p.lexer.lineno))
		sys.exit()

#Guarda resultado de funcion
def p_guarda_resultado_funcion(p):
	'''guarda_resultado_funcion	: 
	'''
	function_called = p[-8]
	function = edjo.function_directory.get_function(function_called)
	function_return = function['return_address']
	function_type = function['return_type']
	temporal_variable_address = edjo.memory.request_temporal_address(function_type)
	edjo.function_directory.add_temporal_to_function(edjo.current_scope, function_type)
	quadruple = Quadruple(edjo.quadruple_number, '=', function_return, None, temporal_variable_address)
	edjo.quadruple_list.append(quadruple)
	edjo.quadruple_number += 1
	edjo.operand_stack.append(temporal_variable_address)
	edjo.type_stack.append(function_type)
	

def p_pos_arreglo(p): #todavia no tenemos arreglos
	'''pos_arreglo	:	SLBRACKET ExpI SRBRACKET
			| 
	'''


def p_funciones(p):
	'''funciones	:	FUNC tipo_funcion VAR_ID LPAREN param RPAREN agrega_funcion LBRACKET Vars reg_brack RBRACKET fin_func_quad funciones
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
		edjo.temporal_parameters_names.insert(0, parameter_name)
		edjo.temporal_parameters_types.insert(0, parameter_type)

#Agrega nueva funcion
def p_agrega_funcion(p):
	'''agrega_funcion	: 
	'''
	edjo.current_scope = p[-4]
	function_type = p[-5]
	parameter_address_list = []
	edjo.function_directory.add_function(edjo.current_scope, function_type)
	edjo.function_directory.set_function_quadruple_number(edjo.current_scope, edjo.quadruple_number)
	if function_type != 'void':
		function_address = edjo.memory.request_global_address(function_type)
		edjo.function_directory.set_function_address(edjo.current_scope, function_address)
	parameters = zip(edjo.temporal_parameters_names, edjo.temporal_parameters_types)
	for parameter_name, parameter_type in parameters:
		parameter_address = edjo.memory.request_local_address(parameter_type)
		parameter_address_list.append(parameter_address)
		edjo.function_directory.add_variable_to_function(edjo.current_scope, parameter_type, parameter_name, parameter_address)
	edjo.function_directory.add_parameter_to_function(edjo.current_scope, list(edjo.temporal_parameters_types), list(parameter_address_list))
	del edjo.temporal_parameters_names[:]
	del edjo.temporal_parameters_types[:]

#Crea quadruple fin de funcion	
def p_fin_func_quad(p):
	'''fin_func_quad	: 
	'''
	function_type = p[-10]
	if function_type == 'void' and edjo.return_flag:
		print('Function {0} of type {1} should not have return statement'.format(edjo.current_scope, function_type))
		sys.exit()
	elif function_type != 'void' and not edjo.return_flag:
		print('Function {0} of type {1} should have return statement'.format(edjo.current_scope, function_type))
		sys.exit()
	else:
		quadruple = Quadruple(edjo.quadruple_number, 'ENDPROC', None, None, None)
		edjo.quadruple_list.append(quadruple)
		
	if edjo.return_flag:
		while edjo.return_list:
			quadruple_number_to_fill = edjo.return_list.pop()
			edjo.quadruple_list[quadruple_number_to_fill - 1].fill_quadruple_jump(edjo.quadruple_number)
	edjo.quadruple_number += 1
	edjo.return_flag = False
	edjo.current_scope = edjo.global_scope
	edjo.memory.reset_temporal_memory()

def p_reg_brack(p):
	'''reg_brack	:	Estatutos reg_brack
			| 
	'''
def p_Estatutos(p):
	'''Estatutos	:	Condicion 
			|	Ciclo  
			|	Return 
			|	Asignacion
			|	Print 
			|	Llamada_Func 
			|	TurtleMotion 
	'''
def p_Condicion(p):
	'''Condicion	:	IF LPAREN ExpI RPAREN crea_GOTOF LBRACKET reg_brack RBRACKET pos_else llena_cuadruplo_if
	'''

def p_crea_GOTOF(p):
	'''crea_GOTOF	: 
	'''
	quadrupleGOTOF(p)

def quadrupleGOTOF(p):#cambiar el if de estilo para que sea diferente
	type_result = edjo.type_stack.pop()
	if type_result != 'bool':
		print('Operation type mismatch in line {0}'.format(p.lexer.lineno))
		sys.exit()
	else:
		result = edjo.operand_stack.pop()
		quadruple = Quadruple(edjo.quadruple_number, 'GOTOF', result, None, None)
		edjo.quadruple_list.append(quadruple)
		edjo.jump_list.append(edjo.quadruple_number - 1)
		edjo.quadruple_number += 1

def p_llena_cuadruplo_if(p):
	'''llena_cuadruplo_if	: 
	'''
	quadruple_number_to_fill = edjo.jump_list.pop()
	quadruple = edjo.quadruple_list[quadruple_number_to_fill]
	quadruple.fill_quadruple_jump(edjo.quadruple_number)


def p_pos_else(p):
	'''pos_else	:	ELSE crea_else_cuadruplo LBRACKET reg_brack RBRACKET
			| 
	'''

def p_crea_else_cuadruplo(p):
	'''crea_else_cuadruplo	: 
	'''
	quadruple = Quadruple(edjo.quadruple_number, 'GOTO', None, None, None)
	edjo.quadruple_list.append(quadruple)
	quadruple_number_to_fill = edjo.jump_list.pop()
	quadruple = edjo.quadruple_list[quadruple_number_to_fill]
	edjo.jump_list.append(edjo.quadruple_number - 1)
	edjo.quadruple_number += 1
	quadruple.fill_quadruple_jump(edjo.quadruple_number)
	

def p_Return(p):
	'''Return 	:	RETURN ExpI SEMICOLON resuelve_return
	'''

#Resuelve el return
def p_resuelve_return(p):
	'''resuelve_return	: 
	'''
	edjo.return_flag = True
	operand = edjo.operand_stack.pop()
	operand_type = edjo.type_stack.pop()
	function = edjo.function_directory.get_function(edjo.current_scope)
	function_type = function['return_type']
	function_return_address = function['return_address']
	if function_type != operand_type:
		print("Return type of function {0} doesn't match function return type".format(edjo.current_scope))
		sys.exit()
	quadruple = Quadruple(edjo.quadruple_number, 'RETURN', operand, None, function_return_address)
	edjo.quadruple_list.append(quadruple)
	edjo.quadruple_number += 1
	quadruple = Quadruple(edjo.quadruple_number, 'GOTO', None, None, None)
	edjo.return_list.append(edjo.quadruple_number)
	edjo.quadruple_list.append(quadruple)
	edjo.quadruple_number += 1
	

def p_Print(p):
	'''Print	:	PRINT LPAREN VAR_STRING RPAREN SEMICOLON
			|	PRINT LPAREN ExpI RPAREN SEMICOLON crea_print
	'''

def p_crea_print(p):
	'''crea_print	: 
	'''
	operand = edjo.operand_stack.pop()
	quadruple = Quadruple(edjo.quadruple_number, 'PRINT', operand, None, None)
	edjo.quadruple_list.append(quadruple)
	edjo.quadruple_number += 1


def p_Llamada_Func(p):
	'''Llamada_Func	:	VAR_ID LPAREN agrega_falso checa_funcion_si_existe argumentos RPAREN quita_falso resuelve_llamada_funcion SEMICOLON vtc_action
	'''

def p_vtc_action(p):
	'''vtc_action	: 
	'''
	function = p[-9]
	function_type = edjo.function_directory.get_function_type(function)
	if function_type != 'void':
		print("This function {0} is not a void function".format(function))
		sys.exit()

def p_Ciclo(p):
	'''Ciclo	:	For
			|	While
			|	DoWhile
	'''

def p_While(p):
	'''While	:	WHILE guarda_numero_cuadruplo LPAREN ExpI RPAREN crea_GOTOF LBRACKET reg_brack RBRACKET regresa_inicio_while
	'''

def p_guarda_numero_cuadruplo(p):
	'''guarda_numero_cuadruplo	: 
	'''
	edjo.jump_list.append(edjo.quadruple_number)
	
def p_regresa_inicio_while(p):
	'''regresa_inicio_while	: 
	'''
	quadruple_number_to_fill = edjo.jump_list.pop()
	quadruple_number_to_return = edjo.jump_list.pop()
	while_quadruple = Quadruple(edjo.quadruple_number, 'GOTO', None, None, quadruple_number_to_return)
	edjo.quadruple_list.append(while_quadruple)
	edjo.quadruple_number += 1
	conditional_quadruple = edjo.quadruple_list[quadruple_number_to_fill]
	conditional_quadruple.fill_quadruple_jump(edjo.quadruple_number)


def p_DoWhile(p):
	'''DoWhile	:	DO LBRACKET reg_brack RBRACKET WHILE LPAREN ExpI RPAREN SEMICOLON
	'''

def p_For(p):
	'''For		:	FOR LPAREN VAR_ID ASSIGN ExpI SEMICOLON ExpI SEMICOLON VAR_ID Exp_ciclo RPAREN LBRACKET reg_brack RBRACKET
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
			|	IniciaTurtle
			|	TerminaTurtle
	'''
def p_Position(p):
	'''Position	:	TUR POINT POS LPAREN ExpI COMMA ExpI RPAREN SEMICOLON pfc_set_position
	'''

def p_pfc_set_position(p):
	'''pfc_set_position	: 
	'''
	y = edjo.operand_stack.pop()
	x = edjo.operand_stack.pop()
	quadruple = Quadruple(edjo.quadruple_number, 'SET_POSITION', x, y, None)
	edjo.quadruple_list.append(quadruple)
	edjo.quadruple_number += 1

def p_Forward(p):
	'''Forward	:	TUR POINT FORWARD LPAREN ExpI RPAREN SEMICOLON pfc_move_forward
	'''

def p_pfc_move_forward(p):
	'''pfc_move_forward	: 
	'''
	operand = edjo.operand_stack.pop()
	quadruple = Quadruple(edjo.quadruple_number, 'MOVE_FORWARD', operand, None, None)
	edjo.quadruple_list.append(quadruple)
	edjo.quadruple_number += 1

def p_Right(p):
	'''Right	:	TUR POINT RIGHT LPAREN ExpI RPAREN SEMICOLON pfc_turn_right
	'''

def p_pfc_turn_right(p):
	'''pfc_turn_right	: 
	'''
	operand = edjo.operand_stack.pop()
	quadruple = Quadruple(edjo.quadruple_number, 'TURN_RIGHT', operand, None, None)
	edjo.quadruple_list.append(quadruple)
	edjo.quadruple_number += 1

def p_Left(p):
	'''Left		:	TUR POINT LEFT LPAREN ExpI RPAREN SEMICOLON pfc_turn_left
	'''

def p_pfc_turn_left(p):
	'''pfc_turn_left	: 
	'''
	operand = edjo.operand_stack.pop()
	quadruple = Quadruple(edjo.quadruple_number, 'TURN_LEFT', operand, None, None)
	edjo.quadruple_list.append(quadruple)
	edjo.quadruple_number += 1

def p_Circle(p):
	'''Circle	:	TUR POINT CIRCLE LPAREN ExpI RPAREN SEMICOLON pfc_draw_circle
	'''

def p_pfc_draw_circle(p):
	'''pfc_draw_circle	: 
	'''
	operand = edjo.operand_stack.pop()
	quadruple = Quadruple(edjo.quadruple_number, 'DRAW_CIRCLE', operand,  None, None)
	edjo.quadruple_list.append(quadruple)
	edjo.quadruple_number += 1
	

def p_IniciaTurtle(p):
	'''IniciaTurtle	:	TUR POINT TURTLE LPAREN RPAREN SEMICOLON pfc_create_turtle
	'''

def p_pfc_create_turtle(p):
	'''pfc_create_turtle	: 
	'''
	quadruple = Quadruple(edjo.quadruple_number, 'CREATE_TURTLE', None, None, None)
	edjo.quadruple_list.append(quadruple)
	edjo.quadruple_number += 1

def p_TerminaTurtle(p):
	'''TerminaTurtle	:	TUR POINT FINISH LPAREN RPAREN SEMICOLON pfc_finish_drawing
	'''

def p_pfc_finish_drawing(p):
	'''pfc_finish_drawing	: 
	'''
	quadruple = Quadruple(edjo.quadruple_number, 'FINISH_DRAWING', None, None, None)
	edjo.quadruple_list.append(quadruple)
	edjo.quadruple_number += 1

def p_Main(p):
	'''Main		:	MAIN agrega_main_funcion LPAREN RPAREN LBRACKET Vars reg_brack RET ZERO SEMICOLON RBRACKET
	'''

def p_agrega_main_funcion(p):
	'''agrega_main_funcion	: 
	'''
	edjo.current_scope = p[-1]
	edjo.function_directory.add_function(edjo.current_scope, 'void')
	edjo.function_directory.set_function_quadruple_number(edjo.current_scope, edjo.quadruple_number)
	quadruple = edjo.quadruple_list[0]
	quadruple.fill_quadruple_jump(edjo.quadruple_number)





import ply.yacc as yacc
import pprint
parser = yacc.yacc()
pp = pprint.PrettyPrinter(indent=4)

with open('prueba.txt','r') as f:
	input = f.read()
	pp.pprint(parser.parse(input))

	edjo.function_directory.print_directory()
	edjo.print_quadruples()
	virtual_machine = VirtualMachine(edjo.memory, edjo.function_directory, edjo.quadruple_list)
	virtual_machine.execute("Y")
	
