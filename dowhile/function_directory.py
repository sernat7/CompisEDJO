import json 

from variable_table import VariableTable

class FunctionDirectory():

    def __init__(self):
        self.function_list = {}

    def add_function(self, function_name, function_type,
            function_parameter_list = [], function_parameter_adresses = []):
        self.function_list[function_name] = {
            'name' : function_name,
            'return_type' : function_type,
            'return_address' : -1,
            'quadruple_number' : -1,
            'parameters' : {
                'types' : function_parameter_list,
                'addresses' : function_parameter_adresses,
            },
            'variables': VariableTable(),
            'number_of_local_variables' : {
                'int' : 0,
                'decimal' : 0,
                'string' : 0,
                'bool' : 0
            },
            'number_of_temporal_variables' : {
                'int' : 0,
                'decimal' : 0,
                'string' : 0,
                'bool' : 0
            }
        }

    def has_function(self, function_name):
        return function_name in self.function_list.keys()

    def get_function(self, function_name):
        if self.has_function(function_name):
            return self.function_list[function_name]
        else:
            print("A function with this name doesn't exist")
            return None

    def add_parameter_to_function(self, function_name, type_list, addresses_list):
        function = self.get_function(function_name)
        if function is not None:
            function['parameters']['types'] = type_list
            function['parameters']['addresses'] = addresses_list
        else:
            print("The function you are trying to add the paremeter doesnt exist")

    def add_variable_to_function(self, function_name, variable_type,
            variable_name, variable_adress=0):
        function = self.get_function(function_name)
        if function is not None:
            if function['variables'].has_variable(variable_name):
                print("This function already has a variable with that name")
            else:
                function['variables'].add_variable(variable_type, variable_name, variable_adress)
                function['number_of_local_variables'][variable_type] += 1
        else:
            print("The function you are trying to add the variable doesnt exists")

    def add_dimensioned_variable_to_function(self, function_name, variable):
        function = self.get_function(function_name)
        if function is not None:
            if function['variables'].has_variable(variable['name']):
                print("This function already has a variable with that name")
            else:
                function['variables'].add_dimensioned_variable(variable)
                for i in range(variable['upper_limit']):
                    function['number_of_local_variables'][variable['type']] += 1
        else:
            print("The function you are trying to add the variable doesnt exists")

    def check_existing_variable(self, function_name, variable_name):
        function = self.get_function(function_name)
        if function is not None:
            if function['variables'].has_variable(variable_name):
                return True
            else:
                return False
        else:
            print("The variable " + variable_name + " has been already declared")

    def add_temporal_to_function(self, function_name, temporal_type):
        function = self.get_function(function_name)
        if function is not None:
            function['number_of_temporal_variables'][temporal_type] += 1
        else:
            print("The function you are trying to add the temporal doesnt exists")

    def get_function_variable(self, function_name, variable_name):
        function = self.get_function(function_name)
        if function is not None:
            variable = function['variables'].get_variable(variable_name)
            if variable is not None:
                return variable
            else:
                return None
        else:
            print("The function you are trying to find when looking for the" +
                "variable doesn't exists")

    def get_function_type(self, function_name):
        function = self.get_function(function_name)
        if function is not None:
            function_type = function['return_type']
            return function_type
        else:
            print("This function doesn't exists")

    def get_function_parameters(self, function_name):
        function = self.get_function(function_name)
        if function is not None:
            return function['parameters']
        else:
            print("The function you are trying to retrieve its parameters" +
                "doesnt exists")

    def set_function_quadruple_number(self, function_name, quadruple_number):
        function = self.get_function(function_name)
        if function is not None:
            function['quadruple_number'] = quadruple_number
        else:
            print("The function you are trying to set the quadruple doesn't exists")

    def set_function_address(self, function_name, address_number):
        function = self.get_function(function_name)
        if function is not None:
            function['return_address'] = address_number
        else:
            print("The function you are trying to add the adress doesn't exists")

    def get_function_quadruple_number(self, function_name,):
        function = self.get_function(function_name)
        if function is not None:
            return function['quadruple_number']
        else:
            print("The function you are trying to retrieve its quadruple doesn't exists")

    def print_directory(self):
        for function, properties in self.function_list.items():
            print("function : " + str(function))
            for prop, value in properties.items():
                if isinstance(value, VariableTable):
                    print("  " + str(prop) + " : " +
                        json.dumps(value.variable_list, indent=4))
                elif isinstance(value, dict):
                    print("  " + str(prop) + " : " +
                        json.dumps(value, indent=4))
                else:
                    print("  " + str(prop) + " : " + str(value))

            print("-" * 80)
