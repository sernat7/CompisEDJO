from memory_segment import MemorySegment
import sys

class Memory():

    def __init__(self):
        self.global_memory = MemorySegment('Global', 5000, 2000)
        self.local_memory = MemorySegment('Local', 9000, 2000)
        self.constant_memory = MemorySegment('Constant', 20000, 2000)
        self.temporal_memory = MemorySegment('Temporal', 43000, 2000)

    def request_global_address(self, value_type, value=None,):
        return self.global_memory.request_address(value_type, value)

    def request_local_address(self, value_type, value=None,):
        return self.local_memory.request_address(value_type, value)

    def request_constant_address(self, value_type, value=None):
        return self.constant_memory.request_address(value_type, value)

    def request_temporal_address(self, value_type, value=None):
        return self.temporal_memory.request_address(value_type, value)

    def request_sequential_global_addresses(self, value_type, total_addresses, value=None):
        return self.global_memory.request_sequential_addresses(value_type,
            total_addresses, value)

    def request_sequential_local_addresses(self, value_type, total_addresses, value=None):
        return self.global_memory.request_sequential_addresses(value_type,
            total_addresses, value)

    def determines_memory_type(self, address):
        if (address >= self.global_memory.initial_address and address <=
            self.global_memory.final_address):
            return 'global'
        elif (address >= self.local_memory.initial_address and address <=
            self.local_memory.final_address):
            return 'local'
        elif (address >= self.temporal_memory.initial_address and address <=
            self.temporal_memory.final_address):
            return 'temporal'
        elif (address >= self.constant_memory.initial_address and address <=
            self.constant_memory.final_address):
            return 'constant'
        else:
            print("Invalid address: " + str(address))
            sys.exit()

    def get_value(self, address):
        memory_type = self.determines_memory_type(address)
        if memory_type == 'global':
            return self.global_memory.get_value(address)
        elif memory_type == 'local':
            return self.local_memory.get_value(address)
        elif memory_type == 'temporal':
            return self.temporal_memory.get_value(address)
        elif memory_type == 'constant':
            return self.constant_memory.get_value(address)

    def edit_value(self, address, value):
        memory_type = self.determines_memory_type(address)
        if memory_type == 'global':
            self.global_memory.edit_value(address, value)
        elif memory_type == 'local':
            self.local_memory.edit_value(address, value)
        elif memory_type == 'temporal':
            self.temporal_memory.edit_value(address, value)
        elif memory_type == 'constant':
            self.constant_memory.edit_value(address, value)

    def check_existing_constant_value(self, value_type, value):
        return self.constant_memory.check_existing_value(value_type, value)

    def reset_temporal_memory(self):
        self.local_memory.reset_memory()
        self.temporal_memory.reset_memory()

    def print_memory(self, memory_type, segment_type = ""):
        if memory_type == 'global':
            self.global_memory.print_segment(segment_type)
        elif memory_type == 'local':
            self.local_memory.print_segment(segment_type)
        elif memory_type == 'temporal':
            self.temporal_memory.print_segment(segment_type)
        elif memory_type == 'constant':
            self.constant_memory.print_segment(segment_type)
        else:
            self.global_memory.print_segment(segment_type)
            self.local_memory.print_segment(segment_type)
            self.temporal_memory.print_segment(segment_type)
            self.constant_memory.print_segment(segment_type)
