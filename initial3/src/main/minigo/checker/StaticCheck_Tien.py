from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce
from typing import List, Tuple

from StaticError import Type as StaticErrorType
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
        self.list_function: List[FuncDecl] =  [
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

    def visitProgram(self, ast: Program, c: None):
        def visitMethodDecl(ast: MethodDecl, c: StructType) -> MethodDecl:
            res = self.lookup(ast.fun.name, c.methods, lambda x: x.fun.name)
            if not res is None:
                raise Redeclared(Method(), ast.fun.name)
            c.methods += [ast]

        list_str = ["getInt", "putInt", "putIntLn", "getFloat", "putFloat", "putFloatLn", "getBool", "putBool", "putBoolLn", "getString", "putString", "putStringLn", "putLn"]
        for item in ast.decl:
            if isinstance(item, Type):
                if item.name in list_str:
                    raise Redeclared(StaticErrorType(), item.name)
                list_str.append(item.name)  

        self.list_type = reduce(lambda acc, ele: [self.visit(ele, acc)] + acc if isinstance(ele, Type) else acc, ast.decl, [])
        self.list_function = self.list_function + list(filter(lambda item: isinstance(item, FuncDecl), ast.decl))

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


    def check(self):
        self.visit(self.ast, None)


    def checkType(self, LHS_type: Type, RHS_type: Type, list_type_permission: List[Tuple[Type, Type]] = []) -> bool:
        if type(RHS_type) == StructType and RHS_type.name == "":
            return True
        LHS_type = self.lookup(LHS_type.name, self.list_type, lambda x: x.name) if isinstance(LHS_type, Id) else LHS_type
        RHS_type = self.lookup(RHS_type.name, self.list_type, lambda x: x.name) if isinstance(RHS_type, Id) else RHS_type
        if (type(LHS_type), type(RHS_type)) in list_type_permission:
            if isinstance(LHS_type, InterfaceType) and isinstance(RHS_type, StructType):
                for method in LHS_type.methods:
                    if not any(
                        struct_method.fun.name == method.name and 
                        self.checkType(method.retType, struct_method.fun.retType) and 
                        len(struct_method.fun.params) == len(method.params) and 
                        all(self.checkType(struct_param.parType, method_param)
                            for struct_param, method_param in zip(struct_method.fun.params, method.params))
                        for struct_method in RHS_type.methods
                    ):
                        return False
                return True
            return True

        if (isinstance(LHS_type, InterfaceType) and isinstance(RHS_type, InterfaceType)) or (isinstance(LHS_type, StructType) and isinstance(RHS_type, StructType)):
            return LHS_type.name == RHS_type.name

        if isinstance(LHS_type, ArrayType) and isinstance(RHS_type, ArrayType):
            return LHS_type.dimens == RHS_type.dimens
        
        return type(LHS_type) == type(RHS_type)

    def visitStructType(self, ast: StructType, c : List[Union[StructType, InterfaceType]]) -> StructType:
        res = self.lookup(ast.name, c, lambda x: x.name)
        if not res is None:
            raise Redeclared(StaticErrorType(), ast.name)  
        
        def visitElements(element: Tuple[str,Type], c: List[Tuple[str,Type]]) -> Tuple[str,Type]:
            if any(ele[0] == element[0] for ele in c):
                raise Redeclared(Field(), element[0])
            return element

        ast.elements = reduce(lambda acc,ele: [visitElements(ele,acc)] + acc , ast.elements , [])
        return ast

    def visitPrototype(self, ast: Prototype, c: List[Prototype]) -> Prototype:
        if any(proto.name == ast.name for proto in c):
            raise Redeclared(Prototype(), ast.name)
        c.append(ast)
        return ast

    def visitInterfaceType(self, ast: InterfaceType, c : List[Union[StructType, InterfaceType]]) -> InterfaceType:
        res = self.lookup(ast.name, c, lambda x: x.name)
        if not res is None:
            raise Redeclared(StaticErrorType(), ast.name)
        reduce(lambda acc,ele: [self.visit(ele,acc)] + acc , ast.methods , [])
        return ast
    
    def visitFuncDecl(self, ast: FuncDecl, c : List[List[Symbol]]) -> Symbol:
        res = self.lookup(ast.name, c[0], lambda x: x.name)
        if not res is None:
            raise Redeclared(Function(), ast.name)

        self.function_current = ast

        self.visit(ast.body, [list(reduce(lambda acc,ele: [self.visit(ele,acc)] + acc, ast.params, []))] + c)
        self.list_function.append(ast)
        return Symbol(ast.name, FuntionType())

    def visitParamDecl(self, ast: ParamDecl, c: list[Symbol]) -> Symbol:
        if any(symbol.name == ast.parName for symbol in c):
            raise Redeclared(Parameter(), ast.parName)

        return Symbol(ast.parName, ast.parType, None)

    def visitMethodDecl(self, ast: MethodDecl, c : List[List[Symbol]]) -> None:
        struct_def = self.lookup(ast.recType.name, self.list_type, lambda x: x.name)
        if struct_def is None:
            raise Undeclared(Type(), ast.recType.name)
        if any(element[0] == ast.fun.name for element in struct_def.elements):
            raise Redeclared(Method(), ast.fun.name)
        struct_def.methods.append(ast)

        self.function_current = ast.fun

        param_scope = list(reduce(lambda acc, ele: [self.visit(ele, acc)] + acc, ast.fun.params, []))
        receiver_scope = [Symbol(ast.receiver, ast.recType, None)]
        self.visit(ast.fun.body, [param_scope + receiver_scope] + [[]])

        
    def visitVarDecl(self, ast: VarDecl, c: List[List[Symbol]]) -> Symbol:
        res = self.lookup(ast.varName, c[0], lambda x: x.name)
        if res is not None:
            raise Redeclared(Variable(), ast.varName)

        if self.lookup(ast.varName, self.list_type, lambda x: x.name):
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

    def visitConstDecl(self, ast: ConstDecl, c : List[List[Symbol]]) -> Symbol:
        res = self.lookup(ast.conName, c[0], lambda x: x.name)
        if res is not None:
            raise Redeclared(Constant(), ast.conName)

        if self.lookup(ast.conName, self.list_type, lambda x: x.name):
            raise Redeclared(Constant(), ast.conName)

        return Symbol(ast.conName, self.visit(ast.iniExpr, c), None)
    
    def visitBlock(self, ast: Block, c: List[List[Symbol]]) -> None:
        reduce(
            lambda acc, ele: [
                ([result] + acc[0]) if isinstance(result := self.visit(ele, acc), Symbol) else acc[0]
            ] + acc[1:], 
            ast.member, 
            [[]] + c
        )

    def visitForBasic(self, ast: ForBasic, c : List[List[Symbol]]) -> None:
        if not isinstance(self.visit(ast.cond, [[]] + c), BoolType):
            raise TypeMismatch(ast)
        self.visit(Block(ast.loop.member), c)

    def visitForStep(self, ast: ForStep, c: List[List[Symbol]]) -> None:
        symbol = self.visit(ast.init, [[]] + c)
        c[0].append(symbol)
        if not isinstance(self.visit(ast.cond, c), BoolType):
            raise TypeMismatch(ast)
        
        try:
            self.visit(ast.upda, c)
        except Undeclared:
            if isinstance(ast.upda, Assign) and isinstance(ast.upda.lhs, Id):
                c[0].append(Symbol(ast.upda.lhs.name, IntType, None))

        for member in ast.loop.member:
            if isinstance(member, VarDecl):
                res = self.lookup(member.varName, c[0], lambda x: x.name)
                if not res is None:
                    raise Redeclared(Variable(), member.varName)
            elif isinstance(member, ConstDecl):
                res = self.lookup(member.conName, c[0], lambda x: x.name)
                if not res is None:
                    raise Redeclared(Constant(), member.conName)
        self.visit(ast.loop, c)

    def visitForEach(self, ast: ForEach, c: List[List[Symbol]]) -> None:
        type_array = self.visit(ast.arr, c)
        if not isinstance(type_array, ArrayType):
            raise TypeMismatch(ast)

        index_type = IntType()
        value_type = type_array.eleType if len(type_array.dimens) == 1 else ArrayType(type_array.dimens[1:], type_array.eleType)

        self.visit(Block([VarDecl(ast.idx.name, index_type, None), VarDecl(ast.value.name, value_type, None)] + ast.loop.member), c)
    
    def visitReturn(self, ast: Return, c: List[List[Symbol]]) -> None:
        expected_type = VoidType() if self.function_current is None else self.function_current.retType
        actual_type = self.visit(ast.expr, c) if ast.expr else VoidType()

        if isinstance(expected_type, VoidType) and ast.expr:
            raise TypeMismatch(ast)
        elif not isinstance(expected_type, VoidType) and not ast.expr:
            raise TypeMismatch(ast)
        elif not self.checkType(expected_type, actual_type):
            raise TypeMismatch(ast)

        
    def visitId(self, ast: Id, c: List[List[Symbol]]) -> Type:
        res = next((symbol for scope in c for symbol in scope if symbol.name == ast.name), None)
        if res and not isinstance(res.mtype, VoidType):
            return res.mtype
        raise Undeclared(Identifier(), ast.name)
   
    def visitFuncCall(self, ast: FuncCall, c: Union[List[List[Symbol]], Tuple[List[List[Symbol]], bool]]) -> Type:
#        is_stmt = False
#        if isinstance(c, tuple):
#            c, is_stmt = c
        
        res = self.lookup(ast.funName, self.list_function, lambda x: x.name)
        if res:
            if len(res.params) != len(ast.args):
                raise TypeMismatch(ast)
            
            for param, arg in zip(res.params, ast.args):
                arg_type = self.visit(arg, c)
                if not self.checkType(param.parType, arg_type):
                    raise TypeMismatch(ast)
                
#            if is_stmt and isinstance(res.retType, VoidType):
#                raise TypeMismatch(ast)
            
#            if not is_stmt and isinstance(res.retType, VoidType):
#                raise TypeMismatch(ast)
            return res.retType
        
        raise Undeclared(Function(), ast.funName)

    def visitFieldAccess(self, ast: FieldAccess, c: List[List[Symbol]]) -> Type:
        type_receiver = self.visit(ast.receiver, c)
        type_receiver = self.lookup(type_receiver.name, self.list_type, lambda x: x.name) if isinstance(type_receiver, Id) else type_receiver
        if isinstance(type_receiver, InterfaceType):
            raise TypeMismatch(ast)
        res = self.lookup(ast.field, type_receiver.elements, lambda x: x[0])
        if res is not None:
            return res[1]
        raise Undeclared(Field(), ast.field)

    def visitMethCall(self, ast: MethCall, c: Union[List[List[Symbol]], Tuple[List[List[Symbol]], bool]]) -> Type:
#        is_stmt = False
#        if isinstance(c, tuple):
#            c, is_stmt = c
        
        receiver_type = self.visit(ast.receiver, c)
        receiver_type = self.lookup(receiver_type.name, self.list_type, lambda x: x.name) if isinstance(receiver_type, Id) else receiver_type
        if not isinstance(receiver_type, (StructType, InterfaceType)):
            raise TypeMismatch(ast)
        
        if isinstance(receiver_type, StructType):
            method = self.lookup(ast.metName, receiver_type.methods, lambda x: x.fun.name)
            if method:
                if len(method.fun.params) != len(ast.args):
                    raise TypeMismatch(ast)

                for param, arg in zip(method.fun.params, ast.args):
                    arg_type = self.visit(arg, c)
                    if not self.checkType(param.parType, arg_type):
                        raise TypeMismatch(ast)
                
#                if is_stmt and not isinstance(method.fun.retType, VoidType):
#                    raise TypeMismatch(ast)
        
#                if not is_stmt and isinstance(method.fun.retType, VoidType):
#                    raise TypeMismatch(ast)
            
                return method.fun.retType

        elif isinstance(receiver_type, InterfaceType):
            method = self.lookup(ast.metName, receiver_type.methods, lambda x: x.name)
            if method:
                if len(method.params) != len(ast.args):
                    raise TypeMismatch(ast)

                for param, arg in zip(method.params, ast.args):
                    arg_type = self.visit(arg, c)
                    if not self.checkType(param.parType, arg_type):
                        raise TypeMismatch(ast)
                    
#                if is_stmt and not isinstance(method.retType, VoidType):
#                    raise TypeMismatch(ast)
        
#                if not is_stmt and isinstance(method.retType, VoidType):
#                    raise TypeMismatch(ast)

                return method.retType

        raise Undeclared(Method(), ast.metName)

    
    def visitIntType(self, ast, c: List[List[Symbol]]) -> Type:
        return IntType()
    
    def visitFloatType(self, ast, c: List[List[Symbol]]) -> Type:
        return FloatType()
    
    def visitBoolType(self, ast, c: List[List[Symbol]]) -> Type:
        return BoolType()
    
    def visitStringType(self, ast, c: List[List[Symbol]]) -> Type:
        return StringType()
    
    def visitVoidType(self, ast, c: List[List[Symbol]]) -> Type:
        return VoidType()
    
    def visitArrayType(self, ast: ArrayType, c: List[List[Symbol]]):
        dimens = list(map(lambda item: self.visit(item, c), ast.dimens))
        return ast

    def visitAssign(self, ast: Assign, c: List[List[Symbol]]) -> None:
        LHS_type = self.visit(ast.lhs, c)

        if isinstance(LHS_type, VoidType):
            raise TypeMismatch(ast)

        RHS_type = self.visit(ast.rhs, c)
        if not self.checkType(LHS_type, RHS_type, [(IntType, IntType), (FloatType, FloatType), (StringType, StringType),
                                                   (BoolType, BoolType), (ArrayType, ArrayType), (StructType, StructType), (InterfaceType, InterfaceType),
                                                   (FloatType, IntType)]):
            raise TypeMismatch(ast)

    def visitIf(self, ast: If, c: List[List[Symbol]]) -> None: 
        if not isinstance(self.visit(ast.expr, c), BoolType):
            raise TypeMismatch(ast)
        self.visit(Block(ast.thenStmt.member), c)
        if ast.elseStmt:
            for else_stmt in ast.elseStmt:
                if not isinstance(self.visit(else_stmt.expr, c), BoolType):
                    raise TypeMismatch(else_stmt)
                self.visit(Block(else_stmt.thenStmt.member), c)

    def visitContinue(self, ast, c: List[List[Symbol]]) -> None:
        return None

    def visitBreak(self, ast, c: List[List[Symbol]]) -> None:
        return None

    def visitBinaryOp(self, ast: BinaryOp, c: List[List[Symbol]]) -> Type:
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
        elif ast.op in ['<', '>', '<=', '>=']:
            if self.checkType(LHS_type, RHS_type, [(IntType, IntType), (FloatType, FloatType)]):
                return BoolType()
        elif ast.op in ['==', '!=']:
            if self.checkType(LHS_type, RHS_type, [(IntType, IntType), (FloatType, FloatType), (StringType, StringType), (BoolType, BoolType)]):
                return BoolType()  
        elif ast.op in ['&&', '||']:
            if self.checkType(LHS_type, RHS_type, [(BoolType, BoolType)]):
                return BoolType()
        raise TypeMismatch(ast)

    def visitUnaryOp(self, ast: UnaryOp, c: List[List[Symbol]]) -> Type:
        operand_type = self.visit(ast.body, c)
        if ast.op == '-':
            if isinstance(operand_type, (IntType, FloatType)):
                return operand_type
        elif ast.op == '!':
            if isinstance(operand_type, BoolType):
                return BoolType()
        raise TypeMismatch(ast)
    
    def visitArrayCell(self, ast: ArrayCell, c: List[List[Symbol]]):
        array_type = self.visit(ast.arr, c)
        if not isinstance(array_type, ArrayType):
            raise TypeMismatch(ast)

        if not all(map(lambda item: isinstance(self.visit(item, c), IntType), ast.idx)):
            raise TypeMismatch(ast)
        
        if len(array_type.dimens) == len(ast.idx):
            return array_type.typ
        elif len(array_type.dimens) > len(ast.idx):
            return ArrayType(array_type.dimens[len(ast.idx):], array_type.typ)
        raise TypeMismatch(ast)

    def visitIntLiteral(self, ast, c: List[List[Symbol]]) -> Type:
        return IntType()
    
    def visitFloatLiteral(self, ast, c: List[List[Symbol]]) -> Type:
        return FloatType()
    
    def visitBooleanLiteral(self, ast, c: List[List[Symbol]]) -> Type:
        return BoolType()
    
    def visitStringLiteral(self, ast, c: List[List[Symbol]]) -> Type:
        return StringType()
    
    def visitArrayLiteral(self, ast:ArrayLiteral , c: List[List[Symbol]]) -> Type:  
        def nested2recursive(dat: Union[Literal, list['NestedList']], c: List[List[Symbol]]):
            if isinstance(dat, list):
                list(map(lambda value: nested2recursive(value, c), dat))
            else:
                self.visit(dat, c)
        nested2recursive(ast.value, c)
        return ArrayType(ast.dimens, ast.eleType)
    
    def visitStructLiteral(self, ast:StructLiteral, c: List[List[Symbol]]) -> Type: 
        list(map(lambda value: self.visit(value[1], c), ast.elements))
        return StructType(ast.name, [], [])

    def visitNilLiteral(self, ast:NilLiteral, c: List[List[Symbol]]) -> Type:
        return StructType("", [], [])

    def evaluate(self, node: AST, c: List[List[Symbol]]) -> int:
        if isinstance(node, IntLiteral):
            return int(node.value)
        elif isinstance(node, Id):
            res = next((symbol for scope in c for symbol in scope if symbol.name == node.name), None)
            if res and isinstance(res.value, int):
                return res.value
            raise Undeclared(Identifier(), node.name)
        elif isinstance(node, BinaryOp):
            left_value = self.evaluate(node.left, c)
            right_value = self.evaluate(node.right, c)
            if node.op == '+':
                return left_value + right_value
            elif node.op == '-':
                return left_value - right_value
            elif node.op == '*':
                return left_value * right_value
            elif node.op == '/':
                return left_value // right_value
        elif isinstance(node, UnaryOp):
            operand_value = self.evaluate(node.body, c)
            if node.op == '-':
                return -operand_value
        raise TypeMismatch(node)
