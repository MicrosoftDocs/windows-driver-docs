---
title: Creating a Per-Stream Context
description: Creating a Per-Stream Context
ms.assetid: e33dba3b-50f7-43d8-b7e8-b7c2c9034d51
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


## <span id="ddk_creating_a_per_stream_context_if"></span><span id="DDK_CREATING_A_PER_STREAM_CONTEXT_IF"></span>


A file system filter driver typically creates a [per-stream context structure](file-streams--stream-contexts--and-per-stream-contexts.md) for a file stream when the file stream is first opened. However, a per-stream context structure can be created and associated with a file stream during any operation.

### <span id="Allocating_the_Per-Stream_Context"></span><span id="allocating_the_per-stream_context"></span><span id="ALLOCATING_THE_PER-STREAM_CONTEXT"></span>Allocating the Per-Stream Context

Per-stream context structures can be allocated from paged or nonpaged pool. To allocate a per-stream context, call [**ExAllocatePoolWithTag**](https://msdn.microsoft.com/library/windows/hardware/ff544520) as shown in the following example:

```cpp
contextSize = sizeof(SPY_STREAM_CONTEXT) + fileName.Length;
ctx = ExAllocatePoolWithTag(NonPagedPool, 
                            contextSize,
                            MYLEGACYFILTER_CONTEXT_TAG);
```

**Note**  If your filter allocates the per-stream context structure from paged pool, it cannot call [**ExAllocatePoolWithTag**](https://msdn.microsoft.com/library/windows/hardware/ff544520) from its create completion routine. This is because completion routines can be called at IRQL DISPATCH\_LEVEL.

 

### <span id="Initializing_the_Per-Stream_Context"></span><span id="initializing_the_per-stream_context"></span><span id="INITIALIZING_THE_PER-STREAM_CONTEXT"></span>Initializing the Per-Stream Context

File system filter drivers call [**FsRtlInitPerStreamContext**](https://msdn.microsoft.com/library/windows/hardware/ff546178) to initialize a per-stream context structure. This routine initializes the FSRTL\_PER\_STREAM\_CONTEXT portion of the context structure. (The remainder of the structure is filter-driver-specific.)

**Note**  If your filter driver creates only one per-stream context structure per file stream, it should pass **NULL** for the *InstanceId* parameter to [**FsRtlInitPerStreamContext**](https://msdn.microsoft.com/library/windows/hardware/ff546178).

 

A filter driver can initialize a per-stream context at any time. However, it must do so before associating the context with a file stream.

 

 




