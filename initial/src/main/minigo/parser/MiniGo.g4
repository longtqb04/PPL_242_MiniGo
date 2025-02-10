grammar MiniGo;

@lexer::header {
from lexererr import *
}

@lexer::members {
def __init__(self, input=None, output:TextIO = sys.stdout):
    super().__init__(input, output)
    self.checkVersion("4.9.2")
    self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
    self._actions = None
    self._predicates = None
    self.preType = None

def emit(self):
    tk = self.type
    self.preType = tk
    valid_types = {
        self.ID, self.INT_LIT, self.FLOAT_LIT, self.STRING_LIT, 
        self.TRUE, self.FALSE, self.RETURN, self.CONTINUE, self.BREAK, 
        self.CRP, self.SRP, self.RP, self.NIL
    }
    if tk == self.NEWLINE:
        if self.preType in valid_types:
            tk = self.SEMICOLON  # Convert newline to semicolon
            self.text = ';'
        else:
            return self.nextToken()  # Ignore the newline
    
    elif tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();

}

options{
	language = Python3;
}

// ! ---------------- LEXER ----------------------- */

// Keywords
IF: 'if';
ELSE: 'else';
FOR: 'for';
RETURN: 'return';
FUNCTION: 'func';
TYPE: 'type';
STRUCT: 'struct';
INTERFACE: 'interface';
STRING: 'string';
INTEGER: 'int';
FLOAT: 'float';
BOOLEAN: 'boolean';
CONSTANT: 'const';
VARIABLE: 'var';
CONTINUE: 'continue';
BREAK: 'break';
RANGE: 'range';
NIL: 'nil';
TRUE: 'true';
FALSE: 'false';

// Operators
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
EQ: '==';
NEQ: '!=';
LT: '<';
GT: '>';
LEQ: '<=';
GEQ: '>=';
AND: '&&';
OR: '||';
NOT: '!';
ASSIGN: '=';
ASSIGN_VAR: ':=';
ASSIGN_ADD: '+=';
ASSIGN_SUB: '-=';
ASSIGN_MUL: '*=';
ASSIGN_DIV: '/=';
ASSIGN_MOD: '%=';
DOT: '.';
COLON: ':';

// Separators
LP: '(';
RP: ')';
SLP: '[';
SRP: ']';
CLP: '{';
CRP: '}';
COMMA: ',';
SEMICOLON: ';';

// Identifiers
ID: [a-zA-Z_][a-zA-Z0-9_]*;

// Literals
INT_LIT: SUB | '0' | [1-9][0-9]*;
FLOAT_LIT: DIGIT+ OPT_FRAC OPT_EXP;
// FLOAT_LIT: '0' OPT_FRAC OPT_EXP
//         | [1-9] DIGIT* OPT_FRAC OPT_EXP;
fragment DIGIT: [0-9];
// fragment DIGITS: DIGIT+;
fragment OPT_FRAC: '.' (DIGIT*)?;
fragment OPT_EXP: ([Ee] [+-]? DIGIT+)?;
// fragment OPT_EXP: ([Ee] [+-]? '0' | [Ee] [+-]? [1-9] DIGIT*)?;

BIN: '0'[bB][0-1]+;
OCT: '0'[oO][0-7]+;
HEX: '0'[xX][0-9a-fA-F]+;

STRING_LIT: '"' STR_CHAR* '"' {
    self.text = self.text[1:-1]
};
fragment STR_CHAR: ~[\n\\"] | ESC_SEQ;
fragment ESC_SEQ: '\\' [rnt"\\] | '\'"';
fragment ESC_ILLEGAL: '\\' ~[ntr'\\];

// Skips

NEWLINE: [\n];
LINE_COMMENT: '//' ~[\r\n]* -> skip;
BLOCK_COMMENT : '/*' (BLOCK_COMMENT | .)*? '*/' -> skip;
WS: [ \t\r\f]+ -> skip;

// Errors
ERROR_CHAR: . {raise ErrorToken(self.text)};

UNCLOSE_STRING: '"' STR_CHAR* ('\r\n' | '\n' | EOF) {
    if(len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
        raise UncloseString(self.text[1:-2])
    elif (self.text[-1] == '\n'):
        raise UncloseString(self.text[1:-1])
    else:
        raise UncloseString(self.text[1:])
};

ILLEGAL_ESCAPE: '"' STR_CHAR* ESC_ILLEGAL '"' {
    raise IllegalEscape(self.text[1:-1])
};

//! ---------------- LEXER ----------------------- */

// ! ---------------- PARSER ----------------------- */

program: NEWLINE* declared (declared | NEWLINE)* EOF;
declared:
	variables_declared
    | constants_declared
	| function_declared
	| method_declared
	| struct_declared
	| interface_declared
    ;

function_declared: function | (variables_declared ignore);

// Declarations
variables_declared: (inferred_var | keyword_type_var | struct_variable_declared) SEMICOLON ignore?; 
inferred_var: VARIABLE ID (type_key_variable | array_literal)? ASSIGN expression;
struct_variable_declared: VARIABLE ID ID (ASSIGN dimensions type_literal)?
    | VARIABLE ID ID ASSIGN dimensions type_literal CLP array_elements CRP
    | VARIABLE ID ID (ASSIGN ID (CLP (struct_literal_recur)? CRP)?)?
    | VARIABLE ID ID ASSIGN expression (ADD | SUB | MUL | DIV | MOD) expression
    | VARIABLE ID ID ASSIGN expression (AND | OR) expression
    | VARIABLE ID ID ASSIGN expression (EQ | NEQ | LT | GT | LEQ | GEQ) expression
    | VARIABLE ID ID ASSIGN ID (DOT ID)*
    | VARIABLE ID ID ASSIGN expression (DOT expression)*
    | VARIABLE ID ID ASSIGN expression SLP expression SRP;

keyword_type_var: VARIABLE ID type_key_variable (ASSIGN expression | ASSIGN array_literal)?
    | VARIABLE ID array_literal (ASSIGN expression | ASSIGN array_literal)?;
keyword_type_var_infunction: (ID | ID LP list_number_lit RP) (type_key | array_literal)?;
keyword_type_var_inmethod: (ID | ID LP list_number_lit RP) (type_key | array_literal);
list_number_lit: INT_LIT | INT_LIT COMMA list_number_lit | FLOAT_LIT | FLOAT_LIT COMMA list_number_lit;
type_key: INTEGER | FLOAT | STRING | BOOLEAN | ID;
type_key_variable: INTEGER | FLOAT | STRING | BOOLEAN;

constants_declared: CONSTANT ID ASSIGN expression (SEMICOLON | NEWLINE) ignore?;

function: FUNCTION ID LP (ID (COMMA ID)* type_key)? (COMMA list_para_infunction)? RP (type_key | array_literal)? CLP ignore? (list_statement_in_function)? CRP ignore?;

list_para_infunction: keyword_type_var_infunction | keyword_type_var_infunction COMMA list_para_infunction;
list_para_infunction_method: keyword_type_var_inmethod | keyword_type_var_inmethod COMMA list_para_infunction_method;

struct_declared: TYPE ID STRUCT CLP ignore? (struct_variable_list)? CRP ignore;

struct_variable_list: struct_variable_list_recur ignore?;
struct_variable_list_recur: ID (type_key | array_literal) | ID (type_key | array_literal) ignore struct_variable_list_recur;

method_declared: FUNCTION LP list_para_inmethod RP ID LP list_para_infunction_method? RP (type_key | array_literal)? CLP (list_statement | argument_list)* CRP;

list_para_inmethod: ID ID | ID ID COMMA list_para_inmethod;

interface_declared: TYPE ID INTERFACE CLP ignore* (list_para_interface)? ignore* CRP ignore?;

list_para_interface: ID LP list_para_infunction? RP (type_key | array_literal)? (ignore ID LP list_para_infunction? RP (type_key | array_literal)?)*;

literal:
	INT_LIT
    | BIN
    | OCT
    | HEX
	| FLOAT_LIT
	| STRING_LIT
	| TRUE
	| FALSE
	| array_literal
	| struct_literal
    ;

// Expressions
expression: expression OR expression1 | expression1;
expression1: expression1 AND expression2 | expression2;
expression2: expression2 (EQ | NEQ | LT | GT | LEQ | GEQ) expression3 | expression3;
expression3: expression3 (ADD | SUB) expression4 | expression4;
expression4: expression4 (MUL | DIV | MOD) expression5 | expression5;
expression5: (NOT | SUB) expression5 | expression6;
expression6: expression6 (LP index_operators_recur? RP)? dimensions
    | expression6 dimensions SLP expression SRP
    | expression6 DOT expression7
    | expression7;
expression7: literal | ID | LP expression RP | call_statement;

// Literals
array_literal: dimensions type_literal (CLP (array_elements | array_element_set) CRP)?;
array_element_set: CLP array_elements CRP | CLP array_elements CRP COMMA array_element_set;
array_literal_declare: dimensions type_literal;
array_elements: valid_element | valid_element COMMA array_elements;
valid_element: INT_LIT | BIN | OCT | HEX | FLOAT_LIT | STRING_LIT | TRUE | FALSE | struct_literal;

dimensions: SLP INT_LIT SRP (SLP INT_LIT SRP)?;
type_literal: STRING | INTEGER | FLOAT | BOOLEAN | ID;
type_literal_except_struct: STRING | INTEGER | FLOAT | BOOLEAN;

struct_literal: ID CLP struct_literal_recur CRP;
struct_literal_recur: ID COLON expression | ID COLON expression COMMA struct_literal_recur;

index_operators: index_operators_recur ignore?;
index_operators_recur: expression | expression COMMA index_operators_recur;

argument_list: argument_list_recur ignore?;
argument_list_recur: expression | expression ignore index_operators_recur;

for_argument_list: expression | (variables_declared_for | assign_statement) SEMICOLON expression SEMICOLON assign_statement | ID (COMMA ID)? ASSIGN_VAR RANGE expression;
variables_declared_for: VARIABLE ID (type_key_variable | array_literal)? ASSIGN expression;

// Statements
list_statement: list_statement_recur ignore?;
list_statement_recur: statement | statement ignore? list_statement_recur;
statement:
	(
		declared_statement
		| assign_statement
		| if_statement
		| for_statement
		| break_statement
		| continue_statement
		| call_statement
		| return_statement
	);

list_statement_in_function: list_statement_in_function_recur ignore?;
list_statement_in_function_recur: statement_in_function | statement_in_function ignore? list_statement_in_function_recur;
statement_in_function:
    (
        declared_statement_no_ignore
        | assign_statement
		| if_statement
		| for_statement
		| break_statement
		| continue_statement
		| call_statement
		| return_statement
    );

declared_statement: variables_declared;

declared_statement_no_ignore: (constants_declared_in_function | inferred_var | keyword_type_var | struct_variable_declared) (SEMICOLON | NEWLINE) ignore?;
constants_declared_in_function: CONSTANT ID ASSIGN expression;

assign_statement: (ID dimensions? (DOT ID dimensions?)* | ID (SLP index_operators SRP)) (ASSIGN_VAR | ASSIGN_ADD | ASSIGN_SUB | ASSIGN_MUL | ASSIGN_DIV | ASSIGN_MOD) expression ignore?;

if_statement: IF (LP argument_list RP) ignore* CLP ignore* list_statement? ignore* CRP ignore* elif_statement* ignore* else_statement?;
elif_statement: ELSE IF (LP argument_list RP) ignore* CLP ignore* list_statement? ignore* CRP;
else_statement: ELSE ignore* CLP ignore* list_statement? ignore* CRP;

for_statement: FOR for_argument_list ignore* CLP ignore* list_statement? CRP ignore*;

break_statement: BREAK ignore;

continue_statement: CONTINUE ignore;

call_statement: (ID DOT | ID dimensions DOT)? function_call (SEMICOLON | NEWLINE | ignore)*;
function_call: ID LP index_operators? RP;

return_statement: RETURN ignore
    | RETURN (ID 
              | literal
              | expression (AND | OR | EQ | NEQ | LEQ | GEQ | LT | GT | ADD | SUB | MUL | DIV | MOD) expression
              | ID (DOT ID)*
              | LP expression RP DOT ID
              | LP expression RP SLP expression SRP (SLP expression SRP)?) ignore?;

ignore: SEMICOLON NEWLINE* | NEWLINE+;

//! ---------------- PARSER ----------------------- */
