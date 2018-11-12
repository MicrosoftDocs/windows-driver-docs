---
title: Varieties of Kernel-Mode Dump Files
description: Varieties of Kernel-Mode Dump Files
ms.assetid: 6db2a755-ed9c-492a-a650-9ae34ae59968
keywords: ["dump file, kernel-mode file types"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Varieties of Kernel-Mode Dump Files


## <span id="ddk_varieties_of_kernel_mode_dump_files_dbg"></span><span id="DDK_VARIETIES_OF_KERNEL_MODE_DUMP_FILES_DBG"></span>


There are five settings for kernel-mode crash dump files:

[Complete Memory Dump](complete-memory-dump.md)

[Kernel Memory Dump](kernel-memory-dump.md)

[Small Memory Dump](small-memory-dump.md)

[Automatic Memory Dump](automatic-memory-dump.md)

[Active Memory Dump](active-memory-dump.md)

The difference between these dump files is one of size. The *Complete Memory Dump* is the largest and contains the most information, including some User-Mode memory. The *Active Memory Dump* is somewhat smaller but contains similar information for most purposes.  The *Kernel Memory Dump* is smaller still and typically omits User-Mode memory, and the *Small Memory Dump* is only 64 KB in size.

If you select *Automatic Memory Dump*, the dump file is the same as a Kernel Memory Dump, but Windows has more flexibility in setting the size of the system paging file.

The advantage to the larger files is that, since they contain more information, they are more likely to help you find the cause of the crash.

The advantage of the smaller files is that they are smaller and written more quickly. Speed is often valuable; if you are running a server, you may want the server to reboot as quickly as possible after a crash, and the reboot will not take place until the dump file has been written.

After a Complete Memory Dump or Kernel Memory Dump has been created, it is possible to create a Small Memory Dump file from the larger dump file. See the [**.dump (Create Dump File)**](-dump--create-dump-file-.md) command for details.

**Note**   Much information can be obtained by analyzing a kernel-mode dump file. However, no kernel-mode dump file can provide as much information as actually debugging the crash directly with a kernel debugger.

 

## <span id="related_topics"></span>Related topics


[Kernel-Mode Dump Files](kernel-mode-dump-files.md)

[Enabling a Kernel-Mode Dump File](enabling-a-kernel-mode-dump-file.md)

 

 






