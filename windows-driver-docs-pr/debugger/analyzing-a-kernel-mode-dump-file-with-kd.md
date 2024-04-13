---
title: Analyzing a Kernel-Mode Dump File with KD
description: Analyzing a Kernel-Mode Dump File with KD
keywords: ["KD, analyzing a dump file", "CAB file containing a dump file, analyzing kernel-mode dump file with KD"]
ms.date: 11/09/2022
---

# Analyzing a Kernel-Mode Dump File with KD


Kernel-mode memory dump files can be analyzed by KD. The processor or Windows version that the dump file was created on does not need to match the platform on which KD is being run.

### Starting KD

To analyze a dump file, start KD with the **-z** command-line option:

**kd -y** *SymbolPath* **-i** *ImagePath* **-z** *DumpFileName*

The **-v** option (verbose mode) is also useful. For a full list of options, see [**KD Command-Line Options**](kd-command-line-options.md).

You can also open a dump file after the debugger is running by using the [**.opendump (Open Dump File)**](../debuggercmds/-opendump--open-dump-file-.md) command, followed with [**g (Go)**](../debuggercmds/g--go-.md).

It is possible to debug multiple dump files at the same time. This can be done by including multiple **-z** switches on the command line (each followed by a different file name), or by using [**.opendump**](../debuggercmds/-opendump--open-dump-file-.md) to add additional dump files as debugger targets. For information about how to control a multiple-target session, see [Debugging Multiple Targets](debugging-multiple-targets.md).

Dump files generally end with the extension .dmp or .mdmp. You can use network shares or Universal Naming Convention (UNC) file names for the memory dump file.

It is also common for dump files to be packed into a CAB file. If you specify the file name (including the .cab extension) after the **-z** option or as the argument to an [**.opendump**](../debuggercmds/-opendump--open-dump-file-.md) command, the debugger can read the dump files directly out of the CAB. However, if there are multiple dump files stored in a single CAB, the debugger will only be able to read one of them. The debugger will not read any additional files from the CAB, even if they were symbol files or other files associated with the dump file.

### Analyzing the Dump File

If you are analyzing a Kernel Memory Dump or a Small Memory Dump, you may need to set the executable image path to point to any executable files which may have been loaded in memory at the time of the crash.

Analysis of a dump file is similar to analysis of a live debugging session. See the [Debugger Commands](../debuggercmds/debugger-commands.md) reference section for details on which commands are available for debugging dump files in kernel mode.

In most cases, you should begin by using [**!analyze**](../debuggercmds/-analyze.md). This extension command performs automatic analysis of the dump file and can often result in a lot of useful information.

The [**.bugcheck (Display Bug Check Data)**](../debuggercmds/-bugcheck--display-bug-check-data-.md) shows the bug check code and its parameters. Look up this bug check in the [Bug Check Code Reference](bug-check-code-reference2.md) for information about the specific error.

The following debugger extensions are especially useful for analyzing a kernel-mode crash dump:

[**lm**](../debuggercmds/lm--list-loaded-modules-.md)

[**!kdext\*.locks**](../debuggercmds/-locks---kdext--locks-.md)

[**!memusage**](../debuggercmds/-memusage.md)

[**!vm**](../debuggercmds/-vm.md)

[**!errlog**](../debuggercmds/-errlog.md)

[**!process 0 0**](../debuggercmds/-process.md)

[**!process 0 7**](../debuggercmds/-process.md)

For techniques that can be used to read specific kinds of information from a dump file, see [Extracting Information from a Dump File](extracting-information-from-a-dump-file.md).


 