from MiniGoVisitor import MiniGoVisitor
from MiniGoParser import MiniGoParser
from AST import *
from typing import Tuple

class ASTGeneration(MiniGoVisitor):
    # program: NEWLINE* declared+ NEWLINE* EOF;
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return Program([self.visit(i) for i in ctx.declared()])


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
            return VarDecl(ctx.ID().getText(), self.visit(ctx.array_literal()), self.visit(ctx.expression()))
        elif ctx.type_key_variable():
            return VarDecl(ctx.ID().getText(), self.visit(ctx.type_key_variable()), self.visit(ctx.expression()))
        return VarDecl(ctx.ID().getText(), None, self.visit(ctx.expression()))


    # struct_variable_declared: VARIABLE ID ID (ASSIGN expression)?;
    def visitStruct_variable_declared(self, ctx:MiniGoParser.Struct_variable_declaredContext):
        return VarDecl(ctx.ID(0).getText(), Id(ctx.ID(1).getText()), self.visit(ctx.expression()))


    # keyword_type_var: VARIABLE ID (type_key_variable | array_literal) (ASSIGN expression)?;
    def visitKeyword_type_var(self, ctx:MiniGoParser.Keyword_type_varContext):
        if ctx.type_key_variable():
            return VarDecl(ctx.ID().getText(), self.visit(ctx.type_key_variable()), self.visit(ctx.expression()) if ctx.ASSIGN() else None)
        return VarDecl(ctx.ID().getText(), self.visit(ctx.array_literal()), self.visit(ctx.expression()) if ctx.ASSIGN() else None)


    # list_number_lit: INT_LIT | INT_LIT COMMA list_number_lit | FLOAT_LIT | FLOAT_LIT COMMA list_number_lit;
    def visitList_number_lit(self, ctx:MiniGoParser.List_number_litContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.getChild(0))]
        return [self.visit(ctx.getChild(0))] + self.visit(ctx.list_number_lit())


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
            return Id(ctx.ID().getText())


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


    # function: FUNCTION ID LP list_parameters? parameter_type? CLP ignore? list_statement_in_function CRP ignore;
    def visitFunction(self, ctx:MiniGoParser.FunctionContext):
        return FuncDecl(ctx.ID().getText(), self.visit(ctx.list_parameters()) if ctx.list_parameters() else [], self.visit(ctx.parameter_type()) if ctx.parameter_type() else VoidType(), Block(self.visit(ctx.list_statement_in_function())) if ctx.list_statement_in_function() else Block([]))


    # struct_declared: TYPE ID STRUCT CLP ignore* struct_variable_list ignore* CRP ignore;
    def visitStruct_declared(self, ctx:MiniGoParser.Struct_declaredContext):
        return StructType(ctx.ID().getText(), self.visit(ctx.struct_variable_list()), [])


    # struct_variable_list: struct_variable_list_recur ignore?;
    def visitStruct_variable_list(self, ctx:MiniGoParser.Struct_variable_listContext):
        return self.visit(ctx.struct_variable_list_recur())


    # struct_variable_list_recur: ID (type_key | array_literal) ignore | ID (type_key | array_literal) ignore struct_variable_list_recur;
    def visitStruct_variable_list_recur(self, ctx:MiniGoParser.Struct_variable_list_recurContext):
        if ctx.struct_variable_list_recur():
            return [(ctx.ID().getText(),self.visit(ctx.getChild(1)))] + self.visit(ctx.struct_variable_list_recur())
        return [(ctx.ID().getText(),self.visit(ctx.getChild(1)))]


    # method_declared: FUNCTION LP ID ID RP ID LP list_parameters? RP parameter_type? CLP list_statement? CRP ignore;
    def visitMethod_declared(self, ctx:MiniGoParser.Method_declaredContext):
        return MethodDecl(ctx.ID()[0].getText(),Id(ctx.ID()[1].getText()),FuncDecl(ctx.ID()[2].getText(), self.visit(ctx.list_parameters()) if ctx.list_parameters() else [], self.visit(ctx.parameter_type()) if ctx.parameter_type() else VoidType(), Block(self.visit(ctx.list_statement())) if self.visit(ctx.list_statement()) else Block([])))   


    # list_parameters: parameter | parameter list_parameters;
    def visitList_parameters(self, ctx:MiniGoParser.List_parametersContext):
        if ctx.list_parameters():
            return self.visit(ctx.parameter()) + self.visit(ctx.list_parameters())
        return self.visit(ctx.parameter())


    # parameter: list_ID parameter_type;
    def visitParameter(self, ctx:MiniGoParser.ParameterContext):
        list_ID = self.visit(ctx.list_ID())
        paramType = self.visit(ctx.parameter_type())
        return [ParamDecl(name, paramType) for name in list_ID]
    
    # parameter_type: type_key | array_literal;
    def visitParameter_type(self, ctx:MiniGoParser.Parameter_typeContext):
        return self.visit(ctx.getChild(0))


    # list_ID: ID | ID COMMA list_ID;
    def visitList_ID(self, ctx:MiniGoParser.List_IDContext):
        if ctx.list_ID():
            return [ctx.ID().getText()] + self.visit(ctx.list_ID())
        return [ctx.ID().getText()]


    # interface_declared: TYPE ID INTERFACE CLP ignore* list_para_interface ignore* CRP ignore;
    def visitInterface_declared(self, ctx:MiniGoParser.Interface_declaredContext):
        return InterfaceType(ctx.ID().getText(), self.visit(ctx.list_para_interface()))


    # list_para_interface: ID LP list_parameters? RP parameter_type? ignore
    # | ID LP list_parameters? RP parameter_type? ignore list_para_interface;
    def visitList_para_interface(self, ctx:MiniGoParser.List_para_interfaceContext):
        if ctx.list_para_interface():
            return [Prototype(ctx.ID().getText(), [i.parType for i in self.visit(ctx.list_parameters())] if ctx.list_parameters() else [], self.visit(ctx.parameter_type()) if ctx.parameter_type() else VoidType())] + self.visit(ctx.list_para_interface())

        return [Prototype(ctx.ID().getText(), [i.parType for i in self.visit(ctx.list_parameters())] if ctx.list_parameters() else [],self.visit(ctx.parameter_type()) if ctx.parameter_type() else VoidType())]


    # literal: INT_LIT | FLOAT_LIT | STRING_LIT | TRUE | FALSE | NIL | array_literal | struct_literal;
    def visitLiteral(self, ctx:MiniGoParser.LiteralContext):
        if ctx.INT_LIT():
            res = 0
            if ctx.INT_LIT().getText().find("0b") != -1 or ctx.INT_LIT().getText().find("0B") != -1:
                res = int(ctx.INT_LIT().getText(), 2)
            elif ctx.INT_LIT().getText().find("0o") != -1 or ctx.INT_LIT().getText().find("0O") != -1:
                res = int(ctx.INT_LIT().getText(), 8)
            elif ctx.INT_LIT().getText().find("0x") != -1 or ctx.INT_LIT().getText().find("0X") != -1:
                res = int(ctx.INT_LIT().getText(), 16)
            else:
                res = int(ctx.INT_LIT().getText())
            return IntLiteral(res)
        elif ctx.FLOAT_LIT():
            return FloatLiteral(float(ctx.FLOAT_LIT().getText()))
        elif ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText())
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
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression1())
        op = ctx.OR().getText()
        left = self.visit(ctx.expression())
        right = self.visit(ctx.expression1())
        return BinaryOp(op, left, right)


    # expression1: expression1 AND expression2 | expression2;
    def visitExpression1(self, ctx:MiniGoParser.Expression1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression2())
        op = ctx.AND().getText()
        left = self.visit(ctx.expression1())
        right = self.visit(ctx.expression2())
        return BinaryOp(op, left, right)


    # expression2: expression2 (EQ | NEQ | LT | GT | LEQ | GEQ) expression3 | expression3;
    def visitExpression2(self, ctx:MiniGoParser.Expression2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression3())
        op = ''
        if ctx.EQ():
            op = ctx.EQ().getText()
        elif ctx.NEQ():
            op = ctx.NEQ().getText()
        elif ctx.LT():
            op = ctx.LT().getText()
        elif ctx.GT():
            op = ctx.GT().getText()
        elif ctx.LEQ():
            op = ctx.LEQ().getText()
        elif ctx.GEQ():
            op = ctx.GEQ().getText()
        left = self.visit(ctx.expression2())
        right = self.visit(ctx.expression3())
        return BinaryOp(op, left, right)


    # expression3: expression3 (ADD | SUB) expression4 | expression4;
    def visitExpression3(self, ctx:MiniGoParser.Expression3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression4())
        op = ''
        if ctx.ADD():
            op = ctx.ADD().getText()
        elif ctx.SUB():
            op = ctx.SUB().getText()
        left = self.visit(ctx.expression3())
        right = self.visit(ctx.expression4())
        return BinaryOp(op, left, right)


    # expression4: expression4 (MUL | DIV | MOD) expression5 | expression5;
    def visitExpression4(self, ctx:MiniGoParser.Expression4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression5())
        op = ''
        if ctx.MUL():
            op = ctx.MUL().getText()
        elif ctx.DIV():
            op = ctx.DIV().getText()
        elif ctx.MOD():
            op = ctx.MOD().getText()
        left = self.visit(ctx.expression4())
        right = self.visit(ctx.expression5())
        return BinaryOp(op, left, right)


    # expression5: (NOT | SUB) expression5 | expression6;
    def visitExpression5(self, ctx:MiniGoParser.Expression5Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression6())
        op = ''
        if ctx.NOT():
            op = ctx.NOT().getText()
        elif ctx.SUB():
            op = ctx.SUB().getText()
        expr = self.visit(ctx.expression5())
        return UnaryOp(op, expr)


    # expression6: expression6 DOT ID LP index_operators_recur? RP | expression6 SLP expression SRP | expression6 DOT ID | expression7;
    def visitExpression6(self, ctx:MiniGoParser.Expression6Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression7())
        elif ctx.LP() and ctx.RP():
            return MethCall(self.visit(ctx.expression6()), ctx.ID().getText(), self.visit(ctx.index_operators_recur()) if ctx.index_operators_recur() else [])
        elif ctx.SLP() and ctx.SRP():
            if type(self.visit(ctx.expression6())) == ArrayCell:
                return ArrayCell(self.visit(ctx.expression6()).arr, self.visit(ctx.expression6()).idx  + [self.visit(ctx.expression())])
            return ArrayCell(self.visit(ctx.expression6()),[self.visit(ctx.expression())])
        return FieldAccess(self.visit(ctx.expression6()), ctx.ID().getText())


    # expression7: literal | ID | LP expression RP | function_call;
    def visitExpression7(self, ctx:MiniGoParser.Expression7Context):
        if ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.LP() and ctx.RP():
            return self.visit(ctx.expression())
        return self.visit(ctx.function_call())

    # array_literal: dimensions type_literal (CLP array_elements CRP)?;
    def visitArray_literal(self, ctx:MiniGoParser.Array_literalContext):
        if not ctx.array_elements():
            return ArrayType(self.visit(ctx.dimensions()), self.visit(ctx.type_literal()))
        return ArrayLiteral(self.visit(ctx.dimensions()), self.visit(ctx.type_literal()), self.visit(ctx.array_elements()) if ctx.array_elements() else [])

    # array_element_set: CLP array_elements CRP;
    def visitArray_element_set(self, ctx:MiniGoParser.Array_element_setContext):
        return self.visit(ctx.array_elements())


    # array_literal_declare: dimensions type_literal;
    def visitArray_literal_declare(self, ctx:MiniGoParser.Array_literal_declareContext):
        return ArrayType(self.visit(ctx.dimensions()), self.visit(ctx.type_literal()))


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
            return StringLiteral(ctx.STRING_LIT().getText())
        elif ctx.TRUE():
            return BooleanLiteral(True)
        elif ctx.FALSE():
            return BooleanLiteral(False)
        elif ctx.NIL():
            return NilLiteral()
        elif ctx.array_element_set():
            return self.visit(ctx.array_element_set())
        return self.visit(ctx.struct_literal())


    # dimensions: SLP cell_type SRP (SLP cell_type SRP)*;
    def visitDimensions(self, ctx:MiniGoParser.DimensionsContext):
        if ctx.getChildCount() == 3:
            return [self.visit(ctx.cell_type()[0])]
        return [self.visit(i) for i in ctx.cell_type()]


    # cell_type: INT_LIT | ID;
    def visitCell_type(self, ctx:MiniGoParser.Cell_typeContext):
        if ctx.INT_LIT():
            return IntLiteral(int(ctx.INT_LIT().getText()))
        return Id(ctx.ID().getText())


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
            return Id(ctx.ID().getText())


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
        if ctx.struct_literal_recur():
            return [(ctx.ID().getText(), self.visit(ctx.expression()))] + self.visit(ctx.struct_literal_recur())
        return [(ctx.ID().getText(), self.visit(ctx.expression()))]


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


    # for_step: FOR (variables_declared_for | assign_statement_for) SEMICOLON expression SEMICOLON assign_statement_for ignore* CLP ignore* list_statement CRP ignore*;
    def visitFor_step(self, ctx:MiniGoParser.For_stepContext):
        if ctx.variables_declared_for():
            return ForStep(self.visit(ctx.variables_declared_for()), self.visit(ctx.expression()), self.visit(ctx.assign_statement_for()[0]), Block(self.visit(ctx.list_statement())))
        return ForStep(self.visit(ctx.assign_statement_for()[0]), self.visit(ctx.expression()), self.visit(ctx.assign_statement_for()[1]), Block(self.visit(ctx.list_statement())))


    # for_each: FOR ID (COMMA ID)? ASSIGN_VAR RANGE expression ignore* CLP ignore* list_statement CRP ignore*;
    def visitFor_each(self, ctx:MiniGoParser.For_eachContext):
        if ctx.COMMA():
            return ForEach(Id(ctx.ID()[0].getText()), Id(ctx.ID()[1].getText()), self.visit(ctx.expression()), Block(self.visit(ctx.list_statement())))
        return ForEach(Id(ctx.ID()[0].getText()), None, self.visit(ctx.expression()), Block(self.visit(ctx.list_statement())))


    # for_basic: FOR expression ignore* CLP ignore* list_statement CRP ignore*;
    def visitFor_basic(self, ctx:MiniGoParser.For_basicContext):
        return ForBasic(self.visit(ctx.expression()), Block(self.visit(ctx.list_statement())))


    # variables_declared_for: VARIABLE ID (type_key_variable | array_literal)? ASSIGN expression;
    def visitVariables_declared_for(self, ctx:MiniGoParser.Variables_declared_forContext):
        if ctx.type_key_variable():
            return VarDecl(ctx.ID().getText(), self.visit(ctx.type_key_variable()), self.visit(ctx.expression()))
        elif ctx.array_literal():
            return VarDecl(ctx.ID().getText(), self.visit(ctx.array_literal()), self.visit(ctx.expression()))
        return VarDecl(ctx.ID().getText(), None, self.visit(ctx.expression()))


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
        return self.visit(ctx.getChild(0))


    # constants_declared_in_function: CONSTANT ID ASSIGN expression;
    def visitConstants_declared_in_function(self, ctx:MiniGoParser.Constants_declared_in_functionContext):
        return ConstDecl(ctx.ID().getText(), None, self.visit(ctx.expression()))


    # assign_statement: lhs (ASSIGN_VAR | ASSIGN_ADD | ASSIGN_SUB | ASSIGN_MUL | ASSIGN_DIV | ASSIGN_MOD) expression ignore?;
    def visitAssign_statement(self, ctx:MiniGoParser.Assign_statementContext):
        if ctx.ASSIGN_ADD():
            return Assign(self.visit(ctx.lhs()), BinaryOp("+", self.visit(ctx.lhs()), self.visit(ctx.expression())))
        elif ctx.ASSIGN_SUB():
            return Assign(self.visit(ctx.lhs()), BinaryOp("-", self.visit(ctx.lhs()), self.visit(ctx.expression())))
        elif ctx.ASSIGN_MUL():
            return Assign(self.visit(ctx.lhs()), BinaryOp("*", self.visit(ctx.lhs()), self.visit(ctx.expression())))
        elif ctx.ASSIGN_DIV():
            return Assign(self.visit(ctx.lhs()), BinaryOp("/", self.visit(ctx.lhs()), self.visit(ctx.expression())))
        elif ctx.ASSIGN_MOD():
            return Assign(self.visit(ctx.lhs()), BinaryOp("%", self.visit(ctx.lhs()), self.visit(ctx.expression())))
        return Assign(self.visit(ctx.lhs()), self.visit(ctx.expression()))


    # assign_statement_for: ID (ASSIGN_VAR | ASSIGN_ADD | ASSIGN_SUB | ASSIGN_MUL | ASSIGN_DIV | ASSIGN_MOD) expression ignore?;
    def visitAssign_statement_for(self, ctx:MiniGoParser.Assign_statement_forContext):
        if ctx.ASSIGN_ADD():
            return Assign(Id(ctx.ID().getText()), BinaryOp("+", Id(ctx.ID().getText()), self.visit(ctx.expression())))
        elif ctx.ASSIGN_SUB():
            return Assign(Id(ctx.ID().getText()), BinaryOp("-", Id(ctx.ID().getText()), self.visit(ctx.expression())))
        elif ctx.ASSIGN_MUL():
            return Assign(Id(ctx.ID().getText()), BinaryOp("*", Id(ctx.ID().getText()), self.visit(ctx.expression())))
        elif ctx.ASSIGN_DIV():
            return Assign(Id(ctx.ID().getText()), BinaryOp("/", Id(ctx.ID().getText()), self.visit(ctx.expression())))
        elif ctx.ASSIGN_MOD():
            return Assign(Id(ctx.ID().getText()), BinaryOp("%", Id(ctx.ID().getText()), self.visit(ctx.expression())))
        return Assign(Id(ctx.ID().getText()), self.visit(ctx.expression()))
    

    # lhs: ID | lhs DOT ID | lhs SLP expression SRP;
    def visitLhs(self, ctx:MiniGoParser.LhsContext):
        if ctx.DOT():
            return FieldAccess(self.visit(ctx.lhs()), ctx.ID().getText())
        elif ctx.expression():
            if type(self.visit(ctx.lhs())) == ArrayCell:
                return ArrayCell(self.visit(ctx.lhs()).arr, self.visit(ctx.lhs()).idx  + [self.visit(ctx.expression())])
            return ArrayCell(self.visit(ctx.lhs()),[self.visit(ctx.expression())])
        return Id(ctx.ID().getText())


    # if_statement: IF (LP expression RP) ignore* CLP ignore* list_statement ignore* CRP ignore* elif_statement* ignore* else_statement?;
    def visitIf_statement(self, ctx: MiniGoParser.If_statementContext):
        cond = self.visit(ctx.expression())
        then_block = Block(self.visit(ctx.list_statement()))
        elif_statements = [self.visit(i) for i in ctx.elif_statement()] if ctx.elif_statement() else []
        else_block = self.visit(ctx.else_statement()) if ctx.else_statement() else None
        current_else = else_block  

        for elif_cond, elif_block in elif_statements[::-1]:
            current_else = If(elif_cond, elif_block, current_else)  

        return If(cond, then_block, current_else)


    # elif_statement: ELSE IF (LP expression RP) ignore* CLP ignore* list_statement ignore* CRP;
    def visitElif_statement(self, ctx: MiniGoParser.Elif_statementContext):
        return (self.visit(ctx.expression()), Block(self.visit(ctx.list_statement())))


    # else_statement: ELSE ignore* CLP ignore* list_statement ignore* CRP;
    def visitElse_statement(self, ctx:MiniGoParser.Else_statementContext):
        return Block(self.visit(ctx.list_statement()))


    # for_statement: for_basic | for_step | for_each;
    def visitFor_statement(self, ctx:MiniGoParser.For_statementContext):
        return self.visit(ctx.getChild(0))


    # break_statement: BREAK ignore;
    def visitBreak_statement(self, ctx:MiniGoParser.Break_statementContext):
        return Break()


    # continue_statement: CONTINUE ignore;
    def visitContinue_statement(self, ctx:MiniGoParser.Continue_statementContext):
        return Continue()


    # call_statement: (lhs DOT)? ID LP index_operators? RP (SEMICOLON | NEWLINE | ignore)*;
    def visitCall_statement(self, ctx:MiniGoParser.Call_statementContext):
        if ctx.DOT():
            return MethCall(self.visit(ctx.lhs()), ctx.ID().getText(), self.visit(ctx.index_operators()) if ctx.index_operators() else [])
        return FuncCall(ctx.ID().getText(), self.visit(ctx.index_operators()) if ctx.index_operators() else [])


    # function_call: ID LP index_operators? RP;
    def visitFunction_call(self, ctx:MiniGoParser.Function_callContext):
        return FuncCall(ctx.ID().getText(), self.visit(ctx.index_operators()) if ctx.index_operators() else [])


    # return_statement: RETURN ignore | RETURN expression;
    def visitReturn_statement(self, ctx:MiniGoParser.Return_statementContext):
        if ctx.expression():
            return Return(self.visit(ctx.expression()))
        return Return(None)

    
    # ignore: SEMICOLON NEWLINE* | NEWLINE;
    def visitIgnore(self, ctx: MiniGoParser.IgnoreContext):
        if ctx.SEMICOLON(): 
            return None
        return self.visitChildren(ctx)
