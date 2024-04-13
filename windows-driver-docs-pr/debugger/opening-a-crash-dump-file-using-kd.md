---
title: Opening a Dump File Using KD
description: Opening a Dump File Using KD
ms.date: 11/28/2017
---

# Opening a Dump File Using KD


## <span id="Command_Prompt"></span><span id="command_prompt"></span><span id="COMMAND_PROMPT"></span>Command Prompt


In a Command Prompt window, you can open a dump file when you launch KD. Use the following command.

**kd -y** *SymbolPath* **-i** *ImagePath* **-z** *DumpFileName*

The **-v** option (verbose mode) is also useful. For more information about the command-line syntax, see [**KD Command-Line Options**](kd-command-line-options.md).

## <span id="KD_Command_Line"></span><span id="kd_command_line"></span><span id="KD_COMMAND_LINE"></span>KD Command Line


You can also open a dump file after the debugger is running by entering the [**.opendump (Open Dump File)**](../debuggercmds/-opendump--open-dump-file-.md) command, followed by [**g (Go)**](../debuggercmds/g--go-.md).

 

 