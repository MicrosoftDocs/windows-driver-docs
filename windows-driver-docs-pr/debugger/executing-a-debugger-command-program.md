---
title: Executing a Debugger Command Program
description: Executing a Debugger Command Program
ms.assetid: ad28a5d6-0d6a-42c0-82f3-6760a8c773ab
keywords: ["debugger command program, execution"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Executing a Debugger Command Program


## <span id="ddk_debugger_command_program_execution_dbg"></span><span id="DDK_DEBUGGER_COMMAND_PROGRAM_EXECUTION_DBG"></span>


You can execute a debugger command program in one of the following ways:

-   Enter all of the statements in the [Debugger Command window](debugger-command-window.md) as a single string, with individual statements and commands separated by semicolons.

-   Add all of the statements in a script file on a single line, with individual statements and commands separated by semicolons. Then, run this script file by using one of the methods described in [Using Script Files](using-script-files.md).

-   Add all of the statements in a script file, with each statement on a separate line. (Alternatively, separate statements by any combination of carriage returns and semicolons.) Then, run this script file by using the [**$&gt;&lt; (Run Script File)**](-----------------------a---run-script-file-.md) or **$$&gt;&lt; (Run Script File)** command. These commands open the specified script file, replace all carriage returns with semicolons, and execute the resulting text as a single command block.

 

 





