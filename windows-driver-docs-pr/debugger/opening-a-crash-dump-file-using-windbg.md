---
title: Open a dump file with WinDbg
description: Learn about various ways to open a crash memory dump file using WinDbg in a debugging session.
ms.date: 12/13/2022
---

# Open a dump file with WinDbg

There are several ways you can use WinDbg to open a crash memory dump file to debug code.

## WinDbg menu

If WinDbg is already running and is in dormant mode, you can open a dump file by choosing **Open crash dump** from the **File** menu or by pressing CTRL+D. When the **Open crash dump** dialog box appears, enter the full path and name of the crash dump file in the **File name** box, or use the dialog box to select the proper path and file name. When the proper file has been chosen, select **Open**.

## Command prompt

In a command-prompt window, you can open a dump file when you launch WinDbg. Use the following command:

```Console
windbg -y <SymbolPath> -i <ImagePath> -z <DumpFileName>
```

The `-v` option, which is verbose mode, is also useful. For more information about command-line syntax, see [WinDbg command-line options](windbg-command-line-options.md).

## Debugger command window

If WinDbg is already in a kernel-mode debugging session, you can open a dump file by using the [.opendump (open dump file)](../debuggercmds/-opendump--open-dump-file-.md) command, followed by the [g (Go)](../debuggercmds/g--go-.md) command.
