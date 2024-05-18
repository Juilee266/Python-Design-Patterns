
# Product
class Computer:
    def __init__(self, cpu, memory):
        self.cpu = cpu
        self.memory = memory

    def __str__(self):
        return f"Computer with {self.cpu} CPU and {self.memory} Memory."

# Builder interface
class ComputerBuilder:
    def set_cpu(self, cpu):
        pass
    def set_memory(self, memory):
        pass
    def build(self) -> Computer:
        pass

# Concrete Builder
class GamingComputerBuilder(ComputerBuilder):
    def set_cpu(self, cpu):
        self.cpu = cpu

    def set_memory(self, memory):
        self.memory = memory

    def build(self) -> Computer:
        return Computer(self.cpu, self.memory)

class Director:
    def __init__(self, builder: ComputerBuilder):
        self.builder = builder

    def construct(self, cpu, memory) -> Computer:
        self.builder.set_cpu(cpu)
        self.builder.set_memory(memory)
        return self.builder.build()

if __name__ == "__main__":
    gc_builder = GamingComputerBuilder()
    director = Director(gc_builder)
    gaming_computer = director.construct("Inter i7", 250)
    print(gaming_computer)