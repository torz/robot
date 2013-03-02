#!/usr/bin/python

import urwid
a = 0

def show_or_exit(key):
	if key == 'esc':
		raise urwid.ExitMainLoop()
	#if key in 'up':
	#	a += 5
	#elif key in 'down':
	#	a -= 5
	#elif key in 'space':
	#	a = 0
	#txt.set_text(repr(a))
	txt.set_text(key)

txt = urwid.Text(u"SkyNet")
fill = urwid.Filler(txt, '50')
loop = urwid.MainLoop(fill, unhandled_input=show_or_exit)
loop.run()



