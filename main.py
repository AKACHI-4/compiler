from lexer import Lexer

text_input = """
solve(4 + 4 - 2);
"""

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

for token in tokens:
  print(token)