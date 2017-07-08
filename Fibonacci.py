Python 3.6.2rc2 (v3.6.2rc2:8913311345, Jul  7 2017, 00:35:45) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
def myfib2(n)
SyntaxError: invalid syntax
>>> def myfib2(n):
	a, b = 0,1
	while b < n:
		print (b)
		a, b = b, a+b

		
>>> myfib2(150)
1
1
2
3
5
8
13
21
34
55
89
144
>>> 
