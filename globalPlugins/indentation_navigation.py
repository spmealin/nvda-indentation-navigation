# This plugin allows NVDA to navigate by indentation level.
# This means for whitespace-sensitive text, such as Python code, you can jump over entire blocks with one keystroke.
# Sean Mealin <spmealin@gmail.com>

import api
import controlTypes
import globalPluginHandler
import speech
import textInfos
import ui
#from logHandler import log

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    def script_moveToNextSibling(self, gesture):
        # Make sure we're in a editable control
        focus = api.getFocusObject()
        if focus.role != controlTypes.ROLE_EDITABLETEXT:
            ui.message("Not in an edit control.")
            return
        
        # Get the current indentation level 
        textInfo = focus.makeTextInfo(textInfos.POSITION_CARET)
        textInfo.expand(textInfos.UNIT_LINE)
        indentationLevel = len(textInfo.text) - len(textInfo.text.strip())
        onEmptyLine = len(textInfo.text) == 1 #1 because an empty line will have the \n character
        
        # Scan each line until we hit the end of the indentation block, the end of the edit area, or find a line with the same indentation level
        found = False
        while textInfo.move(textInfos.UNIT_LINE, 1) == 1:
            textInfo.expand(textInfos.UNIT_LINE)
            newIndentation = len(textInfo.text) - len(textInfo.text.strip())
            
            # Skip over empty lines if we didn't start on one.
            if not onEmptyLine and len(textInfo.text) == 1:
                continue
            
            if newIndentation == indentationLevel:
                # Found it
                found = True
                textInfo.updateCaret()
                speech.speakTextInfo(textInfo, unit=textInfos.UNIT_LINE)
                break
            elif newIndentation < indentationLevel:
                # Not found in this indentation block
                break
        
        # If we didn't find it, tell the user
        if not found:
            ui.message("No next line within indentation block")
    script_moveToNextSibling.__doc__ = "Moves to the next line with the same indentation level as the current line within the current indentation block."
    
    def script_moveToPreviousSibling(self, gesture):
        # Make sure we're in a editable control
        focus = api.getFocusObject()
        if focus.role != controlTypes.ROLE_EDITABLETEXT:
            ui.message("Not in an edit control.")
            return
        
        # Get the current indentation level 
        textInfo = focus.makeTextInfo(textInfos.POSITION_CARET)
        textInfo.expand(textInfos.UNIT_LINE)
        indentationLevel = len(textInfo.text) - len(textInfo.text.strip())
        onEmptyLine = len(textInfo.text) == 1 #1 because an empty line will have the \n character
        
        # Scan each line until we hit the start of the indentation block, the start of the edit area, or find a line with the same indentation level
        found = False
        while textInfo.move(textInfos.UNIT_LINE, -2) == -2:
            textInfo.expand(textInfos.UNIT_LINE)
            newIndentation = len(textInfo.text) - len(textInfo.text.strip())
            
            # Skip over empty lines if we didn't start on one.
            if not onEmptyLine and len(textInfo.text) == 1:
                continue
            
            if newIndentation == indentationLevel:
                # Found it
                found = True
                textInfo.updateCaret()
                speech.speakTextInfo(textInfo, unit=textInfos.UNIT_LINE)
                break
            elif newIndentation < indentationLevel:
                # Not found in this indentation block
                break
        
        # If we didn't find it, tell the user
        if not found:
            ui.message("No previous line within indentation block")
    script_moveToPreviousSibling.__doc__ = "Moves to the previous line with the same indentation level as the current line within the current indentation block."
    
    def script_moveToChild(self, gesture):
        # Make sure we're in a editable control
        focus = api.getFocusObject()
        if focus.role != controlTypes.ROLE_EDITABLETEXT:
            ui.message("Not in an edit control.")
            return
        
        # Get the current indentation level 
        textInfo = focus.makeTextInfo(textInfos.POSITION_CARET)
        textInfo.expand(textInfos.UNIT_LINE)
        indentationLevel = len(textInfo.text) - len(textInfo.text.strip())
        onEmptyLine = len(textInfo.text) == 1 #1 because an empty line will have the \n character
        
        # Scan each line until we hit the end of the indentation block, the end of the edit area, or find a line with grater indentation level
        found = False
        while textInfo.move(textInfos.UNIT_LINE, 1) == 1:
            textInfo.expand(textInfos.UNIT_LINE)
            newIndentation = len(textInfo.text) - len(textInfo.text.strip())
            
            # Skip over empty lines if we didn't start on one.
            if not onEmptyLine and len(textInfo.text) == 1:
                continue
            
            if newIndentation > indentationLevel:
                # Found it
                found = True
                textInfo.updateCaret()
                speech.speakTextInfo(textInfo, unit=textInfos.UNIT_LINE)
                break
            elif newIndentation < indentationLevel:
                # Not found in this indentation block
                break
        
        # If we didn't find it, tell the user
        if not found:
            ui.message("No child block within indentation block")
    script_moveToChild.__doc__ = "Moves to the next line with a greater indentation level than the current line within the current indentation block."
    
    def script_moveToParent(self, gesture):
        # Make sure we're in a editable control
        focus = api.getFocusObject()
        if focus.role != controlTypes.ROLE_EDITABLETEXT:
            ui.message("Not in an edit control.")
            return
        
        # Get the current indentation level 
        textInfo = focus.makeTextInfo(textInfos.POSITION_CARET)
        textInfo.expand(textInfos.UNIT_LINE)
        indentationLevel = len(textInfo.text) - len(textInfo.text.strip())
        onEmptyLine = len(textInfo.text) == 1 #1 because an empty line will have the \n character
        
        # Scan each line until we hit the start of the indentation block, the start of the edit area, or find a line with less indentation level
        found = False
        while textInfo.move(textInfos.UNIT_LINE, -2) == -2:
            textInfo.expand(textInfos.UNIT_LINE)
            newIndentation = len(textInfo.text) - len(textInfo.text.strip())
            
            # Skip over empty lines if we didn't start on one.
            if not onEmptyLine and len(textInfo.text) == 1:
                continue
            
            if newIndentation < indentationLevel:
                # Found it
                found = True
                textInfo.updateCaret()
                speech.speakTextInfo(textInfo, unit=textInfos.UNIT_LINE)
                break
        
        # If we didn't find it, tell the user
        if not found:
            ui.message("No parent of indentation block")
    script_moveToParent.__doc__ = "Moves to the previous line with a lesser indentation level than the current line within the current indentation block."
    
    __gestures={
        "kb:NVDA+control+alt+downArrow": "moveToNextSibling",
        "kb:NVDA+control+alt+upArrow": "moveToPreviousSibling",
        "kb:NVDA+control+alt+leftArrow": "moveToParent",
        "kb:NVDA+control+alt+rightArrow": "moveToChild"
    }