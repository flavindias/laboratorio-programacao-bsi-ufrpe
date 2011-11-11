# -*- coding: utf-8 -*-
"""
0 = Black          1 = Blue            2 = Green
3 = Aqua           4 = Red             5 = Purple
6 = Yellow         7 = White           8 = Gray
9 = Light Blue     10 = Light Green    11 = Light Aqua
12 = Light Red     13 = Light Purple   14 = Light Yellow
"""
import ctypes, sys
class Cor:
    def printColorido(text, color):
        std_out_handle = ctypes.windll.kernel32.GetStdHandle(-11)
        for i in range(0, color):
            ctypes.windll.kernel32.SetConsoleTextAttribute(std_out_handle, color[i])
            sys.stdout.write(text)
        ctypes.windll.kernel32.SetConsoleTextAttribute(std_out_handle, 7)
