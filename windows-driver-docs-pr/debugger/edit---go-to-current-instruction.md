---
title: Edit Go to Current Instruction
description: Edit Go to Current Instruction
ms.assetid: 7bc57ac1-1de6-4534-836b-132e3b072ae5
keywords: ["Edit Go to Current Instruction"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Edit | Go to Current Instruction


## <span id="ddk_edit_go_to_current_instruction_dbg"></span><span id="DDK_EDIT_GO_TO_CURRENT_INSTRUCTION_DBG"></span>


Click **Go to Current Instruction** on the **Edit** menu to open the debugging information window that contains the current instruction and to highlight this instruction.

This command is equivalent to pressing ALT+ASTERISK (using the ASTERISK key on the numeric keypad).

If the current instruction corresponds to a known source file, WinDbg opens the [Source window](source-window.md) that contains this source file. If no such window exists, WinDbg opens one. The current line is highlighted.

If the current instruction is not in a known source file and the [Disassembly window](disassembly-window.md) is open, WinDbg opens the Disassembly window and the current line is highlighted. However, if the Disassembly window is closed, the **Go to Current Instruction** command does not open it.

This command only changes the WinDbg display. This command does not affect the execution of the target or any other debugger operations.

 

 





