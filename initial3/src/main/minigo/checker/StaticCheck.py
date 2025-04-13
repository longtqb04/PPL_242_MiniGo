from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce
from typing import List, Tuple

from StaticError import Type as StaticErrorType
from AST import Type

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

    def __str__(self):
        return "MType([" + ",".join(str(x) for x in self.partype) + "]," + str(self.rettype) + ")"


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
                FuncDecl("putInt", [ParamDecl("x", IntType())], VoidType(), Block([])),
                FuncDecl("putIntLn", [ParamDecl("x", IntType())], VoidType(), Block([])),
                FuncDecl("getFloat", [], FloatType(), Block([])),
                FuncDecl("putFloat", [ParamDecl("x", FloatType())], VoidType(), Block([])),
                FuncDecl("putFloatLn", [ParamDecl("x", FloatType())], VoidType(), Block([])),
                FuncDecl("getBool", [], BoolType(), Block([])),
                FuncDecl("putBool", [ParamDecl("x", BoolType())], VoidType(), Block([])),
                FuncDecl("putBoolLn", [ParamDecl("x", BoolType())], VoidType(), Block([])),
                FuncDecl("getString", [], StringType(), Block([])),
                FuncDecl("putString", [ParamDecl("x", StringType())], VoidType(), Block([])),
                FuncDecl("putStringLn", [ParamDecl("x", StringType())], VoidType(), Block([])),
                FuncDecl("putLn", [], VoidType(), Block([]))
            ]
        self.function_current: FuncDecl = None
        self.is_stmt: bool = False
        self.list_protos: List[Prototype] = []
    
    def check(self):
        self.visit(self.ast, None)

    def visitProgram(self, ast, c):
        def visitMethodDecl(ast, c):
            res = self.lookup(ast.fun.name, c.methods, lambda x: x.fun.name)
            if not res is None:
                raise Redeclared(Method(), ast.fun.name)
            c.methods += [ast]

        list_str = ["getInt", "putInt", "putIntLn", "getFloat", "putFloat", "putFloatLn", "getBool", "putBool", "putBoolLn", "getString", "putString", "putStringLn", "putLn"]

        for item in ast.decl:
            if isinstance(item, (StructType, InterfaceType)):
                if item.name in list_str:
                    raise Redeclared(StaticErrorType(), item.name)
                list_str.append(item.name)
            elif isinstance(item, VarDecl):
                if item.varName in list_str:
                    raise Redeclared(Variable(), item.varName)
                list_str.append(item.varName)
            elif isinstance(item, ConstDecl):
                if item.conName in list_str:
                    raise Redeclared(Constant(), item.conName)
                list_str.append(item.conName)

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
                Symbol("getInt",MType([],IntType())),
                Symbol("putInt",MType([IntType()],VoidType())),
                Symbol("putIntLn",MType([IntType()],VoidType())),
                Symbol("getFloat",MType([],FloatType())),
                Symbol("putFloat",MType([FloatType()],VoidType())),
                Symbol("putFloatLn",MType([FloatType()],VoidType())),
                Symbol("getBool",MType([],BoolType())),
                Symbol("putBool",MType([BoolType()],VoidType())),
                Symbol("putBoolLn",MType([BoolType()],VoidType())),
                Symbol("getString",MType([],StringType())),
                Symbol("putString",MType([StringType()],VoidType())),
                Symbol("putStringLn",MType([StringType()],VoidType())),
                Symbol("putLn",MType([],VoidType()))
            ]]
        )


    def check(self):
        self.visit(self.ast, None)

    # Check if both types are the same. If not, check if they're within the tuples in allowed_types
    def checkType(self, LHS_type, RHS_type, allowed_types = []):
        if type(RHS_type) == StructType and RHS_type.name == "":
            return True
        LHS_type = self.lookup(LHS_type.name, self.list_type, lambda x: x.name) if isinstance(LHS_type, Id) else LHS_type
        RHS_type = self.lookup(RHS_type.name, self.list_type, lambda x: x.name) if isinstance(RHS_type, Id) else RHS_type
        if (type(LHS_type), type(RHS_type)) in allowed_types:
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
            try:
                lhs_dims = [self.evaluate(dim, [[]]) if not isinstance(dim, int) else dim for dim in LHS_type.dimens]
                rhs_dims = [self.evaluate(dim, [[]]) if not isinstance(dim, int) else dim for dim in RHS_type.dimens]
            except:
                return False

            return lhs_dims == rhs_dims and LHS_type.eleType == RHS_type.eleType

        return type(LHS_type) == type(RHS_type)

    def visitStructType(self, ast, c):
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

    def visitInterfaceType(self, ast, c):
        res = self.lookup(ast.name, c, lambda x: x.name)
        if not res is None:
            raise Redeclared(StaticErrorType(), ast.name)
        reduce(lambda acc,ele: [self.visit(ele,acc)] + acc , ast.methods , [])
        return ast
    
    def visitFuncDecl(self, ast, c):
        res = self.lookup(ast.name, c[0], lambda x: x.name)
        if not res is None:
            raise Redeclared(Function(), ast.name)

        self.function_current = ast

        self.visit(ast.body, [list(reduce(lambda acc,ele: [self.visit(ele,acc)] + acc, ast.params, []))] + c)
        param_types = reduce(lambda acc, param: acc + [param.parType], ast.params, [])
        self.global_envi.append(ast)
        return Symbol(ast.name, MType(param_types, ast.retType))

    def visitParamDecl(self, ast, c):
        if any(symbol.name == ast.parName for symbol in c):
            raise Redeclared(Parameter(), ast.parName)

        return Symbol(ast.parName, ast.parType, None)

    def visitMethodDecl(self, ast, c):
        struct_def = self.lookup(ast.recType.name, self.list_type, lambda x: x.name)
        if struct_def is None:
            raise Undeclared(Type(), ast.recType.name)
        if any(element[0] == ast.fun.name for element in struct_def.elements):
            raise Redeclared(Method(), ast.fun.name)
        struct_def.methods.append(ast)

        self.function_current = ast.fun

        param_scope = list(reduce(lambda acc, ele: [self.visit(ele, acc)] + acc, ast.fun.params, []))
        receiver_scope = [Symbol(ast.receiver, ast.recType, None)]
        self.visit(ast.fun.body, [param_scope, receiver_scope] + c)

        
    def visitVarDecl(self, ast, c):
        res = self.lookup(ast.varName, c[0], lambda x: x.name)
        if res is not None:
            raise Redeclared(Variable(), ast.varName)

        if self.lookup(ast.varName, self.list_type, lambda x: x.name):
            raise Redeclared(Variable(), ast.varName)

        LHS_type = ast.varType if ast.varType else None
        RHS_type = self.visit(ast.varInit, c) if ast.varInit else None

        if isinstance(LHS_type, Id):
            resolved = self.lookup(LHS_type.name, self.list_type, lambda x: x.name)
            if resolved is None:
                raise Undeclared(StaticErrorType(), LHS_type.name)
            LHS_type = resolved

        if isinstance(LHS_type, ArrayType):
            try:
                dimens = list(map(lambda item: self.evaluate(item, c), LHS_type.dimens))
                LHS_type = ArrayType(dimens, LHS_type.eleType)
            except:
                raise TypeMismatch(ast)
            
        if isinstance(ast.varInit, ArrayLiteral):
            try:
                dimens = list(map(lambda item: self.evaluate(item, c), ast.varInit.dimens))
                ele_type = self.visit(ast.varInit.value[0], c) if ast.varInit.value else RHS_type.eleType
                RHS_type = ArrayType(dimens, ele_type)
            except:
                raise TypeMismatch(ast)
            
        if isinstance(LHS_type, ArrayType) and isinstance(RHS_type, ArrayType):
            if not self.checkType(LHS_type.eleType, RHS_type.eleType, [(FloatType, IntType), (InterfaceType, StructType)]):
                raise TypeMismatch(ast)

        if RHS_type is None:
            return Symbol(ast.varName, LHS_type, None)
        elif LHS_type is None:
            return Symbol(ast.varName, RHS_type, None)
        elif isinstance(RHS_type, StructType) and RHS_type.name == "":
            if not isinstance(LHS_type, (StructType, InterfaceType)):
                raise TypeMismatch(ast)
            return Symbol(ast.varName, LHS_type, None)
        elif self.checkType(LHS_type, RHS_type, [(FloatType, IntType), (InterfaceType, StructType)]):
            return Symbol(ast.varName, LHS_type, None)
        raise TypeMismatch(ast)

    def visitConstDecl(self, ast, c):
        res = self.lookup(ast.conName, c[0], lambda x: x.name)
        if res is not None:
            raise Redeclared(Constant(), ast.conName)

        if self.lookup(ast.conName, self.list_type, lambda x: x.name):
            raise Redeclared(Constant(), ast.conName)
        
        value = None
        try:
            value = self.evaluate(ast.iniExpr, c)
        except:
            pass

        return Symbol(ast.conName, self.visit(ast.iniExpr, c), value)
    
    def visitBlock(self, ast, c):
        reduce(
            lambda acc, stmt: [
                ([res] + acc[0]) if isinstance(res := self.visit(stmt, (acc, True) if isinstance(stmt, (FuncCall, MethCall)) else acc), Symbol) else acc[0]
            ] + acc[1:], 
            ast.member,
            [[]] + c
        )

    def visitForBasic(self, ast, c):
        if not isinstance(self.visit(ast.cond, [[]] + c), BoolType):
            raise TypeMismatch(ast)
        self.visit(Block(ast.loop.member), c)

    def visitForStep(self, ast, c): 
        init_scope = [[]] + c
        if isinstance(ast.init, VarDecl):
            symbol = self.visit(ast.init, init_scope)
            init_scope[0].append(symbol)
        else:
            self.visit(ast.init, init_scope)
                
        cond_type = self.visit(ast.cond, init_scope)
        if not isinstance(cond_type, BoolType):
            raise TypeMismatch(ast)
        
        if isinstance(ast.upda, Assign) and isinstance(ast.upda.lhs, Id):
            lhs = ast.upda.lhs
            rhs = ast.upda.rhs

            if isinstance(rhs, BinaryOp) and (rhs.left.name == lhs.name if isinstance(rhs.left, Id) else False):
                res = self.lookup(lhs.name, init_scope[0], lambda x: x.name)
                if not res:
                    raise Undeclared(Identifier(), lhs.name)
            else:
                c[0].append(Symbol(lhs.name, None, None))

        loop_scope = [[]] + init_scope
        for stmt in ast.loop.member:
            if isinstance(stmt, (VarDecl, ConstDecl)):
                stmt_name = stmt.varName if isinstance(stmt, VarDecl) else stmt.conName
                
                if isinstance(ast.upda, Assign) and isinstance(ast.upda.lhs, Id) and stmt_name == ast.upda.lhs.name:
                    if isinstance(stmt, ConstDecl):
                        raise Redeclared(Constant(), stmt.conName)
                    else:
                        raise Redeclared(Variable(), stmt.varName)
        
        for stmt in ast.loop.member:
            self.visit(stmt, loop_scope)

        self.visit(ast.upda, init_scope)

    def visitForEach(self, ast, c):
        type_array = self.visit(ast.arr, c)
        if not isinstance(type_array, ArrayType):
            raise TypeMismatch(ast)
        
        type_index = self.visit(ast.idx, c)
        if not isinstance(type_index, IntType):
            raise TypeMismatch(ast)
        
        type_value = self.visit(ast.value, c)
        if not isinstance(type_value, (IntType, ArrayType)):
            raise TypeMismatch(ast)
        
        if isinstance(type_value, ArrayType):
            if len(type_array.dimens) > len(type_value.dimens):
                expected_dims = type_array.dimens[len(type_array.dimens) - len(type_value.dimens):]
                expected_type = ArrayType(expected_dims, type_array.eleType)
                if not self.checkType(expected_type, type_value):
                    raise TypeMismatch(ast)
            if not self.checkType(type_array.eleType, type_value.eleType):
                raise TypeMismatch(ast)

        self.visit(Block(ast.loop.member), c)
    
    def visitReturn(self, ast, c):
        expected_type = self.function_current.retType
        actual_type = self.visit(ast.expr, c) if ast.expr else VoidType()

        if isinstance(expected_type, VoidType) and ast.expr:
            raise TypeMismatch(ast)
        elif not isinstance(expected_type, VoidType) and not ast.expr:
            raise TypeMismatch(ast)
        elif isinstance(expected_type, StructType) and isinstance(actual_type, InterfaceType):
            raise TypeMismatch(ast)
        elif isinstance(expected_type, ArrayType) and isinstance(actual_type, ArrayType):
            if len(expected_type.dimens) != len(actual_type.dimens):
                raise TypeMismatch(ast)
            if isinstance(ast.expr, ArrayLiteral):
                if type(expected_type.eleType) != type(actual_type.eleType):
                        raise TypeMismatch(ast)
        elif not self.checkType(expected_type, actual_type):
            raise TypeMismatch(ast)
        
    def visitId(self, ast, c):
        res = next((symbol for scope in c for symbol in scope if symbol.name == ast.name), None)
        if res and not isinstance(res.mtype, VoidType):
            return res.mtype
        raise Undeclared(Identifier(), ast.name)
   
    def visitFuncCall(self, ast, c):
        is_stmt = False
        if isinstance(c, tuple):
            c, is_stmt = c

        for scope in c:
            for sym in scope:
                if sym.name == ast.funName:
                    if not isinstance(sym.mtype, MType):
                        raise Undeclared(Function(), ast.funName)
                    break 
            
        res = self.lookup(ast.funName, self.global_envi, lambda x: x.name)
        if not res:
            raise Undeclared(Function(), ast.funName)
        
        if len(res.params) != len(ast.args):
            raise TypeMismatch(ast)
        
        for param, arg in zip(res.params, ast.args):
            arg_type = self.visit(arg, c)

            if isinstance(arg_type, StructType) and arg_type.name == "":
                if not (isinstance(param.parType, InterfaceType) or (isinstance(param.parType, Id) and isinstance(self.lookup(param.parType.name, self.list_type, lambda x: x.name), InterfaceType))):
                    raise TypeMismatch(ast)
                continue

            if isinstance(param.parType, Id):
                param.parType = self.lookup(param.parType.name, self.list_type, lambda x: x.name) or param.parType

            if isinstance(param.parType, InterfaceType) and isinstance(arg_type, StructType):
                raise TypeMismatch(ast)
            
            if isinstance(arg, ArrayLiteral):
                try:
                    dimens = list(map(lambda item: self.evaluate(item, c), arg.dimens))
                    ele_type = arg.eleType
                    arg_type = ArrayType(dimens, ele_type)
                except:
                    raise TypeMismatch(ast)
                
            if isinstance(param.parType, ArrayType) and isinstance(arg_type, ArrayType):
                if type(param.parType.eleType) != type(arg_type.eleType):
                    raise TypeMismatch(ast)
                
            if not self.checkType(param.parType, arg_type):
                raise TypeMismatch(ast)
            
        if is_stmt and not isinstance(res.retType, VoidType):
            raise TypeMismatch(ast)
        
        if not is_stmt and isinstance(res.retType, VoidType):
            raise TypeMismatch(ast)
        
        return res.retType

    def visitFieldAccess(self, ast, c):
        type_receiver = self.visit(ast.receiver, c)
        type_receiver = self.lookup(type_receiver.name, self.list_type, lambda x: x.name) if isinstance(type_receiver, Id) else type_receiver
        if not isinstance(type_receiver, StructType):
            raise TypeMismatch(ast)
        res = self.lookup(ast.field, type_receiver.elements, lambda x: x[0])
        if res is not None:
            return res[1]
        raise Undeclared(Field(), ast.field)

    def visitMethCall(self, ast, c):
        is_stmt = False
        if isinstance(c, tuple):
            c, is_stmt = c
            
        receiver_type = self.visit(ast.receiver, c)
        receiver_type = self.lookup(receiver_type.name, self.list_type, lambda x: x.name) if isinstance(receiver_type, Id) else receiver_type
        if not isinstance(receiver_type, (StructType, InterfaceType)):
            raise TypeMismatch(ast)
        
        if isinstance(receiver_type, StructType):
            method = self.lookup(ast.metName, receiver_type.methods, lambda x: x.fun.name)
            if not method:
                raise Undeclared(Method(), ast.metName)
        
            if len(method.fun.params) != len(ast.args):
                raise TypeMismatch(ast)

            for param, arg in zip(method.fun.params, ast.args):
                arg_type = self.visit(arg, c)

                if isinstance(arg_type, StructType) and arg_type.name == "":
                    if not (isinstance(param.parType, InterfaceType) or (isinstance(param.parType, Id) and isinstance(self.lookup(param.parType.name, self.list_type, lambda x: x.name), InterfaceType))):
                        raise TypeMismatch(ast)
                    continue

                if isinstance(param.parType, Id):
                    param.parType = self.lookup(param.parType.name, self.list_type, lambda x: x.name) or param.parType

                if isinstance(param.parType, InterfaceType) and isinstance(arg_type, StructType):
                    raise TypeMismatch(ast)
                
                if isinstance(arg, ArrayLiteral):
                    try:
                        dimens = list(map(lambda item: self.evaluate(item, c), arg.dimens))
                        ele_type = arg.eleType
                        arg_type = ArrayType(dimens, ele_type)
                    except:
                        raise TypeMismatch(ast)
                    
                if isinstance(param.parType, ArrayType) and isinstance(arg_type, ArrayType):
                    if type(param.parType.eleType) != type(arg_type.eleType):
                        raise TypeMismatch(ast)
                
                if not self.checkType(param.parType, arg_type):
                    raise TypeMismatch(ast)
            
            if is_stmt and not isinstance(method.fun.retType, VoidType):
                raise TypeMismatch(ast)
            
            if not is_stmt and isinstance(method.fun.retType, VoidType):
                raise TypeMismatch(ast)
        
            return method.fun.retType

        elif isinstance(receiver_type, InterfaceType):
            method = self.lookup(ast.metName, receiver_type.methods, lambda x: x.name)
            if not method:
                raise Undeclared(Method(), ast.metName)
            
            if len(method.params) != len(ast.args):
                raise TypeMismatch(ast)

            for param, arg in zip(method.params, ast.args):
                arg_type = self.visit(arg, c)

                if isinstance(arg_type, StructType) and arg_type.name == "":
                    if not (isinstance(param.parType, InterfaceType) or (isinstance(param.parType, Id) and isinstance(self.lookup(param.parType.name, self.list_type, lambda x: x.name), InterfaceType))):
                        raise TypeMismatch(ast)
                    continue

                if isinstance(param, Id):
                    param = self.lookup(param.name, self.list_type, lambda x: x.name) or param

                if isinstance(param, InterfaceType) and isinstance(arg_type, StructType):
                    raise TypeMismatch(ast)
                
                if isinstance(arg, ArrayLiteral):
                    try:
                        dimens = list(map(lambda item: self.evaluate(item, c), arg.dimens))
                        ele_type = arg.eleType
                        arg_type = ArrayType(dimens, ele_type)
                    except:
                        raise TypeMismatch(ast)
                    
                if isinstance(param, ArrayType) and isinstance(arg_type, ArrayType):
                    if type(param.eleType) != type(arg_type.eleType):
                        raise TypeMismatch(ast)

                if not self.checkType(param, arg_type):
                    raise TypeMismatch(ast)
                
            if is_stmt and not isinstance(method.retType, VoidType):
                raise TypeMismatch(ast)
            
            if not is_stmt and isinstance(method.retType, VoidType):
                raise TypeMismatch(ast)

            return method.retType

    
    def visitIntType(self, ast, c):
        return IntType()
    
    def visitFloatType(self, ast, c):
        return FloatType()
    
    def visitBoolType(self, ast, c):
        return BoolType()
    
    def visitStringType(self, ast, c):
        return StringType()
    
    def visitVoidType(self, ast, c):
        return VoidType()
    
    def visitArrayType(self, ast, c):
        try:
            dimens = list(map(lambda item: self.evaluate(item, c), ast.dimens))
        except:
            raise TypeMismatch(ast)
        return ArrayType(dimens, self.visit(ast.eleType, c))

    def visitAssign(self, ast, c):
        if isinstance(ast.lhs, Id):
            lhs_name = ast.lhs.name
            res = next((symbol for scope in c for symbol in scope if symbol.name == lhs_name), None)

            if res is None:
                RHS_type = self.visit(ast.rhs, c)
                c[0].append(Symbol(lhs_name, RHS_type, None))
                return None

        LHS_type = self.visit(ast.lhs, c)
        RHS_type = self.visit(ast.rhs, c)

        if isinstance(ast.lhs, ArrayCell) and isinstance(LHS_type, (IntType, FloatType, BoolType, StringType)):
            if isinstance(LHS_type, IntType) and isinstance(RHS_type, FloatType):
                raise TypeMismatch(ast)
            elif isinstance(LHS_type, FloatType) and isinstance(RHS_type, IntType):
                return None

        if self.checkType(LHS_type, RHS_type, [(IntType, IntType), (FloatType, FloatType), (StringType, StringType),
                                                    (BoolType, BoolType), (ArrayType, ArrayType),
                                                    (StructType, StructType), (InterfaceType, InterfaceType),
                                                    (FloatType, IntType)]):
            return None
        else:
            raise TypeMismatch(ast)

    def visitIf(self, ast, c): 
        if not isinstance(self.visit(ast.expr, c), BoolType):
            raise TypeMismatch(ast)
        self.visit(ast.thenStmt, c)
        if ast.elseStmt:
            self.visit(ast.elseStmt, c)

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
        elif ast.op == '%':
            if self.checkType(LHS_type, RHS_type, [(IntType, IntType)]):
                return IntType()
        elif ast.op in ['<', '>', '<=', '>=']:
            if self.checkType(LHS_type, RHS_type, [(IntType, IntType), (FloatType, FloatType), (StringType, StringType)]):
                return BoolType()
        elif ast.op in ['==', '!=']:
            if self.checkType(LHS_type, RHS_type, [(IntType, IntType), (FloatType, FloatType), (StringType, StringType), (BoolType, BoolType)]):
                return BoolType()  
        elif ast.op in ['&&', '||']:
            if self.checkType(LHS_type, RHS_type, [(BoolType, BoolType)]):
                return BoolType()
        raise TypeMismatch(ast)

    def visitUnaryOp(self, ast, c):
        operand_type = self.visit(ast.body, c)
        if ast.op == '-':
            if isinstance(operand_type, (IntType, FloatType)):
                return operand_type
        elif ast.op == '!':
            if isinstance(operand_type, BoolType):
                return BoolType()
        raise TypeMismatch(ast)
    
    def visitArrayCell(self, ast, c):
        array_type = self.visit(ast.arr, c)
        if not isinstance(array_type, ArrayType):
            raise TypeMismatch(ast)

        if not all(map(lambda item: isinstance(self.visit(item, c), IntType), ast.idx)):
            raise TypeMismatch(ast)
        
        if len(array_type.dimens) == len(ast.idx):
            return array_type.eleType
        elif len(array_type.dimens) > len(ast.idx):
            return ArrayType(array_type.dimens[len(ast.idx):], array_type.eleType)
        raise TypeMismatch(ast)

    def visitIntLiteral(self, ast, c):
        return IntType()
    
    def visitFloatLiteral(self, ast, c):
        return FloatType()
    
    def visitBooleanLiteral(self, ast, c):
        return BoolType()
    
    def visitStringLiteral(self, ast, c):
        return StringType()
    
    def visitArrayLiteral(self, ast, c):  
        def nested(dat: Union[Literal, list['NestedList']], c: List[List[Symbol]]):
            if isinstance(dat, list):
                list(map(lambda value: nested(value, c), dat))
            else:
                self.visit(dat, c)
        nested(ast.value, c)
        return ArrayType(ast.dimens, ast.eleType)
    
    def visitStructLiteral(self, ast, c):
        res = self.lookup(ast.name, self.list_type, lambda x: x.name)
        if res is None:
            raise Undeclared(StaticErrorType(), ast.name) 
        list(map(lambda value: self.visit(value[1], c), ast.elements))
        return res

    def visitNilLiteral(self, ast, c):
        return StructType("", [], [])

    # Evaluate values if needed
    def evaluate(self, node, c):
        if isinstance(node, IntLiteral):
            return int(node.value)
        elif isinstance(node, Id):
            res = next((symbol for scope in c for symbol in scope if symbol.name == node.name), None)
            if res and isinstance(res.value, int):
                return res.value
            raise Undeclared(Identifier(), node.name)
        elif isinstance(node, BinaryOp):
            left = self.evaluate(node.left, c)
            right = self.evaluate(node.right, c)
            if node.op == '+':
                return left + right
            elif node.op == '-':
                return left - right
            elif node.op == '*':
                return left * right
            elif node.op == '/':
                return left // right
            elif node.op == '%':
                return left % right
        elif isinstance(node, UnaryOp):
            operand_value = self.evaluate(node.body, c)
            if node.op == '-':
                return -operand_value
        raise TypeMismatch(node)
