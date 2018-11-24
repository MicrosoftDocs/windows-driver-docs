---
title: Specifying Allocator Framing in AVStream Codecs
description: Specifying Allocator Framing in AVStream Codecs
ms.assetid: e5b042ae-9b9c-48e9-9f0c-449e205316a9
keywords:
- AVStream hardware codec support WDK , specifying allocator framing
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Specifying Allocator Framing in AVStream Codecs


Generally, the allocator requirements of a KS pin determine the physical size of streaming buffers that are provided by AVStream.

However, because input pins just pass samples downstream, the buffer size requirements specified in an input pin's KSALLOCATOR\_FRAMING\_EX ([**KS\_FRAMING\_ITEM**](https://msdn.microsoft.com/library/windows/hardware/ff567646).**PhysicalRange**) are not used. The driver should still determine the input frame size after the media type is set and adjust its internal structures accordingly.

Although drivers cannot influence the frame size on input pins, the maximum number of outstanding frames (KS\_FRAMING\_ITEM.**Frames**) does depend on the pin's allocator requirements. For smooth dataflow among streaming components and fewer glitches, we recommend that both the encoder and decoder filters have input and output pins that support a minimum of three outstanding frames.

In addition to providing allocator framing information in the [**KSPIN\_DESCRIPTOR\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff563534) at device initialization time, the driver should also update the relevant [**KSALLOCATOR\_FRAMING\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff560982) structure. This update should be based on the pin's connection media type in the vendor-supplied [*AVStrMiniPinSetDataFormat*](https://msdn.microsoft.com/library/windows/hardware/ff556355) callback routine.

 

 




