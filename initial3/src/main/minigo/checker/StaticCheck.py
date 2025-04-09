from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *
from StaticError import Type as StaticErrorType
from functools import reduce
from typing import List, Tuple
from AST import Type

class FuntionType(Type):
    def __str__(self):
        return "FuntionType"

    def accept(self, v, param):
        return v.visitFuntionType(self, param)


class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return "Symbol(" + str(self.name) + "," + str(self.mtype) + ("" if self.value is None else "," + str(self.value)) + ")"

class StaticChecker(BaseVisitor,Utils):
        
    
    def __init__(self,ast):
        self.ast = ast
        self.list_type: List[Union[StructType, InterfaceType]] = []
        self.global_envi: List[FuncDecl] =  [
                FuncDecl("getInt", [], IntType(), Block([])),
                FuncDecl("putInt", [ParamDecl("VOTIEN", IntType())], VoidType(), Block([])),
                FuncDecl("putIntLn", [ParamDecl("VOTIEN", IntType())], VoidType(), Block([])),
                FuncDecl("getFloat", [], FloatType(), Block([])),
                FuncDecl("putFloat", [ParamDecl("VOTIEN", FloatType())], VoidType(), Block([])),
                FuncDecl("putFloatLn", [ParamDecl("VOTIEN", FloatType())], VoidType(), Block([])),
                FuncDecl("getBool", [], BoolType(), Block([])),
                FuncDecl("putBool", [ParamDecl("VOTIEN", BoolType())], VoidType(), Block([])),
                FuncDecl("putBoolLn", [ParamDecl("VOTIEN", BoolType())], VoidType(), Block([])),
                FuncDecl("getString", [], StringType(), Block([])),
                FuncDecl("putString", [ParamDecl("VOTIEN", StringType())], VoidType(), Block([])),
                FuncDecl("putStringLn", [ParamDecl("VOTIEN", StringType())], VoidType(), Block([])),
                FuncDecl("putLn", [], VoidType(), Block([]))
            ]
        self.function_current: FuncDecl = None
        self.list_protos: List[Prototype] = []
    
    def check(self):
        self.visit(self.ast, None)

    def visitProgram(self, ast, c):
        def visitMethodDecl(ast, c):
            res = self.lookup(ast.fun.name, c.methods, lambda x: x.fun.name)
            if not res is None:
                raise Redeclared(Method(), ast.fun.name)
            c.methods += [ast]

        self.list_type = reduce(lambda acc, ele: [self.visit(ele, acc)] + acc if isinstance(ele, Type) else acc, ast.decl, [])
        self.global_envi = self.global_envi + list(filter(lambda item: isinstance(item, FuncDecl), ast.decl))

        list(map(
            lambda item: visitMethodDecl(item, self.lookup(item.recType.name, self.list_type, lambda x: x.name)), 
             list(filter(lambda item: isinstance(item, MethodDecl), ast.decl))
        ))

        reduce(
            lambda acc, ele: [
                ([result] + acc[0]) if isinstance(result := self.visit(ele, acc), Symbol) else acc[0]
            ] + acc[1:], 
            filter(lambda item: isinstance(item, Decl), ast.decl), 
            [[
                Symbol("getInt", FuntionType()),
                Symbol("putInt", FuntionType()),
                Symbol("putIntLn",FuntionType()),
                Symbol("getFloat",FuntionType()),
                Symbol("putFloat",FuntionType()),
                Symbol("putFloatLn",FuntionType()),
                Symbol("getBool",FuntionType()),
                Symbol("putBool",FuntionType()),
                Symbol("putBoolLn",FuntionType()),
                Symbol("getString",FuntionType()),
                Symbol("putString",FuntionType()),
                Symbol("putStringLn",FuntionType()),
                Symbol("putLn",FuntionType())
            ]]
        )


    def checkType(self, LHS_type, RHS_type, list_type_permission: List[Tuple[Type, Type]] = []):
        if type(RHS_type) == StructType and RHS_type.name == "":
            return True
        LHS_type = self.lookup(LHS_type.name, self.list_type, lambda x: x.name) if isinstance(LHS_type, Id) else LHS_type
        RHS_type = self.lookup(RHS_type.name, self.list_type, lambda x: x.name) if isinstance(RHS_type, Id) else RHS_type
        if (type(LHS_type), type(RHS_type)) in list_type_permission:
            if isinstance(LHS_type, InterfaceType) and isinstance(RHS_type, StructType):
                for method in LHS_type.methods:
                    if not any(struct_method.fun.name == method.fun.name and 
                               type(struct_method.fun.retType) == type(method.fun.retType) and 
                               len(struct_method.fun.params) == len(method.fun.params) and 
                               all(type(struct_param.parType) == type(method_param.parType) 
                                   for struct_param, method_param in zip(struct_method.fun.params, method.fun.params))
                               for struct_method in RHS_type.methods):
                        return False
                return True
            return True

        if (isinstance(LHS_type, InterfaceType) and isinstance(RHS_type, InterfaceType)) or (isinstance(LHS_type, StructType) and isinstance(RHS_type, StructType)):
            return LHS_type.name == RHS_type.name

        if isinstance(LHS_type, ArrayType) and isinstance(RHS_type, ArrayType):
            return LHS_type.dimens == RHS_type.dimens
        return type(LHS_type) == type(RHS_type)

    def visitStructType(self, ast: StructType, c: List[Union[StructType, InterfaceType]]):
        res = self.lookup(ast.name, c, lambda x: x.name)
        if not res is None:
            raise Redeclared(StaticErrorType(), ast.name)  
        
        def visitElements(element: Tuple[str,Type], c: List[Tuple[str,Type]]):
            if any(ele[0] == element[0] for ele in c):
                raise Redeclared(Field(), element[0])
            return element

        ast.elements = reduce(lambda acc,ele: [visitElements(ele,acc)] + acc , ast.elements , [])
        return ast

    def visitPrototype(self, ast, c):
        if any(proto.name == ast.name for proto in c):
            raise Redeclared(Prototype(), ast.name)

        c.append(ast)
        return ast

    def visitInterfaceType(self, ast: InterfaceType, c: List[Union[StructType, InterfaceType]]):
        res = self.lookup(ast.name, c, lambda x: x.name)
        if not res is None:
            raise Redeclared(StaticErrorType(), ast.name)
        reduce(lambda acc,ele: [self.visit(ele,acc)] + acc , ast.methods , [])
        return ast
    
    def visitFuncDecl(self, ast, c):
        res = self.lookup(ast.name, c[0], lambda x: x.name)
        if not res is None:
            raise Redeclared(Function(), ast.name)

        self.visit(ast.body, [list(reduce(lambda acc,ele: [self.visit(ele,acc)] + acc, ast.params, []))] + c)
        self.global_envi.append(ast)
        return Symbol(ast.name, FuntionType())

    def visitParamDecl(self, ast, c):
        if any(symbol.name == ast.parName for symbol in c):
            raise Redeclared(Parameter(), ast.parName)

        return Symbol(ast.parName, ast.parType, None)

    def visitMethodDecl(self, ast, c):
        struct_def = self.lookup(ast.recType.name, self.list_type, lambda x: x.name)
        if struct_def is None:
            raise Undeclared(Type(), ast.recType.name)
#        if any(param.parName == ast.receiver for param in ast.fun.params):
#            raise Redeclared(Parameter(), ast.receiver)
        if any(element[0] == ast.fun.name for element in struct_def.elements):
            raise Redeclared(Method(), ast.fun.name)
        struct_def.methods.append(ast)

        param_scope = list(reduce(lambda acc, ele: [self.visit(ele, acc)] + acc, ast.fun.params, []))
        receiver_scope = [Symbol(ast.receiver, ast.recType, None)]
        self.function_current = ast.fun
        self.visit(ast.fun.body, [param_scope + receiver_scope] + [[]])
        
    def visitVarDecl(self, ast, c):
        res = self.lookup(ast.varName, c[0], lambda x: x.name)
        if not res is None:
            raise Redeclared(Variable(), ast.varName) 
        
        LHS_type = ast.varType if ast.varType else None
        RHS_type = self.visit(ast.varInit, c) if ast.varInit else None

        if RHS_type is None:
            return Symbol(ast.varName, LHS_type, None)
        elif LHS_type is None:
            return Symbol(ast.varName, RHS_type, None)
        elif self.checkType(LHS_type, RHS_type, [(FloatType, IntType), (InterfaceType, StructType)]):
            return Symbol(ast.varName, LHS_type, None)
        raise TypeMismatch(ast)

    def visitConstDecl(self, ast, c):
        res = self.lookup(ast.conName, c[0], lambda x: x.name)
        if not res is None:
            raise Redeclared(Constant(), ast.conName) 

        return Symbol(ast.conName, self.visit(ast.iniExpr, c), None)
    
    def visitBlock(self, ast, c):
        reduce(
            lambda acc, ele: [
                ([result] + acc[0]) if isinstance(result := self.visit(ele, acc), Symbol) else acc[0]
            ] + acc[1:], 
            ast.member, 
            [[]] + c
        )

    def visitForBasic(self, ast, c):
#        if not isinstance(ast.cond, BoolType):
#            raise TypeMismatch(ast)
        self.visit(Block(ast.loop.member), c)

    def visitForStep(self, ast, c): 
        symbol = self.visit(ast.init, [[]] + c)
#        if (not isinstance(symbol, VarDecl)) or (not isinstance(self.visit(ast.cond, c), BoolType)):
#            raise TypeMismatch(ast)
        self.visit(Block([ast.init] + ast.loop.member + [ast.upda]), c)
    
    def visitForEach(self, ast, c): 
        self.visit(Block([VarDecl(ast.idx.name, None, None), VarDecl(ast.value.name, None, None)] + ast.loop.member), c)
    
    def visitReturn(self, ast, c):
        return None
    
    def visitId(self, ast, c):
        res = next((symbol for scope in c for symbol in scope if symbol.name == ast.name), None)
        if res and not isinstance(res.mtype, Function):
            return res.mtype
        raise Undeclared(Identifier(), ast.name)

    
    def visitFuncCall(self, ast, c):
        res = next((func for func in self.global_envi if func.name == ast.funName), None)
        if res:
            return res.retType
        raise Undeclared(Function(), ast.funName)

    def visitFieldAccess(self, ast, c):
        type_receiver = self.visit(ast.receiver, c)
        type_receiver = self.lookup(type_receiver.name, self.list_type, lambda x: x.name) if isinstance(type_receiver, Id) else type_receiver
        if isinstance(type_receiver, InterfaceType):
            raise TypeMismatch(ast)
        res = self.lookup(ast.field, type_receiver.elements, lambda x: x[0])
        if res is not None:
            return res[1]
        raise Undeclared(Field(), ast.field)

    def visitMethCall(self, ast, c):
        type_receiver = self.visit(ast.receiver, c)
        type_receiver = self.lookup(type_receiver.name, self.list_type, lambda x: x.name) if isinstance(type_receiver, Id) else type_receiver

        if not isinstance(type_receiver, (StructType, InterfaceType)):
            raise TypeMismatch(ast)

        method = self.lookup(ast.metName, type_receiver.methods, lambda x: x.fun.name) if isinstance(type_receiver, StructType) else self.lookup(ast.metName, type_receiver.methods, lambda x: x.name)
        if method is None:
            raise Undeclared(Method(), ast.metName)
    
    def visitIntType(self, ast, param):
        return IntType()
    
    def visitFloatType(self, ast, param):
        return FloatType()
    
    def visitBoolType(self, ast, param):
        return BoolType()
    
    def visitStringType(self, ast, param):
        return StringType()
    
    def visitVoidType(self, ast, param):
        return VoidType()
    
    def visitArrayType(self, ast, c):
        list(map(lambda item: self.visit(item, c), ast.dimens))
        return ast

    def visitAssign(self, ast, param):
        return None
    
    def visitIf(self, ast, param):
        return None

    def visitContinue(self, ast, c):
        return None

    def visitBreak(self, ast, c):
        return None

    def visitBinaryOp(self, ast, c):
        LHS_type = self.visit(ast.left, c)
        RHS_type = self.visit(ast.right, c)

        if ast.op == '+':
            if self.checkType(LHS_type, RHS_type, [(FloatType, IntType), (IntType, FloatType)]):
                if isinstance(LHS_type, StringType):
                    return StringType()
                elif isinstance(LHS_type, FloatType):
                    return FloatType()
                elif isinstance(RHS_type, FloatType):
                    return FloatType()
                elif isinstance(LHS_type, IntType):
                    return IntType()
        elif ast.op == '-':
            if self.checkType(LHS_type, RHS_type, [(FloatType, IntType), (IntType, FloatType)]):
                if isinstance(LHS_type, FloatType):
                    return FloatType()
                elif isinstance(RHS_type, FloatType):
                    return FloatType()
                elif isinstance(LHS_type, IntType):
                    return IntType()
        elif ast.op == '*':
            if self.checkType(LHS_type, RHS_type, [(FloatType, IntType), (IntType, FloatType)]):
                if isinstance(LHS_type, FloatType):
                    return FloatType()
                elif isinstance(RHS_type, FloatType):
                    return FloatType()
                elif isinstance(LHS_type, IntType):
                    return IntType()
        elif ast.op == '/':
            if self.checkType(LHS_type, RHS_type, [(FloatType, IntType), (IntType, FloatType)]):
                if isinstance(LHS_type, FloatType):
                    return FloatType()
                elif isinstance(RHS_type, FloatType):
                    return FloatType()
                elif isinstance(LHS_type, IntType):
                    return IntType()
        elif ast.op in ['==', '!=', '<', '>', '<=', '>=']:
            return BoolType()
        raise TypeMismatch(ast)

    def visitUnaryOp(self, ast, param):
        return None
    
    def visitArrayCell(self, ast, param):
        return None

    def visitIntLiteral(self, ast, param):
        return IntType()
    
    def visitFloatLiteral(self, ast, param):
        return FloatType()
    
    def visitBooleanLiteral(self, ast, param):
        return BoolType()
    
    def visitStringLiteral(self, ast, param):
        return StringType()
    
    def visitArrayLiteral(self, ast, param):
        return None
    
    def visitStructLiteral(self, ast, param):
        return None

    def visitNilLiteral(self, ast, c):
        return StructType("", [], [])
