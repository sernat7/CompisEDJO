from type_segment import TypeSegment
import sys

class MemorySegment():

    def __init__(self, memory_name, initial_address, total_addresses):
        self.name = memory_name
        self.type_segment_size = int(total_addresses / 4)
        self.initial_address = initial_address
        self.final_address= initial_address + total_addresses - 1

        # Calculates the initial and final addresses for each type segment
        self.int_initial_address = initial_address
        self.int_final_address = initial_address + self.type_segment_size - 1
        self.decimal_initial_address = initial_address + self.type_segment_size
        self.decimal_final_address = initial_address + self.type_segment_size * 2 - 1
        self.string_initial_address = initial_address + self.type_segment_size * 2
        self.string_final_address = initial_address + self.type_segment_size * 3 - 1
        self.bool_initial_address = initial_address + self.type_segment_size * 3
        self.bool_final_address = initial_address + self.type_segment_size * 4 - 1

        # Creates the type segments
        self.int_segment = TypeSegment('Integer', self.int_initial_address,
            self.int_final_address)
        self.decimal_segment = TypeSegment('Decimal', self.decimal_initial_address,
            self.decimal_final_address)
        self.string_segment = TypeSegment('String', self.string_initial_address,
            self.string_final_address)
        self.bool_segment = TypeSegment('Boolean', self.bool_initial_address,
            self.bool_final_address)

    def request_address(self, segment_type, value=None):
        if segment_type == 'int':
            if value is None:
                value = 0
            return self.int_segment.request_address(value)
        elif segment_type == 'decimal':
            if value is None:
                value = 0.0
            return self.decimal_segment.request_address(value)
        elif segment_type == 'string':
            if value is None:
                value = ""
            return self.string_segment.request_address(value)
        elif segment_type == 'bool':
            if value is None:
                value = False
            return self.bool_segment.request_address(value)

    def request_sequential_addresses(self, segment_type, total_addresses, value=None):
        if segment_type == 'int':
            if value is None:
                value = 0
            return self.int_segment.request_sequential_addresses(total_addresses, value)
        elif segment_type == 'decimal':
            if value is None:
                value = 0.0
            return self.decimal_segment.request_sequential_addresses(total_addresses, value)
        elif segment_type == 'string':
            if value is None:
                value = ""
            return self.string_segment.request_sequential_addresses(total_addresses, value)
        elif segment_type == 'bool':
            if value is None:
                value = False
            return self.bool_segment.request_sequential_addresses(total_addresses, value)

    def determines_segment_tpye(self, address):
        if (address >= self.int_initial_address and address <=
            self.int_final_address):
            return 'int'
        elif (address >= self.decimal_initial_address and address <=
            self.decimal_final_address):
            return 'decimal'
        elif (address >= self.string_initial_address and address <=
            self.string_final_address):
            return 'string'
        elif (address >= self.bool_initial_address and address <=
            self.bool_final_address):
            return 'bool'
        else:
            print("Invalid address in the " + self.name + " memory")
            sys.exit()

    def get_value(self, address):
        segment_type = self.determines_segment_tpye(address)
        if segment_type == 'int':
            return self.int_segment.get_value(address)
        elif segment_type == 'decimal':
            return self.decimal_segment.get_value(address)
        elif segment_type == 'string':
            return self.string_segment.get_value(address)
        elif segment_type == 'bool':
            return self.bool_segment.get_value(address)

    def edit_value(self, address, value):
        segment_type = self.determines_segment_tpye(address)
        if segment_type == 'int':
            self.int_segment.edit_value(address, value)
        elif segment_type == 'decimal':
            self.decimal_segment.edit_value(address, value)
        elif segment_type == 'string':
            self.string_segment.edit_value(address, value)
        elif segment_type =='bool':
            self.bool_segment.edit_value(address, value)

    def check_existing_value(self, segment_type, value):
        if segment_type == 'int':
            return self.int_segment.check_existing_value(value)
        elif segment_type == 'decimal':
            return self.decimal_segment.check_existing_value(value)
        elif segment_type == 'string':
            return self.string_segment.check_existing_value(value)
        elif segment_type =='bool':
            return self.bool_segment.check_existing_value(value)

    def reset_memory(self):
        self.int_segment.reset()
        self.decimal_segment.reset()
        self.bool_segment.reset()
        self.string_segment.reset()

    def print_segment(self, segment_type = ""):
        print("Memory : " + self.name + "\n" +
              "   Initial address : " + str(self.initial_address) + "\n" +
              "   Final address : " + str(self.final_address))
        if segment_type == 'int':
            print(self.int_segment)
        elif segment_type == 'decimal':
            print(self.decimal_segment)
        elif segment_type == 'string':
            print(self.string_segment)
        elif segment_type == 'bool':
            print(self.bool_segment)
        else:
            print(self.int_segment)
            print(self.decimal_segment)
            print(self.string_segment)
            print(self.bool_segment)
