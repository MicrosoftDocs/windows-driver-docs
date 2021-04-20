---
title: Creating a Per-Stream Context
description: Creating a Per-Stream Context
keywords:
- filter drivers WDK file system , per-stream context tracking
- file system filter drivers WDK , per-stream context tracking
- per-stream context tracking WDK file system
- tracking per-stream context WDK file system
- allocating per-stream context
- initializing per-stream context
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating a Per-Stream Context

Legacy file system filter drivers that use a per-stream context structure containing a [**FSRTL_PER_STREAM_CONTEXT**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_fsrtl_per_stream_context) structure can take advantage of built-in per-stream context support in Microsoft Windows XP and later.

A file system filter driver typically creates a [per-stream context structure](file-streams--stream-contexts--and-per-stream-contexts.md) for a file stream when the file stream is first opened. However, a per-stream context structure can be created and associated with a file stream during any operation.

## Allocating the Per-Stream Context

Per-stream context structures can be allocated from paged or nonpaged pool. To allocate a per-stream context, call [**ExAllocatePoolWithTag**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exallocatepoolwithtag) as shown in the following example:

```cpp
contextSize = sizeof(SPY_STREAM_CONTEXT) + fileName.Length;
ctx = ExAllocatePoolWithTag(NonPagedPool,
                            contextSize,
                            MYLEGACYFILTER_CONTEXT_TAG);
```

> [!NOTE]
> If your filter allocates the per-stream context structure from paged pool, it cannot call [**ExAllocatePoolWithTag**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exallocatepoolwithtag) from its create completion routine. This is because completion routines can be called at IRQL DISPATCH_LEVEL.

### Initializing the Per-Stream Context

File system filter drivers call [**FsRtlInitPerStreamContext**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlinitperstreamcontext) to initialize a per-stream context structure. This routine initializes the FSRTL_PER_STREAM_CONTEXT portion of the context structure. (The remainder of the structure is filter-driver-specific.)

> [!NOTE]
> If your filter driver creates only one per-stream context structure per file stream, it should pass **NULL** for the *InstanceId* parameter to [**FsRtlInitPerStreamContext**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlinitperstreamcontext).

A filter driver can initialize a per-stream context at any time. However, it must do so before associating the context with a file stream.
