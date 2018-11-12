---
title: Opening a Dump File Using CDB
description: Opening a Dump File Using CDB
ms.assetid: 204DFA6F-2BA2-4B76-AFE0-28207710322B
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Opening a Dump File Using CDB


## <span id="Command_Prompt"></span><span id="command_prompt"></span><span id="COMMAND_PROMPT"></span>Command Prompt


In a Command Prompt window, you can open a user-mode dump file when you launch CDB. Enter the following command.

**cdb -y** *SymbolPath* **-i** *ImagePath* **-z** *DumpFileName*

The **-v** option (verbose mode) is also useful. For more information about the command-line syntax, see [**CDB Command-Line Options**](cdb-command-line-options.md)

## <span id="CDB_Command_Line"></span><span id="cdb_command_line"></span><span id="CDB_COMMAND_LINE"></span>CDB Command Line


You can also open a dump file after the debugger is running by entering the [**.opendump (Open Dump File)**](-opendump--open-dump-file-.md) command, followed by [**g (Go)**](g--go-.md). This allows you to debug multiple dump files at the same time.

 

 





