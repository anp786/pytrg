def echo(*args,**kwargs):
	print(args,kwargs)
	type(args)
echo(1,2,a=3,b=4)
echo(1,2,3,4,5)
echo('a','b',a=10,b=20)
