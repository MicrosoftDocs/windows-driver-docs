---
title: Allocating DMA Engines
description: Allocating DMA Engines
ms.assetid: 45b772ce-e6ae-4102-bad4-734f8f079817
keywords:
- HD Audio, DMA engines
- High Definition Audio (HD Audio), DMA engines
- allocating DMA engines
- DMA engine allocation WDK audio
- render DMA engines WDK audio
- capture DMA engines WDK audio
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Allocating DMA Engines


The HD Audio controller contains a fixed number of DMA engines. Each engine can perform scatter/gather transfers for a single render or capture stream.

Three types of DMA engines are available:

-   Render DMA engines, which can handle only render streams.

-   Capture DMA engines, which can handle only capture streams.

-   Bidirectional DMA engines, which can be configured to handle either render or capture streams.

When allocating a DMA engine for a render stream, the [**AllocateCaptureDmaEngine**](https://msdn.microsoft.com/library/windows/hardware/ff536177) routine allocates a render DMA engine if one is available. If the supply of render DMA engines is exhausted, the routine allocates a bidirectional DMA engine if one is available.

Similarly, when allocating a DMA engine for a capture stream, the [**AllocateRenderDmaEngine**](https://msdn.microsoft.com/library/windows/hardware/ff536181) routine allocates a capture DMA engine if one is available. If the supply of capture DMA engines is exhausted, the routine allocates a bidirectional DMA engine if one is available.

The Allocate*Xxx*DmaEngine routines are available in both versions of the HD Audio DDI.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Allocating%20DMA%20Engines%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


