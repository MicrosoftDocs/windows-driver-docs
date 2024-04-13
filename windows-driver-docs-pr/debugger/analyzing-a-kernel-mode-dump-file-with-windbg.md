---
title: Analyze a Kernel-Mode Dump File by Using WinDbg
description: Learn how to analyze a kernel-mode dump file by using WinDbg. Analysis of a dump file is similar to analysis of a live debugging session.
keywords: ["WinDbg, analyzing a kernel-mode dump file", "CAB file containing a dump file, analyzing kernel-mode dump file with WinDbg"]
ms.date: 12/21/2023
---

# Analyze a kernel-mode dump file by using WinDbg

You can analyze kernel-mode memory dump files by using WinDbg.

## Start WinDbg

Dump files generally end with the extension *.dmp* or *.mdmp*. You can use network shares or Universal Naming Convention file names for the memory dump file. The processor or Windows version used to create a dump file doesn't need to match the platform on which KD runs.

To analyze a dump file, start WinDbg and include the **-z** command-line option:

```console
windbg -y <SymbolPath> -i <ImagePath> -z <DumpFileName>
```

The **-v** option, which is verbose mode, is also useful. For a full list of options, see [WinDbg command-line options](windbg-command-line-options.md).

If WinDbg is already running in dormant mode, open a crash dump by selecting the **File | Open Crash Dump** menu command or pressing **Ctrl**+**D**. When the **Open Crash Dump** dialog box appears, enter the full path and name of the crash dump file in **File name**, or use the dialog box to select a path and file name. After you specify a file, select **Open**.

Or open a dump file after the debugger is running by using the [.opendump (Open Dump File)](../debuggercmds/-opendump--open-dump-file-.md) command, followed by the [g (Go)](../debuggercmds/g--go-.md) command.

You can debug multiple dump files at the same time. Include multiple **-z** switches on the command line, each followed by a different file name, or run [.opendump](../debuggercmds/-opendump--open-dump-file-.md) to add other dump files as debugger targets. For more information about how to control a multiple-target session, see [Debugging Multiple Targets](debugging-multiple-targets.md).

Dump files can be packed into a CAB file. If you specify the file name, including the *.cab* file name extension, after the **-z** option or as the argument to an [.opendump](../debuggercmds/-opendump--open-dump-file-.md) command, the debugger reads the dump files directly.

If there are multiple dump files stored in a single CAB file, the debugger reads only one of them. The debugger doesn't read any other files from the CAB, even if there are symbol files or other files associated with the dump file.

## Analyze the dump file

To analyze a kernel memory dump or a small memory dump, you might need to set the executable image path to point to executable files in memory during the crash.

Analysis of a dump file is similar to analysis of a live debugging session. For details about commands available for debugging dump files in kernel mode, see the [Debugger commands](../debuggercmds/debugger-commands.md) reference section.

In most cases, begin by using [!analyze](../debuggercmds/-analyze.md). This extension command performs automatic analysis of the dump file, which often provides useful information.

The [.bugcheck (Display bug check data)](../debuggercmds/-bugcheck--display-bug-check-data-.md) command shows the bug check code and its parameters. For information about a specific error, see the [Bug check code reference](bug-check-code-reference2.md).

The following debugger extensions are especially useful for analyzing a kernel-mode crash dump:

- [lm](../debuggercmds/lm--list-loaded-modules-.md)
- [!kdext\*.locks](../debuggercmds/-locks---kdext--locks-.md)
- [!memusage](../debuggercmds/-memusage.md)
- [!vm](../debuggercmds/-vm.md)
- [!errlog](../debuggercmds/-errlog.md)
- [!process 0 0](../debuggercmds/-process.md)
- [!process 0 7](../debuggercmds/-process.md)

For techniques to read specific kinds of information from a dump file, see [Extracting information from a dump file](extracting-information-from-a-dump-file.md).

## See also

[Get started with WinDbg (kernel mode)](getting-started-with-windbg--kernel-mode-.md)

[Debugger operation](debugger-operation-win8.md)

[Debugging techniques](debugging-techniques.md)

[Download and install the WinDbg Windows debugger](./index.md)

[!analyze](../debuggercmds/-analyze.md)