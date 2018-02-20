News:
(Read here for any changes, look at bottom for old news)
	02/19/2018:
		Some changes have been completed and are being finalized. These changes
	are going to make variable declaration easier, and a decorator is going to be
	added to make these declarations easier. 
	No longer will you have to state "return locals()" in your variables function. Now
	you will simply declare you variables inside a dedicated function, and simply 
	decorate that function with the new function decorator that will be released
	soon.

	e.g.:
	@return_variables_to_compiler
	def foo_variables_list:
		font1 = "bar"
		font2 = "baz"

	no more:
	def foo_variables_list:
		font1 = "bar"
		font2 = "baz"
		return locals()	

	Pyle Sheets (or PCSS as you'll often see both names) is an opportunity for everyone to 
enjoy more opportunities to use Python while engaged in web development. Pyle Sheets is a 
competitor with LESS, SASS and other modifications of Cascading Style Sheets that offer
more options such as variables that gives a more programatic and functional feel to 
everyone's favorite Style Sheet.
	
	PCSS compiles to CSS via Python. Currently, it can act "in memory" so you can
simply tinker with it, albeit debugging support needs to be added when not actively
compiling and simply runing a Pyle Sheet in memory. PCSS is intended to be used with other
modules such as Flask in particular, but modules such as Django are great enough that some 
would say it is better than Flask and to top it all off, you have even more options such as
raw Jinja2, Werkzeug (Individual predecessor components of Flask), & various WSGI's. 

	If you have any suggestions or want to tweak this project, feel free!
