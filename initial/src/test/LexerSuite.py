import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))

    def test_102(self):
        """Identifiers"""
        self.assertTrue(TestLexer.checkLexeme("Abc","Abc,<EOF>",102))

    def test_103(self):
        """Identifiers"""
        self.assertTrue(TestLexer.checkLexeme("a34","a34,<EOF>",103))

    def test_104(self):
        """Identifiers"""
        self.assertTrue(TestLexer.checkLexeme("_PPL","_PPL,<EOF>",104))

    def test_105(self):
        """Identifiers"""
        self.assertTrue(TestLexer.checkLexeme("aP1p3_2","aP1p3_2,<EOF>",105))

    def test_106(self):
        """Identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abcd AbCd","abcd,AbCd,<EOF>",106))

    def test_107(self):
        """Identifiers"""
        self.assertTrue(TestLexer.checkLexeme("c19 d20 e21","c19,d20,e21,<EOF>",107))
    
    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme("ab?sVN","ab,ErrorToken ?",108))

    def test_109(self):
        self.assertTrue(TestLexer.checkLexeme("^","ErrorToken ^",109))

    def test_110(self):
        self.assertTrue(TestLexer.checkLexeme("|","ErrorToken |",110))

    def test_111(self):
        self.assertTrue(TestLexer.checkLexeme(""" "PPL\n" ""","Unclosed string: PPL",111))

    def test_112(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Assignment 1""","Unclosed string: Assignment 1",112))

    def test_113(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Abcde\n\n" ""","Unclosed string: Abcde",113))

    def test_114(self):
        self.assertTrue(TestLexer.checkLexeme(""" "PPL\c" ""","Illegal escape in string: PPL\c",114))

    def test_115(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Full Lexer\\f" ""","Illegal escape in string: Full Lexer\\f",115))

    def test_116(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Assignment\d" ""","Illegal escape in string: Assignment\d",116))

    def test_keyword_var(self):
        """test keyword var"""
        self.assertTrue(TestLexer.checkLexeme("var abc int ;","var,abc,int,;,<EOF>",117))

    def test_keyword_func(self):
        """test keyword func"""
        self.assertTrue(TestLexer.checkLexeme("""func abc ( ) ""","""func,abc,(,),<EOF>""",118))

    def test_119(self):
        """Keywords"""
        self.assertTrue(TestLexer.checkLexeme("int","int,<EOF>",119))

    def test_120(self):
        """Keywords"""
        self.assertTrue(TestLexer.checkLexeme("continue","continue,<EOF>",120))

    def test_121(self):
        """Keywords"""
        self.assertTrue(TestLexer.checkLexeme("else","else,<EOF>",121))

    def test_122(self):
        """Keywords"""
        self.assertTrue(TestLexer.checkLexeme("const","const,<EOF>",122))

    def test_123(self):
        """Keywords"""
        self.assertTrue(TestLexer.checkLexeme("interface","interface,<EOF>",123))

    def test_124(self):
        """Keywords"""
        self.assertTrue(TestLexer.checkLexeme("int float boolean","int,float,boolean,<EOF>",124))

    def test_125(self):
        """Keywords"""
        self.assertTrue(TestLexer.checkLexeme("if else","if,else,<EOF>",125))

    def test_126(self):
        """Keywords"""
        self.assertTrue(TestLexer.checkLexeme("type struct interface","type,struct,interface,<EOF>",126))

    def test_127(self):
        """Keywords"""
        self.assertTrue(TestLexer.checkLexeme("return break continue","return,break,continue,<EOF>",127))

    def test_128(self):
        """Keywords"""
        self.assertTrue(TestLexer.checkLexeme("const a = 2;","const,a,=,2,;,<EOF>",128))

    def test_129(self):
        """Keywords"""
        self.assertTrue(TestLexer.checkLexeme("var x boolean = true","var,x,boolean,=,true,<EOF>",129))

    def test_130(self):
        """Keywords"""
        self.assertTrue(TestLexer.checkLexeme("func add(x, y int)","func,add,(,x,,,y,int,),<EOF>",130))

    def test_131(self):
        """Operators"""
        self.assertTrue(TestLexer.checkLexeme("+","+,<EOF>",131))

    def test_132(self):
        """Operators"""
        self.assertTrue(TestLexer.checkLexeme("+=","+=,<EOF>",132))

    def test_133(self):
        """Operators"""
        self.assertTrue(TestLexer.checkLexeme("%","%,<EOF>",133))

    def test_134(self):
        """Operators"""
        self.assertTrue(TestLexer.checkLexeme("&&","&&,<EOF>",134))

    def test_135(self):
        """Operators"""
        self.assertTrue(TestLexer.checkLexeme(">=",">=,<EOF>",135))

    def test_136(self):
        """Operators"""
        self.assertTrue(TestLexer.checkLexeme("+-*/%","+,-,*,/,%,<EOF>",136))

    def test_137(self):
        """Operators"""
        self.assertTrue(TestLexer.checkLexeme("&&||","&&,||,<EOF>",137))

    def test_138(self):
        """Operators"""
        self.assertTrue(TestLexer.checkLexeme("=./<=","=,.,/,<=,<EOF>",138))

    def test_139(self):
        """Operators"""
        self.assertTrue(TestLexer.checkLexeme(":=+=-=*=/=%=",":=,+=,-=,*=,/=,%=,<EOF>",139))

    def test_140(self):
        """Operators"""
        self.assertTrue(TestLexer.checkLexeme("+:=-","+,:=,-,<EOF>",140))

    def test_141(self):
        """Separators"""
        self.assertTrue(TestLexer.checkLexeme("{","{,<EOF>",141))

    def test_142(self):
        """Separators"""
        self.assertTrue(TestLexer.checkLexeme("]","],<EOF>",142))

    def test_143(self):
        """Separators"""
        self.assertTrue(TestLexer.checkLexeme(";",";,<EOF>",143))

    def test_144(self):
        """Separators"""
        self.assertTrue(TestLexer.checkLexeme("(","(,<EOF>",144))

    def test_145(self):
        """Separators"""
        self.assertTrue(TestLexer.checkLexeme("[]","[,],<EOF>",145))

    def test_146(self):
        """Separators"""
        self.assertTrue(TestLexer.checkLexeme("{}[]()","{,},[,],(,),<EOF>",146))

    def test_147(self):
        """Separators"""
        self.assertTrue(TestLexer.checkLexeme(".{}",".,{,},<EOF>",147))

    def test_148(self):
        """Separators"""
        self.assertTrue(TestLexer.checkLexeme("(.]};","(,.,],},;,<EOF>",148))

    def test_149(self):
        """Separators"""
        self.assertTrue(TestLexer.checkLexeme("foo();","foo,(,),;,<EOF>",149))

    def test_150(self):
        """Separators"""
        self.assertTrue(TestLexer.checkLexeme("a.a.foo()","a,.,a,.,foo,(,),<EOF>",150))

    def test_151(self):
        """Literals INT"""
        self.assertTrue(TestLexer.checkLexeme("1","1,<EOF>",151))

    def test_152(self):
        """Literals INT"""
        self.assertTrue(TestLexer.checkLexeme("0","0,<EOF>",152))

    def test_153(self):
        """Literals INT"""
        self.assertTrue(TestLexer.checkLexeme("12345","12345,<EOF>",153))

    def test_154(self):
        """Literals INT"""
        self.assertTrue(TestLexer.checkLexeme("067","0,67,<EOF>",154))

    def test_155(self):
        """Literals INT"""
        self.assertTrue(TestLexer.checkLexeme("10201","10201,<EOF>",155))

    def test_156(self):
        """Literals INT"""
        self.assertTrue(TestLexer.checkLexeme("33 05 125 00","33,0,5,125,0,0,<EOF>",156))

    def test_157(self):
        """Literals INT"""
        self.assertTrue(TestLexer.checkLexeme("15 + 15 - 15 * 15 / 15","15,+,15,-,15,*,15,/,15,<EOF>",157))

    def test_158(self):
        """Literals INT"""
        self.assertTrue(TestLexer.checkLexeme("05 / 5","0,5,/,5,<EOF>",158))

    def test_159(self):
        """Literals INT"""
        self.assertTrue(TestLexer.checkLexeme("20033002","20033002,<EOF>",159))

    def test_160(self):
        """Literals INT"""
        self.assertTrue(TestLexer.checkLexeme("00056","0,0,0,56,<EOF>",160))

    def test_161(self):
        """Literals FLOAT"""
        self.assertTrue(TestLexer.checkLexeme("1.","1.,<EOF>",161))

    def test_162(self):
        """Literals FLOAT"""
        self.assertTrue(TestLexer.checkLexeme("0.","0.,<EOF>",162))

    def test_163(self):
        """Literals FLOAT"""
        self.assertTrue(TestLexer.checkLexeme("09.","09.,<EOF>",163))

    def test_164(self):
        """Literals FLOAT"""
        self.assertTrue(TestLexer.checkLexeme("382.","382.,<EOF>",164))

    def test_165(self):
        """Literals FLOAT"""
        self.assertTrue(TestLexer.checkLexeme("0156.","0156.,<EOF>",165))

    def test_166(self):
        """Literals FLOAT"""
        self.assertTrue(TestLexer.checkLexeme("1.78","1.78,<EOF>",166))

    def test_167(self):
        """Literals FLOAT"""
        self.assertTrue(TestLexer.checkLexeme("0.34","0.34,<EOF>",167))

    def test_168(self):
        """Literals FLOAT"""
        self.assertTrue(TestLexer.checkLexeme("0.0","0.0,<EOF>",168))

    def test_169(self):
        """Literals FLOAT"""
        self.assertTrue(TestLexer.checkLexeme("1.e9","1.e9,<EOF>",169))

    def test_170(self):
        """Literals FLOAT"""
        self.assertTrue(TestLexer.checkLexeme("2.78e10","2.78e10,<EOF>",170))

    def test_171(self):
        """Literals FLOAT"""
        self.assertTrue(TestLexer.checkLexeme("6.e-23","6.e-23,<EOF>",171))

    def test_172(self):
        """Literals FLOAT"""
        self.assertTrue(TestLexer.checkLexeme("08.e4","08.e4,<EOF>",172))

    def test_173(self):
        """Literals FLOAT"""
        self.assertTrue(TestLexer.checkLexeme("4.e05","4.e05,<EOF>",173))

    def test_174(self):
        """Literals FLOAT"""
        self.assertTrue(TestLexer.checkLexeme("010.010e-010","010.010e-010,<EOF>",174))

    def test_175(self):
        """Literals FLOAT"""
        self.assertTrue(TestLexer.checkLexeme("09.e-002","09.e-002,<EOF>",175))

    def test_176(self):
        """Literals BIN"""
        self.assertTrue(TestLexer.checkLexeme("0b0","0b0,<EOF>",176))

    def test_177(self):
        """Literals BIN"""
        self.assertTrue(TestLexer.checkLexeme("0B111101","0B111101,<EOF>",177))

    def test_178(self):
        """Literals BIN"""
        self.assertTrue(TestLexer.checkLexeme("0b012","0b01,2,<EOF>",178))

    def test_179(self):
        """Literals OCT"""
        self.assertTrue(TestLexer.checkLexeme("0o0","0o0,<EOF>",179))

    def test_180(self):
        """Literals OCT"""
        self.assertTrue(TestLexer.checkLexeme("0O34","0O34,<EOF>",180))

    def test_181(self):
        """Literals OCT"""
        self.assertTrue(TestLexer.checkLexeme("0o0018","0o001,8,<EOF>",181))

    def test_182(self):
        """Literals HEX"""
        self.assertTrue(TestLexer.checkLexeme("0x0","0x0,<EOF>",182))

    def test_183(self):
        """Literals HEX"""
        self.assertTrue(TestLexer.checkLexeme("0X1F","0X1F,<EOF>",183))

    def test_184(self):
        """Literals HEX"""
        self.assertTrue(TestLexer.checkLexeme("0x00CAFE","0x00CAFE,<EOF>",184))

    def test_185(self):
        """Literals BOOLEAN"""
        self.assertTrue(TestLexer.checkLexeme("true","true,<EOF>",185))

    def test_186(self):
        """Literals BOOLEAN"""
        self.assertTrue(TestLexer.checkLexeme("false","false,<EOF>",186))

    def test_187(self):
        """Literals NIL"""
        self.assertTrue(TestLexer.checkLexeme("nil","nil,<EOF>",187))

    def test_188(self):
        """Literals STRING"""
        self.assertTrue(TestLexer.checkLexeme(""" "hello" ""","hello,<EOF>",188))

    def test_189(self):
        """Literals STRING"""
        self.assertTrue(TestLexer.checkLexeme(""" "String with newline"\n ""","String with newline,\n,<EOF>",189))

    def test_190(self):
        """Literals STRING"""
        self.assertTrue(TestLexer.checkLexeme(""" "PPL \\r" ""","PPL \\r,<EOF>",190))

    def test_191(self):
        """Literals STRING"""
        self.assertTrue(TestLexer.checkLexeme(""" "I LOVE YOU 3000 \\t" ""","I LOVE YOU 3000 \\t,<EOF>",191))

    def test_192(self):
        """Literals STRING"""
        self.assertTrue(TestLexer.checkLexeme(""" "\\\"Car\\\"" ""","\\\"Car\\\",<EOF>",192))

    def test_193(self):
        """Skips"""
        self.assertTrue(TestLexer.checkLexeme("\n","\n,<EOF>",193))

    def test_194(self):
        """Skips"""
        self.assertTrue(TestLexer.checkLexeme("\t\r\f","<EOF>",194))

    def test_195(self):
        """Skips"""
        self.assertTrue(TestLexer.checkLexeme("// This is a comment.","<EOF>",195))

    def test_196(self):
        """Skips"""
        self.assertTrue(TestLexer.checkLexeme("/* This is another comment. */","<EOF>",196))

    def test_197(self):
        """Skips"""
        self.assertTrue(TestLexer.checkLexeme("""/*
                                              This is a multi-line comment.
                                              */""","<EOF>",197))

    def test_198(self):
        """Skips"""
        self.assertTrue(TestLexer.checkLexeme("""/*
                                            /* a */ /* b */ 
                                            // 321231
                                            */ if /* */ /* */""","if,<EOF>",198))

    def test_199(self):
        """Skips"""
        self.assertTrue(TestLexer.checkLexeme("/* // a * */","<EOF>",199))

    def test_200(self):
        """Skips"""
        self.assertTrue(TestLexer.checkLexeme("// That's all\n","\n,<EOF>",200))
