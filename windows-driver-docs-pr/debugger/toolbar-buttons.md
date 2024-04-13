---
title: Toolbar Buttons - WinDbg (Classic)
description: Toolbar Buttons - WinDbg (Classic)
keywords: ["toolbar (WinDbg), button descriptions", "buttons (WinDbg Toolbar), descriptions"]
ms.date: 05/23/2017
---

# Toolbar Buttons - WinDbg (Classic)

Except for the breakpoint button, each button on the toolbar is equivalent to a menu command. The buttons on the toolbar have the following effects.

|Button|Description|
|----- |---------- |
|:::image type="content" source="images/tbopen.png" alt-text="Screenshot of the Open Source File button on the toolbar.":::|Opens a source file as a read-only file. Equivalent to File >  Open Source File.|
|:::image type="content" source="images/tbcut.png" alt-text="Screenshot of the Cut button on the toolbar.":::|Removes the selected text from the active window and puts it on the clipboard. Equivalent to Edit >  Cut.|
|:::image type="content" source="images/tbcopy.png" alt-text="Screenshot of the Copy button on the toolbar.":::|Copies the selected text from the active window to the clipboard. Edit >  Copy.|
|:::image type="content" source="images/tbpaste.png" alt-text="Screenshot of the Paste button on the toolbar.":::|Pastes the text on the clipboard to where the cursor is located. Equivalent to Edit >  Paste.|
|:::image type="content" source="images/tbgo.png" alt-text="Screenshot of the Go button on the toolbar.":::|Starts or resumes execution. Execution continues until a breakpoint is reached, an exception or event occurs, the process ends, or the debugger breaks into the target. Equivalent to Debug >  Go.|
|:::image type="content" source="images/tbrestart.png" alt-text="Screenshot of the Restart button on the toolbar.":::|Restarts execution at the beginning of the process. Equivalent to Debug >  Restart.|
|:::image type="content" source="images/tbstop.png" alt-text="Screenshot of the Stop Debugging button on the toolbar.":::|Stops execution and terminates the target process permanently. Equivalent to Debug >  Stop Debugging.|
|:::image type="content" source="images/tbbreak.png" alt-text="Screenshot of the Break button on the toolbar.":::|In user mode, this button stops the process and its threads. In kernel mode, this button breaks into the target computer. Control is returned to the debugger. This button is also useful for cutting off long Debugger Command window displays. Equivalent to Debug >  Break.|
|:::image type="content" source="images/tbinto.png" alt-text="Screenshot of the Step Into button on the toolbar.":::|Executes a single instruction. If the instruction is a function call, the debugger steps into the function. Equivalent to Debug >  Step Into.|
|:::image type="content" source="images/tbover.png" alt-text="Screenshot of the Step Over button on the toolbar.":::|Executes a single instruction. If the instruction is a function call, the debugger executes the whole function in one step. Equivalent to Debug >  Step Over.|
|:::image type="content" source="images/tbout.png" alt-text="Screenshot of the Step Out button on the toolbar.":::|Executes the rest of the current function, and breaks when the function return is completed. Equivalent to Debug >  Step Out.|
|:::image type="content" source="images/tbcursor.png" alt-text="Screenshot of the Run to Cursor button on the toolbar.":::|Executes all instructions from the current instruction up to the instruction marked in the active Disassembly window or Source window. Equivalent to Debug >  Run to Cursor.|
|:::image type="content" source="images/tbbp.png" alt-text="Screenshot of the Breakpoints button on the toolbar.":::|If the active window is a Source or Disassembly window: Inserts a breakpoint at the current line. (If there already is a breakpoint set at the current line, this button removes the breakpoint.) Otherwise: Opens the Breakpoints dialog box like Edit >  Breakpoints.|
|:::image type="content" source="images/tbcmd.png" alt-text="Screenshot of the Command button on the toolbar.":::|Opens or activates the Debugger Command window. Equivalent to View >  Command.|
|:::image type="content" source="images/tbwatch.png" alt-text="Screenshot of the Watch button on the toolbar.":::|Opens or activates the Watch window. View >  Watch.|
|:::image type="content" source="images/tblocal.png" alt-text="Screenshot of the Locals button on the toolbar.":::|Opens or activates the Locals window. Equivalent to View >  Locals.|
|:::image type="content" source="images/tbreg.png" alt-text="Screenshot of the Registers button on the toolbar.":::|Opens or activates the Registers window. Equivalent to View >  Registers.|
|:::image type="content" source="images/tbmem.png" alt-text="Screenshot of the Memory button on the toolbar.":::|Opens a new Memory window. Equivalent to View >  Memory.|
|:::image type="content" source="images/tbcall.png" alt-text="Screenshot of the Call Stack button on the toolbar.":::|Opens or activates the Calls window. Equivalent to View >  Call Stack.|
|:::image type="content" source="images/tbdisasm2.png" alt-text="Screenshot of the Disassembly button on the toolbar.":::|Opens or activates the Disassembly window. Equivalent to View >  Disassembly.|
|:::image type="content" source="images/tbspad.png" alt-text="Screenshot of the Scratch Pad button on the toolbar.":::|Opens or activates the Scratch Pad. Equivalent to View >  Scratch Pad.|
|:::image type="content" source="images/tbsrcasm.png" alt-text="Screenshot of the Source Mode button on the toolbar.":::|Switches between source-mode and assembly-mode debugging. Equivalent to selecting or clearing Debug >  Source Mode.|
|:::image type="content" source="images/tbfont.png" alt-text="Screenshot of the Font button on the toolbar.":::|Enables you to change the font that is used in the debugging information windows. Equivalent to View >  Font.|
|:::image type="content" source="images/tbopt.png" alt-text="Screenshot of the Options button on the toolbar.":::|Displays the Options dialog box. Equivalent to View >  Options.|

## See also

[Debugger command window](the-debugger-command-window.md)
