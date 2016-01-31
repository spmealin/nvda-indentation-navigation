# Indentation Navigation (v1.0)
## Sean Mealin <spmealin@gmail.com>

### Description

The Indentation Navigation add-on adds commands to NVDA that allows you to navigate by indentation level in standard editable text controls.  You can jump to lines of text with indentation level that is the same as, greater than, or less than the current line of text.  This is most useful when navigating whitespace-significant text, such as source code for the Python programming language.  This gives you the ability to jump into or over the definition of methods, loops, conditional statements, and more.

The add-on will prevent jumping out of a block of text with similar indentation level, to prevent you from missing the fact that the block has ended.  This means that you will not be able to accidently jump from one block of indented text to another, for example between the definitions of two python methods.  When jumping to the previous indentation level, the curser will navigate to the line directly before the current block of indented text, meaning that you will jump to the defining line of a method or if statement if you are located in the body.  Empty lines will be ignored if the curser is on a non-empty line when a command is given, otherwise it will stop on the next empty line.

### Instilation and Removal

This add-on can be installed and removed just like any standard NVDA add-on.  For detailed instructions, please see the NVDA user manual.

### Default Keybindings

The default keybindings are listed below.  It is possible to customize them by using the standard NVDA Input gestures dialog (under the " Miscellaneous" category).  For detailed instructions, please see the NVDA user manual.

*  ctrl + alt + NVDA key + up arrow: move to previous line with same indentation level
*  ctrl + alt + NVDA key + down arrow: move to next line with same indentation level
*  ctrl + alt + NVDA key + left arrow: move to the previous line with a lesser indentation level
*  ctrl + alt + NVDA key + right arrow: move to the next line with a greater indentation level