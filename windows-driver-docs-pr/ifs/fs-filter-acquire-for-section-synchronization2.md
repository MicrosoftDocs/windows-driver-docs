---
title: Checking the Oplock State of an FS_FILTER_ACQUIRE_FOR_SECTION_SYNCHRONIZATION Operation
description: Checking the Oplock State of an FS_FILTER_ACQUIRE_FOR_SECTION_SYNCHRONIZATION operation
ms.date: 02/07/2025
ms.topic: concept-article
---

# Checking the oplock state of an FS_FILTER_ACQUIRE_FOR_SECTION_SYNCHRONIZATION operation

The FS_FILTER_ACQUIRE_FOR_SECTION_SYNCHRONIZATION operation corresponds to an [FsFilter callback](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-fs_filter_callbacks) *PreAcquireForSectionSynchronization* operation. The file system receives this operation before the memory manager creates a memory-mapped section for a portion of a file.

The following [oplock break](breaking-oplocks.md) conditions apply when both of the following conditions are true:

* The **[FS_FILTER_CALLBACK_DATA](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-fs_filter_callback_data).Parameters.AcquireForSectionSynchronization.SyncType** field contains **SyncTypeCreateSection**.
* The **FS_FILTER_CALLBACK_DATA.Parameters.AcquireForSectionSynchronization.PageProtection** field contains either or both of the flags PAGE_READWRITE or PAGE_EXECUTE_READWRITE.

These conditions indicate that the memory manager is creating a writeable memory-mapped section.

## Conditions for Read, Read-Handle, Read-Write, and Read-Write-Handle request types

* Always break to None.
* No acknowledgment is required; the operation proceeds immediately.

## Conditions for all other request types

This operation doesn't affect other (legacy) oplocks.
