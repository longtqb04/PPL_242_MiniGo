# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniGoParser import MiniGoParser
else:
    from MiniGoParser import MiniGoParser

# This class defines a complete generic visitor for a parse tree produced by MiniGoParser.

class MiniGoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniGoParser#program.
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#declared.
    def visitDeclared(self, ctx:MiniGoParser.DeclaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#function_declared.
    def visitFunction_declared(self, ctx:MiniGoParser.Function_declaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#variables_declared.
    def visitVariables_declared(self, ctx:MiniGoParser.Variables_declaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#inferred_var.
    def visitInferred_var(self, ctx:MiniGoParser.Inferred_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_variable_declared.
    def visitStruct_variable_declared(self, ctx:MiniGoParser.Struct_variable_declaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#keyword_type_var.
    def visitKeyword_type_var(self, ctx:MiniGoParser.Keyword_type_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#keyword_type_var_infunction.
    def visitKeyword_type_var_infunction(self, ctx:MiniGoParser.Keyword_type_var_infunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#keyword_type_var_inmethod.
    def visitKeyword_type_var_inmethod(self, ctx:MiniGoParser.Keyword_type_var_inmethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_number_lit.
    def visitList_number_lit(self, ctx:MiniGoParser.List_number_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#type_key.
    def visitType_key(self, ctx:MiniGoParser.Type_keyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#type_key_variable.
    def visitType_key_variable(self, ctx:MiniGoParser.Type_key_variableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#constants_declared.
    def visitConstants_declared(self, ctx:MiniGoParser.Constants_declaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#function.
    def visitFunction(self, ctx:MiniGoParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_para_infunction.
    def visitList_para_infunction(self, ctx:MiniGoParser.List_para_infunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_para_infunction_method.
    def visitList_para_infunction_method(self, ctx:MiniGoParser.List_para_infunction_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_declared.
    def visitStruct_declared(self, ctx:MiniGoParser.Struct_declaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_variable_list.
    def visitStruct_variable_list(self, ctx:MiniGoParser.Struct_variable_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_variable_list_recur.
    def visitStruct_variable_list_recur(self, ctx:MiniGoParser.Struct_variable_list_recurContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_declared.
    def visitMethod_declared(self, ctx:MiniGoParser.Method_declaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_para_inmethod.
    def visitList_para_inmethod(self, ctx:MiniGoParser.List_para_inmethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_declared.
    def visitInterface_declared(self, ctx:MiniGoParser.Interface_declaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_para_interface.
    def visitList_para_interface(self, ctx:MiniGoParser.List_para_interfaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#literal.
    def visitLiteral(self, ctx:MiniGoParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression.
    def visitExpression(self, ctx:MiniGoParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression1.
    def visitExpression1(self, ctx:MiniGoParser.Expression1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression2.
    def visitExpression2(self, ctx:MiniGoParser.Expression2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression3.
    def visitExpression3(self, ctx:MiniGoParser.Expression3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression4.
    def visitExpression4(self, ctx:MiniGoParser.Expression4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression5.
    def visitExpression5(self, ctx:MiniGoParser.Expression5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression6.
    def visitExpression6(self, ctx:MiniGoParser.Expression6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression7.
    def visitExpression7(self, ctx:MiniGoParser.Expression7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_literal.
    def visitArray_literal(self, ctx:MiniGoParser.Array_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_element_set.
    def visitArray_element_set(self, ctx:MiniGoParser.Array_element_setContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_literal_declare.
    def visitArray_literal_declare(self, ctx:MiniGoParser.Array_literal_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_elements.
    def visitArray_elements(self, ctx:MiniGoParser.Array_elementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#valid_element.
    def visitValid_element(self, ctx:MiniGoParser.Valid_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#dimensions.
    def visitDimensions(self, ctx:MiniGoParser.DimensionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#type_literal.
    def visitType_literal(self, ctx:MiniGoParser.Type_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#type_literal_except_struct.
    def visitType_literal_except_struct(self, ctx:MiniGoParser.Type_literal_except_structContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_literal.
    def visitStruct_literal(self, ctx:MiniGoParser.Struct_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_literal_recur.
    def visitStruct_literal_recur(self, ctx:MiniGoParser.Struct_literal_recurContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#index_operators.
    def visitIndex_operators(self, ctx:MiniGoParser.Index_operatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#index_operators_recur.
    def visitIndex_operators_recur(self, ctx:MiniGoParser.Index_operators_recurContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#argument_list.
    def visitArgument_list(self, ctx:MiniGoParser.Argument_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#argument_list_recur.
    def visitArgument_list_recur(self, ctx:MiniGoParser.Argument_list_recurContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_argument_list.
    def visitFor_argument_list(self, ctx:MiniGoParser.For_argument_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#variables_declared_for.
    def visitVariables_declared_for(self, ctx:MiniGoParser.Variables_declared_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_statement.
    def visitList_statement(self, ctx:MiniGoParser.List_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_statement_recur.
    def visitList_statement_recur(self, ctx:MiniGoParser.List_statement_recurContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#statement.
    def visitStatement(self, ctx:MiniGoParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_statement_in_function.
    def visitList_statement_in_function(self, ctx:MiniGoParser.List_statement_in_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_statement_in_function_recur.
    def visitList_statement_in_function_recur(self, ctx:MiniGoParser.List_statement_in_function_recurContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#statement_in_function.
    def visitStatement_in_function(self, ctx:MiniGoParser.Statement_in_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#declared_statement.
    def visitDeclared_statement(self, ctx:MiniGoParser.Declared_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#declared_statement_no_ignore.
    def visitDeclared_statement_no_ignore(self, ctx:MiniGoParser.Declared_statement_no_ignoreContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#constants_declared_in_function.
    def visitConstants_declared_in_function(self, ctx:MiniGoParser.Constants_declared_in_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assign_statement.
    def visitAssign_statement(self, ctx:MiniGoParser.Assign_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#if_statement.
    def visitIf_statement(self, ctx:MiniGoParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#elif_statement.
    def visitElif_statement(self, ctx:MiniGoParser.Elif_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#else_statement.
    def visitElse_statement(self, ctx:MiniGoParser.Else_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_statement.
    def visitFor_statement(self, ctx:MiniGoParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#break_statement.
    def visitBreak_statement(self, ctx:MiniGoParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#continue_statement.
    def visitContinue_statement(self, ctx:MiniGoParser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#call_statement.
    def visitCall_statement(self, ctx:MiniGoParser.Call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#function_call.
    def visitFunction_call(self, ctx:MiniGoParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#return_statement.
    def visitReturn_statement(self, ctx:MiniGoParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#ignore.
    def visitIgnore(self, ctx:MiniGoParser.IgnoreContext):
        return self.visitChildren(ctx)



del MiniGoParser