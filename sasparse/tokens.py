class _TokenType(tuple):
    parent = None

    def __contains__(self, item):
        return item is not None and (self is item or item[:len(self)] == self)

    def __getattr__(self, attr):
        new = _TokenType(self + (attr,))
        setattr(self, attr, new)
        new.parent = self
        return new
    
    def __repr__(self):
        return "Token" + ("." if self else "") + ".".join(self)
    

Token = _TokenType()

Text = Token.Text
Whitespace = Text.Whitespace
Newline = Text.Newline

Comment = Token.Comment

Format = Token.Format

Name = Token.Name
Variable = Name.Variable

Literal = Token.Literal
Number = Literal.Number
String = Literal.String
Single = String.Single
Double = String.Double

Punctuation = Token.Punctuation
Operator = Token.Operator
Comparison = Operator.Comparison

Wildcard = Token.Wildcard

Keyword = Token.Keyword
Function = Keyword.Function
Macro = Keyword.Macro
Conditional = Keyword.Conditional
Proc = Keyword.Proc
Data = Keyword.Data
EndStep = Keyword.EndStep
Quit = EndStep.Quit
Run = EndStep.Run
Connect = Keyword.Connect
Disconnect = Keyword.Disconnect
ConnectionTo = Keyword.ConnectionTo
Execute = Keyword.Execute
ExecuteBy = Keyword.ExecuteBy
SqlKeyword = Keyword.SqlKeyword

Error = Token.Error

