---
title: Associating a Per-Stream Context With a File Stream
description: Associating a Per-Stream Context With a File Stream
keywords:
- filter drivers WDK file system , per-stream context tracking
- file system filter drivers WDK , per-stream context tracking
- per-stream context tracking WDK file system
- tracking per-stream context WDK file system
- associating per-stream context WDK file system
ms.date: 02/23/2023
---

# Associating a Per-Stream Context With a File Stream

> [!NOTE]
> For optimal reliability and performance, use [file system minifilter drivers](filter-manager-concepts.md) with Filter Manager support instead of legacy file system filter drivers. To port your legacy driver to a minifilter driver, see [Guidelines for Porting Legacy Filter Drivers](guidelines-for-porting-legacy-filter-drivers.md).

A per-stream context structure can be associated with a file stream only after the file system has successfully processed the [**IRP_MJ_CREATE**](irp-mj-create.md) request to open the stream. The reason is because it's only after the file system has processed the create request that a legacy file system filter driver can consider the file object's FsContext pointer to be valid. Because the FsContext pointer uniquely identifies a file stream, it's needed to determine whether the file object represents a file stream that the filter has already seen, and for which the filter has already created a per-stream context. For this reason, it isn't unusual for a filter to create a per-stream context in the create dispatch (or "pre-Create") path, only to delete it in the create completion (or "post-Create") path because it turns out to be a duplicate.

To check whether it has already associated another per-stream context with the same file stream, a file system filter driver calls [**FsRtlLookupPerStreamContext**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtllookupperstreamcontext).

If [**FsRtlLookupPerStreamContext**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtllookupperstreamcontext) finds an existing per-stream context for the same file stream, the filter should delete the newly created per-stream context.

If [**FsRtlLookupPerStreamContext**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtllookupperstreamcontext) doesn't find a per-stream context that your filter has already created previously for the file stream, the filter can call [**FsRtlInsertPerStreamContext**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlinsertperstreamcontext) to associate the newly created stream context with the file stream.

After [**FsRtlInsertPerStreamContext**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlinsertperstreamcontext) is called for a per-stream context, the file system assumes responsibility for deleting and freeing it. If your filter driver allocates a per-stream context and doesn't call **FsRtlInsertPerStreamContext** for it, your filter driver is still responsible for freeing it by calling [**ExFreePool**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-exfreepool).
