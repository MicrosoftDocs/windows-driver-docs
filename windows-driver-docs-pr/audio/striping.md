---
title: Striping
description: Striping
ms.assetid: 29ab650c-0c3b-4693-a277-4d9ba63b7b66
keywords:
- striping WDK audio
- HD Audio, striping
- High Definition Audio (HD Audio), striping
- HD Audio, bandwidth
- High Definition Audio (HD Audio), bandwidth
- bus bandwidth WDK audio
- bandwidth WDK audio
- allocating bandwidth
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Striping


The HD Audio architecture supports a technique called *striping* that can reduce the amount of bus bandwidth that render streams consume. If the HD Audio hardware interface provides more than one SDO line, striping can increase the rate at which a render DMA engine can transfer data by alternately distributing the bits in the data stream among the SDO lines. The first bit (the most significant bit) travels over SDO0, the second bit travels over SDO1, and so on. For example, with two SDO lines, striping effectively doubles the transfer rate by splitting the stream between the two SDO lines. A DMA engine that uses striping to transfer a render stream over two SDO lines consumes only half the bus bandwidth that it would consume if it did not use striping.

The function driver enables striping through the [**AllocateRenderDmaEngine**](https://msdn.microsoft.com/library/windows/hardware/ff536181) routine's *stripe* call parameter.

For more information about striping, see the *Intel High Definition Audio Specification* at the [Intel HD Audio](https://go.microsoft.com/fwlink/p/?linkid=42508) website.

 

 




