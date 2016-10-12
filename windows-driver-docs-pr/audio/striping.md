---
title: Striping
description: Striping
ms.assetid: 29ab650c-0c3b-4693-a277-4d9ba63b7b66
keywords: ["striping WDK audio", "HD Audio, striping", "High Definition Audio (HD Audio), striping", "HD Audio, bandwidth", "High Definition Audio (HD Audio), bandwidth", "bus bandwidth WDK audio", "bandwidth WDK audio", "allocating bandwidth"]
---

# Striping


The HD Audio architecture supports a technique called *striping* that can reduce the amount of bus bandwidth that render streams consume. If the HD Audio hardware interface provides more than one SDO line, striping can increase the rate at which a render DMA engine can transfer data by alternately distributing the bits in the data stream among the SDO lines. The first bit (the most significant bit) travels over SDO0, the second bit travels over SDO1, and so on. For example, with two SDO lines, striping effectively doubles the transfer rate by splitting the stream between the two SDO lines. A DMA engine that uses striping to transfer a render stream over two SDO lines consumes only half the bus bandwidth that it would consume if it did not use striping.

The function driver enables striping through the [**AllocateRenderDmaEngine**](https://msdn.microsoft.com/library/windows/hardware/ff536181) routine's *stripe* call parameter.

For more information about striping, see the *Intel High Definition Audio Specification* at the [Intel HD Audio](http://go.microsoft.com/fwlink/p/?linkid=42508) website.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Striping%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


