from rply import LexerGenerator

class Lexer():
  def __init__(self):
    self.lexer = LexerGenerator()

  def _add_tokens(self):
    self.lexer.add('PRINT', r'solve')
    
    self.lexer.add('OPEN_PAREN', r'\(')
    self.lexer.add('CLOSE_PAREN', r'\)')

    self.lexer.add('NUMBER', r'\d+')

    self.lexer.add('ADD', r'\+')
    self.lexer.add('SUB', r'\-')
    self.lexer.add('MUL', r'\*')
    self.lexer.add('DIV', r'\/')

    self.lexer.add('SEMI_COLON', r'\;')

    self.lexer.ignore('\s+')

  def get_lexer(self):
    self._add_tokens()
    return self.lexer.build()







"""
Token('PRINT', 'print')
Token('OPEN_PAREN', '(')
Token('NUMBER', '4')
Token('SUM', '+')
Token('NUMBER', '4')
Token('SUB', '-')
Token('NUMBER', '2')
Token('CLOSE_PAREN', ')')
Token('SEMI_COLON', ';')
"""