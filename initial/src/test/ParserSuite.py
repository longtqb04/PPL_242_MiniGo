import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: void main() {} """
        input = """func main() {};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))

    def test_more_complex_program(self):
        """More complex program"""
        input = """func foo () {
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))
    
    def test_wrong_miss_close(self):
        """Miss ) void main( {}"""
        input = """func main({};"""
        expect = "Error on line 1 col 11: {"
        self.assertTrue(TestParser.checkParser(input,expect,203))

    def test_wrong_variable(self):
        input = """var int;"""
        expect = "Error on line 1 col 5: int"
        self.assertTrue(TestParser.checkParser(input,expect,204))

    def test_wrong_index(self):
        input = """var i ;"""
        expect = "Error on line 1 col 7: ;"
        self.assertTrue(TestParser.checkParser(input,expect,205))

    def test_206(self):
        """Declared"""
        input = """var x int"""
        expect = "Error on line 1 col 10: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,206))

    def test_207(self):
        """Declared"""
        input = """var x int;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,207))

    def test_208(self):
        """Declared"""
        input = """var x [2][4]float;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,208))

    def test_209(self):
        """Declared"""
        input = """var x [3]int{1, 2, 3};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,209))

    def test_210(self):
        """Declared"""
        input = """var x [4]int{};"""
        expect = "Error on line 1 col 14: }"
        self.assertTrue(TestParser.checkParser(input,expect,210))

    def test_211(self):
        """Declared"""
        input = """var x = 1;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,211))

    def test_212(self):
        """Declared"""
        input = """var x = false;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,212))

    def test_213(self):
        """Declared"""
        input = """var x = [5][0]string{1, \"string\"};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,213))

    def test_214(self):
        """Declared"""
        input = """var x = [2.]ID{1, 4};"""
        expect = "Error on line 1 col 10: 2."
        self.assertTrue(TestParser.checkParser(input,expect,214))

    def test_215(self):
        """Declared"""
        input = """var x = 15 + 3;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,215))

    def test_216(self):
        """Declared"""
        input = """var z int = foo() + 10;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,216))

    def test_217(self):
        """Declared"""
        input = """var z ID = 3.14;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,217))

    def test_218(self):
        """Declared"""
        input = """var z ID = int{1};"""
        expect = "Error on line 1 col 12: int"
        self.assertTrue(TestParser.checkParser(input,expect,218))

    def test_219(self):
        """Declared"""
        input = """var z ID = [true]int{1};"""
        expect = "Error on line 1 col 13: true"
        self.assertTrue(TestParser.checkParser(input,expect,219))

    def test_220(self):
        """Declared"""
        input = """var z ID = [3]int{10, 20, 30};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,220))

    def test_221(self):
        """Declared"""
        input = """const y = 2025;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,221))

    def test_222(self):
        """Declared"""
        input = """const mil = 1.e6;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,222))

    def test_223(self):
        """Declared"""
        input = """const Long = [5][0]string{1, \"string\"};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,223))

    def test_224(self):
        """Declared"""
        input = """const Long = Person{name: \"Alice\", age: 30};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,224))

    def test_225(self):
        """Declared"""
        input = """const Long = [1.]bool{1};"""
        expect = "Error on line 1 col 15: 1."
        self.assertTrue(TestParser.checkParser(input,expect,225))

    def test_226(self):
        """Declared"""
        input = """func factorial(x int) {}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,226))

    def test_227(self):
        """Declared"""
        input = """func add(x int, y int) int {}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,227))

    def test_228(self):
        """Declared"""
        input = """func Table() [2][3] ID {
            // Return a table
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,228))

    def test_229(self):
        """Declared"""
        input = """func pow(x, y int) int {
            /* Return x to the power of y */
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,229))

    def test_230(self):
        """Declared"""
        input = """func reverse(x) {};"""
        expect = "Error on line 1 col 15: )"
        self.assertTrue(TestParser.checkParser(input,expect,230))

    def test_231(self):
        """Declared"""
        input = """func (a Count) Add(x int) int {};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,231))

    def test_232(self):
        """Declared"""
        input = """func (a Count) Add() ID {}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,232))

    def test_233(self):
        """Declared"""
        input = """func (a Count) Plus(x int, y int) int {
            return;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,233))

    def test_234(self):
        """Declared"""
        input = """func (Count) Add(x int) int {};"""
        expect = "Error on line 1 col 12: )"
        self.assertTrue(TestParser.checkParser(input,expect,234))

    def test_235(self):
        """Declared"""
        input = """func (p Person) Greet() string {
            return "Hello, " + p.name
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,235))

    def test_236(self):
        """Declared"""
        input = """type ID struct {}"""
        expect = "Error on line 1 col 17: }"
        self.assertTrue(TestParser.checkParser(input,expect,236))

    def test_237(self):
        """Declared"""
        input = """type Person struct {
            name string;
            age int;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,237))

    def test_238(self):
        """Declared"""
        input = """type ID struct {
            name string;
            list [1][3]ID;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,238))

    def test_239(self):
        """Declared"""
        input = """type int struct {};"""
        expect = "Error on line 1 col 6: int"
        self.assertTrue(TestParser.checkParser(input,expect,239))

    def test_240(self):
        """Declared"""
        input = """type ID struct {
            name string;
            age int;
            score [10.]int;
        }"""
        expect = "Error on line 4 col 20: 10."
        self.assertTrue(TestParser.checkParser(input,expect,240))

    def test_241(self):
        """Declared"""
        input = """type ID interface {}"""
        expect = "Error on line 1 col 20: }"
        self.assertTrue(TestParser.checkParser(input,expect,241))

    def test_242(self):
        """Declared"""
        input = """type Calculator interface {
                                        
            Add(x, y int) int;
            Subtract(a, b float, c int) [3]ID;
            Reset();
                                    
            SayHello(name string);

        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,242))

    def test_243(self):
        """Declared"""
        input = """type int interface {
            Add(x, y int) int;
        };"""
        expect = "Error on line 1 col 6: int"
        self.assertTrue(TestParser.checkParser(input,expect,243))

    def test_244(self):
        """Declared"""
        input = """type ID interface {
            Add() int;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,244))

    def test_245(self):
        """Declared"""
        input = """type ID interface {
            Add() struct;
        };"""
        expect = "Error on line 2 col 19: struct"
        self.assertTrue(TestParser.checkParser(input,expect,245))

    def test_246(self):
        """Expression"""
        input = """var x bool = a || b;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,246))

    def test_247(self):
        """Expression"""
        input = """var x bool = a && b && c;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,247))

    def test_248(self):
        """Expression"""
        input = """var x bool = a1 && b[2] || (c3 || c4);"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,248))

    def test_249(self):
        """Expression"""
        input = """var x bool = a == b;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,249))

    def test_250(self):
        """Expression"""
        input = """var x bool = 10 > 9;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,250))

    def test_251(self):
        """Expression"""
        input = """var x bool = 10 + 2 <= 16 && 13 * 6 != 91;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,251))

    def test_252(self):
        """Expression"""
        input = """var x int = 1 + 11 + 111;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,252))

    def test_253(self):
        """Expression"""
        input = """var x float = 25.6 - 2.56 - 0.256;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,253))

    def test_254(self):
        """Expression"""
        input = """var x int = a + b - c + a.foo() - b[1][3];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,254))

    def test_255(self):
        """Expression"""
        input = """var x int = 12 * 3;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,255))

    def test_256(self):
        """Expression"""
        input = """var x int = a / b / c;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,256))

    def test_257(self):
        """Expression"""
        input = """var x int = (100 + 6) * 3 * 75 - 50 / 25 % 3;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,257))

    def test_258(self):
        """Expression"""
        input = """var x bool = !a || b[12][34] && (c || (d.d.foo() && !e));"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,258))

    def test_259(self):
        """Expression"""
        input = """var x float = -0.067 * 13.0;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,259))

    def test_260(self):
        """Expression"""
        input = """var x int = 0b11 + 0x10;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,260))

    def test_261(self):
        """Expression"""
        input = """var z ID = a >= 2 <= "string" > a[2][3] < ID{A: 2} >= [2]S{2};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,261))

    def test_262(self):
        """Expression"""
        input = """var x = a.a.foo() + a.b.c.d.e;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,262))

    def test_263(self):
        """Expression"""
        input = """var x ID = a[1][2][b + 3 + 5];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,263))

    def test_264(self):
        """Expression"""
        input = """var x ID = a.a.a[2].foo();"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,264))

    def test_265(self):
        """Expression"""
        input = """var x int = 100 + 10 + 1 func Add(x int) {}"""
        expect = "Error on line 1 col 26: func"
        self.assertTrue(TestParser.checkParser(input,expect,265))

    def test_266(self):
        """Statement"""
        input = """func Add() {
            var x int;
            var y int;
            var total = x + y;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,266))

    def test_267(self):
        """Statement"""
        input = """func Add() {
            const a = a[2].b;
            var a = a[2][4].b;
            var a string = "s";
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,267))

    def test_268(self):
        """Statement"""
        input = """func Add() {
            var x int;
            var y int var a string = "s"
        }"""
        expect = "Error on line 3 col 23: var"
        self.assertTrue(TestParser.checkParser(input,expect,268))

    def test_269(self):
        """Statement"""
        input = """func reverse(x, y int) {
            var t int;
            t := x;
            x := y;
            y := t;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,269))

    def test_270(self):
        """Statement"""
        input = """func (c calculator) Add(x int) int {
            c.value += x;
            return c.value;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,270))

    def test_271(self):
        """Statement"""
        input = """func check(x int) {
            if (x >= 50) {
                return "Pass";
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,271))

    def test_272(self):
        """Statement"""
        input = """func check(x int) {
            if (x >= 50) {
                return "Pass";
            } else {
                return "Fail";
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,272))

    def test_273(self):
        """Statement"""
        input = """func check(x int) {
            if (x > 0) {
                return "x is positive";
            }
            else if (x < 0) {
                return "x is negative";
            }
            else {
                return "x = 0";
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,273))

    def test_274(self):
        """Statement"""
        input = """func check(x int) {
            if x >= 50 {
                return "Pass";
            }
        }"""
        expect = "Error on line 2 col 16: x"
        self.assertTrue(TestParser.checkParser(input,expect,274))

    def test_275(self):
        """Statement"""
        input = """func check(x int) {
            if (x >= 50) return "Pass";
        }"""
        expect = "Error on line 2 col 26: return"
        self.assertTrue(TestParser.checkParser(input,expect,275))
