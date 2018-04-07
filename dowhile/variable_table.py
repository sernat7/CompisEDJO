class VariableTable():

    def __init__(self):
        self.variable_list = {}

    def add_variable(self, variable_type, variable_name,
            variable_memory_adress = 0):
        self.variable_list[variable_name] = {
            'name' : variable_name,
            'type' : variable_type,
            'memory_adress' : variable_memory_adress
        }

    def add_dimensioned_variable(self, variable):
        self.variable_list[variable['name']] = variable 

    def has_variable(self, variable_name):
        return variable_name in self.variable_list.keys()

    def get_variable(self, variable_name):
        if self.has_variable(variable_name):
            return self.variable_list[variable_name]
        else:
            return None

    def __str__(self):
        return self.variable_list
