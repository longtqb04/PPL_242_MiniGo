// Name: Tran Quoc Bao Long
// Student ID: 2252453

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
    
    if tk == self.UNCLOSE_STRING:       
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
INT_LIT: SUB | '0' | [1-9][0-9]* | BIN | OCT | HEX;
FLOAT_LIT: DIGIT+ OPT_FRAC OPT_EXP;
fragment DIGIT: [0-9];
fragment OPT_FRAC: '.' (DIGIT*)?;
fragment OPT_EXP: ([Ee] [+-]? DIGIT+)?;

BIN: '0'[bB][0-1]+;
OCT: '0'[oO][0-7]+;
HEX: '0'[xX][0-9a-fA-F]+;

STRING_LIT: '"' STR_CHAR* '"';
fragment STR_CHAR: ~[\n\\"] | ESC_SEQ;
fragment ESC_SEQ: '\\' [rnt"\\] | '\'"';
fragment ESC_ILLEGAL: '\\' ~[ntr'\\];

// Skips

NEWLINE: [\r]? [\n] {
    valid_types = {
        self.ID, self.INT_LIT, self.BIN, self.OCT, self.HEX, self.FLOAT_LIT, self.STRING_LIT, 
        self.TRUE, self.FALSE, self.RETURN, self.CONTINUE, self.BREAK, 
        self.CRP, self.SRP, self.RP, self.NIL
    }
    if self.preType in valid_types:
        self.type = self.SEMICOLON
        self.text = ';'
    else:
        return self.nextToken()
};
LINE_COMMENT: '//' ~[\r\n]* -> skip;
BLOCK_COMMENT : '/*' (BLOCK_COMMENT | .)*? '*/' -> skip;
WS: [ \t\r\f]+ -> skip;

// Errors
ERROR_CHAR: . {raise ErrorToken(self.text)};

UNCLOSE_STRING: '"' STR_CHAR* ('\r\n' | '\n' | EOF) {
    if(len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
        raise UncloseString(self.text[:-2])
    elif (self.text[-1] == '\n'):
        raise UncloseString(self.text[:-1])
    else:
        raise UncloseString(self.text)
};

ILLEGAL_ESCAPE: '"' STR_CHAR* ESC_ILLEGAL '"' {
    raise IllegalEscape(self.text[:-1])
};

//! ---------------- LEXER ----------------------- */

// ! ---------------- PARSER ----------------------- */

program: NEWLINE* (declared | statement) (declared | statement | NEWLINE)* EOF;
declared: variables_declared | constants_declared | function_declared | method_declared | struct_declared | interface_declared;

function_declared: function | (variables_declared ignore);

// Declarations
variables_declared: (inferred_var | keyword_type_var | struct_variable_declared) SEMICOLON ignore?; 
inferred_var: VARIABLE ID (type_key_variable | array_literal)? ASSIGN expression;
struct_variable_declared: VARIABLE ID ID (ASSIGN expression)?;

keyword_type_var: VARIABLE ID type_key_variable (ASSIGN expression | ASSIGN array_literal)?
    | VARIABLE ID array_literal (ASSIGN expression | ASSIGN array_literal)?;
keyword_type_var_infunction: (ID | ID LP list_number_lit RP) (type_key | array_literal)?;
keyword_type_var_inmethod: (ID | ID LP list_number_lit RP) (type_key | array_literal);
list_number_lit: INT_LIT | INT_LIT COMMA list_number_lit | FLOAT_LIT | FLOAT_LIT COMMA list_number_lit;
type_key: INTEGER | FLOAT | STRING | BOOLEAN | ID;
type_key_variable: INTEGER | FLOAT | STRING | BOOLEAN;

constants_declared: CONSTANT ID ASSIGN expression (SEMICOLON | NEWLINE) ignore?;

function: FUNCTION ID LP (ID (COMMA ID)* (type_key | array_literal))? (COMMA list_para_infunction)? RP (type_key | array_literal)? CLP ignore? list_statement_in_function CRP ignore;

list_para_infunction: keyword_type_var_infunction | keyword_type_var_infunction COMMA list_para_infunction;
list_para_infunction_method: keyword_type_var_inmethod | keyword_type_var_inmethod COMMA list_para_infunction_method;

struct_declared: TYPE ID STRUCT CLP ignore* struct_variable_list ignore* CRP ignore;

struct_variable_list: struct_variable_list_recur ignore?;
struct_variable_list_recur: ID (type_key | array_literal) ignore | ID (type_key | array_literal) ignore struct_variable_list_recur;

method_declared: FUNCTION LP list_para_inmethod RP ID LP (ID (COMMA ID)* (type_key | array_literal))? (COMMA list_para_infunction_method)? RP (type_key | array_literal)? CLP (list_statement | argument_list)* CRP ignore;

list_para_inmethod: ID ID | ID ID COMMA list_para_inmethod;

interface_declared: TYPE ID INTERFACE CLP ignore* list_para_interface ignore* CRP ignore;

list_para_interface: ID LP list_para_infunction? RP (type_key | array_literal)? ignore | ID LP list_para_infunction? RP (type_key | array_literal)? ignore list_para_interface;

literal:
	INT_LIT
	| FLOAT_LIT
	| STRING_LIT
	| TRUE
	| FALSE
    | NIL
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
expression6: expression6 LP index_operators_recur? RP
    | expression6 SLP expression SRP
    | expression6 DOT ID
    | expression7;
expression7: literal | ID | LP expression RP | call_statement;

// Literals
array_literal: dimensions type_literal (CLP array_elements CRP)?;
array_element_set: CLP array_elements CRP;
array_literal_declare: dimensions type_literal;
array_elements: valid_element | valid_element COMMA array_elements;
valid_element: INT_LIT | FLOAT_LIT | STRING_LIT | TRUE | FALSE | NIL | array_element_set | struct_literal;

dimensions: SLP (INT_LIT | ID) SRP (SLP (INT_LIT | ID) SRP)?;
type_literal: STRING | INTEGER | FLOAT | BOOLEAN | ID;
type_literal_except_struct: STRING | INTEGER | FLOAT | BOOLEAN;

struct_literal: ID CLP struct_literal_recur? CRP;
struct_literal_recur: ID COLON expression | ID COLON expression COMMA struct_literal_recur;

index_operators: index_operators_recur ignore?;
index_operators_recur: expression | expression COMMA index_operators_recur;

argument_list: argument_list_recur ignore?;
argument_list_recur: expression | expression ignore index_operators_recur;

for_argument_list: 
    (variables_declared_for | assign_statement) SEMICOLON expression SEMICOLON assign_statement_for 
    | ID (COMMA ID)? ASSIGN_VAR RANGE expression
    | expression;
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

assign_statement: ID dimensions? (SLP index_operators SRP)? (DOT ID dimensions? (SLP index_operators SRP)?)* (ASSIGN_VAR | ASSIGN_ADD | ASSIGN_SUB | ASSIGN_MUL | ASSIGN_DIV | ASSIGN_MOD) expression ignore?;
assign_statement_for: ID (ASSIGN_ADD | ASSIGN_SUB | ASSIGN_MUL | ASSIGN_DIV | ASSIGN_MOD) expression ignore?;

if_statement: IF (LP argument_list RP) ignore* CLP ignore* list_statement? ignore* CRP ignore* elif_statement* ignore* else_statement?;
elif_statement: ELSE IF (LP argument_list RP) ignore* CLP ignore* list_statement? ignore* CRP;
else_statement: ELSE ignore* CLP ignore* list_statement? ignore* CRP;

for_statement: FOR for_argument_list ignore* CLP ignore* list_statement? CRP ignore*;

break_statement: BREAK ignore;

continue_statement: CONTINUE ignore;

call_statement: (ID DOT | ID dimensions DOT)? function_call (SEMICOLON | NEWLINE | ignore)*;
function_call: ID LP index_operators? RP;

return_statement: RETURN ignore | RETURN expression;

ignore: SEMICOLON NEWLINE* | NEWLINE+;

//! ---------------- PARSER ----------------------- */
