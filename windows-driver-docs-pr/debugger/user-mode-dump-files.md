---
title: User-mode dump files
description: Get an overview of user-mode dump files and how to use them to help resolve bugs and crashes.
keywords: ["dump file, user-mode"]
ms.date: 12/30/2022
---

# User-mode dump files

In this article, get an overview of user-mode dump files and how to use them to help resolve bugs and crashes.

For information about analyzing a dump file, see [Analyze a user-mode dump file](analyzing-a-user-mode-dump-file.md).

<a name="varieties"></a>

## Types of user-mode dump files

Several types of user-mode crash dump files are available. The different types of dump files are divided into two categories:

- [Full user-mode dumps](#full)
- [Minidumps](#minidumps)

You can get a substantial amount of information by analyzing a dump file. However, no dump file can provide the amount of information you get from debugging the crash by using a debugger.

<a name="full"></a>

### Full user-mode dumps

A *full user-mode dump* is the basic user-mode dump file. A full user-mode dump file includes:

- The entire memory space of a process.
- The program's executable image.
- The handle table.
- Other information that helps the debugger reconstruct the memory that was in use when the dump occurred.

You can *shrink* a full user-mode dump file into a minidump. To shrink a full user-mode dump file, first, load the dump file in the debugger. Then, use the [.dump (Create Dump File)](-dump--create-dump-file-.md) command to save a new dump file in minidump format.

Despite their names, the largest minidump file contains more information than the full user-mode dump file. For example, the `.dump /mf` and `.dump /ma` commands create larger and more complete files than the `.dump /f` command.

In user mode, `.dump /m`\[*MiniOptions*\] is often the best choice. The dump files you create by using this switch might vary in size from very small to very large. By specifying the correct *MiniOptions* switch, you can control exactly what information is included.

<a name="minidumps"></a>

### Minidumps

The size and contents of a minidump file vary depending on the program being dumped and the application doing the dumping and the options selected. Sometimes, a minidump file is moderately large and includes the full memory and handle table. Other times, the minidump file is much smaller. For example, a minidump file might contain only information about a single thread, or it might contain only information about modules that are referenced in the stack.

The term *minidump* is misleading because the largest minidump files contain more information than a full user-mode dump file. For example, `.dump /mf` or `.dump /ma` creates a larger and more complete file than `.dump /f`. For this reason, we recommend that you use `.dump /m`\[*MiniOptions*\] instead of `.dump /f` to create all user-mode dump files.

If you create a minidump file by using the debugger, you can choose what information to include. The `.dump /m` command includes basic information about the loaded modules that make up the target process, thread information, and stack information. You can modify the basic command by using any of the switch options that are described in the following table:

| `.dump` option | Effect on dump file |
| --- | --- |
| `/ma` | Creates a minidump with all optional additions. The `/ma` option is equivalent to `/mfFhut`. It adds full memory data, handle data, unloaded module information, basic memory information, and thread time information to the minidump. |
| `/mf` | Adds full memory data to the minidump. All accessible committed pages owned by the target application are included. |
| `/mF` | Adds all basic memory information to the minidump. This switch adds a stream to the minidump that contains all basic memory information, not only information about valid memory. The debugger uses the information to reconstruct the complete virtual memory layout of the process when the minidump is being debugged. |
| `/mh` | Adds data about the handles that are associated with the target application to the minidump. |
| `/mu` | Adds unloaded module information to the minidump. This option is available only in Windows Server 2003 and later versions of Windows. |
| `/mt` | Adds more thread information to the minidump. The thread information includes thread times, which can be displayed by using [.ttime (Display Thread Times)](-ttime--display-thread-times-.md) when you debug the minidump. |
| `/mi` | Adds secondary memory to the minidump. *Secondary memory* is any memory that's referenced by a pointer on the stack or backing store, plus a small region surrounding this address. |
| `/mp` | Adds process environment block and thread environment block data to the minidump. This information can be useful if you need access to Windows system information regarding the application's processes and threads. |
| `/mw` | Adds all committed read-write private pages to the minidump. |
| `/md` | Adds all read-write data segments within the executable image to the minidump. |
| `/mc` | Adds code sections within images.|
| `/mr` | Deletes from the minidump portions of the stack and store memory that aren't used to re-create the stack trace. Local variables and other data type values are also deleted. This option doesn't make the minidump smaller (the unused memory sections are zeroed), but it's useful if you want to protect the privacy of other applications.|
| `/mR` | Deletes the full module paths from the minidump. Only module *names* are included. This option is useful if you want to protect the privacy of the user's directory structure. |

You can combine these switch options. For example, use the command `.dump /mfiu` to create a moderately large minidump that contains unloaded and secondary memory. Use the command `.dump /mrR` to create a minidump that removes some of the user's information. For full syntax details, see [.dump (Create Dump File)](-dump--create-dump-file-.md).

## Tools to use to create a dump file

There are several different tools you can use to create a user-mode dump file:

- ProcDump
- CDB
- WinDbg

### ProcDump

ProcDump is a command-line utility you can use to monitor an application for CPU spikes and to generate crash dumps during a spike. An administrator or developer can use the crash dump files to determine the cause of the spike. ProcDump also includes monitoring for hung windows (by using the same definition of a window hang that Windows and Task Manager use) and unhandled exceptions. You can use ProcDump to generate dumps based on the values of system performance counters. ProcDump also can serve as a general process dump utility that you can embed in other scripts.

For information about creating a user-mode dump file by using the Sysinternals ProcDump utility, see [ProcDump](/sysinternals/downloads/procdump).

### CDB and WinDbg

Console Debugger (CDB) and Windows Debugger (WinDbg) are debugging tools that are included in Windows Software Development Kit and Windows Driver Kit. See options to [install Windows debugger tools](index.md#install-debugging-tools-for-windows).

You can use CDB or WinDbg to create user-mode dump files in multiple ways:

- Create a dump file automatically.
- Create dump files when you debug.
- Shrink an existing dump file.

For more information about the tools, see [Debug by using CDB](debugging-using-cdb-and-ntsd.md) and [Download debugger tools for Windows](debugger-download-tools.md).

## Create a dump file automatically

When an application error occurs, Windows might respond in one of several ways, depending on the postmortem debugging settings. If these settings instruct a debugging tool to create a dump file, a user-mode memory dump file is created. For more information, see [Enable postmortem debugging](enabling-postmortem-debugging.md).

## Create dump files when you're debugging

When CDB or WinDbg is debugging a user-mode application, you can also use the [.dump (Create Dump File)](-dump--create-dump-file-.md) command to create a dump file.

This command doesn't cause the target application to terminate. By selecting specific command options, you can create a minidump file that contains exactly the amount of information you want.

## Shrink an existing dump file

You can use CDB or WinDbg to shrink a dump file. To shrink a dump file, begin debugging an existing dump file. Then, use the `.dump` command to create a dump file of a smaller size.

## Time Travel Debugging

Another option to debug user-mode applications is Time Travel Debugging (TTD). TTD is a tool you can use to record your process while it runs. You can replay the recording of the debugger session to find the bug. You can easily go to different parts of the recording to understand conditions that led up to the bug and how to fix the problem.

TTD has significant advantages over crash dump files, which often are missing the code execution that led to the failure. The ability to travel backwards in the code execution, can be useful in determining the root cause.

For more information, see the [Time Travel Debugging overview](time-travel-debugging-overview.md).

## Next steps

- Learn how to [analyze a user-mode dump file](analyzing-a-user-mode-dump-file.md).
- Get tips to [extract information from a dump file](extracting-information-from-a-dump-file.md).
