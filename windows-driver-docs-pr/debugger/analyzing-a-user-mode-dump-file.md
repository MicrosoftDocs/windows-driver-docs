---
title: Analyzing a User-Mode Dump File
description: This article describes analyzing a User-Mode Dump File with WinDbg and CDB
keywords: ["dump file, analyzing a user-mode dump file"]
ms.date: 01/24/2025
ms.topic: concept-article
---

# Analyzing a User-Mode Dump File

This article includes:

- [Analyzing a User-Mode Dump File with WinDbg](#analyzing-a-user-mode-dump-file-with-windbg)
- [Analyzing a User-Mode Dump File with CDB](#analyzing-a-user-mode-dump-file-with-cdb)

## Analyzing a User-Mode Dump File with WinDbg

You can analyze user-mode memory dump files with WinDbg. The processor or Windows version that created the dump file doesn't need to match the platform on which you're running WinDbg.

### Installing Symbol Files

Before analyzing the memory dump file, access the symbol files for the version of Windows that generated the dump file. The debugger you choose to analyze the dump file uses these files. For information about working with the symbol server, see [Microsoft Public Symbols](microsoft-public-symbols.md).

You also need to install all the symbol files for the user-mode process, either an application or system service, that caused the system to generate the dump file. If you wrote this code, the symbol files are generated when you compile and link the code. If this code is commercial, contact the software manufacturer to see if symbol files are available.

### Starting WinDbg

To analyze a dump file, start WinDbg with the **-z** command-line option:

**windbg -y** *SymbolPath* **-i** *ImagePath* **-z** *DumpFileName*

The **-v** option (verbose mode) is also useful. For a full list of options, see [**WinDbg Command-Line Options**](windbg-command-line-options.md).

If WinDbg is already running and in dormant mode, you can open a crash dump by selecting the **File | Open Crash Dump** menu command or pressing **CTRL+D**. When the **Open Crash Dump** dialog box appears, enter the full path and name of the crash dump file in the **File name** text box, or use the dialog box to select the proper path and file name. When the proper file is chosen, select **Open**.

You can also open a dump file after the debugger is running by using the [**.opendump (Open Dump File)**](../debuggercmds/-opendump--open-dump-file-.md) command, followed with [**g (Go)**](../debuggercmds/g--go-.md).

You can debug multiple dump files at the same time. To do this, include multiple **-z** switches on the command line (each followed by a different file name), or use [**.opendump**](../debuggercmds/-opendump--open-dump-file-.md) to add additional dump files as debugger targets. For information about how to control a multiple-target session, see [Debugging Multiple Targets](debugging-multiple-targets.md).

Dump files generally end with the extension .dmp or .mdmp. You can use network shares or Universal Naming Convention (UNC) file names for the memory dump file.

It's common to pack dump files into a CAB file. If you specify the file name (including the .cab extension) after the **-z** option or as the argument to an [**.opendump**](../debuggercmds/-opendump--open-dump-file-.md) command, the debugger can read the dump files directly from the CAB. However, if there are multiple dump files stored in a single CAB, the debugger can read only one of them. The debugger doesn't read any additional files from the CAB, even if they're symbol files or executables associated with the dump file.

### Analyzing a Full User Dump File

Analyzing a full user dump file is similar to analyzing a live debugging session. For details about the commands available for debugging dump files in user mode, see the [Debugger Commands](../debuggercmds/debugger-commands.md) reference section.

### Analyzing Minidump Files

Analyzing a user-mode minidump file is done the same way as analyzing a full user dump. However, because the minidump preserves much less memory, you're more limited in the actions you can perform. Commands that attempt to access memory beyond what is preserved in the minidump file don't function properly.

### Additional Techniques

For techniques that you can use to read specific kinds of information from a dump file, see [Extracting Information from a Dump File](extracting-information-from-a-dump-file.md).

## Analyzing a User-Mode Dump File with CDB

You can use CDB to analyze user-mode memory dump files. The processor or Windows version that created the dump file doesn't need to match the platform on which you're running CDB.

### Installing Symbol Files

Before analyzing the memory dump file, access the symbol files for the version of Windows that generated the dump file. The debugger you choose to analyze the dump file uses these files. For information about working with the symbol server, see [Microsoft Public Symbols](microsoft-public-symbols.md).

You also need to install all the symbol files for the user-mode process, either an application or system service, that caused the system to generate the dump file. If you wrote this code, the symbol files are generated when you compile and link the code. If this code is commercial, contact the software manufacturer to see if symbol files are available.

### Starting CDB

To analyze a dump file, start CDB with the **-z** command-line option:

**cdb -y** *SymbolPath* **-i** *ImagePath* **-z** *DumpFileName*

The **-v** option (verbose mode) is also useful. For a full list of options, see [**CDB Command-Line Options**](cdb-command-line-options.md).

You can also open a dump file after the debugger is running by using the [**.opendump (Open Dump File)**](../debuggercmds/-opendump--open-dump-file-.md) command, followed with [**g (Go)**](../debuggercmds/g--go-.md). This command allows you to debug multiple dump files at the same time.


You can debug multiple dump files at the same time. To do this, include multiple **-z** switches on the command line (each followed by a different file name), or use [**.opendump**](../debuggercmds/-opendump--open-dump-file-.md) to add additional dump files as debugger targets. For information about how to control a multiple-target session, see [Debugging Multiple Targets](debugging-multiple-targets.md).

Dump files generally end with the extension .dmp or .mdmp. You can use network shares or Universal Naming Convention (UNC) file names for the memory dump file.

It's common to pack dump files into a CAB file. If you specify the file name (including the .cab extension) after the **-z** option or as the argument to an [**.opendump**](../debuggercmds/-opendump--open-dump-file-.md) command, the debugger can read the dump files directly from the CAB. However, if there are multiple dump files stored in a single CAB, the debugger can read only one of them. The debugger doesn't read any additional files from the CAB, even if they're symbol files or executables associated with the dump file.

### Analyzing a Full User Dump File

Analyzing a full user dump file is similar to analyzing a live debugging session. For details about the commands available for debugging dump files in user mode, see the [Debugger Commands](../debuggercmds/debugger-commands.md) reference section.

### Analyzing Minidump Files

Analysis of a user-mode minidump file is done in the much the same way as a full user dump. However, because the minidump preserves much less memory, you're more limited in the actions you can perform. Commands that attempt to access memory beyond what the minidump file preserves don't function properly.

### Additional Techniques

For techniques that you can use to read specific kinds of information from a dump file, see [Extracting Information from a Dump File](extracting-information-from-a-dump-file.md).
