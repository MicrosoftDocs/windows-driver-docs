---
title: AVStream DMA Services
description: AVStream DMA Services
ms.assetid: ba1c525b-26b0-4778-b58b-f4169cfb972e
keywords:
- AVStream WDK , hardware
- hardware WDK AVStream
- DMA services WDK AVStream
- Direct Memory Access WDK AVStream
- capture buffers WDK AVStream
- buffers WDK AVStream
- AVStream DMA WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# AVStream DMA Services





To develop an AVStream minidriver that uses direct memory access (DMA), you can perform standard DMA directly into user-mode capture buffers or you can implement common buffer DMA.

Both methods require that your driver obtain a DMA adapter by calling [**IoGetDmaAdapter**](https://msdn.microsoft.com/library/windows/hardware/ff549220).

 

 




