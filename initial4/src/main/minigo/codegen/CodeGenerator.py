from Utils import *
from StaticCheck import *
from StaticError import *
from Emitter import *
from Frame import Frame
from abc import ABC, abstractmethod
from functools import reduce
from Visitor import *
from AST import *

class CodeGenerator(BaseVisitor,Utils):
    def __init__(self):
        self.className = "MiniGoClass"
        self.astTree = None
        self.path = None
        self.emit = None
        self.function = None
        self.list_function = []
        self.arrayCell = None
        self.arrayCellType = None
        self.list_type = {}
        self.struct: StructType = None

    def init(self):
        mem = [
            Symbol("getInt", MType([], VoidType()), CName("io", True)),
            Symbol("putInt", MType([IntType()], VoidType()), CName("io", True)),
            Symbol("putIntLn", MType([IntType()], VoidType()), CName("io", True)),
            Symbol("getFloat", MType([], VoidType()), CName("io", True)),
            Symbol("putFloat", MType([FloatType()], VoidType()), CName("io", True)),
            Symbol("putFloatLn", MType([FloatType()], VoidType()), CName("io", True)),
            Symbol("getBool", MType([], VoidType()), CName("io", True)),
            Symbol("putBool", MType([BoolType()], VoidType()), CName("io", True)),
            Symbol("putBoolLn", MType([BoolType()], VoidType()), CName("io", True)),
            Symbol("getString", MType([], VoidType()), CName("io", True)),
            Symbol("putString", MType([StringType()], VoidType()), CName("io", True)),
            Symbol("putStringLn", MType([StringType()], VoidType()), CName("io", True)),
            Symbol("putLn", MType([], VoidType()), CName("io", True))
        ]
        return mem

    def gen(self, ast, dir_):
        gl = self.init()
        self.astTree = ast
        self.path = dir_
        self.emit = Emitter(dir_ + "/" + self.className + ".j")
        self.visit(ast, gl)

    def emitObjectInit(self):
        frame = Frame("<init>", VoidType())  
        self.emit.printout(self.emit.emitMETHOD("<init>", MType([], VoidType()), False, frame)) 
        frame.enterScope(True) 
        self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame)) 
        self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))  
        self.emit.printout(self.emit.emitENDMETHOD(frame))  
        frame.exitScope()  

    def emitObjectCInit(self, ast, env):
        frame = Frame("<cinit>", VoidType())  
        self.emit.printout(self.emit.emitMETHOD("<clinit>", MType([], VoidType()), True, frame)) 
        frame.enterScope(True)  
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        env['frame'] = frame

        objects = [Assign(Id(item.varName), item.varInit) for item in ast.decl if isinstance(item, VarDecl)] + [Assign(Id(item.conName), item.iniExpr) for item in ast.decl if isinstance(item, ConstDecl)]
        self.visit(Block(objects), env)

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))  
        self.emit.printout(self.emit.emitENDMETHOD(frame))  
        frame.exitScope()

    def visitProgram(self, ast, c):
        self.list_function = c + [Symbol(item.name, MType(list(map(lambda x: x.parType, item.params)), item.retType), CName(self.className)) for item in ast.decl if isinstance(item, FuncDecl)]
        self.list_type = {item.name: item for item in ast.decl if isinstance(item, (StructType, InterfaceType))}        
        
        for decl in ast.decl:
            if isinstance(decl, MethodDecl):
                receiver = decl.recType
                if receiver and isinstance(receiver, Id):
                    struct_name = receiver.name
                    if struct_name in self.list_type and isinstance(self.list_type[struct_name], StructType):
                        self.list_type[struct_name].methods.append(decl)  
                    elif struct_name in self.list_type and isinstance(self.list_type[struct_name], InterfaceType):
                        self.list_type[struct_name].methods.append(decl)

        env = {}
        env['env'] = [c]

        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        env = reduce(lambda a, x: self.visit(x, a) if isinstance(x, VarDecl) or isinstance(x, ConstDecl) else a, ast.decl, env)
        reduce(lambda a, x: self.visit(x, a) if isinstance(x, FuncDecl) else a, ast.decl, env)

        self.emitObjectInit()
        self.emitObjectCInit(ast, env)
        self.emit.printout(self.emit.emitEPILOG())
        
        for item in self.list_type.values():
            if isinstance(item, InterfaceType):
                self.emit = Emitter(self.path + "/" + item.name + ".j")
                self.visit(item, {'env': env['env']})
            elif isinstance(item, StructType):
                self.struct = item
                self.emit = Emitter(self.path + "/" + item.name + ".j")
                self.visit(item, {'env': env['env']})

        return env
    
    def visitFuncDecl(self, ast, o):
        self.function = ast
        frame = Frame(ast.name, ast.retType)
        isMain = ast.name == "main"
        if isMain:
            mtype = MType([ArrayType([None],StringType())], VoidType())
            ast.body = Block([] + ast.body.member)
        else:
            mtype = MType(list(map(lambda x: x.parType, ast.params)), ast.retType)        

        env = o.copy() 
        env['frame'] = frame
        self.emit.printout(self.emit.emitMETHOD(ast.name, mtype,True, frame))
        frame.enterScope(True)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        env['env'] = [[]] + env['env']

        if isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType([None],StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        else:
            env = reduce(lambda acc,e: self.visit(e,acc),ast.params,env)

        self.visit(ast.body, env)
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))

        if type(ast.retType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame)) 
        self.emit.printout(self.emit.emitENDMETHOD(frame))

        frame.exitScope()
        return o

    def visitParamDecl(self, ast, o):
        frame = o['frame']
        index = frame.getNewIndex()
        o['env'][0].append(Symbol(ast.parName, ast.parType, Index(index)))
        self.emit.printout(self.emit.emitVAR(index, ast.parName, ast.parType, frame.getStartLabel() ,frame.getEndLabel(), frame))     
        return o

    def visitVarDecl(self, ast, o):
        def create_init(varType, o):
            if type(varType) is IntType:
                return IntLiteral(0)
            elif type(varType) is FloatType:
                return FloatLiteral(0.0)
            elif type(varType) is StringType:
                return StringLiteral("")
            elif type(varType) is BoolType:
                return BooleanLiteral("false")
            elif type(varType) is ArrayType:                
                def create_array(dimensions, eleType):
                    if len(dimensions) == 1:
                        if type(eleType) is IntType:
                            return [IntLiteral(0) for _ in range(self.evaluate(dimensions[0], o))]
                        elif type(eleType) is FloatType:
                            return [FloatLiteral(0.0) for _ in range(self.evaluate(dimensions[0], o))]
                        elif type(eleType) is StringType:
                            return [StringLiteral("") for _ in range(self.evaluate(dimensions[0], o))]
                        elif type(eleType) is BoolType:
                            return [BooleanLiteral("false") for _ in range(self.evaluate(dimensions[0], o))]
                        elif type(eleType) is Id:
                                structType = self.list_type.get(eleType.name)
                                if structType and isinstance(structType, StructType):
                                    return [StructLiteral(structType.name, list(map(lambda field: (field[0], create_init(field[1], o)), structType.elements))) for _ in range(self.evaluate(dimensions[0], o))]
                                if structType and isinstance(structType, InterfaceType):
                                    return [NilLiteral() for _ in range(self.evaluate(dimensions[0], o))]
                    else:
                        return [create_array(dimensions[1:], eleType) for _ in range(self.evaluate(dimensions[0], o))]

                return ArrayLiteral(varType.dimens, varType.eleType, create_array(varType.dimens, varType.eleType))
            elif type(varType) is Id:
                structType = self.list_type.get(varType.name)
                if structType and isinstance(structType, StructType):
                    return StructLiteral(structType.name, list(map(lambda field: (field[0], create_init(field[1], o)), structType.elements)))
                if structType and isinstance(structType, InterfaceType):
                    return NilLiteral()
                
        varInit = ast.varInit
        varType = ast.varType
        if isinstance(varInit, ArrayLiteral):
            varType = ArrayType(varInit.dimens, varInit.eleType)

        if not varInit:
            varInit = create_init(varType, o)
            if type(varType) is ArrayType:
                if isinstance(varType.eleType, InterfaceType):
                    dimCode = self.emit.emitPUSHCONST(len(varType.dimens[0]), frame)
                    code = dimCode + self.emit.emitMULTIANEWARRAY(varType.eleType.name, frame)
                    self.emit.printout(code)
                else:
                    varInit = ArrayLiteral(varType.dimens, varType.eleType, varInit)
            ast.varInit = varInit

            ast.varInit = varInit
        env = o.copy()
        env['frame'] = Frame("<template_VT>", VoidType()) 

        if isinstance(varInit, ArrayCell):
            rhsCode, rhsType = self.visit(varInit, env)
            varType = rhsType

        rhsCode, rhsType = self.visit(varInit, env)

        if not varType:
            varType = rhsType

        if isinstance(varType, Id):
            structType = self.list_type.get(varType.name)
            if structType and isinstance(structType, StructType):
                varType = structType
            elif structType and isinstance(structType, InterfaceType):
                varType = structType

        if 'frame' not in o:
            o['env'][0].append(Symbol(ast.varName, varType, varInit))
            self.emit.printout(self.emit.emitATTRIBUTE(ast.varName, varType, True, False, None))
        else:
            frame = o['frame']

            index = frame.getNewIndex()
            o['env'][0].append(Symbol(ast.varName, varType, Index(index)))

            self.emit.printout(self.emit.emitVAR(index, ast.varName, varType, frame.getStartLabel(), frame.getEndLabel(), frame))  
            rhsCode, rhsType = self.visit(varInit, o)
            if type(varType) is FloatType and type(rhsType) is IntType:
                rhsCode += self.emit.emitI2F(frame)

            if isinstance(varInit, NilLiteral):
                self.emit.printout(self.emit.emitPUSHNULL(o['frame']))
                self.emit.printout("astore_" + str(index))
                
            self.emit.printout(rhsCode)
            self.emit.printout(self.emit.emitWRITEVAR(ast.varName, varType, index, frame))                   
        return o

    
    def visitFuncCall(self, ast, o):
        sym = next(filter(lambda x: x.name == ast.funName, self.list_function),None)

        if ast.funName == "getInt":
            return self.emit.emitPUSHICONST(1, o['frame']), IntType()
        if ast.funName == "getString":
            return self.emit.emitINVOKESTATIC("io/getString", MType([], StringType()), o['frame']), StringType()
    
        if o.get('stmt'):
            new_o = o.copy()
            new_o['stmt'] = False
            args_code = "".join([self.visit(x, new_o)[0] for x in ast.args])

            self.emit.printout(args_code)
            self.emit.printout(self.emit.emitINVOKESTATIC(f"{sym.value.value}/{ast.funName}",sym.mtype, o['frame']))

            return "", VoidType()
        
        output = "".join([str(self.visit(x, o)[0]) for x in ast.args])
        output += self.emit.emitINVOKESTATIC(f"{sym.value.value}/{ast.funName}", sym.mtype, o['frame'])

        return output, sym.mtype.rettype

    def visitBlock(self, ast, o):
        env = o.copy()
        env['env'] = [[]] + env['env']
        env['frame'].enterScope(False)
        self.emit.printout(self.emit.emitLABEL(o['frame'].getStartLabel(), o['frame']))

        for item in ast.member:
            if type(item) is FuncCall:
                env["stmt"] = True
                self.visit(item, env)
            elif type(item) is MethCall:
                env["stmt"] = True
                self.visit(item, env)
            else:
                env = self.visit(item, env)


        self.emit.printout(self.emit.emitLABEL(o['frame'].getEndLabel(), o['frame']))

        env['frame'].exitScope()
        return o
    
    def visitId(self, ast, o):
        sym = next((x for i in o['env'] for x in i if x.name == ast.name), None)

        if sym is None:
            if o.get('isLeft'):
                return self.emit.emitWRITEVAR("this", ClassType(self.className), 0, o['frame']), Id(self.struct.name)
            return self.emit.emitREADVAR("this", ClassType(self.className), 0, o['frame']), Id(self.struct.name)

        if o.get('isLeft'):
            if type(sym.value) is Index:
                return self.emit.emitWRITEVAR(ast.name, sym.mtype, sym.value.value, o['frame']), sym.mtype
            else:
                return self.emit.emitPUTSTATIC(f"{self.className}/{ast.name}", sym.mtype, o['frame']), sym.mtype
        
        if type(sym.value) is Index:
            return self.emit.emitREADVAR(ast.name, sym.mtype, sym.value.value, o['frame']), sym.mtype
        else:
            return self.emit.emitGETSTATIC(f"{self.className}/{ast.name}", sym.mtype, o['frame']), sym.mtype      

    def visitAssign(self, ast, o):
        if isinstance(ast.lhs, Id) and not next((x for i in o['env'] for x in i if x.name == ast.lhs.name), None):
            return self.visit(VarDecl(ast.lhs.name, None, ast.rhs), o)
    
        rhsCode, rhsType = self.visit(ast.rhs, o)
        o['isLeft'] = True
        lhsCode, lhsType = self.visit(ast.lhs, o)
        o['isLeft'] = False

        if isinstance(lhsType, FloatType) and isinstance(rhsType, IntType):
            rhsCode += self.emit.emitI2F(o['frame'])

        if isinstance(ast.lhs, ArrayCell):
            self.emit.printout(lhsCode)
            self.emit.printout(rhsCode)
            self.emit.printout(self.emit.emitASTORE(self.arrayCellType, o['frame']))
        elif isinstance(ast.lhs, FieldAccess):
            recvCode, recvType = self.visit(ast.lhs.receiver, o)
            if isinstance(recvType, Id):
                recvType = self.list_type[recvType.name]
            fieldName = ast.lhs.field.name if isinstance(ast.lhs.field, Id) else ast.lhs.field
            fieldType = next((ft for fn, ft in recvType.elements if fn == fieldName), None)
            rhsCode, rhsType = self.visit(ast.rhs, o)
            if isinstance(fieldType, FloatType) and isinstance(rhsType, IntType):
                rhsCode += self.emit.emitI2F(o['frame'])
            code = recvCode + rhsCode + self.emit.emitPUTFIELD(f"{recvType.name}/{fieldName}", fieldType, o['frame'])
            self.emit.printout(code)
        else:
            self.emit.printout(rhsCode)
            self.emit.printout(lhsCode)

        return o

    def visitReturn(self, ast, o):
        if ast.expr:
            code, typ = self.visit(ast.expr, o)
            self.emit.printout(code)
            self.emit.printout(self.emit.emitRETURN(typ, o['frame']))
        else:
            self.emit.printout(self.emit.emitRETURN(VoidType(), o['frame']))
        return o

    def visitBinaryOp(self, ast, o):
        op = ast.op
        frame = o['frame']
        codeLeft, typeLeft = self.visit(ast.left, o)
        codeRight, typeRight = self.visit(ast.right, o)

        if op in ['+', '-'] and type(typeLeft) in [FloatType, IntType]:
            typeReturn = IntType() if type(typeLeft) is IntType and type(typeRight) is IntType else FloatType()
            if type(typeReturn) is FloatType:
                if type(typeLeft) is IntType:
                    codeLeft += self.emit.emitI2F(frame)
                if type(typeRight) is IntType:
                    codeRight += self.emit.emitI2F(frame)
            return codeLeft + codeRight + self.emit.emitADDOP(op, typeReturn, frame), typeReturn
        if op in ['*', '/']:
            typeReturn = IntType() if type(typeLeft) is IntType and type(typeRight) is IntType else FloatType()
            if type(typeReturn) is FloatType:
                if type(typeLeft) is IntType:
                    codeLeft += self.emit.emitI2F(frame)
                if type(typeRight) is IntType:
                    codeRight += self.emit.emitI2F(frame)
            return codeLeft + codeRight + self.emit.emitMULOP(op, typeReturn, frame), typeReturn
        if op in ['%']:
            return codeLeft + codeRight + self.emit.emitMOD(frame), IntType()
        if op in ['==', '!=', '<', '>', '>=', '<='] and type(typeLeft) in [FloatType, IntType]:
            return codeLeft + codeRight + self.emit.emitREOP(op, typeLeft, frame), BoolType()  
        if op in ['||']:
            return codeLeft + codeRight + self.emit.emitOROP(frame), BoolType()
        if op in ['&&']:
            return codeLeft + codeRight + self.emit.emitANDOP(frame), BoolType() 

        if op in ['+', '-'] and type(typeLeft) in [StringType]:
            return codeLeft + codeRight + self.emit.emitINVOKEVIRTUAL("java/lang/String/concat", MType([StringType()], StringType()), frame), StringType()
        if op in ['==', '!=', '<', '>', '>=', '<='] and type(typeLeft) in [StringType]:
            code = codeLeft + codeRight + self.emit.emitINVOKEVIRTUAL("java/lang/String/compareTo", MType([StringType()], IntType()), frame)
            code += self.emit.emitPUSHICONST(0, frame)
            code = code + self.emit.emitREOP(op, IntType(), frame)
            return code, BoolType()        
              
    def visitUnaryOp(self, ast, o):
        if ast.op == '!':
            code, type_return = self.visit(ast.body, o)
            return code + self.emit.emitNOT(BoolType(), o['frame']), BoolType()

        if ast.op == '-':
            code, type_return = self.visit(ast.body, o)
            if type(type_return) is IntType:
                return code + self.emit.emitNEGOP(IntType(), o['frame']), IntType()
            if type(type_return) is FloatType:
                return code + self.emit.emitNEGOP(FloatType(), o['frame']), FloatType()


    def visitIntLiteral(self, ast, o):
        return self.emit.emitPUSHICONST(ast.value, o['frame']), IntType()
    
    def visitFloatLiteral(self, ast, o):
        return self.emit.emitPUSHFCONST(ast.value, o['frame']), FloatType()
    
    def visitBooleanLiteral(self, ast, o):
        return self.emit.emitPUSHICONST(ast.value, o['frame']), BoolType()
    
    def visitStringLiteral(self, ast, o):
        return self.emit.emitPUSHCONST(ast.value, StringType(), o['frame']), StringType()
    
    def visitIf(self, ast, o):
        frame = o['frame']
        label_exit = frame.getNewLabel()
        label_end_if = frame.getNewLabel()
        condCode, _ = self.visit(ast.expr, o)
        self.emit.printout(condCode)
        self.emit.printout(self.emit.emitIFFALSE(label_end_if, frame))
        self.visit(ast.thenStmt, o)
        self.emit.printout(self.emit.emitGOTO(label_exit, frame))
        self.emit.printout(self.emit.emitLABEL(label_end_if, frame))

        if ast.elseStmt is not None:
            self.visit(ast.elseStmt, o)
        self.emit.printout(self.emit.emitLABEL(label_exit, frame))
        return o
    
    def visitForBasic(self, ast, o):
        frame = o['frame']
        frame.enterLoop()
        loopStartLabel = frame.getNewLabel()
        breakLabel = frame.getBreakLabel() 
        continueLabel = frame.getContinueLabel()
        self.emit.printout(self.emit.emitLABEL(loopStartLabel, frame))
        self.emit.printout(self.visit(ast.cond, o)[0])
        self.emit.printout(self.emit.emitIFFALSE(breakLabel, frame))
        self.visit(ast.loop, o)
        self.emit.printout(self.emit.emitLABEL(continueLabel, frame))
        self.emit.printout(self.emit.emitGOTO(loopStartLabel, frame))
        self.emit.printout(self.emit.emitLABEL(breakLabel, frame))
        frame.exitLoop()
        return o
        
    def visitForStep(self, ast, o):
        frame = o["frame"]
        frame.enterLoop()
        env = o.copy()
        env['env'] = [[]] + o['env']
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        self.visit(ast.init, env)
        continueLabel = frame.getContinueLabel()
        breakLabel = frame.getBreakLabel()
        loopStartLabel = frame.getNewLabel()
        self.emit.printout(self.emit.emitLABEL(loopStartLabel, frame))
        condCode, condType = self.visit(ast.cond, env)
        self.emit.printout(condCode)
        self.emit.printout(self.emit.emitIFFALSE(breakLabel, frame))
        self.visit(ast.loop, env)
        self.emit.printout(self.emit.emitLABEL(continueLabel, frame))
        self.visit(ast.upda, env)
        self.emit.printout(self.emit.emitGOTO(loopStartLabel, frame))
        self.emit.printout(self.emit.emitLABEL(breakLabel, frame))
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        o['env'].pop()
        frame.exitLoop()
        return o

    def visitForEach(self, ast, o):
        return o

    def visitContinue(self, ast, o):
        self.emit.printout(self.emit.emitGOTO(o['frame'].getContinueLabel(), o['frame']))
        return o

    def visitBreak(self, ast, o):
        self.emit.printout(self.emit.emitGOTO(o['frame'].getBreakLabel(), o['frame']))
        return o

    def visitArrayCell(self, ast, o):
        newO = o.copy()
        newO['isLeft'] = False

        codeGen, arrType = self.visit(ast.arr, newO)

        for idx, item in enumerate(ast.idx):
            codeGen += self.visit(item, newO)[0]
            o['frame'].push()
            if idx != len(ast.idx) - 1:
                codeGen += self.emit.emitALOAD(StringType(), o['frame'])

        if len(arrType.dimens) == len(ast.idx):
            retType = arrType.eleType
            if isinstance(retType, Id):
                retType = self.list_type[retType.name]
            if not o.get('isLeft'):
                codeGen += self.emit.emitALOAD(retType, o['frame'])
            else:
                self.arrayCellType = retType
        else:
            retType = ArrayType(arrType.dimens[len(ast.idx):], self.list_type[arrType.eleType.name] if isinstance(arrType.eleType, Id) else arrType.eleType)
            if not o.get('isLeft'):
                codeGen += self.emit.emitALOAD(retType, o['frame'])
            else:
                self.arrayCellType = retType
        
        return codeGen, retType


    def visitArrayLiteral(self, ast, o):
        def nested2recursive(dat: Union[Literal, list['NestedList']], o: dict) -> tuple[str, Type]:
            
            frame = o['frame']
            
            if not isinstance(dat, list):
                return self.visit(dat, o)

            if not isinstance(dat[0], list):
                _, type_element_array = self.visit(dat[0], o)
                element_type = type_element_array.eleType if isinstance(type_element_array, ArrayType) else type_element_array

                codeGen = self.emit.emitPUSHCONST(len(dat), IntType(), frame)
                if isinstance(element_type, (IntType, FloatType, BoolType, StringType)):
                    codeGen += self.emit.emitNEWARRAY(element_type, frame)
                elif isinstance(element_type, (StructType, InterfaceType)):
                    codeGen += self.emit.emitMULTIANEWARRAY(element_type, frame)
                else:
                    codeGen += self.emit.emitANEWARRAY(element_type, frame)

                for idx, item in enumerate(dat):
                    codeGen += self.emit.emitDUP(frame)
                    codeGen += self.emit.emitPUSHCONST(idx, IntType(), frame)
                    codeItem, typeItem = self.visit(item, o)
                    codeGen += codeItem or ""
                    codeGen += self.emit.emitASTORE(typeItem, frame)

                return codeGen, ArrayType([len(dat)], element_type)

            codeGen = self.emit.emitPUSHCONST(len(dat), IntType(), frame)

            subCode0, subType = nested2recursive(dat[0], o)

            wrapped_type = subType
            codeGen += self.emit.emitANEWARRAY(wrapped_type, frame)

            for idx, sublist in enumerate(dat):
                codeGen += self.emit.emitDUP(frame)
                codeGen += self.emit.emitPUSHCONST(idx, IntType(), frame)
                subCode, _ = nested2recursive(sublist, o)
                codeGen += subCode
                codeGen += self.emit.emitASTORE(wrapped_type, frame)

            return codeGen, ArrayType([len(dat)] + wrapped_type.dimens, wrapped_type.eleType)
        
        if type(ast.value) is ArrayType:
            return self.visit(ast.value, o)

        return nested2recursive(ast.value, o)
    
    def visitArrayType(self, ast, o):
        codeGen = ""
        for dim in ast.dimens:
            dimCode, _ = self.visit(dim, o)
            codeGen += dimCode
        codeGen += self.emit.emitMULTIANEWARRAY(ast, o['frame'])
        return codeGen, ast
    
    def visitConstDecl(self, ast, o):
        if isinstance(ast.iniExpr, BinaryOp) or isinstance(ast.iniExpr, UnaryOp) or isinstance(ast.iniExpr, ArrayCell):
            value = self.evaluate(ast.iniExpr, o)
            ast.iniExpr = IntLiteral(value) if isinstance(value, int) else FloatLiteral(value) if isinstance(value, float) else StringLiteral(value) if isinstance(value, str) else BooleanLiteral(value)
        return self.visit(VarDecl(ast.conName, ast.conType, ast.iniExpr), o)
    
    def evaluate(self, node, o):
        if isinstance(node, IntLiteral):
            return int(node.value)
        elif isinstance(node, FloatLiteral):
            return float(node.value)
        elif isinstance(node, StringLiteral):
            return str(node.value)
        elif isinstance(node, BooleanLiteral):
            return bool(node.value)
        elif isinstance(node, Id):
            res = next((symbol for scope in o['env'] for symbol in scope if symbol.name == node.name), None)
            if res:
                if isinstance(res.value, CName):
                    if hasattr(res, 'mtype') and isinstance(res.mtype, IntType):
                        return int(res.value.value)
                elif isinstance(res.value, int):
                    return res.value
                elif isinstance(res.value, Index):
                    return int(res.value.value)
                elif isinstance(res.value, IntLiteral):
                    return int(res.value.value)
                elif isinstance(res.value, FloatLiteral):
                    return float(res.value.value)
                elif isinstance(res.value, StringLiteral):
                    return str(res.value.value)
                elif isinstance(res.value, BooleanLiteral):
                    return bool(res.value.value)
        elif isinstance(node, BinaryOp):
            left = self.evaluate(node.left, o)
            right = self.evaluate(node.right, o)

            if isinstance(left, str) or isinstance(right, str):
                if isinstance(left, str):
                    left = left.strip('"')
                if isinstance(right, str):
                    right = right.strip('"')
                return f'"{left}{right}"'

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
            operand = self.evaluate(node.body, o)
            if node.op == '-':
                return -operand

        elif isinstance(node, ArrayCell):
            arr = self.evaluate(node.arr, o)
            if isinstance(arr, ArrayLiteral):
                arr = arr.value
            elif isinstance(arr, list):
                pass
            else:
                sym = next((x for i in o['env'] for x in i if x.name == node.arr.name), None)
                if sym and hasattr(sym, 'value'):
                    if isinstance(sym.value, ArrayLiteral):
                        arr = sym.value.value
                    else:
                        arr = sym.value

            indices = [self.evaluate(idx, o) for idx in node.idx]
            
            result = arr
            for idx in indices:
                if isinstance(result, (list, ArrayLiteral)):
                    if isinstance(result, ArrayLiteral):
                        result = result.value
                    result = result[idx]
                else:
                    result = arr[idx]
                    break
                    
            if isinstance(result, ArrayLiteral):
                result = result.value
            
            return result.value

        elif isinstance(node, ArrayLiteral):
            return [self.evaluate(elem, o) if not isinstance(elem, (int, float, str, bool)) else elem for elem in node.value]

    def visitFieldAccess(self, ast, o):
        code, typ = self.visit(ast.receiver, o)
        if isinstance(typ, Id):
            typ = self.list_type[typ.name]
        fieldType = next((fieldType for fieldName, fieldType in typ.elements if fieldName == ast.field), None)

        if o.get('isLeft'):
            code += self.emit.emitDUP(o['frame'])
        
        return code + self.emit.emitGETFIELD(f"{typ.name}/{ast.field}", fieldType, o['frame']), fieldType

    def visitMethodDecl(self, ast, o):
        self.function = ast.fun
        frame = Frame(ast.fun.name, ast.fun.retType)
        mtype = MType(list(map(lambda x: x.parType, ast.fun.params)), ast.fun.retType)
        
        env = o.copy()
        env['frame'] = frame
        self.emit.printout(self.emit.emitMETHOD(ast.fun.name, mtype, False, frame))
        
        frame.enterScope(True)
        self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.struct.name), frame.getStartLabel(), frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        
        if ast.fun.name == "<init>":
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.struct.name), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))

        env['env'] = [[]] + env['env']
        env = reduce(lambda acc, e: self.visit(e, acc), ast.fun.params, env)

        self.visit(ast.fun.body, env)

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(ast.fun.retType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
            
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()
        return o

    def visitMethCall(self, ast, o):
        code, typ = self.visit(ast.receiver, o)

        if isinstance(typ, Id):
            typ = self.list_type.get(typ.name)

        is_stmt = o.pop("stmt", False)

        args_code = ""
        for arg in ast.args:
            arg_code, _ = self.visit(arg, o)
            args_code += arg_code
            o['frame'].push()
        
        code += args_code

        returnType = None
        if isinstance(typ, StructType):
            method = next((m for m in typ.methods if m.fun.name == ast.metName), None)
            mtype = MType([p.parType for p in method.fun.params], method.fun.retType)
            returnType = method.fun.retType
            code += self.emit.emitINVOKEVIRTUAL(f"{typ.name}/{ast.metName}", mtype, o['frame'])
        elif isinstance(typ, InterfaceType):
            method = next((m for m in typ.methods if m.name == ast.metName), None)
            mtype = MType([p for p in method.params], method.retType)
            returnType = method.retType
            code += self.emit.emitINVOKEINTERFACE(f"{typ.name}/{ast.metName}", mtype, o['frame'])
        
        if is_stmt:
            self.emit.printout(code)
            return o

        return code, returnType
    

    def visitStructType(self, ast, o):
        self.emit.printout(self.emit.emitPROLOG(ast.name, "java.lang.Object"))

        for item in self.list_type.values():
            if item.name == ast.name:
                continue
            if self.checkType(item, ast, [(InterfaceType, StructType)]):
                self.emit.printout(f".implements {item.name}\n")

        for item in ast.elements:
            self.emit.printout(self.emit.emitATTRIBUTE(item[0], item[1], False, False, None))

        if ast.elements:
            self.visit(MethodDecl(None, None, FuncDecl("<init>", [ParamDecl(item[0], item[1]) for item in ast.elements], VoidType(), Block([Assign(FieldAccess(Id("this"), Id(item[0])), Id(item[0])) for item in ast.elements]))), o)

        self.visit(MethodDecl(None, None, FuncDecl("<init>", [], VoidType(), Block([]))), o)

        for m in ast.methods:
            self.visit(MethodDecl(ast.name, ast, m.fun), o)

        self.emit.printout(self.emit.emitEPILOG())

    def visitStructLiteral(self, ast, o):
        code = self.emit.emitNEW(ast.name, o['frame'])
        code += self.emit.emitDUP(o['frame'])
        list_type = []
        for item in ast.elements:
            c, t = self.visit(item[1], o)
            code += c
            o['frame'].push()
            list_type.append(t)
        code += self.emit.emitINVOKESPECIAL(o['frame'], f"{ast.name}/<init>", MType(list_type, VoidType()) if len(ast.elements) else MType([], VoidType()))
        return code, Id(ast.name)    

    def visitNilLiteral(self, ast, o):
        return self.emit.emitPUSHNULL(o['frame']), Id("")
    
    def visitInterfaceType(self, ast, o):
        self.emit.printout(f".source {ast.name}.java\n")
        self.emit.printout(f".class public interface {ast.name}\n")
        self.emit.printout(".super java.lang.Object\n")

        for item in ast.methods:
            self.emit.printout(".method public abstract " + item.name + "(")
            for param in item.params:
                self.emit.printout(self.emit.getJVMType(param.parType))
            self.emit.printout(")" + self.emit.getJVMType(item.retType) + "\n")
            self.emit.printout(".end method\n")
        self.emit.printout(self.emit.emitEPILOG())

    def checkType(self, lhsType, rhsType, allowed_types = []):
        if type(rhsType) == StructType and rhsType.name == "":
            return True
        lhsType = self.lookup(lhsType.name, self.list_type, lambda x: x.name) if isinstance(lhsType, Id) else lhsType
        rhsType = self.lookup(rhsType.name, self.list_type, lambda x: x.name) if isinstance(rhsType, Id) else rhsType
        if (type(lhsType), type(rhsType)) in allowed_types:
            if isinstance(lhsType, InterfaceType) and isinstance(rhsType, StructType):
                for method in lhsType.methods:
                    if not any(
                        struct_method.fun.name == method.name and 
                        self.checkType(method.retType, struct_method.fun.retType) and 
                        len(struct_method.fun.params) == len(method.params) and 
                        all(self.checkType(struct_param.parType, method_param)
                            for struct_param, method_param in zip(struct_method.fun.params, method.params))
                        for struct_method in rhsType.methods
                    ):
                        return False
                return True
            return True

        if (isinstance(lhsType, InterfaceType) and isinstance(rhsType, InterfaceType)) or (isinstance(lhsType, StructType) and isinstance(rhsType, StructType)):
            return lhsType.name == rhsType.name

        if isinstance(lhsType, ArrayType) and isinstance(rhsType, ArrayType):
            try:
                lhs_dims = [self.evaluate(dim, [[]]) if not isinstance(dim, int) else dim for dim in lhsType.dimens]
                rhs_dims = [self.evaluate(dim, [[]]) if not isinstance(dim, int) else dim for dim in rhsType.dimens]
            except:
                return False

            return lhs_dims == rhs_dims and lhsType.eleType == rhsType.eleType

        return type(lhsType) == type(rhsType)
