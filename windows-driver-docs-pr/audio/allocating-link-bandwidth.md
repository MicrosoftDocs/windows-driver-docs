---
title: Allocating Link Bandwidth
description: Allocating Link Bandwidth
ms.assetid: 7a5d5364-d869-4f6a-a7c3-9326ec347150
keywords:
- HD Audio, bandwidth
- High Definition Audio (HD Audio), bandwidth
- bus bandwidth WDK audio
- bandwidth WDK audio
- allocating bandwidth
- link bandwidth WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Allocating Link Bandwidth


The HD Audio Link has a finite amount of bus bandwidth available for render and capture streams to use. To ensure glitchless audio, the HD Audio bus driver manages bus bandwidth as a shared resource. When a function driver allocates a DMA engine, it must also allocate a portion of the available bus bandwidth for the DMA engine's render or capture stream to use.

A fixed amount of bus bandwidth is available on the HD Audio Link's serial data in (SDI) lines and on the serial data out (SDO) lines. The HD Audio bus driver monitors bandwidth consumption separately on the SDI and SDO lines. If a request to allocate input or output bus bandwidth exceeds the available bandwidth, the bus driver fails the request.

When the function driver calls the bus driver's [**AllocateCaptureDmaEngine**](https://msdn.microsoft.com/library/windows/hardware/ff536177) and [**AllocateRenderDmaEngine**](https://msdn.microsoft.com/library/windows/hardware/ff536181) routines, it specifies a stream format. The stream format specifies the stream's sample rate, sample size, and number of channels. From this information, the Allocate*Xxx*DmaEngine routine determines the stream's bus bandwidth requirements. If sufficient bandwidth is available, the routine allocates the required bandwidth for the DMA engine to use. Otherwise, the call to Allocate*Xxx*DmaEngine fails.

A function driver can call [**ChangeBandwidthAllocation**](https://msdn.microsoft.com/library/windows/hardware/ff536229) to request a change in the bandwidth allocation for an existing DMA engine allocation.

The Allocate*Xxx*DmaEngine and [**ChangeBandwidthAllocation**](https://msdn.microsoft.com/library/windows/hardware/ff536229) routines are available in both versions of the HD Audio DDI.

 

 




