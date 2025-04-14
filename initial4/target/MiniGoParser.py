# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3C")
        buf.write("\u0392\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\3\2\7\2\u0094\n\2\f\2")
        buf.write("\16\2\u0097\13\2\3\2\6\2\u009a\n\2\r\2\16\2\u009b\3\2")
        buf.write("\7\2\u009f\n\2\f\2\16\2\u00a2\13\2\3\2\3\2\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\5\3\u00ac\n\3\3\4\3\4\3\4\3\4\5\4\u00b2\n")
        buf.write("\4\3\5\3\5\3\5\5\5\u00b7\n\5\3\5\3\5\5\5\u00bb\n\5\3\6")
        buf.write("\3\6\3\6\3\6\5\6\u00c1\n\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7")
        buf.write("\3\7\5\7\u00cb\n\7\3\b\3\b\3\b\3\b\5\b\u00d1\n\b\3\b\3")
        buf.write("\b\5\b\u00d5\n\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u00df")
        buf.write("\n\t\3\n\3\n\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u00eb")
        buf.write("\n\f\3\r\3\r\3\r\3\r\5\r\u00f1\n\r\3\r\3\r\5\r\u00f5\n")
        buf.write("\r\3\r\3\r\5\r\u00f9\n\r\3\r\5\r\u00fc\n\r\3\r\3\r\3\r")
        buf.write("\3\16\3\16\3\16\3\16\3\16\7\16\u0106\n\16\f\16\16\16\u0109")
        buf.write("\13\16\3\16\3\16\7\16\u010d\n\16\f\16\16\16\u0110\13\16")
        buf.write("\3\16\3\16\3\16\3\17\3\17\5\17\u0117\n\17\3\20\3\20\3")
        buf.write("\20\5\20\u011c\n\20\3\20\3\20\3\20\3\20\3\20\5\20\u0123")
        buf.write("\n\20\3\20\3\20\3\20\5\20\u0128\n\20\3\21\3\21\3\21\3")
        buf.write("\21\3\21\3\21\3\21\3\21\5\21\u0132\n\21\3\21\3\21\5\21")
        buf.write("\u0136\n\21\3\21\3\21\5\21\u013a\n\21\3\21\3\21\3\21\3")
        buf.write("\22\3\22\3\22\3\22\3\22\5\22\u0144\n\22\3\23\3\23\3\23")
        buf.write("\3\24\3\24\5\24\u014b\n\24\3\25\3\25\3\25\3\25\5\25\u0151")
        buf.write("\n\25\3\26\3\26\3\26\3\26\3\26\7\26\u0158\n\26\f\26\16")
        buf.write("\26\u015b\13\26\3\26\3\26\7\26\u015f\n\26\f\26\16\26\u0162")
        buf.write("\13\26\3\26\3\26\3\26\3\27\3\27\3\27\5\27\u016a\n\27\3")
        buf.write("\27\3\27\5\27\u016e\n\27\3\27\3\27\3\27\3\27\5\27\u0174")
        buf.write("\n\27\3\27\3\27\5\27\u0178\n\27\3\27\3\27\3\27\5\27\u017d")
        buf.write("\n\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\5\30\u0187")
        buf.write("\n\30\3\31\3\31\3\31\3\31\3\31\3\31\7\31\u018f\n\31\f")
        buf.write("\31\16\31\u0192\13\31\3\32\3\32\3\32\3\32\3\32\3\32\7")
        buf.write("\32\u019a\n\32\f\32\16\32\u019d\13\32\3\33\3\33\3\33\3")
        buf.write("\33\3\33\3\33\7\33\u01a5\n\33\f\33\16\33\u01a8\13\33\3")
        buf.write("\34\3\34\3\34\3\34\3\34\3\34\7\34\u01b0\n\34\f\34\16\34")
        buf.write("\u01b3\13\34\3\35\3\35\3\35\3\35\3\35\3\35\7\35\u01bb")
        buf.write("\n\35\f\35\16\35\u01be\13\35\3\36\3\36\3\36\5\36\u01c3")
        buf.write("\n\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\5\37\u01cd")
        buf.write("\n\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\7\37")
        buf.write("\u01d8\n\37\f\37\16\37\u01db\13\37\3 \3 \3 \3 \3 \3 \3")
        buf.write(" \5 \u01e4\n \3!\3!\3!\3!\3!\3!\5!\u01ec\n!\3\"\3\"\3")
        buf.write("\"\3\"\3#\3#\3#\3$\3$\3$\3$\3$\5$\u01fa\n$\3%\3%\3%\3")
        buf.write("%\3%\3%\3%\3%\5%\u0204\n%\3&\3&\3&\3&\3&\3&\3&\7&\u020d")
        buf.write("\n&\f&\16&\u0210\13&\3\'\3\'\3(\3(\3)\3)\3*\3*\3*\5*\u021b")
        buf.write("\n*\3*\3*\3+\3+\3+\3+\3+\3+\3+\3+\3+\5+\u0228\n+\3,\3")
        buf.write(",\5,\u022c\n,\3-\3-\3-\3-\3-\5-\u0233\n-\3.\3.\5.\u0237")
        buf.write("\n.\3/\3/\3/\3/\3/\5/\u023e\n/\3\60\3\60\3\60\5\60\u0243")
        buf.write("\n\60\3\60\3\60\3\60\3\60\3\60\7\60\u024a\n\60\f\60\16")
        buf.write("\60\u024d\13\60\3\60\3\60\7\60\u0251\n\60\f\60\16\60\u0254")
        buf.write("\13\60\3\60\3\60\3\60\7\60\u0259\n\60\f\60\16\60\u025c")
        buf.write("\13\60\3\61\3\61\3\61\3\61\5\61\u0262\n\61\3\61\3\61\3")
        buf.write("\61\3\61\7\61\u0268\n\61\f\61\16\61\u026b\13\61\3\61\3")
        buf.write("\61\7\61\u026f\n\61\f\61\16\61\u0272\13\61\3\61\3\61\3")
        buf.write("\61\7\61\u0277\n\61\f\61\16\61\u027a\13\61\3\62\3\62\3")
        buf.write("\62\7\62\u027f\n\62\f\62\16\62\u0282\13\62\3\62\3\62\7")
        buf.write("\62\u0286\n\62\f\62\16\62\u0289\13\62\3\62\3\62\3\62\7")
        buf.write("\62\u028e\n\62\f\62\16\62\u0291\13\62\3\63\3\63\3\63\3")
        buf.write("\63\5\63\u0297\n\63\3\63\3\63\3\63\3\64\3\64\5\64\u029e")
        buf.write("\n\64\3\65\3\65\3\65\5\65\u02a3\n\65\3\65\3\65\5\65\u02a7")
        buf.write("\n\65\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\5\66\u02b1")
        buf.write("\n\66\3\67\3\67\5\67\u02b5\n\67\38\38\38\58\u02ba\n8\3")
        buf.write("8\38\58\u02be\n8\39\39\39\39\39\39\39\39\59\u02c8\n9\3")
        buf.write(":\3:\3;\3;\3;\3;\5;\u02d0\n;\3;\3;\5;\u02d4\n;\3<\3<\3")
        buf.write("<\3<\3<\3=\3=\3=\3=\5=\u02df\n=\3>\3>\3>\3>\5>\u02e5\n")
        buf.write(">\3?\3?\3?\3?\3?\3?\3?\3?\3?\3?\3?\7?\u02f2\n?\f?\16?")
        buf.write("\u02f5\13?\3@\3@\3@\3@\3@\3@\7@\u02fd\n@\f@\16@\u0300")
        buf.write("\13@\3@\3@\7@\u0304\n@\f@\16@\u0307\13@\3@\3@\7@\u030b")
        buf.write("\n@\f@\16@\u030e\13@\3@\3@\7@\u0312\n@\f@\16@\u0315\13")
        buf.write("@\3@\7@\u0318\n@\f@\16@\u031b\13@\3@\7@\u031e\n@\f@\16")
        buf.write("@\u0321\13@\3@\5@\u0324\n@\3A\3A\3A\3A\3A\3A\3A\7A\u032d")
        buf.write("\nA\fA\16A\u0330\13A\3A\3A\7A\u0334\nA\fA\16A\u0337\13")
        buf.write("A\3A\3A\7A\u033b\nA\fA\16A\u033e\13A\3A\3A\3B\3B\7B\u0344")
        buf.write("\nB\fB\16B\u0347\13B\3B\3B\7B\u034b\nB\fB\16B\u034e\13")
        buf.write("B\3B\3B\7B\u0352\nB\fB\16B\u0355\13B\3B\3B\3C\3C\3C\5")
        buf.write("C\u035c\nC\3D\3D\3D\3E\3E\3E\3F\3F\3F\5F\u0367\nF\3F\3")
        buf.write("F\3F\5F\u036c\nF\3F\3F\3F\3F\7F\u0372\nF\fF\16F\u0375")
        buf.write("\13F\3G\3G\3G\5G\u037a\nG\3G\3G\3H\3H\3H\3H\5H\u0382\n")
        buf.write("H\3I\3I\7I\u0386\nI\fI\16I\u0389\13I\3I\6I\u038c\nI\r")
        buf.write("I\16I\u038d\5I\u0390\nI\3I\2\t\60\62\64\668<|J\2\4\6\b")
        buf.write("\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668")
        buf.write(":<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084")
        buf.write("\u0086\u0088\u008a\u008c\u008e\u0090\2\13\4\2\13\16\66")
        buf.write("\66\3\2\13\16\4\2\65\65==\3\2\34!\3\2\27\30\3\2\31\33")
        buf.write("\4\2\30\30$$\3\2\66\67\3\2&+\2\u03db\2\u0095\3\2\2\2\4")
        buf.write("\u00ab\3\2\2\2\6\u00b1\3\2\2\2\b\u00b6\3\2\2\2\n\u00bc")
        buf.write("\3\2\2\2\f\u00c5\3\2\2\2\16\u00cc\3\2\2\2\20\u00de\3\2")
        buf.write("\2\2\22\u00e0\3\2\2\2\24\u00e2\3\2\2\2\26\u00e4\3\2\2")
        buf.write("\2\30\u00ec\3\2\2\2\32\u0100\3\2\2\2\34\u0114\3\2\2\2")
        buf.write("\36\u0127\3\2\2\2 \u0129\3\2\2\2\"\u0143\3\2\2\2$\u0145")
        buf.write("\3\2\2\2&\u014a\3\2\2\2(\u0150\3\2\2\2*\u0152\3\2\2\2")
        buf.write(",\u017c\3\2\2\2.\u0186\3\2\2\2\60\u0188\3\2\2\2\62\u0193")
        buf.write("\3\2\2\2\64\u019e\3\2\2\2\66\u01a9\3\2\2\28\u01b4\3\2")
        buf.write("\2\2:\u01c2\3\2\2\2<\u01c4\3\2\2\2>\u01e3\3\2\2\2@\u01e5")
        buf.write("\3\2\2\2B\u01ed\3\2\2\2D\u01f1\3\2\2\2F\u01f9\3\2\2\2")
        buf.write("H\u0203\3\2\2\2J\u0205\3\2\2\2L\u0211\3\2\2\2N\u0213\3")
        buf.write("\2\2\2P\u0215\3\2\2\2R\u0217\3\2\2\2T\u0227\3\2\2\2V\u0229")
        buf.write("\3\2\2\2X\u0232\3\2\2\2Z\u0234\3\2\2\2\\\u023d\3\2\2\2")
        buf.write("^\u023f\3\2\2\2`\u025d\3\2\2\2b\u027b\3\2\2\2d\u0292\3")
        buf.write("\2\2\2f\u029b\3\2\2\2h\u02a6\3\2\2\2j\u02b0\3\2\2\2l\u02b2")
        buf.write("\3\2\2\2n\u02bd\3\2\2\2p\u02c7\3\2\2\2r\u02c9\3\2\2\2")
        buf.write("t\u02cf\3\2\2\2v\u02d5\3\2\2\2x\u02da\3\2\2\2z\u02e0\3")
        buf.write("\2\2\2|\u02e6\3\2\2\2~\u02f6\3\2\2\2\u0080\u0325\3\2\2")
        buf.write("\2\u0082\u0341\3\2\2\2\u0084\u035b\3\2\2\2\u0086\u035d")
        buf.write("\3\2\2\2\u0088\u0360\3\2\2\2\u008a\u0366\3\2\2\2\u008c")
        buf.write("\u0376\3\2\2\2\u008e\u0381\3\2\2\2\u0090\u038f\3\2\2\2")
        buf.write("\u0092\u0094\7=\2\2\u0093\u0092\3\2\2\2\u0094\u0097\3")
        buf.write("\2\2\2\u0095\u0093\3\2\2\2\u0095\u0096\3\2\2\2\u0096\u0099")
        buf.write("\3\2\2\2\u0097\u0095\3\2\2\2\u0098\u009a\5\4\3\2\u0099")
        buf.write("\u0098\3\2\2\2\u009a\u009b\3\2\2\2\u009b\u0099\3\2\2\2")
        buf.write("\u009b\u009c\3\2\2\2\u009c\u00a0\3\2\2\2\u009d\u009f\7")
        buf.write("=\2\2\u009e\u009d\3\2\2\2\u009f\u00a2\3\2\2\2\u00a0\u009e")
        buf.write("\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\u00a3\3\2\2\2\u00a2")
        buf.write("\u00a0\3\2\2\2\u00a3\u00a4\7\2\2\3\u00a4\3\3\2\2\2\u00a5")
        buf.write("\u00ac\5\b\5\2\u00a6\u00ac\5\26\f\2\u00a7\u00ac\5\6\4")
        buf.write("\2\u00a8\u00ac\5 \21\2\u00a9\u00ac\5\32\16\2\u00aa\u00ac")
        buf.write("\5*\26\2\u00ab\u00a5\3\2\2\2\u00ab\u00a6\3\2\2\2\u00ab")
        buf.write("\u00a7\3\2\2\2\u00ab\u00a8\3\2\2\2\u00ab\u00a9\3\2\2\2")
        buf.write("\u00ab\u00aa\3\2\2\2\u00ac\5\3\2\2\2\u00ad\u00b2\5\30")
        buf.write("\r\2\u00ae\u00af\5\b\5\2\u00af\u00b0\5\u0090I\2\u00b0")
        buf.write("\u00b2\3\2\2\2\u00b1\u00ad\3\2\2\2\u00b1\u00ae\3\2\2\2")
        buf.write("\u00b2\7\3\2\2\2\u00b3\u00b7\5\n\6\2\u00b4\u00b7\5\16")
        buf.write("\b\2\u00b5\u00b7\5\f\7\2\u00b6\u00b3\3\2\2\2\u00b6\u00b4")
        buf.write("\3\2\2\2\u00b6\u00b5\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8")
        buf.write("\u00ba\7\65\2\2\u00b9\u00bb\5\u0090I\2\u00ba\u00b9\3\2")
        buf.write("\2\2\u00ba\u00bb\3\2\2\2\u00bb\t\3\2\2\2\u00bc\u00bd\7")
        buf.write("\20\2\2\u00bd\u00c0\7\66\2\2\u00be\u00c1\5\24\13\2\u00bf")
        buf.write("\u00c1\5@!\2\u00c0\u00be\3\2\2\2\u00c0\u00bf\3\2\2\2\u00c0")
        buf.write("\u00c1\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2\u00c3\7%\2\2")
        buf.write("\u00c3\u00c4\5\60\31\2\u00c4\13\3\2\2\2\u00c5\u00c6\7")
        buf.write("\20\2\2\u00c6\u00c7\7\66\2\2\u00c7\u00ca\7\66\2\2\u00c8")
        buf.write("\u00c9\7%\2\2\u00c9\u00cb\5\60\31\2\u00ca\u00c8\3\2\2")
        buf.write("\2\u00ca\u00cb\3\2\2\2\u00cb\r\3\2\2\2\u00cc\u00cd\7\20")
        buf.write("\2\2\u00cd\u00d0\7\66\2\2\u00ce\u00d1\5\24\13\2\u00cf")
        buf.write("\u00d1\5@!\2\u00d0\u00ce\3\2\2\2\u00d0\u00cf\3\2\2\2\u00d1")
        buf.write("\u00d4\3\2\2\2\u00d2\u00d3\7%\2\2\u00d3\u00d5\5\60\31")
        buf.write("\2\u00d4\u00d2\3\2\2\2\u00d4\u00d5\3\2\2\2\u00d5\17\3")
        buf.write("\2\2\2\u00d6\u00df\7\67\2\2\u00d7\u00d8\7\67\2\2\u00d8")
        buf.write("\u00d9\7\64\2\2\u00d9\u00df\5\20\t\2\u00da\u00df\78\2")
        buf.write("\2\u00db\u00dc\78\2\2\u00dc\u00dd\7\64\2\2\u00dd\u00df")
        buf.write("\5\20\t\2\u00de\u00d6\3\2\2\2\u00de\u00d7\3\2\2\2\u00de")
        buf.write("\u00da\3\2\2\2\u00de\u00db\3\2\2\2\u00df\21\3\2\2\2\u00e0")
        buf.write("\u00e1\t\2\2\2\u00e1\23\3\2\2\2\u00e2\u00e3\t\3\2\2\u00e3")
        buf.write("\25\3\2\2\2\u00e4\u00e5\7\17\2\2\u00e5\u00e6\7\66\2\2")
        buf.write("\u00e6\u00e7\7%\2\2\u00e7\u00e8\5\60\31\2\u00e8\u00ea")
        buf.write("\t\4\2\2\u00e9\u00eb\5\u0090I\2\u00ea\u00e9\3\2\2\2\u00ea")
        buf.write("\u00eb\3\2\2\2\u00eb\27\3\2\2\2\u00ec\u00ed\7\7\2\2\u00ed")
        buf.write("\u00ee\7\66\2\2\u00ee\u00f0\7.\2\2\u00ef\u00f1\5\"\22")
        buf.write("\2\u00f0\u00ef\3\2\2\2\u00f0\u00f1\3\2\2\2\u00f1\u00f2")
        buf.write("\3\2\2\2\u00f2\u00f4\7/\2\2\u00f3\u00f5\5&\24\2\u00f4")
        buf.write("\u00f3\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5\u00f6\3\2\2\2")
        buf.write("\u00f6\u00f8\7\62\2\2\u00f7\u00f9\5\u0090I\2\u00f8\u00f7")
        buf.write("\3\2\2\2\u00f8\u00f9\3\2\2\2\u00f9\u00fb\3\2\2\2\u00fa")
        buf.write("\u00fc\5l\67\2\u00fb\u00fa\3\2\2\2\u00fb\u00fc\3\2\2\2")
        buf.write("\u00fc\u00fd\3\2\2\2\u00fd\u00fe\7\63\2\2\u00fe\u00ff")
        buf.write("\5\u0090I\2\u00ff\31\3\2\2\2\u0100\u0101\7\b\2\2\u0101")
        buf.write("\u0102\7\66\2\2\u0102\u0103\7\t\2\2\u0103\u0107\7\62\2")
        buf.write("\2\u0104\u0106\5\u0090I\2\u0105\u0104\3\2\2\2\u0106\u0109")
        buf.write("\3\2\2\2\u0107\u0105\3\2\2\2\u0107\u0108\3\2\2\2\u0108")
        buf.write("\u010a\3\2\2\2\u0109\u0107\3\2\2\2\u010a\u010e\5\34\17")
        buf.write("\2\u010b\u010d\5\u0090I\2\u010c\u010b\3\2\2\2\u010d\u0110")
        buf.write("\3\2\2\2\u010e\u010c\3\2\2\2\u010e\u010f\3\2\2\2\u010f")
        buf.write("\u0111\3\2\2\2\u0110\u010e\3\2\2\2\u0111\u0112\7\63\2")
        buf.write("\2\u0112\u0113\5\u0090I\2\u0113\33\3\2\2\2\u0114\u0116")
        buf.write("\5\36\20\2\u0115\u0117\5\u0090I\2\u0116\u0115\3\2\2\2")
        buf.write("\u0116\u0117\3\2\2\2\u0117\35\3\2\2\2\u0118\u011b\7\66")
        buf.write("\2\2\u0119\u011c\5\22\n\2\u011a\u011c\5@!\2\u011b\u0119")
        buf.write("\3\2\2\2\u011b\u011a\3\2\2\2\u011c\u011d\3\2\2\2\u011d")
        buf.write("\u011e\5\u0090I\2\u011e\u0128\3\2\2\2\u011f\u0122\7\66")
        buf.write("\2\2\u0120\u0123\5\22\n\2\u0121\u0123\5@!\2\u0122\u0120")
        buf.write("\3\2\2\2\u0122\u0121\3\2\2\2\u0123\u0124\3\2\2\2\u0124")
        buf.write("\u0125\5\u0090I\2\u0125\u0126\5\36\20\2\u0126\u0128\3")
        buf.write("\2\2\2\u0127\u0118\3\2\2\2\u0127\u011f\3\2\2\2\u0128\37")
        buf.write("\3\2\2\2\u0129\u012a\7\7\2\2\u012a\u012b\7.\2\2\u012b")
        buf.write("\u012c\7\66\2\2\u012c\u012d\7\66\2\2\u012d\u012e\7/\2")
        buf.write("\2\u012e\u012f\7\66\2\2\u012f\u0131\7.\2\2\u0130\u0132")
        buf.write("\5\"\22\2\u0131\u0130\3\2\2\2\u0131\u0132\3\2\2\2\u0132")
        buf.write("\u0133\3\2\2\2\u0133\u0135\7/\2\2\u0134\u0136\5&\24\2")
        buf.write("\u0135\u0134\3\2\2\2\u0135\u0136\3\2\2\2\u0136\u0137\3")
        buf.write("\2\2\2\u0137\u0139\7\62\2\2\u0138\u013a\5f\64\2\u0139")
        buf.write("\u0138\3\2\2\2\u0139\u013a\3\2\2\2\u013a\u013b\3\2\2\2")
        buf.write("\u013b\u013c\7\63\2\2\u013c\u013d\5\u0090I\2\u013d!\3")
        buf.write("\2\2\2\u013e\u0144\5$\23\2\u013f\u0140\5$\23\2\u0140\u0141")
        buf.write("\7\64\2\2\u0141\u0142\5\"\22\2\u0142\u0144\3\2\2\2\u0143")
        buf.write("\u013e\3\2\2\2\u0143\u013f\3\2\2\2\u0144#\3\2\2\2\u0145")
        buf.write("\u0146\5(\25\2\u0146\u0147\5&\24\2\u0147%\3\2\2\2\u0148")
        buf.write("\u014b\5\22\n\2\u0149\u014b\5@!\2\u014a\u0148\3\2\2\2")
        buf.write("\u014a\u0149\3\2\2\2\u014b\'\3\2\2\2\u014c\u0151\7\66")
        buf.write("\2\2\u014d\u014e\7\66\2\2\u014e\u014f\7\64\2\2\u014f\u0151")
        buf.write("\5(\25\2\u0150\u014c\3\2\2\2\u0150\u014d\3\2\2\2\u0151")
        buf.write(")\3\2\2\2\u0152\u0153\7\b\2\2\u0153\u0154\7\66\2\2\u0154")
        buf.write("\u0155\7\n\2\2\u0155\u0159\7\62\2\2\u0156\u0158\5\u0090")
        buf.write("I\2\u0157\u0156\3\2\2\2\u0158\u015b\3\2\2\2\u0159\u0157")
        buf.write("\3\2\2\2\u0159\u015a\3\2\2\2\u015a\u015c\3\2\2\2\u015b")
        buf.write("\u0159\3\2\2\2\u015c\u0160\5,\27\2\u015d\u015f\5\u0090")
        buf.write("I\2\u015e\u015d\3\2\2\2\u015f\u0162\3\2\2\2\u0160\u015e")
        buf.write("\3\2\2\2\u0160\u0161\3\2\2\2\u0161\u0163\3\2\2\2\u0162")
        buf.write("\u0160\3\2\2\2\u0163\u0164\7\63\2\2\u0164\u0165\5\u0090")
        buf.write("I\2\u0165+\3\2\2\2\u0166\u0167\7\66\2\2\u0167\u0169\7")
        buf.write(".\2\2\u0168\u016a\5\"\22\2\u0169\u0168\3\2\2\2\u0169\u016a")
        buf.write("\3\2\2\2\u016a\u016b\3\2\2\2\u016b\u016d\7/\2\2\u016c")
        buf.write("\u016e\5&\24\2\u016d\u016c\3\2\2\2\u016d\u016e\3\2\2\2")
        buf.write("\u016e\u016f\3\2\2\2\u016f\u017d\5\u0090I\2\u0170\u0171")
        buf.write("\7\66\2\2\u0171\u0173\7.\2\2\u0172\u0174\5\"\22\2\u0173")
        buf.write("\u0172\3\2\2\2\u0173\u0174\3\2\2\2\u0174\u0175\3\2\2\2")
        buf.write("\u0175\u0177\7/\2\2\u0176\u0178\5&\24\2\u0177\u0176\3")
        buf.write("\2\2\2\u0177\u0178\3\2\2\2\u0178\u0179\3\2\2\2\u0179\u017a")
        buf.write("\5\u0090I\2\u017a\u017b\5,\27\2\u017b\u017d\3\2\2\2\u017c")
        buf.write("\u0166\3\2\2\2\u017c\u0170\3\2\2\2\u017d-\3\2\2\2\u017e")
        buf.write("\u0187\7\67\2\2\u017f\u0187\78\2\2\u0180\u0187\7<\2\2")
        buf.write("\u0181\u0187\7\25\2\2\u0182\u0187\7\26\2\2\u0183\u0187")
        buf.write("\7\24\2\2\u0184\u0187\5@!\2\u0185\u0187\5R*\2\u0186\u017e")
        buf.write("\3\2\2\2\u0186\u017f\3\2\2\2\u0186\u0180\3\2\2\2\u0186")
        buf.write("\u0181\3\2\2\2\u0186\u0182\3\2\2\2\u0186\u0183\3\2\2\2")
        buf.write("\u0186\u0184\3\2\2\2\u0186\u0185\3\2\2\2\u0187/\3\2\2")
        buf.write("\2\u0188\u0189\b\31\1\2\u0189\u018a\5\62\32\2\u018a\u0190")
        buf.write("\3\2\2\2\u018b\u018c\f\4\2\2\u018c\u018d\7#\2\2\u018d")
        buf.write("\u018f\5\62\32\2\u018e\u018b\3\2\2\2\u018f\u0192\3\2\2")
        buf.write("\2\u0190\u018e\3\2\2\2\u0190\u0191\3\2\2\2\u0191\61\3")
        buf.write("\2\2\2\u0192\u0190\3\2\2\2\u0193\u0194\b\32\1\2\u0194")
        buf.write("\u0195\5\64\33\2\u0195\u019b\3\2\2\2\u0196\u0197\f\4\2")
        buf.write("\2\u0197\u0198\7\"\2\2\u0198\u019a\5\64\33\2\u0199\u0196")
        buf.write("\3\2\2\2\u019a\u019d\3\2\2\2\u019b\u0199\3\2\2\2\u019b")
        buf.write("\u019c\3\2\2\2\u019c\63\3\2\2\2\u019d\u019b\3\2\2\2\u019e")
        buf.write("\u019f\b\33\1\2\u019f\u01a0\5\66\34\2\u01a0\u01a6\3\2")
        buf.write("\2\2\u01a1\u01a2\f\4\2\2\u01a2\u01a3\t\5\2\2\u01a3\u01a5")
        buf.write("\5\66\34\2\u01a4\u01a1\3\2\2\2\u01a5\u01a8\3\2\2\2\u01a6")
        buf.write("\u01a4\3\2\2\2\u01a6\u01a7\3\2\2\2\u01a7\65\3\2\2\2\u01a8")
        buf.write("\u01a6\3\2\2\2\u01a9\u01aa\b\34\1\2\u01aa\u01ab\58\35")
        buf.write("\2\u01ab\u01b1\3\2\2\2\u01ac\u01ad\f\4\2\2\u01ad\u01ae")
        buf.write("\t\6\2\2\u01ae\u01b0\58\35\2\u01af\u01ac\3\2\2\2\u01b0")
        buf.write("\u01b3\3\2\2\2\u01b1\u01af\3\2\2\2\u01b1\u01b2\3\2\2\2")
        buf.write("\u01b2\67\3\2\2\2\u01b3\u01b1\3\2\2\2\u01b4\u01b5\b\35")
        buf.write("\1\2\u01b5\u01b6\5:\36\2\u01b6\u01bc\3\2\2\2\u01b7\u01b8")
        buf.write("\f\4\2\2\u01b8\u01b9\t\7\2\2\u01b9\u01bb\5:\36\2\u01ba")
        buf.write("\u01b7\3\2\2\2\u01bb\u01be\3\2\2\2\u01bc\u01ba\3\2\2\2")
        buf.write("\u01bc\u01bd\3\2\2\2\u01bd9\3\2\2\2\u01be\u01bc\3\2\2")
        buf.write("\2\u01bf\u01c0\t\b\2\2\u01c0\u01c3\5:\36\2\u01c1\u01c3")
        buf.write("\5<\37\2\u01c2\u01bf\3\2\2\2\u01c2\u01c1\3\2\2\2\u01c3")
        buf.write(";\3\2\2\2\u01c4\u01c5\b\37\1\2\u01c5\u01c6\5> \2\u01c6")
        buf.write("\u01d9\3\2\2\2\u01c7\u01c8\f\6\2\2\u01c8\u01c9\7,\2\2")
        buf.write("\u01c9\u01ca\7\66\2\2\u01ca\u01cc\7.\2\2\u01cb\u01cd\5")
        buf.write("X-\2\u01cc\u01cb\3\2\2\2\u01cc\u01cd\3\2\2\2\u01cd\u01ce")
        buf.write("\3\2\2\2\u01ce\u01d8\7/\2\2\u01cf\u01d0\f\5\2\2\u01d0")
        buf.write("\u01d1\7\60\2\2\u01d1\u01d2\5\60\31\2\u01d2\u01d3\7\61")
        buf.write("\2\2\u01d3\u01d8\3\2\2\2\u01d4\u01d5\f\4\2\2\u01d5\u01d6")
        buf.write("\7,\2\2\u01d6\u01d8\7\66\2\2\u01d7\u01c7\3\2\2\2\u01d7")
        buf.write("\u01cf\3\2\2\2\u01d7\u01d4\3\2\2\2\u01d8\u01db\3\2\2\2")
        buf.write("\u01d9\u01d7\3\2\2\2\u01d9\u01da\3\2\2\2\u01da=\3\2\2")
        buf.write("\2\u01db\u01d9\3\2\2\2\u01dc\u01e4\5.\30\2\u01dd\u01e4")
        buf.write("\7\66\2\2\u01de\u01df\7.\2\2\u01df\u01e0\5\60\31\2\u01e0")
        buf.write("\u01e1\7/\2\2\u01e1\u01e4\3\2\2\2\u01e2\u01e4\5\u008c")
        buf.write("G\2\u01e3\u01dc\3\2\2\2\u01e3\u01dd\3\2\2\2\u01e3\u01de")
        buf.write("\3\2\2\2\u01e3\u01e2\3\2\2\2\u01e4?\3\2\2\2\u01e5\u01e6")
        buf.write("\5J&\2\u01e6\u01eb\5N(\2\u01e7\u01e8\7\62\2\2\u01e8\u01e9")
        buf.write("\5F$\2\u01e9\u01ea\7\63\2\2\u01ea\u01ec\3\2\2\2\u01eb")
        buf.write("\u01e7\3\2\2\2\u01eb\u01ec\3\2\2\2\u01ecA\3\2\2\2\u01ed")
        buf.write("\u01ee\7\62\2\2\u01ee\u01ef\5F$\2\u01ef\u01f0\7\63\2\2")
        buf.write("\u01f0C\3\2\2\2\u01f1\u01f2\5J&\2\u01f2\u01f3\5N(\2\u01f3")
        buf.write("E\3\2\2\2\u01f4\u01fa\5H%\2\u01f5\u01f6\5H%\2\u01f6\u01f7")
        buf.write("\7\64\2\2\u01f7\u01f8\5F$\2\u01f8\u01fa\3\2\2\2\u01f9")
        buf.write("\u01f4\3\2\2\2\u01f9\u01f5\3\2\2\2\u01faG\3\2\2\2\u01fb")
        buf.write("\u0204\7\67\2\2\u01fc\u0204\78\2\2\u01fd\u0204\7<\2\2")
        buf.write("\u01fe\u0204\7\25\2\2\u01ff\u0204\7\26\2\2\u0200\u0204")
        buf.write("\7\24\2\2\u0201\u0204\5B\"\2\u0202\u0204\5R*\2\u0203\u01fb")
        buf.write("\3\2\2\2\u0203\u01fc\3\2\2\2\u0203\u01fd\3\2\2\2\u0203")
        buf.write("\u01fe\3\2\2\2\u0203\u01ff\3\2\2\2\u0203\u0200\3\2\2\2")
        buf.write("\u0203\u0201\3\2\2\2\u0203\u0202\3\2\2\2\u0204I\3\2\2")
        buf.write("\2\u0205\u0206\7\60\2\2\u0206\u0207\5L\'\2\u0207\u020e")
        buf.write("\7\61\2\2\u0208\u0209\7\60\2\2\u0209\u020a\5L\'\2\u020a")
        buf.write("\u020b\7\61\2\2\u020b\u020d\3\2\2\2\u020c\u0208\3\2\2")
        buf.write("\2\u020d\u0210\3\2\2\2\u020e\u020c\3\2\2\2\u020e\u020f")
        buf.write("\3\2\2\2\u020fK\3\2\2\2\u0210\u020e\3\2\2\2\u0211\u0212")
        buf.write("\t\t\2\2\u0212M\3\2\2\2\u0213\u0214\t\2\2\2\u0214O\3\2")
        buf.write("\2\2\u0215\u0216\t\3\2\2\u0216Q\3\2\2\2\u0217\u0218\7")
        buf.write("\66\2\2\u0218\u021a\7\62\2\2\u0219\u021b\5T+\2\u021a\u0219")
        buf.write("\3\2\2\2\u021a\u021b\3\2\2\2\u021b\u021c\3\2\2\2\u021c")
        buf.write("\u021d\7\63\2\2\u021dS\3\2\2\2\u021e\u021f\7\66\2\2\u021f")
        buf.write("\u0220\7-\2\2\u0220\u0228\5\60\31\2\u0221\u0222\7\66\2")
        buf.write("\2\u0222\u0223\7-\2\2\u0223\u0224\5\60\31\2\u0224\u0225")
        buf.write("\7\64\2\2\u0225\u0226\5T+\2\u0226\u0228\3\2\2\2\u0227")
        buf.write("\u021e\3\2\2\2\u0227\u0221\3\2\2\2\u0228U\3\2\2\2\u0229")
        buf.write("\u022b\5X-\2\u022a\u022c\5\u0090I\2\u022b\u022a\3\2\2")
        buf.write("\2\u022b\u022c\3\2\2\2\u022cW\3\2\2\2\u022d\u0233\5\60")
        buf.write("\31\2\u022e\u022f\5\60\31\2\u022f\u0230\7\64\2\2\u0230")
        buf.write("\u0231\5X-\2\u0231\u0233\3\2\2\2\u0232\u022d\3\2\2\2\u0232")
        buf.write("\u022e\3\2\2\2\u0233Y\3\2\2\2\u0234\u0236\5\\/\2\u0235")
        buf.write("\u0237\5\u0090I\2\u0236\u0235\3\2\2\2\u0236\u0237\3\2")
        buf.write("\2\2\u0237[\3\2\2\2\u0238\u023e\5\60\31\2\u0239\u023a")
        buf.write("\5\60\31\2\u023a\u023b\5\u0090I\2\u023b\u023c\5\\/\2\u023c")
        buf.write("\u023e\3\2\2\2\u023d\u0238\3\2\2\2\u023d\u0239\3\2\2\2")
        buf.write("\u023e]\3\2\2\2\u023f\u0242\7\5\2\2\u0240\u0243\5d\63")
        buf.write("\2\u0241\u0243\5z>\2\u0242\u0240\3\2\2\2\u0242\u0241\3")
        buf.write("\2\2\2\u0243\u0244\3\2\2\2\u0244\u0245\7\65\2\2\u0245")
        buf.write("\u0246\5\60\31\2\u0246\u0247\7\65\2\2\u0247\u024b\5z>")
        buf.write("\2\u0248\u024a\5\u0090I\2\u0249\u0248\3\2\2\2\u024a\u024d")
        buf.write("\3\2\2\2\u024b\u0249\3\2\2\2\u024b\u024c\3\2\2\2\u024c")
        buf.write("\u024e\3\2\2\2\u024d\u024b\3\2\2\2\u024e\u0252\7\62\2")
        buf.write("\2\u024f\u0251\5\u0090I\2\u0250\u024f\3\2\2\2\u0251\u0254")
        buf.write("\3\2\2\2\u0252\u0250\3\2\2\2\u0252\u0253\3\2\2\2\u0253")
        buf.write("\u0255\3\2\2\2\u0254\u0252\3\2\2\2\u0255\u0256\5f\64\2")
        buf.write("\u0256\u025a\7\63\2\2\u0257\u0259\5\u0090I\2\u0258\u0257")
        buf.write("\3\2\2\2\u0259\u025c\3\2\2\2\u025a\u0258\3\2\2\2\u025a")
        buf.write("\u025b\3\2\2\2\u025b_\3\2\2\2\u025c\u025a\3\2\2\2\u025d")
        buf.write("\u025e\7\5\2\2\u025e\u0261\7\66\2\2\u025f\u0260\7\64\2")
        buf.write("\2\u0260\u0262\7\66\2\2\u0261\u025f\3\2\2\2\u0261\u0262")
        buf.write("\3\2\2\2\u0262\u0263\3\2\2\2\u0263\u0264\7&\2\2\u0264")
        buf.write("\u0265\7\23\2\2\u0265\u0269\5\60\31\2\u0266\u0268\5\u0090")
        buf.write("I\2\u0267\u0266\3\2\2\2\u0268\u026b\3\2\2\2\u0269\u0267")
        buf.write("\3\2\2\2\u0269\u026a\3\2\2\2\u026a\u026c\3\2\2\2\u026b")
        buf.write("\u0269\3\2\2\2\u026c\u0270\7\62\2\2\u026d\u026f\5\u0090")
        buf.write("I\2\u026e\u026d\3\2\2\2\u026f\u0272\3\2\2\2\u0270\u026e")
        buf.write("\3\2\2\2\u0270\u0271\3\2\2\2\u0271\u0273\3\2\2\2\u0272")
        buf.write("\u0270\3\2\2\2\u0273\u0274\5f\64\2\u0274\u0278\7\63\2")
        buf.write("\2\u0275\u0277\5\u0090I\2\u0276\u0275\3\2\2\2\u0277\u027a")
        buf.write("\3\2\2\2\u0278\u0276\3\2\2\2\u0278\u0279\3\2\2\2\u0279")
        buf.write("a\3\2\2\2\u027a\u0278\3\2\2\2\u027b\u027c\7\5\2\2\u027c")
        buf.write("\u0280\5\60\31\2\u027d\u027f\5\u0090I\2\u027e\u027d\3")
        buf.write("\2\2\2\u027f\u0282\3\2\2\2\u0280\u027e\3\2\2\2\u0280\u0281")
        buf.write("\3\2\2\2\u0281\u0283\3\2\2\2\u0282\u0280\3\2\2\2\u0283")
        buf.write("\u0287\7\62\2\2\u0284\u0286\5\u0090I\2\u0285\u0284\3\2")
        buf.write("\2\2\u0286\u0289\3\2\2\2\u0287\u0285\3\2\2\2\u0287\u0288")
        buf.write("\3\2\2\2\u0288\u028a\3\2\2\2\u0289\u0287\3\2\2\2\u028a")
        buf.write("\u028b\5f\64\2\u028b\u028f\7\63\2\2\u028c\u028e\5\u0090")
        buf.write("I\2\u028d\u028c\3\2\2\2\u028e\u0291\3\2\2\2\u028f\u028d")
        buf.write("\3\2\2\2\u028f\u0290\3\2\2\2\u0290c\3\2\2\2\u0291\u028f")
        buf.write("\3\2\2\2\u0292\u0293\7\20\2\2\u0293\u0296\7\66\2\2\u0294")
        buf.write("\u0297\5\24\13\2\u0295\u0297\5@!\2\u0296\u0294\3\2\2\2")
        buf.write("\u0296\u0295\3\2\2\2\u0296\u0297\3\2\2\2\u0297\u0298\3")
        buf.write("\2\2\2\u0298\u0299\7%\2\2\u0299\u029a\5\60\31\2\u029a")
        buf.write("e\3\2\2\2\u029b\u029d\5h\65\2\u029c\u029e\5\u0090I\2\u029d")
        buf.write("\u029c\3\2\2\2\u029d\u029e\3\2\2\2\u029eg\3\2\2\2\u029f")
        buf.write("\u02a7\5j\66\2\u02a0\u02a2\5j\66\2\u02a1\u02a3\5\u0090")
        buf.write("I\2\u02a2\u02a1\3\2\2\2\u02a2\u02a3\3\2\2\2\u02a3\u02a4")
        buf.write("\3\2\2\2\u02a4\u02a5\5h\65\2\u02a5\u02a7\3\2\2\2\u02a6")
        buf.write("\u029f\3\2\2\2\u02a6\u02a0\3\2\2\2\u02a7i\3\2\2\2\u02a8")
        buf.write("\u02b1\5r:\2\u02a9\u02b1\5x=\2\u02aa\u02b1\5~@\2\u02ab")
        buf.write("\u02b1\5\u0084C\2\u02ac\u02b1\5\u0086D\2\u02ad\u02b1\5")
        buf.write("\u0088E\2\u02ae\u02b1\5\u008aF\2\u02af\u02b1\5\u008eH")
        buf.write("\2\u02b0\u02a8\3\2\2\2\u02b0\u02a9\3\2\2\2\u02b0\u02aa")
        buf.write("\3\2\2\2\u02b0\u02ab\3\2\2\2\u02b0\u02ac\3\2\2\2\u02b0")
        buf.write("\u02ad\3\2\2\2\u02b0\u02ae\3\2\2\2\u02b0\u02af\3\2\2\2")
        buf.write("\u02b1k\3\2\2\2\u02b2\u02b4\5n8\2\u02b3\u02b5\5\u0090")
        buf.write("I\2\u02b4\u02b3\3\2\2\2\u02b4\u02b5\3\2\2\2\u02b5m\3\2")
        buf.write("\2\2\u02b6\u02be\5p9\2\u02b7\u02b9\5p9\2\u02b8\u02ba\5")
        buf.write("\u0090I\2\u02b9\u02b8\3\2\2\2\u02b9\u02ba\3\2\2\2\u02ba")
        buf.write("\u02bb\3\2\2\2\u02bb\u02bc\5n8\2\u02bc\u02be\3\2\2\2\u02bd")
        buf.write("\u02b6\3\2\2\2\u02bd\u02b7\3\2\2\2\u02beo\3\2\2\2\u02bf")
        buf.write("\u02c8\5t;\2\u02c0\u02c8\5x=\2\u02c1\u02c8\5~@\2\u02c2")
        buf.write("\u02c8\5\u0084C\2\u02c3\u02c8\5\u0086D\2\u02c4\u02c8\5")
        buf.write("\u0088E\2\u02c5\u02c8\5\u008aF\2\u02c6\u02c8\5\u008eH")
        buf.write("\2\u02c7\u02bf\3\2\2\2\u02c7\u02c0\3\2\2\2\u02c7\u02c1")
        buf.write("\3\2\2\2\u02c7\u02c2\3\2\2\2\u02c7\u02c3\3\2\2\2\u02c7")
        buf.write("\u02c4\3\2\2\2\u02c7\u02c5\3\2\2\2\u02c7\u02c6\3\2\2\2")
        buf.write("\u02c8q\3\2\2\2\u02c9\u02ca\5\b\5\2\u02cas\3\2\2\2\u02cb")
        buf.write("\u02d0\5v<\2\u02cc\u02d0\5\n\6\2\u02cd\u02d0\5\16\b\2")
        buf.write("\u02ce\u02d0\5\f\7\2\u02cf\u02cb\3\2\2\2\u02cf\u02cc\3")
        buf.write("\2\2\2\u02cf\u02cd\3\2\2\2\u02cf\u02ce\3\2\2\2\u02d0\u02d1")
        buf.write("\3\2\2\2\u02d1\u02d3\t\4\2\2\u02d2\u02d4\5\u0090I\2\u02d3")
        buf.write("\u02d2\3\2\2\2\u02d3\u02d4\3\2\2\2\u02d4u\3\2\2\2\u02d5")
        buf.write("\u02d6\7\17\2\2\u02d6\u02d7\7\66\2\2\u02d7\u02d8\7%\2")
        buf.write("\2\u02d8\u02d9\5\60\31\2\u02d9w\3\2\2\2\u02da\u02db\5")
        buf.write("|?\2\u02db\u02dc\t\n\2\2\u02dc\u02de\5\60\31\2\u02dd\u02df")
        buf.write("\5\u0090I\2\u02de\u02dd\3\2\2\2\u02de\u02df\3\2\2\2\u02df")
        buf.write("y\3\2\2\2\u02e0\u02e1\7\66\2\2\u02e1\u02e2\t\n\2\2\u02e2")
        buf.write("\u02e4\5\60\31\2\u02e3\u02e5\5\u0090I\2\u02e4\u02e3\3")
        buf.write("\2\2\2\u02e4\u02e5\3\2\2\2\u02e5{\3\2\2\2\u02e6\u02e7")
        buf.write("\b?\1\2\u02e7\u02e8\7\66\2\2\u02e8\u02f3\3\2\2\2\u02e9")
        buf.write("\u02ea\f\4\2\2\u02ea\u02eb\7,\2\2\u02eb\u02f2\7\66\2\2")
        buf.write("\u02ec\u02ed\f\3\2\2\u02ed\u02ee\7\60\2\2\u02ee\u02ef")
        buf.write("\5\60\31\2\u02ef\u02f0\7\61\2\2\u02f0\u02f2\3\2\2\2\u02f1")
        buf.write("\u02e9\3\2\2\2\u02f1\u02ec\3\2\2\2\u02f2\u02f5\3\2\2\2")
        buf.write("\u02f3\u02f1\3\2\2\2\u02f3\u02f4\3\2\2\2\u02f4}\3\2\2")
        buf.write("\2\u02f5\u02f3\3\2\2\2\u02f6\u02f7\7\3\2\2\u02f7\u02f8")
        buf.write("\7.\2\2\u02f8\u02f9\5\60\31\2\u02f9\u02fa\7/\2\2\u02fa")
        buf.write("\u02fe\3\2\2\2\u02fb\u02fd\5\u0090I\2\u02fc\u02fb\3\2")
        buf.write("\2\2\u02fd\u0300\3\2\2\2\u02fe\u02fc\3\2\2\2\u02fe\u02ff")
        buf.write("\3\2\2\2\u02ff\u0301\3\2\2\2\u0300\u02fe\3\2\2\2\u0301")
        buf.write("\u0305\7\62\2\2\u0302\u0304\5\u0090I\2\u0303\u0302\3\2")
        buf.write("\2\2\u0304\u0307\3\2\2\2\u0305\u0303\3\2\2\2\u0305\u0306")
        buf.write("\3\2\2\2\u0306\u0308\3\2\2\2\u0307\u0305\3\2\2\2\u0308")
        buf.write("\u030c\5f\64\2\u0309\u030b\5\u0090I\2\u030a\u0309\3\2")
        buf.write("\2\2\u030b\u030e\3\2\2\2\u030c\u030a\3\2\2\2\u030c\u030d")
        buf.write("\3\2\2\2\u030d\u030f\3\2\2\2\u030e\u030c\3\2\2\2\u030f")
        buf.write("\u0313\7\63\2\2\u0310\u0312\5\u0090I\2\u0311\u0310\3\2")
        buf.write("\2\2\u0312\u0315\3\2\2\2\u0313\u0311\3\2\2\2\u0313\u0314")
        buf.write("\3\2\2\2\u0314\u0319\3\2\2\2\u0315\u0313\3\2\2\2\u0316")
        buf.write("\u0318\5\u0080A\2\u0317\u0316\3\2\2\2\u0318\u031b\3\2")
        buf.write("\2\2\u0319\u0317\3\2\2\2\u0319\u031a\3\2\2\2\u031a\u031f")
        buf.write("\3\2\2\2\u031b\u0319\3\2\2\2\u031c\u031e\5\u0090I\2\u031d")
        buf.write("\u031c\3\2\2\2\u031e\u0321\3\2\2\2\u031f\u031d\3\2\2\2")
        buf.write("\u031f\u0320\3\2\2\2\u0320\u0323\3\2\2\2\u0321\u031f\3")
        buf.write("\2\2\2\u0322\u0324\5\u0082B\2\u0323\u0322\3\2\2\2\u0323")
        buf.write("\u0324\3\2\2\2\u0324\177\3\2\2\2\u0325\u0326\7\4\2\2\u0326")
        buf.write("\u0327\7\3\2\2\u0327\u0328\7.\2\2\u0328\u0329\5\60\31")
        buf.write("\2\u0329\u032a\7/\2\2\u032a\u032e\3\2\2\2\u032b\u032d")
        buf.write("\5\u0090I\2\u032c\u032b\3\2\2\2\u032d\u0330\3\2\2\2\u032e")
        buf.write("\u032c\3\2\2\2\u032e\u032f\3\2\2\2\u032f\u0331\3\2\2\2")
        buf.write("\u0330\u032e\3\2\2\2\u0331\u0335\7\62\2\2\u0332\u0334")
        buf.write("\5\u0090I\2\u0333\u0332\3\2\2\2\u0334\u0337\3\2\2\2\u0335")
        buf.write("\u0333\3\2\2\2\u0335\u0336\3\2\2\2\u0336\u0338\3\2\2\2")
        buf.write("\u0337\u0335\3\2\2\2\u0338\u033c\5f\64\2\u0339\u033b\5")
        buf.write("\u0090I\2\u033a\u0339\3\2\2\2\u033b\u033e\3\2\2\2\u033c")
        buf.write("\u033a\3\2\2\2\u033c\u033d\3\2\2\2\u033d\u033f\3\2\2\2")
        buf.write("\u033e\u033c\3\2\2\2\u033f\u0340\7\63\2\2\u0340\u0081")
        buf.write("\3\2\2\2\u0341\u0345\7\4\2\2\u0342\u0344\5\u0090I\2\u0343")
        buf.write("\u0342\3\2\2\2\u0344\u0347\3\2\2\2\u0345\u0343\3\2\2\2")
        buf.write("\u0345\u0346\3\2\2\2\u0346\u0348\3\2\2\2\u0347\u0345\3")
        buf.write("\2\2\2\u0348\u034c\7\62\2\2\u0349\u034b\5\u0090I\2\u034a")
        buf.write("\u0349\3\2\2\2\u034b\u034e\3\2\2\2\u034c\u034a\3\2\2\2")
        buf.write("\u034c\u034d\3\2\2\2\u034d\u034f\3\2\2\2\u034e\u034c\3")
        buf.write("\2\2\2\u034f\u0353\5f\64\2\u0350\u0352\5\u0090I\2\u0351")
        buf.write("\u0350\3\2\2\2\u0352\u0355\3\2\2\2\u0353\u0351\3\2\2\2")
        buf.write("\u0353\u0354\3\2\2\2\u0354\u0356\3\2\2\2\u0355\u0353\3")
        buf.write("\2\2\2\u0356\u0357\7\63\2\2\u0357\u0083\3\2\2\2\u0358")
        buf.write("\u035c\5b\62\2\u0359\u035c\5^\60\2\u035a\u035c\5`\61\2")
        buf.write("\u035b\u0358\3\2\2\2\u035b\u0359\3\2\2\2\u035b\u035a\3")
        buf.write("\2\2\2\u035c\u0085\3\2\2\2\u035d\u035e\7\22\2\2\u035e")
        buf.write("\u035f\5\u0090I\2\u035f\u0087\3\2\2\2\u0360\u0361\7\21")
        buf.write("\2\2\u0361\u0362\5\u0090I\2\u0362\u0089\3\2\2\2\u0363")
        buf.write("\u0364\5|?\2\u0364\u0365\7,\2\2\u0365\u0367\3\2\2\2\u0366")
        buf.write("\u0363\3\2\2\2\u0366\u0367\3\2\2\2\u0367\u0368\3\2\2\2")
        buf.write("\u0368\u0369\7\66\2\2\u0369\u036b\7.\2\2\u036a\u036c\5")
        buf.write("V,\2\u036b\u036a\3\2\2\2\u036b\u036c\3\2\2\2\u036c\u036d")
        buf.write("\3\2\2\2\u036d\u0373\7/\2\2\u036e\u0372\7\65\2\2\u036f")
        buf.write("\u0372\7=\2\2\u0370\u0372\5\u0090I\2\u0371\u036e\3\2\2")
        buf.write("\2\u0371\u036f\3\2\2\2\u0371\u0370\3\2\2\2\u0372\u0375")
        buf.write("\3\2\2\2\u0373\u0371\3\2\2\2\u0373\u0374\3\2\2\2\u0374")
        buf.write("\u008b\3\2\2\2\u0375\u0373\3\2\2\2\u0376\u0377\7\66\2")
        buf.write("\2\u0377\u0379\7.\2\2\u0378\u037a\5V,\2\u0379\u0378\3")
        buf.write("\2\2\2\u0379\u037a\3\2\2\2\u037a\u037b\3\2\2\2\u037b\u037c")
        buf.write("\7/\2\2\u037c\u008d\3\2\2\2\u037d\u037e\7\6\2\2\u037e")
        buf.write("\u0382\5\u0090I\2\u037f\u0380\7\6\2\2\u0380\u0382\5\60")
        buf.write("\31\2\u0381\u037d\3\2\2\2\u0381\u037f\3\2\2\2\u0382\u008f")
        buf.write("\3\2\2\2\u0383\u0387\7\65\2\2\u0384\u0386\7=\2\2\u0385")
        buf.write("\u0384\3\2\2\2\u0386\u0389\3\2\2\2\u0387\u0385\3\2\2\2")
        buf.write("\u0387\u0388\3\2\2\2\u0388\u0390\3\2\2\2\u0389\u0387\3")
        buf.write("\2\2\2\u038a\u038c\7=\2\2\u038b\u038a\3\2\2\2\u038c\u038d")
        buf.write("\3\2\2\2\u038d\u038b\3\2\2\2\u038d\u038e\3\2\2\2\u038e")
        buf.write("\u0390\3\2\2\2\u038f\u0383\3\2\2\2\u038f\u038b\3\2\2\2")
        buf.write("\u0390\u0091\3\2\2\2l\u0095\u009b\u00a0\u00ab\u00b1\u00b6")
        buf.write("\u00ba\u00c0\u00ca\u00d0\u00d4\u00de\u00ea\u00f0\u00f4")
        buf.write("\u00f8\u00fb\u0107\u010e\u0116\u011b\u0122\u0127\u0131")
        buf.write("\u0135\u0139\u0143\u014a\u0150\u0159\u0160\u0169\u016d")
        buf.write("\u0173\u0177\u017c\u0186\u0190\u019b\u01a6\u01b1\u01bc")
        buf.write("\u01c2\u01cc\u01d7\u01d9\u01e3\u01eb\u01f9\u0203\u020e")
        buf.write("\u021a\u0227\u022b\u0232\u0236\u023d\u0242\u024b\u0252")
        buf.write("\u025a\u0261\u0269\u0270\u0278\u0280\u0287\u028f\u0296")
        buf.write("\u029d\u02a2\u02a6\u02b0\u02b4\u02b9\u02bd\u02c7\u02cf")
        buf.write("\u02d3\u02de\u02e4\u02f1\u02f3\u02fe\u0305\u030c\u0313")
        buf.write("\u0319\u031f\u0323\u032e\u0335\u033c\u0345\u034c\u0353")
        buf.write("\u035b\u0366\u036b\u0371\u0373\u0379\u0381\u0387\u038d")
        buf.write("\u038f")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'for'", "'return'", 
                     "'func'", "'type'", "'struct'", "'interface'", "'string'", 
                     "'int'", "'float'", "'boolean'", "'const'", "'var'", 
                     "'continue'", "'break'", "'range'", "'nil'", "'true'", 
                     "'false'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
                     "'!='", "'<'", "'>'", "'<='", "'>='", "'&&'", "'||'", 
                     "'!'", "'='", "':='", "'+='", "'-='", "'*='", "'/='", 
                     "'%='", "'.'", "':'", "'('", "')'", "'['", "']'", "'{'", 
                     "'}'", "','", "';'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "FOR", "RETURN", "FUNCTION", 
                      "TYPE", "STRUCT", "INTERFACE", "STRING", "INTEGER", 
                      "FLOAT", "BOOLEAN", "CONSTANT", "VARIABLE", "CONTINUE", 
                      "BREAK", "RANGE", "NIL", "TRUE", "FALSE", "ADD", "SUB", 
                      "MUL", "DIV", "MOD", "EQ", "NEQ", "LT", "GT", "LEQ", 
                      "GEQ", "AND", "OR", "NOT", "ASSIGN", "ASSIGN_VAR", 
                      "ASSIGN_ADD", "ASSIGN_SUB", "ASSIGN_MUL", "ASSIGN_DIV", 
                      "ASSIGN_MOD", "DOT", "COLON", "LP", "RP", "SLP", "SRP", 
                      "CLP", "CRP", "COMMA", "SEMICOLON", "ID", "INT_LIT", 
                      "FLOAT_LIT", "BIN", "OCT", "HEX", "STRING_LIT", "NEWLINE", 
                      "LINE_COMMENT", "BLOCK_COMMENT", "WS", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_declared = 1
    RULE_function_declared = 2
    RULE_variables_declared = 3
    RULE_inferred_var = 4
    RULE_struct_variable_declared = 5
    RULE_keyword_type_var = 6
    RULE_list_number_lit = 7
    RULE_type_key = 8
    RULE_type_key_variable = 9
    RULE_constants_declared = 10
    RULE_function = 11
    RULE_struct_declared = 12
    RULE_struct_variable_list = 13
    RULE_struct_variable_list_recur = 14
    RULE_method_declared = 15
    RULE_list_parameters = 16
    RULE_parameter = 17
    RULE_parameter_type = 18
    RULE_list_ID = 19
    RULE_interface_declared = 20
    RULE_list_para_interface = 21
    RULE_literal = 22
    RULE_expression = 23
    RULE_expression1 = 24
    RULE_expression2 = 25
    RULE_expression3 = 26
    RULE_expression4 = 27
    RULE_expression5 = 28
    RULE_expression6 = 29
    RULE_expression7 = 30
    RULE_array_literal = 31
    RULE_array_element_set = 32
    RULE_array_literal_declare = 33
    RULE_array_elements = 34
    RULE_valid_element = 35
    RULE_dimensions = 36
    RULE_cell_type = 37
    RULE_type_literal = 38
    RULE_type_literal_except_struct = 39
    RULE_struct_literal = 40
    RULE_struct_literal_recur = 41
    RULE_index_operators = 42
    RULE_index_operators_recur = 43
    RULE_argument_list = 44
    RULE_argument_list_recur = 45
    RULE_for_step = 46
    RULE_for_each = 47
    RULE_for_basic = 48
    RULE_variables_declared_for = 49
    RULE_list_statement = 50
    RULE_list_statement_recur = 51
    RULE_statement = 52
    RULE_list_statement_in_function = 53
    RULE_list_statement_in_function_recur = 54
    RULE_statement_in_function = 55
    RULE_declared_statement = 56
    RULE_declared_statement_no_ignore = 57
    RULE_constants_declared_in_function = 58
    RULE_assign_statement = 59
    RULE_assign_statement_for = 60
    RULE_lhs = 61
    RULE_if_statement = 62
    RULE_elif_statement = 63
    RULE_else_statement = 64
    RULE_for_statement = 65
    RULE_break_statement = 66
    RULE_continue_statement = 67
    RULE_call_statement = 68
    RULE_function_call = 69
    RULE_return_statement = 70
    RULE_ignore = 71

    ruleNames =  [ "program", "declared", "function_declared", "variables_declared", 
                   "inferred_var", "struct_variable_declared", "keyword_type_var", 
                   "list_number_lit", "type_key", "type_key_variable", "constants_declared", 
                   "function", "struct_declared", "struct_variable_list", 
                   "struct_variable_list_recur", "method_declared", "list_parameters", 
                   "parameter", "parameter_type", "list_ID", "interface_declared", 
                   "list_para_interface", "literal", "expression", "expression1", 
                   "expression2", "expression3", "expression4", "expression5", 
                   "expression6", "expression7", "array_literal", "array_element_set", 
                   "array_literal_declare", "array_elements", "valid_element", 
                   "dimensions", "cell_type", "type_literal", "type_literal_except_struct", 
                   "struct_literal", "struct_literal_recur", "index_operators", 
                   "index_operators_recur", "argument_list", "argument_list_recur", 
                   "for_step", "for_each", "for_basic", "variables_declared_for", 
                   "list_statement", "list_statement_recur", "statement", 
                   "list_statement_in_function", "list_statement_in_function_recur", 
                   "statement_in_function", "declared_statement", "declared_statement_no_ignore", 
                   "constants_declared_in_function", "assign_statement", 
                   "assign_statement_for", "lhs", "if_statement", "elif_statement", 
                   "else_statement", "for_statement", "break_statement", 
                   "continue_statement", "call_statement", "function_call", 
                   "return_statement", "ignore" ]

    EOF = Token.EOF
    IF=1
    ELSE=2
    FOR=3
    RETURN=4
    FUNCTION=5
    TYPE=6
    STRUCT=7
    INTERFACE=8
    STRING=9
    INTEGER=10
    FLOAT=11
    BOOLEAN=12
    CONSTANT=13
    VARIABLE=14
    CONTINUE=15
    BREAK=16
    RANGE=17
    NIL=18
    TRUE=19
    FALSE=20
    ADD=21
    SUB=22
    MUL=23
    DIV=24
    MOD=25
    EQ=26
    NEQ=27
    LT=28
    GT=29
    LEQ=30
    GEQ=31
    AND=32
    OR=33
    NOT=34
    ASSIGN=35
    ASSIGN_VAR=36
    ASSIGN_ADD=37
    ASSIGN_SUB=38
    ASSIGN_MUL=39
    ASSIGN_DIV=40
    ASSIGN_MOD=41
    DOT=42
    COLON=43
    LP=44
    RP=45
    SLP=46
    SRP=47
    CLP=48
    CRP=49
    COMMA=50
    SEMICOLON=51
    ID=52
    INT_LIT=53
    FLOAT_LIT=54
    BIN=55
    OCT=56
    HEX=57
    STRING_LIT=58
    NEWLINE=59
    LINE_COMMENT=60
    BLOCK_COMMENT=61
    WS=62
    ERROR_CHAR=63
    UNCLOSE_STRING=64
    ILLEGAL_ESCAPE=65

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NEWLINE)
            else:
                return self.getToken(MiniGoParser.NEWLINE, i)

        def declared(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.DeclaredContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.DeclaredContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.NEWLINE:
                self.state = 144
                self.match(MiniGoParser.NEWLINE)
                self.state = 149
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 151 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 150
                self.declared()
                self.state = 153 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.FUNCTION) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONSTANT) | (1 << MiniGoParser.VARIABLE))) != 0)):
                    break

            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.NEWLINE:
                self.state = 155
                self.match(MiniGoParser.NEWLINE)
                self.state = 160
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 161
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variables_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Variables_declaredContext,0)


        def constants_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Constants_declaredContext,0)


        def function_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Function_declaredContext,0)


        def method_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Method_declaredContext,0)


        def struct_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_declaredContext,0)


        def interface_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_declaredContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclared" ):
                return visitor.visitDeclared(self)
            else:
                return visitor.visitChildren(self)




    def declared(self):

        localctx = MiniGoParser.DeclaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declared)
        try:
            self.state = 169
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 163
                self.variables_declared()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 164
                self.constants_declared()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 165
                self.function_declared()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 166
                self.method_declared()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 167
                self.struct_declared()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 168
                self.interface_declared()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function(self):
            return self.getTypedRuleContext(MiniGoParser.FunctionContext,0)


        def variables_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Variables_declaredContext,0)


        def ignore(self):
            return self.getTypedRuleContext(MiniGoParser.IgnoreContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_function_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_declared" ):
                return visitor.visitFunction_declared(self)
            else:
                return visitor.visitChildren(self)




    def function_declared(self):

        localctx = MiniGoParser.Function_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_function_declared)
        try:
            self.state = 175
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.FUNCTION]:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                self.function()
                pass
            elif token in [MiniGoParser.VARIABLE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 172
                self.variables_declared()
                self.state = 173
                self.ignore()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variables_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def inferred_var(self):
            return self.getTypedRuleContext(MiniGoParser.Inferred_varContext,0)


        def keyword_type_var(self):
            return self.getTypedRuleContext(MiniGoParser.Keyword_type_varContext,0)


        def struct_variable_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_variable_declaredContext,0)


        def ignore(self):
            return self.getTypedRuleContext(MiniGoParser.IgnoreContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_variables_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariables_declared" ):
                return visitor.visitVariables_declared(self)
            else:
                return visitor.visitChildren(self)




    def variables_declared(self):

        localctx = MiniGoParser.Variables_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_variables_declared)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 177
                self.inferred_var()
                pass

            elif la_ == 2:
                self.state = 178
                self.keyword_type_var()
                pass

            elif la_ == 3:
                self.state = 179
                self.struct_variable_declared()
                pass


            self.state = 182
            self.match(MiniGoParser.SEMICOLON)
            self.state = 184
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 183
                self.ignore()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Inferred_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(MiniGoParser.VARIABLE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def type_key_variable(self):
            return self.getTypedRuleContext(MiniGoParser.Type_key_variableContext,0)


        def array_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Array_literalContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_inferred_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInferred_var" ):
                return visitor.visitInferred_var(self)
            else:
                return visitor.visitChildren(self)




    def inferred_var(self):

        localctx = MiniGoParser.Inferred_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_inferred_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.match(MiniGoParser.VARIABLE)
            self.state = 187
            self.match(MiniGoParser.ID)
            self.state = 190
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INTEGER, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.state = 188
                self.type_key_variable()
                pass
            elif token in [MiniGoParser.SLP]:
                self.state = 189
                self.array_literal()
                pass
            elif token in [MiniGoParser.ASSIGN]:
                pass
            else:
                pass
            self.state = 192
            self.match(MiniGoParser.ASSIGN)
            self.state = 193
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_variable_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(MiniGoParser.VARIABLE, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_variable_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_variable_declared" ):
                return visitor.visitStruct_variable_declared(self)
            else:
                return visitor.visitChildren(self)




    def struct_variable_declared(self):

        localctx = MiniGoParser.Struct_variable_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_struct_variable_declared)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.match(MiniGoParser.VARIABLE)
            self.state = 196
            self.match(MiniGoParser.ID)
            self.state = 197
            self.match(MiniGoParser.ID)
            self.state = 200
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ASSIGN:
                self.state = 198
                self.match(MiniGoParser.ASSIGN)
                self.state = 199
                self.expression(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Keyword_type_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(MiniGoParser.VARIABLE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def type_key_variable(self):
            return self.getTypedRuleContext(MiniGoParser.Type_key_variableContext,0)


        def array_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Array_literalContext,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_keyword_type_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKeyword_type_var" ):
                return visitor.visitKeyword_type_var(self)
            else:
                return visitor.visitChildren(self)




    def keyword_type_var(self):

        localctx = MiniGoParser.Keyword_type_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_keyword_type_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.match(MiniGoParser.VARIABLE)
            self.state = 203
            self.match(MiniGoParser.ID)
            self.state = 206
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INTEGER, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.state = 204
                self.type_key_variable()
                pass
            elif token in [MiniGoParser.SLP]:
                self.state = 205
                self.array_literal()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 210
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ASSIGN:
                self.state = 208
                self.match(MiniGoParser.ASSIGN)
                self.state = 209
                self.expression(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_number_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_number_lit(self):
            return self.getTypedRuleContext(MiniGoParser.List_number_litContext,0)


        def FLOAT_LIT(self):
            return self.getToken(MiniGoParser.FLOAT_LIT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_list_number_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_number_lit" ):
                return visitor.visitList_number_lit(self)
            else:
                return visitor.visitChildren(self)




    def list_number_lit(self):

        localctx = MiniGoParser.List_number_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_list_number_lit)
        try:
            self.state = 220
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 212
                self.match(MiniGoParser.INT_LIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 213
                self.match(MiniGoParser.INT_LIT)
                self.state = 214
                self.match(MiniGoParser.COMMA)
                self.state = 215
                self.list_number_lit()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 216
                self.match(MiniGoParser.FLOAT_LIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 217
                self.match(MiniGoParser.FLOAT_LIT)
                self.state = 218
                self.match(MiniGoParser.COMMA)
                self.state = 219
                self.list_number_lit()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_keyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(MiniGoParser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_type_key

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_key" ):
                return visitor.visitType_key(self)
            else:
                return visitor.visitChildren(self)




    def type_key(self):

        localctx = MiniGoParser.Type_keyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_type_key)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INTEGER) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.ID))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_key_variableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(MiniGoParser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_type_key_variable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_key_variable" ):
                return visitor.visitType_key_variable(self)
            else:
                return visitor.visitChildren(self)




    def type_key_variable(self):

        localctx = MiniGoParser.Type_key_variableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_type_key_variable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INTEGER) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Constants_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONSTANT(self):
            return self.getToken(MiniGoParser.CONSTANT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def NEWLINE(self):
            return self.getToken(MiniGoParser.NEWLINE, 0)

        def ignore(self):
            return self.getTypedRuleContext(MiniGoParser.IgnoreContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_constants_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstants_declared" ):
                return visitor.visitConstants_declared(self)
            else:
                return visitor.visitChildren(self)




    def constants_declared(self):

        localctx = MiniGoParser.Constants_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_constants_declared)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.match(MiniGoParser.CONSTANT)
            self.state = 227
            self.match(MiniGoParser.ID)
            self.state = 228
            self.match(MiniGoParser.ASSIGN)
            self.state = 229
            self.expression(0)
            self.state = 230
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.SEMICOLON or _la==MiniGoParser.NEWLINE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 232
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 231
                self.ignore()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(MiniGoParser.FUNCTION, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def CLP(self):
            return self.getToken(MiniGoParser.CLP, 0)

        def CRP(self):
            return self.getToken(MiniGoParser.CRP, 0)

        def ignore(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.IgnoreContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.IgnoreContext,i)


        def list_parameters(self):
            return self.getTypedRuleContext(MiniGoParser.List_parametersContext,0)


        def parameter_type(self):
            return self.getTypedRuleContext(MiniGoParser.Parameter_typeContext,0)


        def list_statement_in_function(self):
            return self.getTypedRuleContext(MiniGoParser.List_statement_in_functionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_function

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = MiniGoParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.match(MiniGoParser.FUNCTION)
            self.state = 235
            self.match(MiniGoParser.ID)
            self.state = 236
            self.match(MiniGoParser.LP)
            self.state = 238
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 237
                self.list_parameters()


            self.state = 240
            self.match(MiniGoParser.RP)
            self.state = 242
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INTEGER) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.SLP) | (1 << MiniGoParser.ID))) != 0):
                self.state = 241
                self.parameter_type()


            self.state = 244
            self.match(MiniGoParser.CLP)
            self.state = 246
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.SEMICOLON or _la==MiniGoParser.NEWLINE:
                self.state = 245
                self.ignore()


            self.state = 249
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONSTANT) | (1 << MiniGoParser.VARIABLE) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.ID))) != 0):
                self.state = 248
                self.list_statement_in_function()


            self.state = 251
            self.match(MiniGoParser.CRP)
            self.state = 252
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def STRUCT(self):
            return self.getToken(MiniGoParser.STRUCT, 0)

        def CLP(self):
            return self.getToken(MiniGoParser.CLP, 0)

        def struct_variable_list(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_variable_listContext,0)


        def CRP(self):
            return self.getToken(MiniGoParser.CRP, 0)

        def ignore(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.IgnoreContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.IgnoreContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_declared" ):
                return visitor.visitStruct_declared(self)
            else:
                return visitor.visitChildren(self)




    def struct_declared(self):

        localctx = MiniGoParser.Struct_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_struct_declared)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.match(MiniGoParser.TYPE)
            self.state = 255
            self.match(MiniGoParser.ID)
            self.state = 256
            self.match(MiniGoParser.STRUCT)
            self.state = 257
            self.match(MiniGoParser.CLP)
            self.state = 261
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.SEMICOLON or _la==MiniGoParser.NEWLINE:
                self.state = 258
                self.ignore()
                self.state = 263
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 264
            self.struct_variable_list()
            self.state = 268
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.SEMICOLON or _la==MiniGoParser.NEWLINE:
                self.state = 265
                self.ignore()
                self.state = 270
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 271
            self.match(MiniGoParser.CRP)
            self.state = 272
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_variable_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_variable_list_recur(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_variable_list_recurContext,0)


        def ignore(self):
            return self.getTypedRuleContext(MiniGoParser.IgnoreContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_variable_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_variable_list" ):
                return visitor.visitStruct_variable_list(self)
            else:
                return visitor.visitChildren(self)




    def struct_variable_list(self):

        localctx = MiniGoParser.Struct_variable_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_struct_variable_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.struct_variable_list_recur()
            self.state = 276
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 275
                self.ignore()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_variable_list_recurContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ignore(self):
            return self.getTypedRuleContext(MiniGoParser.IgnoreContext,0)


        def type_key(self):
            return self.getTypedRuleContext(MiniGoParser.Type_keyContext,0)


        def array_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Array_literalContext,0)


        def struct_variable_list_recur(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_variable_list_recurContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_variable_list_recur

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_variable_list_recur" ):
                return visitor.visitStruct_variable_list_recur(self)
            else:
                return visitor.visitChildren(self)




    def struct_variable_list_recur(self):

        localctx = MiniGoParser.Struct_variable_list_recurContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_struct_variable_list_recur)
        try:
            self.state = 293
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 278
                self.match(MiniGoParser.ID)
                self.state = 281
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.STRING, MiniGoParser.INTEGER, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.ID]:
                    self.state = 279
                    self.type_key()
                    pass
                elif token in [MiniGoParser.SLP]:
                    self.state = 280
                    self.array_literal()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 283
                self.ignore()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 285
                self.match(MiniGoParser.ID)
                self.state = 288
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.STRING, MiniGoParser.INTEGER, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.ID]:
                    self.state = 286
                    self.type_key()
                    pass
                elif token in [MiniGoParser.SLP]:
                    self.state = 287
                    self.array_literal()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 290
                self.ignore()
                self.state = 291
                self.struct_variable_list_recur()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(MiniGoParser.FUNCTION, 0)

        def LP(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LP)
            else:
                return self.getToken(MiniGoParser.LP, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def RP(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RP)
            else:
                return self.getToken(MiniGoParser.RP, i)

        def CLP(self):
            return self.getToken(MiniGoParser.CLP, 0)

        def CRP(self):
            return self.getToken(MiniGoParser.CRP, 0)

        def ignore(self):
            return self.getTypedRuleContext(MiniGoParser.IgnoreContext,0)


        def list_parameters(self):
            return self.getTypedRuleContext(MiniGoParser.List_parametersContext,0)


        def parameter_type(self):
            return self.getTypedRuleContext(MiniGoParser.Parameter_typeContext,0)


        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_declared" ):
                return visitor.visitMethod_declared(self)
            else:
                return visitor.visitChildren(self)




    def method_declared(self):

        localctx = MiniGoParser.Method_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_method_declared)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.match(MiniGoParser.FUNCTION)
            self.state = 296
            self.match(MiniGoParser.LP)
            self.state = 297
            self.match(MiniGoParser.ID)
            self.state = 298
            self.match(MiniGoParser.ID)
            self.state = 299
            self.match(MiniGoParser.RP)
            self.state = 300
            self.match(MiniGoParser.ID)
            self.state = 301
            self.match(MiniGoParser.LP)
            self.state = 303
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 302
                self.list_parameters()


            self.state = 305
            self.match(MiniGoParser.RP)
            self.state = 307
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INTEGER) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.SLP) | (1 << MiniGoParser.ID))) != 0):
                self.state = 306
                self.parameter_type()


            self.state = 309
            self.match(MiniGoParser.CLP)
            self.state = 311
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.VARIABLE) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.ID))) != 0):
                self.state = 310
                self.list_statement()


            self.state = 313
            self.match(MiniGoParser.CRP)
            self.state = 314
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_parametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self):
            return self.getTypedRuleContext(MiniGoParser.ParameterContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_parameters(self):
            return self.getTypedRuleContext(MiniGoParser.List_parametersContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_parameters

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_parameters" ):
                return visitor.visitList_parameters(self)
            else:
                return visitor.visitChildren(self)




    def list_parameters(self):

        localctx = MiniGoParser.List_parametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_list_parameters)
        try:
            self.state = 321
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 316
                self.parameter()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 317
                self.parameter()
                self.state = 318
                self.match(MiniGoParser.COMMA)
                self.state = 319
                self.list_parameters()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_ID(self):
            return self.getTypedRuleContext(MiniGoParser.List_IDContext,0)


        def parameter_type(self):
            return self.getTypedRuleContext(MiniGoParser.Parameter_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_parameter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = MiniGoParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            self.list_ID()
            self.state = 324
            self.parameter_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_key(self):
            return self.getTypedRuleContext(MiniGoParser.Type_keyContext,0)


        def array_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Array_literalContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_parameter_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter_type" ):
                return visitor.visitParameter_type(self)
            else:
                return visitor.visitChildren(self)




    def parameter_type(self):

        localctx = MiniGoParser.Parameter_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_parameter_type)
        try:
            self.state = 328
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INTEGER, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 326
                self.type_key()
                pass
            elif token in [MiniGoParser.SLP]:
                self.enterOuterAlt(localctx, 2)
                self.state = 327
                self.array_literal()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_IDContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_ID(self):
            return self.getTypedRuleContext(MiniGoParser.List_IDContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_ID

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_ID" ):
                return visitor.visitList_ID(self)
            else:
                return visitor.visitChildren(self)




    def list_ID(self):

        localctx = MiniGoParser.List_IDContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_list_ID)
        try:
            self.state = 334
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 330
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 331
                self.match(MiniGoParser.ID)
                self.state = 332
                self.match(MiniGoParser.COMMA)
                self.state = 333
                self.list_ID()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def INTERFACE(self):
            return self.getToken(MiniGoParser.INTERFACE, 0)

        def CLP(self):
            return self.getToken(MiniGoParser.CLP, 0)

        def list_para_interface(self):
            return self.getTypedRuleContext(MiniGoParser.List_para_interfaceContext,0)


        def CRP(self):
            return self.getToken(MiniGoParser.CRP, 0)

        def ignore(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.IgnoreContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.IgnoreContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_declared" ):
                return visitor.visitInterface_declared(self)
            else:
                return visitor.visitChildren(self)




    def interface_declared(self):

        localctx = MiniGoParser.Interface_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_interface_declared)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self.match(MiniGoParser.TYPE)
            self.state = 337
            self.match(MiniGoParser.ID)
            self.state = 338
            self.match(MiniGoParser.INTERFACE)
            self.state = 339
            self.match(MiniGoParser.CLP)
            self.state = 343
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.SEMICOLON or _la==MiniGoParser.NEWLINE:
                self.state = 340
                self.ignore()
                self.state = 345
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 346
            self.list_para_interface()
            self.state = 350
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.SEMICOLON or _la==MiniGoParser.NEWLINE:
                self.state = 347
                self.ignore()
                self.state = 352
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 353
            self.match(MiniGoParser.CRP)
            self.state = 354
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_para_interfaceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def ignore(self):
            return self.getTypedRuleContext(MiniGoParser.IgnoreContext,0)


        def list_parameters(self):
            return self.getTypedRuleContext(MiniGoParser.List_parametersContext,0)


        def parameter_type(self):
            return self.getTypedRuleContext(MiniGoParser.Parameter_typeContext,0)


        def list_para_interface(self):
            return self.getTypedRuleContext(MiniGoParser.List_para_interfaceContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_para_interface

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_para_interface" ):
                return visitor.visitList_para_interface(self)
            else:
                return visitor.visitChildren(self)




    def list_para_interface(self):

        localctx = MiniGoParser.List_para_interfaceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_list_para_interface)
        self._la = 0 # Token type
        try:
            self.state = 378
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 356
                self.match(MiniGoParser.ID)
                self.state = 357
                self.match(MiniGoParser.LP)
                self.state = 359
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.ID:
                    self.state = 358
                    self.list_parameters()


                self.state = 361
                self.match(MiniGoParser.RP)
                self.state = 363
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INTEGER) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.SLP) | (1 << MiniGoParser.ID))) != 0):
                    self.state = 362
                    self.parameter_type()


                self.state = 365
                self.ignore()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 366
                self.match(MiniGoParser.ID)
                self.state = 367
                self.match(MiniGoParser.LP)
                self.state = 369
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.ID:
                    self.state = 368
                    self.list_parameters()


                self.state = 371
                self.match(MiniGoParser.RP)
                self.state = 373
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INTEGER) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.SLP) | (1 << MiniGoParser.ID))) != 0):
                    self.state = 372
                    self.parameter_type()


                self.state = 375
                self.ignore()
                self.state = 376
                self.list_para_interface()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(MiniGoParser.FLOAT_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(MiniGoParser.STRING_LIT, 0)

        def TRUE(self):
            return self.getToken(MiniGoParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MiniGoParser.FALSE, 0)

        def NIL(self):
            return self.getToken(MiniGoParser.NIL, 0)

        def array_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Array_literalContext,0)


        def struct_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literalContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = MiniGoParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_literal)
        try:
            self.state = 388
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 380
                self.match(MiniGoParser.INT_LIT)
                pass
            elif token in [MiniGoParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 381
                self.match(MiniGoParser.FLOAT_LIT)
                pass
            elif token in [MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 382
                self.match(MiniGoParser.STRING_LIT)
                pass
            elif token in [MiniGoParser.TRUE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 383
                self.match(MiniGoParser.TRUE)
                pass
            elif token in [MiniGoParser.FALSE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 384
                self.match(MiniGoParser.FALSE)
                pass
            elif token in [MiniGoParser.NIL]:
                self.enterOuterAlt(localctx, 6)
                self.state = 385
                self.match(MiniGoParser.NIL)
                pass
            elif token in [MiniGoParser.SLP]:
                self.enterOuterAlt(localctx, 7)
                self.state = 386
                self.array_literal()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 8)
                self.state = 387
                self.struct_literal()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def OR(self):
            return self.getToken(MiniGoParser.OR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
            self.expression1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 398
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 393
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 394
                    self.match(MiniGoParser.OR)
                    self.state = 395
                    self.expression1(0) 
                self.state = 400
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression2(self):
            return self.getTypedRuleContext(MiniGoParser.Expression2Context,0)


        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def AND(self):
            return self.getToken(MiniGoParser.AND, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression1" ):
                return visitor.visitExpression1(self)
            else:
                return visitor.visitChildren(self)



    def expression1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_expression1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402
            self.expression2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 409
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression1)
                    self.state = 404
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 405
                    self.match(MiniGoParser.AND)
                    self.state = 406
                    self.expression2(0) 
                self.state = 411
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression3(self):
            return self.getTypedRuleContext(MiniGoParser.Expression3Context,0)


        def expression2(self):
            return self.getTypedRuleContext(MiniGoParser.Expression2Context,0)


        def EQ(self):
            return self.getToken(MiniGoParser.EQ, 0)

        def NEQ(self):
            return self.getToken(MiniGoParser.NEQ, 0)

        def LT(self):
            return self.getToken(MiniGoParser.LT, 0)

        def GT(self):
            return self.getToken(MiniGoParser.GT, 0)

        def LEQ(self):
            return self.getToken(MiniGoParser.LEQ, 0)

        def GEQ(self):
            return self.getToken(MiniGoParser.GEQ, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression2" ):
                return visitor.visitExpression2(self)
            else:
                return visitor.visitChildren(self)



    def expression2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_expression2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 413
            self.expression3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 420
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                    self.state = 415
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 416
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQ) | (1 << MiniGoParser.NEQ) | (1 << MiniGoParser.LT) | (1 << MiniGoParser.GT) | (1 << MiniGoParser.LEQ) | (1 << MiniGoParser.GEQ))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 417
                    self.expression3(0) 
                self.state = 422
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression4(self):
            return self.getTypedRuleContext(MiniGoParser.Expression4Context,0)


        def expression3(self):
            return self.getTypedRuleContext(MiniGoParser.Expression3Context,0)


        def ADD(self):
            return self.getToken(MiniGoParser.ADD, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression3" ):
                return visitor.visitExpression3(self)
            else:
                return visitor.visitChildren(self)



    def expression3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_expression3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 424
            self.expression4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 431
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                    self.state = 426
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 427
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.ADD or _la==MiniGoParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 428
                    self.expression4(0) 
                self.state = 433
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression5(self):
            return self.getTypedRuleContext(MiniGoParser.Expression5Context,0)


        def expression4(self):
            return self.getTypedRuleContext(MiniGoParser.Expression4Context,0)


        def MUL(self):
            return self.getToken(MiniGoParser.MUL, 0)

        def DIV(self):
            return self.getToken(MiniGoParser.DIV, 0)

        def MOD(self):
            return self.getToken(MiniGoParser.MOD, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression4" ):
                return visitor.visitExpression4(self)
            else:
                return visitor.visitChildren(self)



    def expression4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_expression4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 435
            self.expression5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 442
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                    self.state = 437
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 438
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 439
                    self.expression5() 
                self.state = 444
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression5(self):
            return self.getTypedRuleContext(MiniGoParser.Expression5Context,0)


        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def expression6(self):
            return self.getTypedRuleContext(MiniGoParser.Expression6Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expression5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression5" ):
                return visitor.visitExpression5(self)
            else:
                return visitor.visitChildren(self)




    def expression5(self):

        localctx = MiniGoParser.Expression5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_expression5)
        self._la = 0 # Token type
        try:
            self.state = 448
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SUB, MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 445
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.SUB or _la==MiniGoParser.NOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 446
                self.expression5()
                pass
            elif token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.LP, MiniGoParser.SLP, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 447
                self.expression6(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression7(self):
            return self.getTypedRuleContext(MiniGoParser.Expression7Context,0)


        def expression6(self):
            return self.getTypedRuleContext(MiniGoParser.Expression6Context,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def index_operators_recur(self):
            return self.getTypedRuleContext(MiniGoParser.Index_operators_recurContext,0)


        def SLP(self):
            return self.getToken(MiniGoParser.SLP, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def SRP(self):
            return self.getToken(MiniGoParser.SRP, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression6" ):
                return visitor.visitExpression6(self)
            else:
                return visitor.visitChildren(self)



    def expression6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_expression6, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 451
            self.expression7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 471
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,45,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 469
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expression6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression6)
                        self.state = 453
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 454
                        self.match(MiniGoParser.DOT)
                        self.state = 455
                        self.match(MiniGoParser.ID)
                        self.state = 456
                        self.match(MiniGoParser.LP)
                        self.state = 458
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LP) | (1 << MiniGoParser.SLP) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                            self.state = 457
                            self.index_operators_recur()


                        self.state = 460
                        self.match(MiniGoParser.RP)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expression6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression6)
                        self.state = 461
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 462
                        self.match(MiniGoParser.SLP)
                        self.state = 463
                        self.expression(0)
                        self.state = 464
                        self.match(MiniGoParser.SRP)
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.Expression6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression6)
                        self.state = 466
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 467
                        self.match(MiniGoParser.DOT)
                        self.state = 468
                        self.match(MiniGoParser.ID)
                        pass

             
                self.state = 473
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,45,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def function_call(self):
            return self.getTypedRuleContext(MiniGoParser.Function_callContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expression7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression7" ):
                return visitor.visitExpression7(self)
            else:
                return visitor.visitChildren(self)




    def expression7(self):

        localctx = MiniGoParser.Expression7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_expression7)
        try:
            self.state = 481
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 474
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 475
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 476
                self.match(MiniGoParser.LP)
                self.state = 477
                self.expression(0)
                self.state = 478
                self.match(MiniGoParser.RP)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 480
                self.function_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dimensions(self):
            return self.getTypedRuleContext(MiniGoParser.DimensionsContext,0)


        def type_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Type_literalContext,0)


        def CLP(self):
            return self.getToken(MiniGoParser.CLP, 0)

        def array_elements(self):
            return self.getTypedRuleContext(MiniGoParser.Array_elementsContext,0)


        def CRP(self):
            return self.getToken(MiniGoParser.CRP, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal" ):
                return visitor.visitArray_literal(self)
            else:
                return visitor.visitChildren(self)




    def array_literal(self):

        localctx = MiniGoParser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 483
            self.dimensions()
            self.state = 484
            self.type_literal()
            self.state = 489
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.state = 485
                self.match(MiniGoParser.CLP)
                self.state = 486
                self.array_elements()
                self.state = 487
                self.match(MiniGoParser.CRP)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_element_setContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLP(self):
            return self.getToken(MiniGoParser.CLP, 0)

        def array_elements(self):
            return self.getTypedRuleContext(MiniGoParser.Array_elementsContext,0)


        def CRP(self):
            return self.getToken(MiniGoParser.CRP, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_element_set

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_element_set" ):
                return visitor.visitArray_element_set(self)
            else:
                return visitor.visitChildren(self)




    def array_element_set(self):

        localctx = MiniGoParser.Array_element_setContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_array_element_set)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 491
            self.match(MiniGoParser.CLP)
            self.state = 492
            self.array_elements()
            self.state = 493
            self.match(MiniGoParser.CRP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literal_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dimensions(self):
            return self.getTypedRuleContext(MiniGoParser.DimensionsContext,0)


        def type_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Type_literalContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_literal_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal_declare" ):
                return visitor.visitArray_literal_declare(self)
            else:
                return visitor.visitChildren(self)




    def array_literal_declare(self):

        localctx = MiniGoParser.Array_literal_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_array_literal_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 495
            self.dimensions()
            self.state = 496
            self.type_literal()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_elementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def valid_element(self):
            return self.getTypedRuleContext(MiniGoParser.Valid_elementContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def array_elements(self):
            return self.getTypedRuleContext(MiniGoParser.Array_elementsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_elements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_elements" ):
                return visitor.visitArray_elements(self)
            else:
                return visitor.visitChildren(self)




    def array_elements(self):

        localctx = MiniGoParser.Array_elementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_array_elements)
        try:
            self.state = 503
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 498
                self.valid_element()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 499
                self.valid_element()
                self.state = 500
                self.match(MiniGoParser.COMMA)
                self.state = 501
                self.array_elements()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Valid_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(MiniGoParser.FLOAT_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(MiniGoParser.STRING_LIT, 0)

        def TRUE(self):
            return self.getToken(MiniGoParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MiniGoParser.FALSE, 0)

        def NIL(self):
            return self.getToken(MiniGoParser.NIL, 0)

        def array_element_set(self):
            return self.getTypedRuleContext(MiniGoParser.Array_element_setContext,0)


        def struct_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literalContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_valid_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValid_element" ):
                return visitor.visitValid_element(self)
            else:
                return visitor.visitChildren(self)




    def valid_element(self):

        localctx = MiniGoParser.Valid_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_valid_element)
        try:
            self.state = 513
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 505
                self.match(MiniGoParser.INT_LIT)
                pass
            elif token in [MiniGoParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 506
                self.match(MiniGoParser.FLOAT_LIT)
                pass
            elif token in [MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 507
                self.match(MiniGoParser.STRING_LIT)
                pass
            elif token in [MiniGoParser.TRUE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 508
                self.match(MiniGoParser.TRUE)
                pass
            elif token in [MiniGoParser.FALSE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 509
                self.match(MiniGoParser.FALSE)
                pass
            elif token in [MiniGoParser.NIL]:
                self.enterOuterAlt(localctx, 6)
                self.state = 510
                self.match(MiniGoParser.NIL)
                pass
            elif token in [MiniGoParser.CLP]:
                self.enterOuterAlt(localctx, 7)
                self.state = 511
                self.array_element_set()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 8)
                self.state = 512
                self.struct_literal()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimensionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SLP(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SLP)
            else:
                return self.getToken(MiniGoParser.SLP, i)

        def cell_type(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Cell_typeContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Cell_typeContext,i)


        def SRP(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SRP)
            else:
                return self.getToken(MiniGoParser.SRP, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_dimensions

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimensions" ):
                return visitor.visitDimensions(self)
            else:
                return visitor.visitChildren(self)




    def dimensions(self):

        localctx = MiniGoParser.DimensionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_dimensions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 515
            self.match(MiniGoParser.SLP)
            self.state = 516
            self.cell_type()
            self.state = 517
            self.match(MiniGoParser.SRP)
            self.state = 524
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.SLP:
                self.state = 518
                self.match(MiniGoParser.SLP)
                self.state = 519
                self.cell_type()
                self.state = 520
                self.match(MiniGoParser.SRP)
                self.state = 526
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cell_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_cell_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCell_type" ):
                return visitor.visitCell_type(self)
            else:
                return visitor.visitChildren(self)




    def cell_type(self):

        localctx = MiniGoParser.Cell_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_cell_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 527
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.ID or _la==MiniGoParser.INT_LIT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def INTEGER(self):
            return self.getToken(MiniGoParser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_type_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_literal" ):
                return visitor.visitType_literal(self)
            else:
                return visitor.visitChildren(self)




    def type_literal(self):

        localctx = MiniGoParser.Type_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_type_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 529
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INTEGER) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.ID))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_literal_except_structContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def INTEGER(self):
            return self.getToken(MiniGoParser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_type_literal_except_struct

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_literal_except_struct" ):
                return visitor.visitType_literal_except_struct(self)
            else:
                return visitor.visitChildren(self)




    def type_literal_except_struct(self):

        localctx = MiniGoParser.Type_literal_except_structContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_type_literal_except_struct)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 531
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INTEGER) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def CLP(self):
            return self.getToken(MiniGoParser.CLP, 0)

        def CRP(self):
            return self.getToken(MiniGoParser.CRP, 0)

        def struct_literal_recur(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literal_recurContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_literal" ):
                return visitor.visitStruct_literal(self)
            else:
                return visitor.visitChildren(self)




    def struct_literal(self):

        localctx = MiniGoParser.Struct_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_struct_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 533
            self.match(MiniGoParser.ID)
            self.state = 534
            self.match(MiniGoParser.CLP)
            self.state = 536
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 535
                self.struct_literal_recur()


            self.state = 538
            self.match(MiniGoParser.CRP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_literal_recurContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COLON(self):
            return self.getToken(MiniGoParser.COLON, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def struct_literal_recur(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literal_recurContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_literal_recur

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_literal_recur" ):
                return visitor.visitStruct_literal_recur(self)
            else:
                return visitor.visitChildren(self)




    def struct_literal_recur(self):

        localctx = MiniGoParser.Struct_literal_recurContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_struct_literal_recur)
        try:
            self.state = 549
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 540
                self.match(MiniGoParser.ID)
                self.state = 541
                self.match(MiniGoParser.COLON)
                self.state = 542
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 543
                self.match(MiniGoParser.ID)
                self.state = 544
                self.match(MiniGoParser.COLON)
                self.state = 545
                self.expression(0)
                self.state = 546
                self.match(MiniGoParser.COMMA)
                self.state = 547
                self.struct_literal_recur()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_operatorsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def index_operators_recur(self):
            return self.getTypedRuleContext(MiniGoParser.Index_operators_recurContext,0)


        def ignore(self):
            return self.getTypedRuleContext(MiniGoParser.IgnoreContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_index_operators

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operators" ):
                return visitor.visitIndex_operators(self)
            else:
                return visitor.visitChildren(self)




    def index_operators(self):

        localctx = MiniGoParser.Index_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_index_operators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 551
            self.index_operators_recur()
            self.state = 553
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.SEMICOLON or _la==MiniGoParser.NEWLINE:
                self.state = 552
                self.ignore()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_operators_recurContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def index_operators_recur(self):
            return self.getTypedRuleContext(MiniGoParser.Index_operators_recurContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_index_operators_recur

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operators_recur" ):
                return visitor.visitIndex_operators_recur(self)
            else:
                return visitor.visitChildren(self)




    def index_operators_recur(self):

        localctx = MiniGoParser.Index_operators_recurContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_index_operators_recur)
        try:
            self.state = 560
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 555
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 556
                self.expression(0)
                self.state = 557
                self.match(MiniGoParser.COMMA)
                self.state = 558
                self.index_operators_recur()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Argument_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argument_list_recur(self):
            return self.getTypedRuleContext(MiniGoParser.Argument_list_recurContext,0)


        def ignore(self):
            return self.getTypedRuleContext(MiniGoParser.IgnoreContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_argument_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument_list" ):
                return visitor.visitArgument_list(self)
            else:
                return visitor.visitChildren(self)




    def argument_list(self):

        localctx = MiniGoParser.Argument_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_argument_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 562
            self.argument_list_recur()
            self.state = 564
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.SEMICOLON or _la==MiniGoParser.NEWLINE:
                self.state = 563
                self.ignore()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Argument_list_recurContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def ignore(self):
            return self.getTypedRuleContext(MiniGoParser.IgnoreContext,0)


        def argument_list_recur(self):
            return self.getTypedRuleContext(MiniGoParser.Argument_list_recurContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_argument_list_recur

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument_list_recur" ):
                return visitor.visitArgument_list_recur(self)
            else:
                return visitor.visitChildren(self)




    def argument_list_recur(self):

        localctx = MiniGoParser.Argument_list_recurContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_argument_list_recur)
        try:
            self.state = 571
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,56,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 566
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 567
                self.expression(0)
                self.state = 568
                self.ignore()
                self.state = 569
                self.argument_list_recur()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stepContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMICOLON)
            else:
                return self.getToken(MiniGoParser.SEMICOLON, i)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def assign_statement_for(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Assign_statement_forContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Assign_statement_forContext,i)


        def CLP(self):
            return self.getToken(MiniGoParser.CLP, 0)

        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def CRP(self):
            return self.getToken(MiniGoParser.CRP, 0)

        def variables_declared_for(self):
            return self.getTypedRuleContext(MiniGoParser.Variables_declared_forContext,0)


        def ignore(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.IgnoreContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.IgnoreContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_step

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_step" ):
                return visitor.visitFor_step(self)
            else:
                return visitor.visitChildren(self)




    def for_step(self):

        localctx = MiniGoParser.For_stepContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_for_step)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 573
            self.match(MiniGoParser.FOR)
            self.state = 576
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.VARIABLE]:
                self.state = 574
                self.variables_declared_for()
                pass
            elif token in [MiniGoParser.ID]:
                self.state = 575
                self.assign_statement_for()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 578
            self.match(MiniGoParser.SEMICOLON)
            self.state = 579
            self.expression(0)
            self.state = 580
            self.match(MiniGoParser.SEMICOLON)
            self.state = 581
            self.assign_statement_for()
            self.state = 585
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.SEMICOLON or _la==MiniGoParser.NEWLINE:
                self.state = 582
                self.ignore()
                self.state = 587
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 588
            self.match(MiniGoParser.CLP)
            self.state = 592
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.SEMICOLON or _la==MiniGoParser.NEWLINE:
                self.state = 589
                self.ignore()
                self.state = 594
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 595
            self.list_statement()
            self.state = 596
            self.match(MiniGoParser.CRP)
            self.state = 600
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,60,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 597
                    self.ignore() 
                self.state = 602
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,60,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_eachContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def ASSIGN_VAR(self):
            return self.getToken(MiniGoParser.ASSIGN_VAR, 0)

        def RANGE(self):
            return self.getToken(MiniGoParser.RANGE, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def CLP(self):
            return self.getToken(MiniGoParser.CLP, 0)

        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def CRP(self):
            return self.getToken(MiniGoParser.CRP, 0)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def ignore(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.IgnoreContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.IgnoreContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_each

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_each" ):
                return visitor.visitFor_each(self)
            else:
                return visitor.visitChildren(self)




    def for_each(self):

        localctx = MiniGoParser.For_eachContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_for_each)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 603
            self.match(MiniGoParser.FOR)
            self.state = 604
            self.match(MiniGoParser.ID)
            self.state = 607
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.COMMA:
                self.state = 605
                self.match(MiniGoParser.COMMA)
                self.state = 606
                self.match(MiniGoParser.ID)


            self.state = 609
            self.match(MiniGoParser.ASSIGN_VAR)
            self.state = 610
            self.match(MiniGoParser.RANGE)
            self.state = 611
            self.expression(0)
            self.state = 615
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.SEMICOLON or _la==MiniGoParser.NEWLINE:
                self.state = 612
                self.ignore()
                self.state = 617
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 618
            self.match(MiniGoParser.CLP)
            self.state = 622
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.SEMICOLON or _la==MiniGoParser.NEWLINE:
                self.state = 619
                self.ignore()
                self.state = 624
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 625
            self.list_statement()
            self.state = 626
            self.match(MiniGoParser.CRP)
            self.state = 630
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,64,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 627
                    self.ignore() 
                self.state = 632
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,64,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_basicContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def CLP(self):
            return self.getToken(MiniGoParser.CLP, 0)

        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def CRP(self):
            return self.getToken(MiniGoParser.CRP, 0)

        def ignore(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.IgnoreContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.IgnoreContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_basic

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_basic" ):
                return visitor.visitFor_basic(self)
            else:
                return visitor.visitChildren(self)




    def for_basic(self):

        localctx = MiniGoParser.For_basicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_for_basic)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 633
            self.match(MiniGoParser.FOR)
            self.state = 634
            self.expression(0)
            self.state = 638
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.SEMICOLON or _la==MiniGoParser.NEWLINE:
                self.state = 635
                self.ignore()
                self.state = 640
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 641
            self.match(MiniGoParser.CLP)
            self.state = 645
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.SEMICOLON or _la==MiniGoParser.NEWLINE:
                self.state = 642
                self.ignore()
                self.state = 647
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 648
            self.list_statement()
            self.state = 649
            self.match(MiniGoParser.CRP)
            self.state = 653
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,67,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 650
                    self.ignore() 
                self.state = 655
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,67,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variables_declared_forContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(MiniGoParser.VARIABLE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def type_key_variable(self):
            return self.getTypedRuleContext(MiniGoParser.Type_key_variableContext,0)


        def array_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Array_literalContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_variables_declared_for

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariables_declared_for" ):
                return visitor.visitVariables_declared_for(self)
            else:
                return visitor.visitChildren(self)




    def variables_declared_for(self):

        localctx = MiniGoParser.Variables_declared_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_variables_declared_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 656
            self.match(MiniGoParser.VARIABLE)
            self.state = 657
            self.match(MiniGoParser.ID)
            self.state = 660
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INTEGER, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.state = 658
                self.type_key_variable()
                pass
            elif token in [MiniGoParser.SLP]:
                self.state = 659
                self.array_literal()
                pass
            elif token in [MiniGoParser.ASSIGN]:
                pass
            else:
                pass
            self.state = 662
            self.match(MiniGoParser.ASSIGN)
            self.state = 663
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_statement_recur(self):
            return self.getTypedRuleContext(MiniGoParser.List_statement_recurContext,0)


        def ignore(self):
            return self.getTypedRuleContext(MiniGoParser.IgnoreContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_statement" ):
                return visitor.visitList_statement(self)
            else:
                return visitor.visitChildren(self)




    def list_statement(self):

        localctx = MiniGoParser.List_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_list_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 665
            self.list_statement_recur()
            self.state = 667
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,69,self._ctx)
            if la_ == 1:
                self.state = 666
                self.ignore()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_statement_recurContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(MiniGoParser.StatementContext,0)


        def list_statement_recur(self):
            return self.getTypedRuleContext(MiniGoParser.List_statement_recurContext,0)


        def ignore(self):
            return self.getTypedRuleContext(MiniGoParser.IgnoreContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_statement_recur

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_statement_recur" ):
                return visitor.visitList_statement_recur(self)
            else:
                return visitor.visitChildren(self)




    def list_statement_recur(self):

        localctx = MiniGoParser.List_statement_recurContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_list_statement_recur)
        self._la = 0 # Token type
        try:
            self.state = 676
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,71,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 669
                self.statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 670
                self.statement()
                self.state = 672
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.SEMICOLON or _la==MiniGoParser.NEWLINE:
                    self.state = 671
                    self.ignore()


                self.state = 674
                self.list_statement_recur()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declared_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Declared_statementContext,0)


        def assign_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_statementContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(MiniGoParser.If_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(MiniGoParser.For_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Continue_statementContext,0)


        def call_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Call_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Return_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MiniGoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 686
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,72,self._ctx)
            if la_ == 1:
                self.state = 678
                self.declared_statement()
                pass

            elif la_ == 2:
                self.state = 679
                self.assign_statement()
                pass

            elif la_ == 3:
                self.state = 680
                self.if_statement()
                pass

            elif la_ == 4:
                self.state = 681
                self.for_statement()
                pass

            elif la_ == 5:
                self.state = 682
                self.break_statement()
                pass

            elif la_ == 6:
                self.state = 683
                self.continue_statement()
                pass

            elif la_ == 7:
                self.state = 684
                self.call_statement()
                pass

            elif la_ == 8:
                self.state = 685
                self.return_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_statement_in_functionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_statement_in_function_recur(self):
            return self.getTypedRuleContext(MiniGoParser.List_statement_in_function_recurContext,0)


        def ignore(self):
            return self.getTypedRuleContext(MiniGoParser.IgnoreContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_statement_in_function

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_statement_in_function" ):
                return visitor.visitList_statement_in_function(self)
            else:
                return visitor.visitChildren(self)




    def list_statement_in_function(self):

        localctx = MiniGoParser.List_statement_in_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_list_statement_in_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 688
            self.list_statement_in_function_recur()
            self.state = 690
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.SEMICOLON or _la==MiniGoParser.NEWLINE:
                self.state = 689
                self.ignore()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_statement_in_function_recurContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement_in_function(self):
            return self.getTypedRuleContext(MiniGoParser.Statement_in_functionContext,0)


        def list_statement_in_function_recur(self):
            return self.getTypedRuleContext(MiniGoParser.List_statement_in_function_recurContext,0)


        def ignore(self):
            return self.getTypedRuleContext(MiniGoParser.IgnoreContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_statement_in_function_recur

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_statement_in_function_recur" ):
                return visitor.visitList_statement_in_function_recur(self)
            else:
                return visitor.visitChildren(self)




    def list_statement_in_function_recur(self):

        localctx = MiniGoParser.List_statement_in_function_recurContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_list_statement_in_function_recur)
        self._la = 0 # Token type
        try:
            self.state = 699
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,75,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 692
                self.statement_in_function()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 693
                self.statement_in_function()
                self.state = 695
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.SEMICOLON or _la==MiniGoParser.NEWLINE:
                    self.state = 694
                    self.ignore()


                self.state = 697
                self.list_statement_in_function_recur()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statement_in_functionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declared_statement_no_ignore(self):
            return self.getTypedRuleContext(MiniGoParser.Declared_statement_no_ignoreContext,0)


        def assign_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_statementContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(MiniGoParser.If_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(MiniGoParser.For_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Continue_statementContext,0)


        def call_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Call_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Return_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_statement_in_function

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement_in_function" ):
                return visitor.visitStatement_in_function(self)
            else:
                return visitor.visitChildren(self)




    def statement_in_function(self):

        localctx = MiniGoParser.Statement_in_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_statement_in_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 709
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,76,self._ctx)
            if la_ == 1:
                self.state = 701
                self.declared_statement_no_ignore()
                pass

            elif la_ == 2:
                self.state = 702
                self.assign_statement()
                pass

            elif la_ == 3:
                self.state = 703
                self.if_statement()
                pass

            elif la_ == 4:
                self.state = 704
                self.for_statement()
                pass

            elif la_ == 5:
                self.state = 705
                self.break_statement()
                pass

            elif la_ == 6:
                self.state = 706
                self.continue_statement()
                pass

            elif la_ == 7:
                self.state = 707
                self.call_statement()
                pass

            elif la_ == 8:
                self.state = 708
                self.return_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declared_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variables_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Variables_declaredContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_declared_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclared_statement" ):
                return visitor.visitDeclared_statement(self)
            else:
                return visitor.visitChildren(self)




    def declared_statement(self):

        localctx = MiniGoParser.Declared_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_declared_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 711
            self.variables_declared()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declared_statement_no_ignoreContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def NEWLINE(self):
            return self.getToken(MiniGoParser.NEWLINE, 0)

        def constants_declared_in_function(self):
            return self.getTypedRuleContext(MiniGoParser.Constants_declared_in_functionContext,0)


        def inferred_var(self):
            return self.getTypedRuleContext(MiniGoParser.Inferred_varContext,0)


        def keyword_type_var(self):
            return self.getTypedRuleContext(MiniGoParser.Keyword_type_varContext,0)


        def struct_variable_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_variable_declaredContext,0)


        def ignore(self):
            return self.getTypedRuleContext(MiniGoParser.IgnoreContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_declared_statement_no_ignore

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclared_statement_no_ignore" ):
                return visitor.visitDeclared_statement_no_ignore(self)
            else:
                return visitor.visitChildren(self)




    def declared_statement_no_ignore(self):

        localctx = MiniGoParser.Declared_statement_no_ignoreContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_declared_statement_no_ignore)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 717
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,77,self._ctx)
            if la_ == 1:
                self.state = 713
                self.constants_declared_in_function()
                pass

            elif la_ == 2:
                self.state = 714
                self.inferred_var()
                pass

            elif la_ == 3:
                self.state = 715
                self.keyword_type_var()
                pass

            elif la_ == 4:
                self.state = 716
                self.struct_variable_declared()
                pass


            self.state = 719
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.SEMICOLON or _la==MiniGoParser.NEWLINE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 721
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,78,self._ctx)
            if la_ == 1:
                self.state = 720
                self.ignore()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Constants_declared_in_functionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONSTANT(self):
            return self.getToken(MiniGoParser.CONSTANT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_constants_declared_in_function

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstants_declared_in_function" ):
                return visitor.visitConstants_declared_in_function(self)
            else:
                return visitor.visitChildren(self)




    def constants_declared_in_function(self):

        localctx = MiniGoParser.Constants_declared_in_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_constants_declared_in_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 723
            self.match(MiniGoParser.CONSTANT)
            self.state = 724
            self.match(MiniGoParser.ID)
            self.state = 725
            self.match(MiniGoParser.ASSIGN)
            self.state = 726
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(MiniGoParser.LhsContext,0)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def ASSIGN_VAR(self):
            return self.getToken(MiniGoParser.ASSIGN_VAR, 0)

        def ASSIGN_ADD(self):
            return self.getToken(MiniGoParser.ASSIGN_ADD, 0)

        def ASSIGN_SUB(self):
            return self.getToken(MiniGoParser.ASSIGN_SUB, 0)

        def ASSIGN_MUL(self):
            return self.getToken(MiniGoParser.ASSIGN_MUL, 0)

        def ASSIGN_DIV(self):
            return self.getToken(MiniGoParser.ASSIGN_DIV, 0)

        def ASSIGN_MOD(self):
            return self.getToken(MiniGoParser.ASSIGN_MOD, 0)

        def ignore(self):
            return self.getTypedRuleContext(MiniGoParser.IgnoreContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assign_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_statement" ):
                return visitor.visitAssign_statement(self)
            else:
                return visitor.visitChildren(self)




    def assign_statement(self):

        localctx = MiniGoParser.Assign_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_assign_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 728
            self.lhs(0)
            self.state = 729
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.ASSIGN_VAR) | (1 << MiniGoParser.ASSIGN_ADD) | (1 << MiniGoParser.ASSIGN_SUB) | (1 << MiniGoParser.ASSIGN_MUL) | (1 << MiniGoParser.ASSIGN_DIV) | (1 << MiniGoParser.ASSIGN_MOD))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 730
            self.expression(0)
            self.state = 732
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,79,self._ctx)
            if la_ == 1:
                self.state = 731
                self.ignore()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_statement_forContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def ASSIGN_VAR(self):
            return self.getToken(MiniGoParser.ASSIGN_VAR, 0)

        def ASSIGN_ADD(self):
            return self.getToken(MiniGoParser.ASSIGN_ADD, 0)

        def ASSIGN_SUB(self):
            return self.getToken(MiniGoParser.ASSIGN_SUB, 0)

        def ASSIGN_MUL(self):
            return self.getToken(MiniGoParser.ASSIGN_MUL, 0)

        def ASSIGN_DIV(self):
            return self.getToken(MiniGoParser.ASSIGN_DIV, 0)

        def ASSIGN_MOD(self):
            return self.getToken(MiniGoParser.ASSIGN_MOD, 0)

        def ignore(self):
            return self.getTypedRuleContext(MiniGoParser.IgnoreContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assign_statement_for

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_statement_for" ):
                return visitor.visitAssign_statement_for(self)
            else:
                return visitor.visitChildren(self)




    def assign_statement_for(self):

        localctx = MiniGoParser.Assign_statement_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_assign_statement_for)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 734
            self.match(MiniGoParser.ID)
            self.state = 735
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.ASSIGN_VAR) | (1 << MiniGoParser.ASSIGN_ADD) | (1 << MiniGoParser.ASSIGN_SUB) | (1 << MiniGoParser.ASSIGN_MUL) | (1 << MiniGoParser.ASSIGN_DIV) | (1 << MiniGoParser.ASSIGN_MOD))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 736
            self.expression(0)
            self.state = 738
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,80,self._ctx)
            if la_ == 1:
                self.state = 737
                self.ignore()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def lhs(self):
            return self.getTypedRuleContext(MiniGoParser.LhsContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def SLP(self):
            return self.getToken(MiniGoParser.SLP, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def SRP(self):
            return self.getToken(MiniGoParser.SRP, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)



    def lhs(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.LhsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 122
        self.enterRecursionRule(localctx, 122, self.RULE_lhs, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 741
            self.match(MiniGoParser.ID)
            self._ctx.stop = self._input.LT(-1)
            self.state = 753
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,82,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 751
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,81,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.LhsContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_lhs)
                        self.state = 743
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 744
                        self.match(MiniGoParser.DOT)
                        self.state = 745
                        self.match(MiniGoParser.ID)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.LhsContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_lhs)
                        self.state = 746
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 747
                        self.match(MiniGoParser.SLP)
                        self.state = 748
                        self.expression(0)
                        self.state = 749
                        self.match(MiniGoParser.SRP)
                        pass

             
                self.state = 755
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,82,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def CLP(self):
            return self.getToken(MiniGoParser.CLP, 0)

        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def CRP(self):
            return self.getToken(MiniGoParser.CRP, 0)

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def ignore(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.IgnoreContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.IgnoreContext,i)


        def elif_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Elif_statementContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Elif_statementContext,i)


        def else_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Else_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = MiniGoParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 756
            self.match(MiniGoParser.IF)

            self.state = 757
            self.match(MiniGoParser.LP)
            self.state = 758
            self.expression(0)
            self.state = 759
            self.match(MiniGoParser.RP)
            self.state = 764
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.SEMICOLON or _la==MiniGoParser.NEWLINE:
                self.state = 761
                self.ignore()
                self.state = 766
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 767
            self.match(MiniGoParser.CLP)
            self.state = 771
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.SEMICOLON or _la==MiniGoParser.NEWLINE:
                self.state = 768
                self.ignore()
                self.state = 773
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 774
            self.list_statement()
            self.state = 778
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.SEMICOLON or _la==MiniGoParser.NEWLINE:
                self.state = 775
                self.ignore()
                self.state = 780
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 781
            self.match(MiniGoParser.CRP)
            self.state = 785
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,86,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 782
                    self.ignore() 
                self.state = 787
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,86,self._ctx)

            self.state = 791
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,87,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 788
                    self.elif_statement() 
                self.state = 793
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,87,self._ctx)

            self.state = 797
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,88,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 794
                    self.ignore() 
                self.state = 799
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,88,self._ctx)

            self.state = 801
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ELSE:
                self.state = 800
                self.else_statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def CLP(self):
            return self.getToken(MiniGoParser.CLP, 0)

        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def CRP(self):
            return self.getToken(MiniGoParser.CRP, 0)

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def ignore(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.IgnoreContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.IgnoreContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_elif_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_statement" ):
                return visitor.visitElif_statement(self)
            else:
                return visitor.visitChildren(self)




    def elif_statement(self):

        localctx = MiniGoParser.Elif_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_elif_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 803
            self.match(MiniGoParser.ELSE)
            self.state = 804
            self.match(MiniGoParser.IF)

            self.state = 805
            self.match(MiniGoParser.LP)
            self.state = 806
            self.expression(0)
            self.state = 807
            self.match(MiniGoParser.RP)
            self.state = 812
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.SEMICOLON or _la==MiniGoParser.NEWLINE:
                self.state = 809
                self.ignore()
                self.state = 814
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 815
            self.match(MiniGoParser.CLP)
            self.state = 819
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.SEMICOLON or _la==MiniGoParser.NEWLINE:
                self.state = 816
                self.ignore()
                self.state = 821
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 822
            self.list_statement()
            self.state = 826
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.SEMICOLON or _la==MiniGoParser.NEWLINE:
                self.state = 823
                self.ignore()
                self.state = 828
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 829
            self.match(MiniGoParser.CRP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def CLP(self):
            return self.getToken(MiniGoParser.CLP, 0)

        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def CRP(self):
            return self.getToken(MiniGoParser.CRP, 0)

        def ignore(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.IgnoreContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.IgnoreContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_else_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_statement" ):
                return visitor.visitElse_statement(self)
            else:
                return visitor.visitChildren(self)




    def else_statement(self):

        localctx = MiniGoParser.Else_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_else_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 831
            self.match(MiniGoParser.ELSE)
            self.state = 835
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.SEMICOLON or _la==MiniGoParser.NEWLINE:
                self.state = 832
                self.ignore()
                self.state = 837
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 838
            self.match(MiniGoParser.CLP)
            self.state = 842
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.SEMICOLON or _la==MiniGoParser.NEWLINE:
                self.state = 839
                self.ignore()
                self.state = 844
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 845
            self.list_statement()
            self.state = 849
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.SEMICOLON or _la==MiniGoParser.NEWLINE:
                self.state = 846
                self.ignore()
                self.state = 851
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 852
            self.match(MiniGoParser.CRP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def for_basic(self):
            return self.getTypedRuleContext(MiniGoParser.For_basicContext,0)


        def for_step(self):
            return self.getTypedRuleContext(MiniGoParser.For_stepContext,0)


        def for_each(self):
            return self.getTypedRuleContext(MiniGoParser.For_eachContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = MiniGoParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_for_statement)
        try:
            self.state = 857
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,96,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 854
                self.for_basic()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 855
                self.for_step()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 856
                self.for_each()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MiniGoParser.BREAK, 0)

        def ignore(self):
            return self.getTypedRuleContext(MiniGoParser.IgnoreContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_break_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = MiniGoParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 859
            self.match(MiniGoParser.BREAK)
            self.state = 860
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MiniGoParser.CONTINUE, 0)

        def ignore(self):
            return self.getTypedRuleContext(MiniGoParser.IgnoreContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_continue_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = MiniGoParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 862
            self.match(MiniGoParser.CONTINUE)
            self.state = 863
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def lhs(self):
            return self.getTypedRuleContext(MiniGoParser.LhsContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def index_operators(self):
            return self.getTypedRuleContext(MiniGoParser.Index_operatorsContext,0)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMICOLON)
            else:
                return self.getToken(MiniGoParser.SEMICOLON, i)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NEWLINE)
            else:
                return self.getToken(MiniGoParser.NEWLINE, i)

        def ignore(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.IgnoreContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.IgnoreContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_call_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_statement" ):
                return visitor.visitCall_statement(self)
            else:
                return visitor.visitChildren(self)




    def call_statement(self):

        localctx = MiniGoParser.Call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_call_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 868
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,97,self._ctx)
            if la_ == 1:
                self.state = 865
                self.lhs(0)
                self.state = 866
                self.match(MiniGoParser.DOT)


            self.state = 870
            self.match(MiniGoParser.ID)
            self.state = 871
            self.match(MiniGoParser.LP)
            self.state = 873
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LP) | (1 << MiniGoParser.SLP) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                self.state = 872
                self.index_operators()


            self.state = 875
            self.match(MiniGoParser.RP)
            self.state = 881
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,100,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 879
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,99,self._ctx)
                    if la_ == 1:
                        self.state = 876
                        self.match(MiniGoParser.SEMICOLON)
                        pass

                    elif la_ == 2:
                        self.state = 877
                        self.match(MiniGoParser.NEWLINE)
                        pass

                    elif la_ == 3:
                        self.state = 878
                        self.ignore()
                        pass

             
                self.state = 883
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,100,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def index_operators(self):
            return self.getTypedRuleContext(MiniGoParser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_function_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call" ):
                return visitor.visitFunction_call(self)
            else:
                return visitor.visitChildren(self)




    def function_call(self):

        localctx = MiniGoParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_function_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 884
            self.match(MiniGoParser.ID)
            self.state = 885
            self.match(MiniGoParser.LP)
            self.state = 887
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LP) | (1 << MiniGoParser.SLP) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                self.state = 886
                self.index_operators()


            self.state = 889
            self.match(MiniGoParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MiniGoParser.RETURN, 0)

        def ignore(self):
            return self.getTypedRuleContext(MiniGoParser.IgnoreContext,0)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_return_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = MiniGoParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_return_statement)
        try:
            self.state = 895
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,102,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 891
                self.match(MiniGoParser.RETURN)
                self.state = 892
                self.ignore()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 893
                self.match(MiniGoParser.RETURN)
                self.state = 894
                self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IgnoreContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NEWLINE)
            else:
                return self.getToken(MiniGoParser.NEWLINE, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_ignore

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIgnore" ):
                return visitor.visitIgnore(self)
            else:
                return visitor.visitChildren(self)




    def ignore(self):

        localctx = MiniGoParser.IgnoreContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_ignore)
        try:
            self.state = 909
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SEMICOLON]:
                self.enterOuterAlt(localctx, 1)
                self.state = 897
                self.match(MiniGoParser.SEMICOLON)
                self.state = 901
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,103,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 898
                        self.match(MiniGoParser.NEWLINE) 
                    self.state = 903
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,103,self._ctx)

                pass
            elif token in [MiniGoParser.NEWLINE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 905 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 904
                        self.match(MiniGoParser.NEWLINE)

                    else:
                        raise NoViableAltException(self)
                    self.state = 907 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,104,self._ctx)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[23] = self.expression_sempred
        self._predicates[24] = self.expression1_sempred
        self._predicates[25] = self.expression2_sempred
        self._predicates[26] = self.expression3_sempred
        self._predicates[27] = self.expression4_sempred
        self._predicates[29] = self.expression6_sempred
        self._predicates[61] = self.lhs_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expression1_sempred(self, localctx:Expression1Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expression2_sempred(self, localctx:Expression2Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expression3_sempred(self, localctx:Expression3Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expression4_sempred(self, localctx:Expression4Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def expression6_sempred(self, localctx:Expression6Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         

    def lhs_sempred(self, localctx:LhsContext, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 1)
         




