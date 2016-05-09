---
title: Associating a Per-Stream Context With a File Stream
description: Associating a Per-Stream Context With a File Stream
ms.assetid: 99c93574-2ba6-417a-89a4-a5b9a350a8da
keywords: ["filter drivers WDK file system , per-stream context tracking", "file system filter drivers WDK , per-stream context tracking", "per-stream context tracking WDK file system", "tracking per-stream context WDK file system", "associating per-stream context WDK file system"]
---

# Associating a Per-Stream Context With a File Stream


## <span id="ddk_associating_a_per_stream_context_with_a_file_stream_if"></span><span id="DDK_ASSOCIATING_A_PER_STREAM_CONTEXT_WITH_A_FILE_STREAM_IF"></span>


A per-stream context structure can be associated with a file stream only after the file system has successfully processed the [**IRP\_MJ\_CREATE**](https://msdn.microsoft.com/library/windows/hardware/ff548630) request to open the stream. This is because it is only after the file system has processed the create request that the file object's FsContext pointer can be considered valid by a file system filter driver. Because the FsContext pointer uniquely identifies a file stream, it is needed to determine whether the file object represents a file stream that the filter has already seen -- and for which the filter has already created a per-stream context. For this reason, it is not unusual for a filter to create a per-stream context in the create dispatch (or "pre-Create") path, only to delete it in the create completion (or "post-Create") path because it turns out to be a duplicate.

To check whether it has already associated another per-stream context with the same file stream, a file system filter driver calls [**FsRtlLookupPerStreamContext**](https://msdn.microsoft.com/library/windows/hardware/ff546945).

If [**FsRtlLookupPerStreamContext**](https://msdn.microsoft.com/library/windows/hardware/ff546945) finds an existing per-stream context for the same file stream, the filter should delete the newly created per-stream context.

If [**FsRtlLookupPerStreamContext**](https://msdn.microsoft.com/library/windows/hardware/ff546945) does not find a per-stream context that your filter has already created previously for the file stream, the filter can call [**FsRtlInsertPerStreamContext**](https://msdn.microsoft.com/library/windows/hardware/ff546194) to associate the newly created stream context with the file stream.

After [**FsRtlInsertPerStreamContext**](https://msdn.microsoft.com/library/windows/hardware/ff546194) is called for a per-stream context, the file system assumes responsibility for deleting and freeing it. If your filter driver allocates a per-stream context and does not call **FsRtlInsertPerStreamContext** for it, your filter driver is still responsible for freeing it by calling [**ExFreePool**](https://msdn.microsoft.com/library/windows/hardware/ff544590).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Associating%20a%20Per-Stream%20Context%20With%20a%20File%20Stream%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




