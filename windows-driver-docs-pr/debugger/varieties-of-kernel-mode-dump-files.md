---
title: Varieties of Kernel-Mode Dump Files
description: This article describes the five varieties of Kernel-Mode Dump Files
keywords: ["dump file, kernel-mode file types"]
ms.date: 01/24/2025
ms.topic: concept-article
---

# Varieties of Kernel-Mode Dump Files

There are five settings for kernel-mode crash dump files:

[Complete Memory Dump](complete-memory-dump.md)

[Kernel Memory Dump](kernel-memory-dump.md)

[Small Memory Dump](small-memory-dump.md)

[Automatic Memory Dump](automatic-memory-dump.md)

[Active Memory Dump](active-memory-dump.md)

The difference between these dump files is one of size. The *Complete Memory Dump* is the largest and contains the most information, including some User-Mode memory. The *Active Memory Dump* is somewhat smaller but contains similar information for most purposes.  The *Kernel Memory Dump* is smaller still and typically omits User-Mode memory, and the *Small Memory Dump* is only 64 KB in size.

If you select *Automatic Memory Dump*, the dump file is the same as a Kernel Memory Dump, but Windows has more flexibility in setting the size of the system paging file.

The advantage of larger files is that they contain more information, making them more likely to help you find the cause of the crash.

The advantage of smaller files is that they're quicker to write. Speed is often valuable; if you're running a server, you probably want it to reboot as quickly as possible after a crash. The reboot doesn't take place until the dump file is written.

After a Complete Memory Dump or Kernel Memory Dump is created, you can create a Small Memory Dump file from the larger dump file. For more information, see the [**.dump (Create Dump File)**](../debuggercmds/-dump--create-dump-file-.md) command.

**Note**   You can obtain much information by analyzing a kernel-mode dump file. However, no kernel-mode dump file can provide as much information as debugging the crash directly with a kernel debugger. A dump file is a snapshot in time, where with live debugging, you can view all memory values in real time as the program executes.

## See also

[Kernel-Mode Dump Files](kernel-mode-dump-files.md)

[Enabling a Kernel-Mode Dump File](enabling-a-kernel-mode-dump-file.md)
