---
title: Memory Manager Support Routines
description: Memory Manager Support Routines
ms.assetid: 9cdcddd7-a086-415d-a7bd-5d149019b8b4
ms.date: 09/30/2019
ms.localizationpriority: medium
---

# Memory Manager Support Routines

The following table lists the subset of system-supplied memory management support routines that can be used by kernel-mode file systems and file system (minifilter and legacy) filter drivers. These routines cannot be used by device drivers.

In addition to the routines documented here, file systems and file system filter drivers can also call any of the **Mm**_Xxx_ routines that are described in the Kernel-Mode Driver Architecture Reference and that are declared in *ntifs.h*.

**Header File:** *ntifs.h*

**Prefix: Mm**_Xxx_

| Function or Macro | Description |
| ----------------- | ----------- |
| **MmCanFileBeTruncated** | Checks whether a file can be truncated. |
| **MmDoesFileHaveUserWritableReferences** | Returns the number of writable references for a file object. |
| **MmFlushImageSection** | Flushes the image section for a file. |
| **MmForceSectionClosed** | Deletes the data and image sections for a file that is no longer in use. |
| **MmGetMaximumFileSectionSize** | Returns the maximum possible size of a file section for the current version of Windows. |
| **MmIsRecursiveIoFault** | Determines whether the current page fault is occurring during an I/O operation. |
| **MmPrefetchPages** | Reads groups of pages from secondary storage in the optimal fashion. |
| **MmSetAddressRangeModified** | Marks currently valid pages in the specified range of the system cache as modified. |
