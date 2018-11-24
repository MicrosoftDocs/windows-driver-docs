---
title: Deleting a Per-Stream Context
description: Deleting a Per-Stream Context
ms.assetid: 293a2ba2-af8a-4c1b-bc35-5e37e6e84d57
keywords:
- filter drivers WDK file system , per-stream context tracking
- file system filter drivers WDK , per-stream context tracking
- per-stream context tracking WDK file system
- tracking per-stream context WDK file system
- deleting per-stream context
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Deleting a Per-Stream Context


## <span id="ddk_deleting_a_per_stream_context_if"></span><span id="DDK_DELETING_A_PER_STREAM_CONTEXT_IF"></span>


When a per-stream context that is associated with a file stream is no longer needed, it should be deleted. Stream contexts are deleted in one of two ways:

-   Manually, when the filter driver calls [**FsRtlRemovePerStreamContext**](https://msdn.microsoft.com/library/windows/hardware/ff547238).

-   Automatically, when the file system calls [**FsRtlTeardownPerStreamContexts**](https://msdn.microsoft.com/library/windows/hardware/ff547295), which in turn calls the stream context's [**FreeCallback**](https://msdn.microsoft.com/library/windows/hardware/ff547357) routine.

### <span id="When_the_Filter_Deletes_the_Per-Stream_Context"></span><span id="when_the_filter_deletes_the_per-stream_context"></span><span id="WHEN_THE_FILTER_DELETES_THE_PER-STREAM_CONTEXT"></span>When the Filter Deletes the Per-Stream Context

When a filter driver needs to delete its per-stream context for a file stream while the file stream is still open, it first calls [**FsRtlRemovePerStreamContext**](https://msdn.microsoft.com/library/windows/hardware/ff547238) to remove the context from the global list of contexts associated with the given file. After calling **FsRtlRemovePerStreamContext**, the filter usually frees the context structure.

**Note**   After your filter driver has called [**FsRtlInsertPerStreamContext**](https://msdn.microsoft.com/library/windows/hardware/ff546194) to associate a per-stream context structure with a file stream, it must call [**FsRtlRemovePerStreamContext**](https://msdn.microsoft.com/library/windows/hardware/ff547238) for the context before freeing it. Otherwise, the system will crash when the file stream is closed.

 

### <span id="When_the_Per-Stream_Context_s_FreeCallback_Is_Called"></span><span id="when_the_per-stream_context_s_freecallback_is_called"></span><span id="WHEN_THE_PER-STREAM_CONTEXT_S_FREECALLBACK_IS_CALLED"></span>When the Per-Stream Context's FreeCallback Is Called

When the file stream is being closed or deleted, the file system frees its own stream context for the file stream. At this time, the file system also calls [**FsRtlTeardownPerStreamContexts**](https://msdn.microsoft.com/library/windows/hardware/ff547295), which in turn calls the [**FreeCallback**](https://msdn.microsoft.com/library/windows/hardware/ff547357) routines registered for all of the per-stream contexts contained in the global list of contexts for that file stream. (A **FreeCallback** routine is registered when the filter driver calls [**FsRtlInitPerStreamContext**](https://msdn.microsoft.com/library/windows/hardware/ff546178) to initialize a per-stream context structure. For more information, see **FSRTL\_PER\_STREAM\_CONTEXT**.)

**Note**   After your filter driver has called [**FsRtlInsertPerStreamContext**](https://msdn.microsoft.com/library/windows/hardware/ff546194) to associate a per-stream context structure with a file stream, the file system is responsible for ensuring that the [**FreeCallback**](https://msdn.microsoft.com/library/windows/hardware/ff547357) routine for the filter's per-stream context is called when there are no longer any open references to the stream.

 

 

 




