---
title: Kernel Memory Dump
description: Kernel Memory Dump
ms.assetid: 466f5b92-c9bd-4050-9ef8-469979ba0cbe
keywords: ["dump file, Kernel Memory Dump", "Kernel Memory Dump"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Kernel Memory Dump


## <span id="ddk_kernel_memory_dump_dbg"></span><span id="DDK_KERNEL_MEMORY_DUMP_DBG"></span>


A *Kernel Memory Dump* contains all the memory in use by the kernel at the time of the crash.

This kind of dump file is significantly smaller than the Complete Memory Dump. Typically, the dump file will be around one-third the size of the physical memory on the system. This quantity will vary considerably, depending on your circumstances.

This dump file will not include unallocated memory, or any memory allocated to user-mode applications. It only includes memory allocated to the Windows kernel and hardware abstraction level (HAL), as well as memory allocated to kernel-mode drivers and other kernel-mode programs.

For most purposes, this crash dump is the most useful. It is significantly smaller than the Complete Memory Dump, but it only omits those portions of memory that are unlikely to have been involved in the crash.

Since this kind of dump file does not contain images of any user-mode executables residing in memory at the time of the crash, you may also need to set the executable image path if these executables turn out to be important.

The Kernel Memory Dump file is written to %SystemRoot%\\Memory.dmp by default.

If a second bug check occurs and another Kernel Memory Dump (or Complete Memory Dump) is created, the previous file will be overwritten.

To suppress missing page error messages when debugging a Kernel Memory Dump, use the [**.ignore\_missing\_pages**](-ignore-missing-pages--suppress-missing-page-errors-.md) command.

## <span id="related_topics"></span>Related topics


[Varieties of Kernel-Mode Dump Files](varieties-of-kernel-mode-dump-files.md)

 

 






