class Quadruple():
    def __init__(self, quadruple_number, operator, left_operand, right_operand,
            result):
        self.quadruple_number = quadruple_number
        self.operator = operator
        self.left_operand = left_operand
        self.right_operand = right_operand
        self.result = result

    def fill_quadruple_jump(self, jump_number):
        self.result = jump_number

    def __str__(self):
        return (str(self.quadruple_number)  + "\t | \t" + str(self.operator) + "\t | \t"
            + str(self.left_operand) + "\t |  \t" + str(self.right_operand) + "\t |  \t"
            + str(self.result))
