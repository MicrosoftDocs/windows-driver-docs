---
title: Complete Memory Dump
description: Complete Memory Dump
ms.assetid: ccc4d22a-89af-4c7d-a982-f77c682cd001
keywords: ["dump file, Complete Memory Dump", "Complete Memory Dump"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Complete Memory Dump


## <span id="ddk_complete_memory_dump_dbg"></span><span id="DDK_COMPLETE_MEMORY_DUMP_DBG"></span>


A *Complete Memory Dump* is the largest kernel-mode dump file. This file includes all of the physical memory that is used by Windows. A complete memory dump does not, by default, include physical memory that is used by the platform firmware.

Starting with Windows 8, you can register a [*BugCheckAddPagesCallback*](https://msdn.microsoft.com/library/windows/hardware/ff540669) routine that is called during a complete memory dump. Your *BugCheckAddPagesCallback* routine can specify driver-specific data to add to the dump file. For example, this additional data can include physical pages that are not mapped to the system address range in virtual memory but that contain information that can help you to debug your driver. The *BugCheckAddPagesCallback* routine might add to the dump file any driver-owned physical pages that are unmapped or that are mapped to user-mode addresses in virtual memory.

This dump file requires a pagefile on your boot drive that is at least as large as your main system memory; it should be able to hold a file whose size equals your entire RAM plus one megabyte.

The Complete Memory Dump file is written to %SystemRoot%\\Memory.dmp by default.

If a second bug check occurs and another Complete Memory Dump (or Kernel Memory Dump) is created, the previous file will be overwritten.

## <span id="related_topics"></span>Related topics


[Varieties of Kernel-Mode Dump Files](varieties-of-kernel-mode-dump-files.md)

 

 






