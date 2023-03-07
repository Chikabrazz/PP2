class mystring():
    def ___init___(self, txt):
        self.txt = ""
    def get_string(self):
        self.txt = input()
    def print_string(self):
        print(self.txt.upper())
        
p1 = mystring()
p1.get_string()
p1.print_string()