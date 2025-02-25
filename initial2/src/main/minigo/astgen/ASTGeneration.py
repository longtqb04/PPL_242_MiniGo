from MiniGoVisitor import MiniGoVisitor
from MiniGoParser import MiniGoParser
from AST import *

class ASTGeneration(MiniGoVisitor):
    # program: NEWLINE* argument_list EOF;
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return Program(self.visit(ctx.argument_list()))


    # declared: variables_declared | constants_declared | function_declared | method_declared | struct_declared | interface_declared;
    def visitDeclared(self, ctx:MiniGoParser.DeclaredContext):
        return self.visit(ctx.getChild(0))


    # function_declared: function | (variables_declared ignore);
    def visitFunction_declared(self, ctx:MiniGoParser.Function_declaredContext):
        return self.visit(ctx.getChild(0))


    # variables_declared: (inferred_var | keyword_type_var | struct_variable_declared) SEMICOLON ignore?;
    def visitVariables_declared(self, ctx:MiniGoParser.Variables_declaredContext):
        return self.visit(ctx.getChild(0))


    # inferred_var: VARIABLE ID (type_key_variable | array_literal)? ASSIGN expression;
    def visitInferred_var(self, ctx:MiniGoParser.Inferred_varContext):
        if ctx.array_literal():
            return VarDecl(ctx.ID().getText(), ArrayType(), self.visit(ctx.expression()))
        elif ctx.type_key_variable():
            return VarDecl(ctx.ID().getText(), self.visit(ctx.type_key_variable()), self.visit(ctx.expression()))
        return VarDecl(ctx.ID().getText(), None, self.visit(ctx.expression()))


    # struct_variable_declared: VARIABLE ID ID (ASSIGN expression)?;
    def visitStruct_variable_declared(self, ctx:MiniGoParser.Struct_variable_declaredContext):
        return VarDecl(ctx.ID(0).getText(), StructType(ctx.ID(1).getText(), None, None), self.visit(ctx.expression()))


    # keyword_type_var: VARIABLE ID type_key_variable (ASSIGN expression | ASSIGN array_literal)? | VARIABLE ID array_literal (ASSIGN expression | ASSIGN array_literal)?;
    def visitKeyword_type_var(self, ctx:MiniGoParser.Keyword_type_varContext):
        if ctx.type_key_variable():
            return VarDecl(ctx.ID().getText(), self.visit(ctx.type_key_variable()), self.visit(ctx.expression()))
        return VarDecl(ctx.ID().getText(), self.visit(ctx.array_literal()), self.visit(ctx.expression()))


    # keyword_type_var_infunction: (ID | ID LP list_number_lit RP) (type_key | array_literal)?;
    def visitKeyword_type_var_infunction(self, ctx:MiniGoParser.Keyword_type_var_infunctionContext):
        return self.visitChildren(ctx)


    # keyword_type_var_inmethod: (ID | ID LP list_number_lit RP) (type_key | array_literal);
    def visitKeyword_type_var_inmethod(self, ctx:MiniGoParser.Keyword_type_var_inmethodContext):
        return self.visitChildren(ctx)


    # list_number_lit: INT_LIT | INT_LIT COMMA list_number_lit | FLOAT_LIT | FLOAT_LIT COMMA list_number_lit;
    def visitList_number_lit(self, ctx:MiniGoParser.List_number_litContext):
        if ctx.getChildCount() == 1:
            return [ctx.getChild(0)]
        return [ctx.getChild(0)] + self.visit(ctx.list_number_lit())


    # type_key: INTEGER | FLOAT | STRING | BOOLEAN | ID;
    def visitType_key(self, ctx:MiniGoParser.Type_keyContext):
        if ctx.INTEGER():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STRING():
            return StringType()
        elif ctx.BOOLEAN():
            return BoolType()
        else:
            return StructType()


    # type_key_variable: INTEGER | FLOAT | STRING | BOOLEAN;
    def visitType_key_variable(self, ctx:MiniGoParser.Type_key_variableContext):
        if ctx.INTEGER():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STRING():
            return StringType()
        else:
            return BoolType()


    # constants_declared: CONSTANT ID ASSIGN expression (SEMICOLON | NEWLINE) ignore?;
    def visitConstants_declared(self, ctx:MiniGoParser.Constants_declaredContext):
        return ConstDecl(ctx.ID().getText(), None, self.visit(ctx.expression()))


    # function: FUNCTION ID LP (ID (COMMA ID)* (type_key | array_literal))? (COMMA list_para_infunction)?
    # RP (type_key | array_literal)? CLP ignore? list_statement_in_function CRP ignore;
    def visitFunction(self, ctx:MiniGoParser.FunctionContext):
        return [FuncDecl(ctx.ID().getText(), [], VoidType())] #incomplete


    # list_para_infunction: keyword_type_var_infunction | keyword_type_var_infunction COMMA list_para_infunction;
    def visitList_para_infunction(self, ctx:MiniGoParser.List_para_infunctionContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.keyword_type_var_infunction())]
        return [self.visit(ctx.keyword_type_var_infunction())] + self.visit(ctx.list_para_infunction())

    # list_para_infunction_method: keyword_type_var_inmethod | keyword_type_var_inmethod COMMA list_para_infunction_method;
    def visitList_para_infunction_method(self, ctx:MiniGoParser.List_para_infunction_methodContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.keyword_type_var_inmethod())]
        return [self.visit(ctx.keyword_type_var_inmethod())] + self.visit(ctx.list_para_infunction_method())


    # struct_declared: TYPE ID STRUCT CLP ignore* struct_variable_list ignore* CRP ignore;
    def visitStruct_declared(self, ctx:MiniGoParser.Struct_declaredContext):
        return self.visitChildren(ctx)


    # struct_variable_list: struct_variable_list_recur ignore?;
    def visitStruct_variable_list(self, ctx:MiniGoParser.Struct_variable_listContext):
        return self.visit(ctx.struct_variable_list_recur())


    # struct_variable_list_recur: ID (type_key | array_literal) ignore | ID (type_key | array_literal) ignore struct_variable_list_recur;
    def visitStruct_variable_list_recur(self, ctx:MiniGoParser.Struct_variable_list_recurContext):
        return self.visitChildren(ctx)


    # method_declared: FUNCTION LP list_para_inmethod RP ID LP (ID (COMMA ID)* (type_key | array_literal))?
    # (COMMA list_para_infunction_method)? RP (type_key | array_literal)? CLP (list_statement | argument_list)* CRP ignore;
    def visitMethod_declared(self, ctx:MiniGoParser.Method_declaredContext):
        return self.visitChildren(ctx)


    # list_para_inmethod: ID ID | ID ID COMMA list_para_inmethod;
    def visitList_para_inmethod(self, ctx:MiniGoParser.List_para_inmethodContext):
        return self.visitChildren(ctx)


    # interface_declared: TYPE ID INTERFACE CLP ignore* list_para_interface ignore* CRP ignore;
    def visitInterface_declared(self, ctx:MiniGoParser.Interface_declaredContext):
        return self.visitChildren(ctx)


    # list_para_interface: ID LP list_para_infunction? RP (type_key | array_literal)? ignore
    # | ID LP list_para_infunction? RP (type_key | array_literal)? ignore list_para_interface;
    def visitList_para_interface(self, ctx:MiniGoParser.List_para_interfaceContext):
        return self.visitChildren(ctx)


    # literal: INT_LIT | FLOAT_LIT | STRING_LIT | TRUE | FALSE | NIL | array_literal | struct_literal;
    def visitLiteral(self, ctx:MiniGoParser.LiteralContext):
        if ctx.INT_LIT():
            return IntLiteral(int(ctx.INT_LIT().getText()))
        elif ctx.FLOAT_LIT():
            return FloatLiteral(float(ctx.FLOAT_LIT().getText()))
        elif ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText()[1:-1])
        elif ctx.TRUE():
            return BooleanLiteral(True)
        elif ctx.FALSE():
            return BooleanLiteral(False)
        elif ctx.NIL():
            return NilLiteral()
        elif ctx.array_literal():
            return self.visit(ctx.array_literal())
        return self.visit(ctx.struct_literal())


    # expression: expression OR expression1 | expression1;
    def visitExpression(self, ctx:MiniGoParser.ExpressionContext):
        return self.visitChildren(ctx)


    # expression1: expression1 AND expression2 | expression2;
    def visitExpression1(self, ctx:MiniGoParser.Expression1Context):
        return self.visitChildren(ctx)


    # expression2: expression2 (EQ | NEQ | LT | GT | LEQ | GEQ) expression3 | expression3;
    def visitExpression2(self, ctx:MiniGoParser.Expression2Context):
        return self.visitChildren(ctx)


    # expression3: expression3 (ADD | SUB) expression4 | expression4;
    def visitExpression3(self, ctx:MiniGoParser.Expression3Context):
        return self.visitChildren(ctx)


    # expression4: expression4 (MUL | DIV | MOD) expression5 | expression5;
    def visitExpression4(self, ctx:MiniGoParser.Expression4Context):
        return self.visitChildren(ctx)


    # expression5: (NOT | SUB) expression5 | expression6;
    def visitExpression5(self, ctx:MiniGoParser.Expression5Context):
        return self.visitChildren(ctx)


    # expression6: expression6 LP index_operators_recur? RP | expression6 SLP expression SRP | expression6 DOT ID | expression7;
    def visitExpression6(self, ctx:MiniGoParser.Expression6Context):
        return self.visitChildren(ctx)


    # expression7: literal | ID | LP expression RP | call_statement;
    def visitExpression7(self, ctx:MiniGoParser.Expression7Context):
        return self.visitChildren(ctx)


    # array_literal: dimensions type_literal (CLP array_elements CRP)?;
    def visitArray_literal(self, ctx:MiniGoParser.Array_literalContext):
        return self.visitChildren(ctx)


    # array_element_set: CLP array_elements CRP;
    def visitArray_element_set(self, ctx:MiniGoParser.Array_element_setContext):
        return self.visitChildren(ctx)


    # array_literal_declare: dimensions type_literal;
    def visitArray_literal_declare(self, ctx:MiniGoParser.Array_literal_declareContext):
        return ArrayLiteral(self.visit(ctx.dimensions()), self.visit(ctx.type_literal()), None)


    # array_elements: valid_element | valid_element COMMA array_elements;
    def visitArray_elements(self, ctx:MiniGoParser.Array_elementsContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.valid_element())]
        return [self.visit(ctx.valid_element())] + self.visit(ctx.array_elements())


    # valid_element: INT_LIT | FLOAT_LIT | STRING_LIT | TRUE | FALSE | NIL | array_element_set | struct_literal;
    def visitValid_element(self, ctx:MiniGoParser.Valid_elementContext):
        if ctx.INT_LIT():
            return IntLiteral(int(ctx.INT_LIT().getText()))
        elif ctx.FLOAT_LIT():
            return FloatLiteral(float(ctx.FLOAT_LIT().getText()))
        elif ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText()[1:-1])
        elif ctx.TRUE():
            return BooleanLiteral(True)
        elif ctx.FALSE():
            return BooleanLiteral(False)
        elif ctx.NIL():
            return NilLiteral()
        elif ctx.array_element_set():
            return self.visit(ctx.array_element_set())
        return self.visit(ctx.struct_literal())



    # dimensions: SLP (INT_LIT | ID) SRP (SLP (INT_LIT | ID) SRP)?;
    def visitDimensions(self, ctx:MiniGoParser.DimensionsContext):
        if ctx.getChildCount() == 3:
            return [IntLiteral(int(ctx.INT_LIT().getText()))] if ctx.INT_LIT() else [Id(ctx.ID().getText())]
        return [IntLiteral(int(ctx.INT_LIT(0).getText())) if ctx.getChild(1) == ctx.INT_LIT() else Id(ctx.ID(0).getText()), IntLiteral(int(ctx.INT_LIT(1).getText())) if ctx.getChild(4) == ctx.INT_LIT() else Id(ctx.ID(1).getText())]


    # type_literal: STRING | INTEGER | FLOAT | BOOLEAN | ID;
    def visitType_literal(self, ctx:MiniGoParser.Type_literalContext):
        if ctx.INTEGER():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STRING():
            return StringType()
        elif ctx.BOOLEAN():
            return BoolType()
        else:
            return StructType()


    # type_literal_except_struct: STRING | INTEGER | FLOAT | BOOLEAN;
    def visitType_literal_except_struct(self, ctx:MiniGoParser.Type_literal_except_structContext):
        if ctx.INTEGER():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STRING():
            return StringType()
        return BoolType()


    # struct_literal: ID CLP struct_literal_recur? CRP;
    def visitStruct_literal(self, ctx:MiniGoParser.Struct_literalContext):
        ele = self.visit(ctx.struct_literal_recur()) if ctx.struct_literal_recur() else []
        return StructLiteral(ctx.ID().getText(), ele)


    # struct_literal_recur: ID COLON expression | ID COLON expression COMMA struct_literal_recur;
    def visitStruct_literal_recur(self, ctx:MiniGoParser.Struct_literal_recurContext):
        return self.visitChildren(ctx)


    # index_operators: index_operators_recur ignore?;
    def visitIndex_operators(self, ctx:MiniGoParser.Index_operatorsContext):
        return self.visit(ctx.index_operators_recur())


    # index_operators_recur: expression | expression COMMA index_operators_recur;
    def visitIndex_operators_recur(self, ctx:MiniGoParser.Index_operators_recurContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expression())]
        return [self.visit(ctx.expression())] + self.visit(ctx.index_operators_recur())


    # argument_list: argument_list_recur ignore?;
    def visitArgument_list(self, ctx:MiniGoParser.Argument_listContext):
        return self.visit(ctx.argument_list_recur())


    # argument_list_recur: expression | expression ignore argument_list_recur;
    def visitArgument_list_recur(self, ctx:MiniGoParser.Argument_list_recurContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expression())]
        return [self.visit(ctx.expression())] + self.visit(ctx.argument_list_recur())


    # for_argument_list: (variables_declared_for | assign_statement) SEMICOLON expression SEMICOLON assign_statement_for | ID (COMMA ID)? ASSIGN_VAR RANGE expression | expression;
    def visitFor_argument_list(self, ctx:MiniGoParser.For_argument_listContext):
        return self.visitChildren(ctx)


    # variables_declared_for: VARIABLE ID (type_key_variable | array_literal)? ASSIGN expression;
    def visitVariables_declared_for(self, ctx:MiniGoParser.Variables_declared_forContext):
        return self.visitChildren(ctx)


    # list_statement: list_statement_recur ignore?;
    def visitList_statement(self, ctx:MiniGoParser.List_statementContext):
        return self.visit(ctx.list_statement_recur())


    # list_statement_recur: statement | statement ignore? list_statement_recur;
    def visitList_statement_recur(self, ctx:MiniGoParser.List_statement_recurContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.statement())]
        return [self.visit(ctx.statement())] + self.visit(ctx.list_statement_recur())


    # statement: (declared_statement | assign_statement | if_statement | for_statement | break_statement | continue_statement | call_statement | return_statement);
    def visitStatement(self, ctx:MiniGoParser.StatementContext):
        return self.visit(ctx.getChild(0))


    # list_statement_in_function: list_statement_in_function_recur ignore?;
    def visitList_statement_in_function(self, ctx:MiniGoParser.List_statement_in_functionContext):
        return self.visit(ctx.list_statement_in_function_recur())


    # list_statement_in_function_recur: statement_in_function | statement_in_function ignore? list_statement_in_function_recur;
    def visitList_statement_in_function_recur(self, ctx:MiniGoParser.List_statement_in_function_recurContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.statement_in_function())]
        return [self.visit(ctx.statement_in_function())] + self.visit(ctx.list_statement_in_function_recur())


    # statement_in_function: (declared_statement_in_function | assign_statement | if_statement | for_statement | break_statement | continue_statement | call_statement | return_statement);
    def visitStatement_in_function(self, ctx:MiniGoParser.Statement_in_functionContext):
        return self.visit(ctx.getChild(0))


    # declared_statement: variables_declared;
    def visitDeclared_statement(self, ctx:MiniGoParser.Declared_statementContext):
        return self.visit(ctx.variables_declared())


    # declared_statement_no_ignore: (constants_declared_in_function | inferred_var | keyword_type_var | struct_variable_declared) (SEMICOLON | NEWLINE) ignore?;
    def visitDeclared_statement_no_ignore(self, ctx:MiniGoParser.Declared_statement_no_ignoreContext):
        return self.visit(ctx.getChild[0])


    # constants_declared_in_function: CONSTANT ID ASSIGN expression;
    def visitConstants_declared_in_function(self, ctx:MiniGoParser.Constants_declared_in_functionContext):
        return ConstDecl(ctx.ID().getText(), None, self.visit(ctx.expression()))


    # assign_statement: ID dimensions? (SLP index_operators SRP)? (DOT ID dimensions? (SLP index_operators SRP)?)* (ASSIGN_VAR | ASSIGN_ADD | ASSIGN_SUB | ASSIGN_MUL | ASSIGN_DIV | ASSIGN_MOD) expression ignore?;
    def visitAssign_statement(self, ctx:MiniGoParser.Assign_statementContext):
        return self.visitChildren(ctx)


    # assign_statement_for: ID (ASSIGN_ADD | ASSIGN_SUB | ASSIGN_MUL | ASSIGN_DIV | ASSIGN_MOD) expression ignore?;
    def visitAssign_statement_for(self, ctx:MiniGoParser.Assign_statement_forContext):
        if ctx.ASSIGN_ADD():
            return Assign(ctx.ID().getText(), BinaryOp(ctx.ASSIGN_ADD().getText(), ctx.ID().getText(), self.visit(ctx.expression())))
        elif ctx.ASSIGN_SUB():
            return Assign(ctx.ID().getText(), BinaryOp(ctx.ASSIGN_SUB().getText(), ctx.ID().getText(), self.visit(ctx.expression())))
        elif ctx.ASSIGN_MUL():
            return Assign(ctx.ID().getText(), BinaryOp(ctx.ASSIGN_MUL().getText(), ctx.ID().getText(), self.visit(ctx.expression())))
        elif ctx.ASSIGN_DIV():
            return Assign(ctx.ID().getText(), BinaryOp(ctx.ASSIGN_DIV().getText(), ctx.ID().getText(), self.visit(ctx.expression())))
        return Assign(ctx.ID().getText(), BinaryOp(ctx.ASSIGN_MOD().getText(), ctx.ID().getText(), self.visit(ctx.expression())))
        


    # if_statement: IF (LP argument_list RP) ignore* CLP ignore* list_statement? ignore* CRP ignore* elif_statement* ignore* else_statement?;
    def visitIf_statement(self, ctx:MiniGoParser.If_statementContext):
        return self.visitChildren(ctx)


    # elif_statement: ELSE IF (LP argument_list RP) ignore* CLP ignore* list_statement? ignore* CRP;
    def visitElif_statement(self, ctx:MiniGoParser.Elif_statementContext):
        return self.visitChildren(ctx)


    # else_statement: ELSE ignore* CLP ignore* list_statement? ignore* CRP;
    def visitElse_statement(self, ctx:MiniGoParser.Else_statementContext):
        return self.visitChildren(ctx)


    # for_statement: FOR for_argument_list ignore* CLP ignore* list_statement? CRP ignore*;
    def visitFor_statement(self, ctx:MiniGoParser.For_statementContext):
        return self.visitChildren(ctx)


    # break_statement: BREAK ignore;
    def visitBreak_statement(self, ctx:MiniGoParser.Break_statementContext):
        return Break()


    # continue_statement: CONTINUE ignore;
    def visitContinue_statement(self, ctx:MiniGoParser.Continue_statementContext):
        return Continue()


    # call_statement: (ID DOT | ID dimensions DOT)? function_call (SEMICOLON | NEWLINE | ignore)*;
    def visitCall_statement(self, ctx:MiniGoParser.Call_statementContext):
        return self.visitChildren(ctx)


    # function_call: ID LP index_operators? RP;
    def visitFunction_call(self, ctx:MiniGoParser.Function_callContext):
        return FuncCall(ctx.ID().getText(), self.visit(ctx.index_operators()) if ctx.index_operators() else None)


    # return_statement: RETURN ignore | RETURN expression;
    def visitReturn_statement(self, ctx:MiniGoParser.Return_statementContext):
        if ctx.expression():
            return Return(self.visit(ctx.expression()))
        return Return(None)


    # ignore: SEMICOLON NEWLINE* | NEWLINE+;
    def visitIgnore(self, ctx:MiniGoParser.IgnoreContext):
        return self.visitChildren(ctx)
