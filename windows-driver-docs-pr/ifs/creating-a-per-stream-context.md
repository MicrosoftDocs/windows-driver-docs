---
title: Creating a Per-Stream Context
author: windows-driver-content
description: Creating a Per-Stream Context
ms.assetid: e33dba3b-50f7-43d8-b7e8-b7c2c9034d51
keywords: ["filter drivers WDK file system , per-stream context tracking", "file system filter drivers WDK , per-stream context tracking", "per-stream context tracking WDK file system", "tracking per-stream context WDK file system", "allocating per-stream context", "initializing per-stream context"]
---

# Creating a Per-Stream Context


## <span id="ddk_creating_a_per_stream_context_if"></span><span id="DDK_CREATING_A_PER_STREAM_CONTEXT_IF"></span>


A file system filter driver typically creates a [per-stream context structure](file-streams--stream-contexts--and-per-stream-contexts.md) for a file stream when the file stream is first opened. However, a per-stream context structure can be created and associated with a file stream during any operation.

### <span id="Allocating_the_Per-Stream_Context"></span><span id="allocating_the_per-stream_context"></span><span id="ALLOCATING_THE_PER-STREAM_CONTEXT"></span>Allocating the Per-Stream Context

Per-stream context structures can be allocated from paged or nonpaged pool. To allocate a per-stream context, call [**ExAllocatePoolWithTag**](https://msdn.microsoft.com/library/windows/hardware/ff544520) as shown in the following example:

```
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Creating%20a%20Per-Stream%20Context%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


