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
