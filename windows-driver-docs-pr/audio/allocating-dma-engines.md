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
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 




