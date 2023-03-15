---
title: .dump (Create Dump File)
description: The .dump command creates a user-mode or kernel-mode crash dump file.
keywords: ["Create Dump File (.dump) command", "dump file, Create Dump File (.dump) command", ".dump (Create Dump File) Windows Debugging"]
ms.date: 07/17/2020
topic_type:
- apiref
ms.topic: reference
api_name:
- .dump (Create Dump File)
api_type:
- NA
---

# .dump (Create Dump File)

The **.dump** command creates a user-mode or kernel-mode crash dump file.

```dbgcmd
.dump [options] FileName
.dump /?
```

## Parameters

*Options*  
Represents one or more of the following options.

**/a**  
Create dumps for all processes (requires -u).

**/b[a]**  
Package dump in a CAB and delete dump. Additional information is included if the *a* option is specified.

**/c \<comment\>**  
Add a comment (not supported in all formats).

**/j \<addr\>**  
Provide a JIT_DEBUG_INFO address.

**/o**  
Overwrites an existing dump file with the same name. If this option is not used and there is a file with the same file name, the dump file is not written.

**/u**  
Append unique identifier to dump name.

**/f\[**<em>FullOptions</em>**\]**  
(Kernel mode:) Creates a [complete memory dump](complete-memory-dump.md).

(User mode:) Creates a *full user-mode dump*. For more information, see [Varieties of User-Mode Dump Files](user-mode-dump-files.md#varieties). Despite their names, the largest minidump file actually contains more information than a full user-mode dump. For example, **.dump /mf** or **.dump /ma** creates a larger and more complete file than **.dump /f**. In user mode, **.dump** **/m\[**<em>MiniOptions</em>**\]** is always preferable to **.dump /f**.

You can add the following *FullOptions* to change the contents of the dump file; the option is case-sensitive.

|FullOption|Effect|
|--- |--- |
|**y**| Adds AVX register information to the dump file.|

**/m\[**<em>MiniOptions</em>**\]**  
Creates a *small memory dump* (in kernel mode) or a *minidump* (in user mode) For more information, see [User-Mode Dump Files](user-mode-dump-files.md). If neither **/f** nor **/m** is specified, **/m** is the default.

In user mode, **/m** can be followed with additional *MiniOptions* specifying extra data that is to be included in the dump. If no *MiniOptions* are included, the dump will include module, thread, and stack information, but no additional data. You can add any of the following *MiniOptions* to change the contents of the dump file; they are case-sensitive.

|MiniOption|Effect|
|--- |--- |
|a|Creates a minidump with all optional additions. The /ma option is equivalent to /mfFhut -- it adds full memory data, handle data, unloaded module information, basic memory information, and thread time information to the minidump. Any failure to read inaccessable memory results in termination of the minidump generation.|
|A|The /mA option is equivalent to /ma except that it ignores any failure to read inaccessable memory and continues generating the minidump.|
|f|Adds full memory data to the minidump. All accessible committed pages owned by the target application will be included.|
|F|Adds all basic memory information to the minidump. This adds a stream to the minidump that contains all basic memory information, not just information about valid memory. This allows the debugger to reconstruct the complete virtual memory layout of the process when the minidump is being debugged.|
|h|Adds data about the handles associated with the target application to the minidump.|
|u|Adds unloaded module information to the minidump. This is available only in Windows Server 2003 and later versions of Windows.|
|t|Adds additional thread information to the minidump. This includes thread times, which can be displayed by using the !runaway extension or the .ttime (Display Thread Times) command when debugging the minidump.|
|i|Adds secondary memory to the minidump. Secondary memory is any memory referenced by a pointer on the stack or backing store, plus a small region surrounding this address.|
|p|Adds process environment block (PEB) and thread environment block (TEB) data to the minidump. This can be useful if you need access to Windows system information regarding the application's processes and threads.|
|w|Adds all committed read-write private pages to the minidump.|
|d|Adds all read-write data segments within the executable image to the minidump.|
|c|Adds code sections within images.|
|r|Deletes from the minidump those portions of the stack and store memory that are not useful for recreating the stack trace. Local variables and other data type values are deleted as well. This option does not make the minidump smaller (because these memory sections are simply zeroed), but it is useful if you want to protect the privacy of other applications.|
|R|Deletes the full module paths from the minidump. Only the module names will be included. This is a useful option if you want to protect the privacy of the user's directory structure.|
|y|Adds AVX register information to the dump file.|

### Kernel Mode Options

The following options are available in kernel mode.

**/k**  
Create a dump with kernel memory only.

**/ka**  
Create a dump with active kernel and user mode memory.

## Additional Information

For a description of kernel-mode dump files and an explanation of their use, see [Kernel-Mode Dump Files](kernel-mode-dump-files.md). For a description of user-mode dump files and an explanation of their use, see [User-Mode Dump Files](user-mode-dump-files.md).

## Remarks

This command can be used in a variety of situations:

- During live user-mode debugging, this command directs the target application to generate a dump file, but the target application does not terminate.

- During live kernel-mode debugging, this command directs the target computer to generate a dump file, but the target computer does not crash.

- During crash dump debugging, this command creates a new crash dump file from the old one. This is useful if you have a large crash dump file and want to create a smaller one.

You can control what type of dump file will be produced:

- In kernel mode, to produce a [complete memory dump](complete-memory-dump.md), use the **/f** option. To produce a [small memory dump](small-memory-dump.md), use the **/m** option (or no options). The .dump command cannot produce a [kernel memory dump](kernel-memory-dump.md).

- In user mode, **.dump** **/m\[**<em>MiniOptions</em>**\]** is the best choice. Although "m" stands for "minidump", the dump files created by using this *MiniOption* can vary in size from very small to very large. By specifying the proper *MiniOptions* you can control exactly what information is included. For example, **.dump /ma** produces a dump with a great deal of information. The older command, **.dump /f**, produces a moderately large "standard dump" file and cannot be customized.

You cannot specify which process is dumped. All running processes will be dumped.

The **/xc**, **/xr**, **/xp**, and **/xt** options are used to store exception and context information in the dump file. This allows the [**.ecxr (Display Exception Context Record)**](-ecxr--display-exception-context-record-.md) command to be run on this dump file.

The following example will create a user-mode minidump, containing full memory and handle information:

```dbgcmd
0:000> .dump /mfh myfile.dmp
```

Handle information can be read by using the [**!handle**](-handle.md) extension command.

## See Also

[Varieties of Kernel-Mode Dump Files](varieties-of-kernel-mode-dump-files.md)
