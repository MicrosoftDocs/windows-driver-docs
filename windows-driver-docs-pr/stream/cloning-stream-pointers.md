---
title: Cloning Stream Pointers
author: windows-driver-content
description: Cloning Stream Pointers
ms.assetid: bbe01f48-db86-41c9-b7b8-b48a4a295d21
keywords: ["stream pointers WDK AVStream , cloning", "cloning stream pointers WDK AVStream", "duplicating stream pointers WDK AVStream", "copying stream pointers WDK AVStream"]
---

# Cloning Stream Pointers


## <a href="" id="ddk-cloning-stream-pointers-ksg"></a>


Multiple stream pointers can reference a single frame. To duplicate a stream pointer, call [**KsStreamPointerClone**](https://msdn.microsoft.com/library/windows/hardware/ff567129).

The resulting copy of the stream pointer is referred to as a stream pointer *clone*. The clone is a new stream pointer that is identical to the parent. Initially, the clone references the same frame and has the same lock status. After it is created, a clone is independent of its parent stream pointer.

You can clone leading edge, trailing edge, or current clone stream pointers.

Adding a clone stream pointer increments the reference count on that particular frame. See [Introduction to Stream Pointers](introduction-to-stream-pointers.md) For more information about reference counts.

Enumerate clone stream pointers by using [**KsPinGetFirstCloneStreamPointer**](https://msdn.microsoft.com/library/windows/hardware/ff563512) and [**KsStreamPointerGetNextClone**](https://msdn.microsoft.com/library/windows/hardware/ff567133).

Clones exist until you delete them by calling [**KsStreamPointerDelete**](https://msdn.microsoft.com/library/windows/hardware/ff567130). When the minidriver deletes a clone, AVStream decrements the reference count for the corresponding frame.

See [AVStream DMA Services](avstream-dma-services.md) for an example of how to use stream pointer clones.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Cloning%20Stream%20Pointers%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


