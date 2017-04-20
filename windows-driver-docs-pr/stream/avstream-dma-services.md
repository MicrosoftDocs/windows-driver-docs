---
title: AVStream DMA Services
author: windows-driver-content
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
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# AVStream DMA Services


## <a href="" id="ddk-avstream-dma-services-ksg"></a>


To develop an AVStream minidriver that uses direct memory access (DMA), you can perform standard DMA directly into user-mode capture buffers or you can implement common buffer DMA.

Both methods require that your driver obtain a DMA adapter by calling [**IoGetDmaAdapter**](https://msdn.microsoft.com/library/windows/hardware/ff549220).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20AVStream%20DMA%20Services%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


