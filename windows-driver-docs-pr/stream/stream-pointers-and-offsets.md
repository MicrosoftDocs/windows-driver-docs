---
title: Stream Pointers and Offsets
author: windows-driver-content
description: Stream Pointers and Offsets
ms.assetid: ef9dc015-f0ee-49a6-8774-cfb0223c8b12
keywords:
- stream pointers WDK AVStream , offsets
- offsets WDK AVStream
- stream positions WDK AVStream
- input positions WDK AVStream
- output positions WDK AVStream
- AVStream pointers WDK
- AVStream offsets WDK
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Stream Pointers and Offsets


## <a href="" id="ddk-stream-pointers-and-offsets-ksg"></a>


A [**KSSTREAM\_POINTER**](https://msdn.microsoft.com/library/windows/hardware/ff567139) structure contains two [**KSSTREAM\_POINTER\_OFFSET**](https://msdn.microsoft.com/library/windows/hardware/ff567140) structures that index input and output positions within a frame. A minidriver can either manipulate these offsets or access the data at frame resolution.

To advance a stream pointer within a frame, the minidriver calls [**KsStreamPointerAdvanceOffsets**](https://msdn.microsoft.com/library/windows/hardware/ff567126) and [**KsStreamPointerAdvanceOffsetsAndUnlock**](https://msdn.microsoft.com/library/windows/hardware/ff567127).

Minidrivers that access stream data with virtual addresses can use these offsets to specify a stream position at byte resolution. Minidrivers that use scatter/gather physical mappings can specify stream position at the granularity of a [**KSMAPPING**](https://msdn.microsoft.com/library/windows/hardware/ff563394) structure.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Stream%20Pointers%20and%20Offsets%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


