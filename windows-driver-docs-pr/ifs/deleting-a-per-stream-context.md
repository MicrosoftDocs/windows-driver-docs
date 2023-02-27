---
title: Deleting a Per-Stream Context
description: Deleting a Per-Stream Context
keywords:
- filter drivers WDK file system , per-stream context tracking
- file system filter drivers WDK , per-stream context tracking
- per-stream context tracking WDK file system
- tracking per-stream context WDK file system
- deleting per-stream context
ms.date: 02/23/2023
---

# Deleting a Per-Stream Context

> [!NOTE]
> For optimal reliability and performance, use [file system minifilter drivers](filter-manager-concepts.md) with Filter Manager support instead of legacy file system filter drivers. To port your legacy driver to a minifilter driver, see [Guidelines for Porting Legacy Filter Drivers](guidelines-for-porting-legacy-filter-drivers.md).

When a per-stream context that is associated with a file stream is no longer needed, it should be deleted. Stream contexts are deleted in one of two ways:

- Manually, when the filter driver calls [**FsRtlRemovePerStreamContext**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlremoveperstreamcontext).

- Automatically, when the file system calls [**FsRtlTeardownPerStreamContexts**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlteardownperstreamcontexts), which in turn calls the stream context's [**FreeCallback**](/previous-versions/ff547357(v=vs.85)) routine.

## When the Filter Deletes the Per-Stream Context

When a filter driver needs to delete its per-stream context for a file stream while the file stream is still open, it first calls [**FsRtlRemovePerStreamContext**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlremoveperstreamcontext) to remove the context from the global list of contexts associated with the given file. The filter usually frees the context structure after calling **FsRtlRemovePerStreamContext**.

After your filter driver has called [**FsRtlInsertPerStreamContext**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlinsertperstreamcontext) to associate a per-stream context structure with a file stream, it must call [**FsRtlRemovePerStreamContext**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlremoveperstreamcontext) for the context before freeing it. Otherwise, the system crashes when the file stream is closed.

## When the Per-Stream Context's FreeCallback Is Called

When the file stream is being closed or deleted, the file system frees its own stream context for the file stream. At this time, the file system also calls [**FsRtlTeardownPerStreamContexts**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlteardownperstreamcontexts), which in turn calls the [**FreeCallback**](/previous-versions/ff547357(v=vs.85)) routines registered for all of the per-stream contexts contained in the global list of contexts for that file stream. (A **FreeCallback** routine is registered when the filter driver calls [**FsRtlInitPerStreamContext**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlinitperstreamcontext) to initialize a per-stream context structure. For more information, see **FSRTL_PER_STREAM_CONTEXT**.)

**Note**   After your filter driver has called [**FsRtlInsertPerStreamContext**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlinsertperstreamcontext) to associate a per-stream context structure with a file stream, the file system is responsible for ensuring that the [**FreeCallback**](/previous-versions/ff547357(v=vs.85)) routine for the filter's per-stream context is called when there are no longer any open references to the stream.
