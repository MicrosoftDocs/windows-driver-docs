---
title: Active Memory Dump
description: Active Memory Dump
ms.assetid: b40979b6-cd9a-4655-8030-8bde25d75113
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Active Memory Dump


## <span id="ddk_kernel_memory_dump_dbg"></span><span id="DDK_KERNEL_MEMORY_DUMP_DBG"></span>


An *Active Memory Dump* is similar to a [Complete Memory Dump](complete-memory-dump.md), but it filters out pages that are not likely to be relevant to troubleshooting problems on the host machine. Because of this filtering, it is typically significantly smaller than a complete memory dump. 

This dump file does include any memory allocated to user-mode applications. It also includes memory allocated to the Windows kernel and hardware abstraction level (HAL), as well as memory allocated to kernel-mode drivers and other kernel-mode programs. The dump includes active pages mapped into the kernel or user space that are useful for debugging, as well as selected Pagefile-backed Transition, Standby, and Modified pages such as the memory allocated with VirtualAlloc or page-file backed sections. Active dumps do not include pages on the free and zeroed lists, the file cache, guest VM pages and various other types of memory that are not likely to be useful during debugging. 

An Active Memory Dump is particularly useful when Windows is hosting virtual machines (VMs). When taking a complete memory dump, the contents of each VM is included. When there are multiple VMs running, this can account for a large amount of memory in use on the host system. Many times, the code activities of interest are in the parent host OS, not the child VMs. An active memory dump filters out the memory associated with all of the child VMs. 

The Active Memory Dump file is written to %SystemRoot%\\Memory.dmp by default.

The Active Memory Dump is available in Windows 10 and later.

**Note**  To suppress missing page error messages when debugging an Active Memory Dump, use the [**.ignore\_missing\_pages**](-ignore-missing-pages--suppress-missing-page-errors-.md) command.

 

## <span id="related_topics"></span>Related topics


[Varieties of Kernel-Mode Dump Files](varieties-of-kernel-mode-dump-files.md)

 

 






