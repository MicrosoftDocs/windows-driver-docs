---
title: Associating a Per-Stream Context With a File Stream
description: Associating a Per-Stream Context With a File Stream
ms.assetid: 99c93574-2ba6-417a-89a4-a5b9a350a8da
keywords:
- filter drivers WDK file system , per-stream context tracking
- file system filter drivers WDK , per-stream context tracking
- per-stream context tracking WDK file system
- tracking per-stream context WDK file system
- associating per-stream context WDK file system
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Associating a Per-Stream Context With a File Stream


## <span id="ddk_associating_a_per_stream_context_with_a_file_stream_if"></span><span id="DDK_ASSOCIATING_A_PER_STREAM_CONTEXT_WITH_A_FILE_STREAM_IF"></span>


A per-stream context structure can be associated with a file stream only after the file system has successfully processed the [**IRP\_MJ\_CREATE**](https://msdn.microsoft.com/library/windows/hardware/ff548630) request to open the stream. This is because it is only after the file system has processed the create request that the file object's FsContext pointer can be considered valid by a file system filter driver. Because the FsContext pointer uniquely identifies a file stream, it is needed to determine whether the file object represents a file stream that the filter has already seen -- and for which the filter has already created a per-stream context. For this reason, it is not unusual for a filter to create a per-stream context in the create dispatch (or "pre-Create") path, only to delete it in the create completion (or "post-Create") path because it turns out to be a duplicate.

To check whether it has already associated another per-stream context with the same file stream, a file system filter driver calls [**FsRtlLookupPerStreamContext**](https://msdn.microsoft.com/library/windows/hardware/ff546945).

If [**FsRtlLookupPerStreamContext**](https://msdn.microsoft.com/library/windows/hardware/ff546945) finds an existing per-stream context for the same file stream, the filter should delete the newly created per-stream context.

If [**FsRtlLookupPerStreamContext**](https://msdn.microsoft.com/library/windows/hardware/ff546945) does not find a per-stream context that your filter has already created previously for the file stream, the filter can call [**FsRtlInsertPerStreamContext**](https://msdn.microsoft.com/library/windows/hardware/ff546194) to associate the newly created stream context with the file stream.

After [**FsRtlInsertPerStreamContext**](https://msdn.microsoft.com/library/windows/hardware/ff546194) is called for a per-stream context, the file system assumes responsibility for deleting and freeing it. If your filter driver allocates a per-stream context and does not call **FsRtlInsertPerStreamContext** for it, your filter driver is still responsible for freeing it by calling [**ExFreePool**](https://msdn.microsoft.com/library/windows/hardware/ff544590).

 

 




