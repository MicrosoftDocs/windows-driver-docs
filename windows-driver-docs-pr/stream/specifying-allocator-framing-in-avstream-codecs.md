---
title: Specifying Allocator Framing in AVStream Codecs
author: windows-driver-content
description: Specifying Allocator Framing in AVStream Codecs
ms.assetid: e5b042ae-9b9c-48e9-9f0c-449e205316a9
keywords:
- AVStream hardware codec support WDK , specifying allocator framing
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Specifying Allocator Framing in AVStream Codecs


Generally, the allocator requirements of a KS pin determine the physical size of streaming buffers that are provided by AVStream.

However, because input pins just pass samples downstream, the buffer size requirements specified in an input pin's KSALLOCATOR\_FRAMING\_EX ([**KS\_FRAMING\_ITEM**](https://msdn.microsoft.com/library/windows/hardware/ff567646).**PhysicalRange**) are not used. The driver should still determine the input frame size after the media type is set and adjust its internal structures accordingly.

Although drivers cannot influence the frame size on input pins, the maximum number of outstanding frames (KS\_FRAMING\_ITEM.**Frames**) does depend on the pin's allocator requirements. For smooth dataflow among streaming components and fewer glitches, we recommend that both the encoder and decoder filters have input and output pins that support a minimum of three outstanding frames.

In addition to providing allocator framing information in the [**KSPIN\_DESCRIPTOR\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff563534) at device initialization time, the driver should also update the relevant [**KSALLOCATOR\_FRAMING\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff560982) structure. This update should be based on the pin's connection media type in the vendor-supplied [*AVStrMiniPinSetDataFormat*](https://msdn.microsoft.com/library/windows/hardware/ff556355) callback routine.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Specifying%20Allocator%20Framing%20in%20AVStream%20Codecs%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


