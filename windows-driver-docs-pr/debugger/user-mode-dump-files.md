---
title: User-Mode Dump Files
description: User-Mode Dump Files
keywords: ["dump file, user-mode"]
ms.date: 12/03/2019
ms.localizationpriority: medium
---

# User-Mode Dump Files

This section includes:

- [Varieties of User-Mode Dump Files](#varieties)

- [Creating a User-Mode Dump File](#creating)

For information on analyzing a dump file, see [Analyzing a User-Mode Dump File](analyzing-a-user-mode-dump-file.md).

## <span id="varieties"></span><span id="VARIETIES"></span> Varieties of User-Mode Dump Files

There are several kinds of user-mode crash dump files, but they are divided into two categories:

[Full User-Mode Dumps](#full)

[Minidumps](#minidumps)

The difference between these dump files is one of size. Minidumps are usually more compact, and can be easily sent to an analyst.

**Note**   Much information can be obtained by analyzing a dump file. However, no dump file can provide as much information as actually debugging the crash directly with a debugger.

## <span id="full"></span><span id="FULL"></span>Full User-Mode Dumps

A *full user-mode dump* is the basic user-mode dump file.

This dump file includes the entire memory space of a process, the program's executable image itself, the handle table, and other information that will be useful to the debugger in reconstructing the memory that was in use when the dump occurred.

It is possible to "shrink" a full user-mode dump file into a minidump. Simply load the dump file into the debugger and then use the [**.dump (Create Dump File)**](-dump--create-dump-file-.md) command to save a new dump file in minidump format.

**Note**   Despite their names, the largest "minidump" file actually contains more information than the full user-mode dump. For example, **.dump /mf** or **.dump /ma** will create a larger and more complete file than **.dump /f**.

In user mode, **.dump /m\[**<em>MiniOptions</em>**\]** is the best choice. The dump files created with this switch can vary in size from very small to very large. By specifying the proper *MiniOptions* you can control exactly what information is included.

## <span id="minidumps"></span><span id="MINIDUMPS"></span>Minidumps

A user-mode dump file that includes only selected parts of the memory associated with a process is called a *minidump*.

The size and contents of a minidump file vary depending on the program being dumped and the application doing the dumping. Sometimes, a minidump file is fairly large and includes the full memory and handle table. Other times, it is much smaller -- for example, it might only contain information about a single thread, or only contain information about modules that are actually referenced in the stack.

The name "minidump" is misleading, because the largest minidump files actually contain more information than the "full" user-mode dump. For example, **.dump /mf** or **.dump /ma** will create a larger and more complete file than **.dump /f**. For this reason, **.dump /m**\[*MiniOptions*\] recommended over **.dump /f** for all user-mode dump file creation.

If you are creating a minidump file with the debugger, you can choose exactly what information to include. A simple **.dump /m** command will include basic information about the loaded modules that make up the target process, thread information, and stack information. This can be modified by using any of the following options:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">.dump option</th>
<th align="left">Effect on dump file</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>/ma</strong></p></td>
<td align="left"><p>Creates a minidump with all optional additions. The <strong>/ma</strong> option is equivalent to <strong>/mfFhut</strong> -- it adds full memory data, handle data, unloaded module information, basic memory information, and thread time information to the minidump.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>/mf</strong></p></td>
<td align="left"><p>Adds full memory data to the minidump. All accessible committed pages owned by the target application will be included.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>/mF</strong></p></td>
<td align="left"><p>Adds all basic memory information to the minidump. This adds a stream to the minidump that contains all basic memory information, not just information about valid memory. This allows the debugger to reconstruct the complete virtual memory layout of the process when the minidump is being debugged.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>/mh</strong></p></td>
<td align="left"><p>Adds data about the handles associated with the target application to the minidump.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>/mu</strong></p></td>
<td align="left"><p>Adds unloaded module information to the minidump. This is only available in Windows Server 2003 and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>/mt</strong></p></td>
<td align="left"><p>Adds additional thread information to the minidump. This includes thread times, which can be displayed by using <strong><a href="-ttime--display-thread-times-.md" data-raw-source="[.ttime (Display Thread Times)](-ttime--display-thread-times-.md)">.ttime (Display Thread Times)</a></strong> when debugging the minidump.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>/mi</strong></p></td>
<td align="left"><p>Adds <em>secondary memory</em> to the minidump. Secondary memory is any memory referenced by a pointer on the stack or backing store, plus a small region surrounding this address.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>/mp</strong></p></td>
<td align="left"><p>Adds process environment block (PEB) and thread environment block (TEB) data to the minidump. This can be useful if you need access to Windows system information regarding the application's processes and threads.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>/mw</strong></p></td>
<td align="left"><p>Adds all committed read-write private pages to the minidump.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>/md</strong></p></td>
<td align="left"><p>Adds all read-write data segments within the executable image to the minidump.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>/mc</strong></p></td>
<td align="left"><p>Adds code sections within images.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>/mr</strong></p></td>
<td align="left"><p>Deletes from the minidump those portions of the stack and store memory that are not useful for recreating the stack trace. Local variables and other data type values are deleted as well. This option does not make the minidump smaller (since these memory sections are simply zeroed), but it is useful if you wish to protect the privacy of other applications.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>/mR</strong></p></td>
<td align="left"><p>Deletes the full module paths from the minidump. Only the module <em>names</em> will be included. This is a useful option if you wish to protect the privacy of the user's directory structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>/mk "</strong> <em>FileName</em> <strong>"</strong></p></td>
<td align="left"><p>(Windows Vista only) Creates a kernel-mode minidump in addition to the user-mode minidump. The kernel-mode minidump will be restricted to the same threads that are stored in the user-mode minidump. <em>FileName</em> must be enclosed in quotation marks.</p></td>
</tr>
</tbody>
</table>

These options can be combined. For example, the command **.dump /mfiu** can be used to create a fairly large minidump, or the command **.dump /mrR** can be used to create a minidump that preserves the user's privacy. For full syntax details, see [**.dump (Create Dump File)**](-dump--create-dump-file-.md).

## <span id="creating"></span><span id="CREATING"></span>Creating a User-Mode Dump File

There are several different tools that can be used to create a user-mode dump file: CDB, WinDbg and Procdump.

## <span id="procdump"></span><span id="Procdump"></span>ProcDump

ProcDump is a command-line utility whose primary purpose is monitoring an application for CPU spikes and generating crash dumps during a spike that an administrator or developer can use to determine the cause of the spike. ProcDump also includes hung window monitoring (using the same definition of a window hang that Windows and Task Manager use), unhandled exception monitoring and can generate dumps based on the values of system performance counters. It also can serve as a general process dump utility that you can embed in other scripts.

For information about creating a user-mode dump file using the Sysinternals ProcDump utility, see [ProcDump](/sysinternals/downloads/procdump).

## <span id="cdb-windbg"></span><span id="CDB-WINDBG"></span>CDB and WinDbg

CDB and WinDbg can create user-mode dump files in a variety of ways.

### <span id="creating_a_dump_file_automatically"></span><span id="CREATING_A_DUMP_FILE_AUTOMATICALLY"></span>Creating a Dump File Automatically

When an application error occurs, Windows can respond in several different ways, depending on the postmortem debugging settings. If these settings instruct a debugging tool to create a dump file, a user-mode memory dump file will be created. For more information, see [Enabling Postmortem Debugging](enabling-postmortem-debugging.md).

### <span id="creating_dump_files_while_debugging"></span><span id="CREATING_DUMP_FILES_WHILE_DEBUGGING"></span>Creating Dump Files While Debugging

When CDB or WinDbg is debugging a user-mode application, you can also use the [**.dump (Create Dump File)**](-dump--create-dump-file-.md) command to create a dump file.

This command does not cause the target application to terminate. By selecting the proper command options, you can create a minidump file that contains exactly the amount of information you wish.

### <span id="shrinking_an_existing_dump_file"></span><span id="SHRINKING_AN_EXISTING_DUMP_FILE"></span>Shrinking an Existing Dump File

CDB and WinDbg can also be used to *shrink* a dump file. To do this, begin debugging an existing dump file, and then use the **.dump** command to create a dump file of smaller size.

## <span id="cdb-windbg"></span><span id="CDB-WINDBG"></span> Time Travel Debugging (TTD)

In addition to CDB, WinDbg and Procdump, another option to debug user mode applications is Time Travel Debugging (TTD). Time Travel Debugging, is a tool that allows you to record an execution of your process running, then replay it later both forwards and backwards. Time Travel Debugging (TTD) can help you debug issues easier by letting you "rewind" your debugger session, instead of having to reproduce the issue until you find the bug.

TTD allows you to go back in time to better understand the conditions that lead up to the bug and replay it multiple times to learn how best to fix the problem.

TTD can have advantages over crash dump files, which often are missing the code execution that led up to the ultimate failure.

For more information on Time Travel Debugging (TTD), see [Time Travel Debugging - Overview](time-travel-debugging-overview.md).
