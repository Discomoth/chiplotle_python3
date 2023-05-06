# Chiplotle

Chiplotle is a Python library that implements and extends the HPGL
(Hewlett-Packard Graphics Language) plotter control language. It
supports all the standard HPGL commands as well as our own more complex
"compound HPGL" commands, implemented as Python classes. Chiplotle also
provides direct control of your HPGL-aware hardware via a standard
usb<->serial port interface.

Chiplotle has been tested with a variety of HPGL devices from various
companies, including Hewlett-Packard, Roland Digital Group, Houston
Instrument, etc. It includes plotter-specific configuration files for
many different plotter models, as well as a generic configuration that
should work with any HPGL-compliant device.

Chiplotle is written and maintained by Victor Adan and Douglas Repetto.

Find all there is to know about Chiplotle at:
http://music.columbia.edu/cmc/chiplotle

# What is different from vanilla Chiplotle?

This fork was created from a fork that was in the process of being refactored to function on Python 3 (not sure which version, it was worked on years ago).
I took this work that had been done and got it to the point of mostly working with the pen plotters I possess. Thank you to willprice for the work they had done on it! 

# What is the goal?

I hope to use this module to support a program I am constucting to allow interactive, straight forward control of pen plotters. The original goal was for it to be used exclusively on vintage pen plotters, but I'd like to expand the functionality in the future to other devices such as the AxiDraw series by EvilMadScientist as well as some other obscure plotting techniques such as XY voltage controlled pen plotters. <br>
<br>
For whatever reason, these machines facinate me so! I want to help others be able to express themselves and create art without the requirement of being a programmer to control them! <br>
Feel free to reach out to me, contribute, suggest, test, debug, etc. <br>
I consider myself a 'junkyard'/fledgeling Python programmer, I'm starting to get the hang of it, but I have a good ways to go to be fully proficient! 