---
title: Using Hardware Mediums in AVStream Codecs
author: windows-driver-content
description: Using Hardware Mediums in AVStream Codecs
MS-HAID:
- 'shed\_dg\_30c99718-2581-4878-b68f-de3e7d47654a.xml'
- 'stream.using\_hardware\_mediums\_in\_avstream\_codecs'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 07c25875-c549-4d47-ac0d-605f2aa9daa4
keywords: ["AVStream hardware codec support WDK , using hardware mediums"]
---

# Using Hardware Mediums in AVStream Codecs


An AVStream minidriver that supports private mediums can transfer data in the device hardware, without an intermediate transfer to system memory.

Specifically, if two filters share the same private medium and medium instance, Media Foundation transfers media exclusively in device hardware. This transfer happens without bringing the functions to the system memory. For example, a decoder and an encoder from the same device can share a private medium, which results in significantly improved performance.

To use private mediums, the minidriver should do the following in the pin's [*AVStrMiniPinProcess*](https://msdn.microsoft.com/library/windows/hardware/ff556351) function:

1.  If a driver's custom medium is selected for the pin connection (for example, the pin's medium is not KSMEDIUMSETID\_Standard), the driver should route the data through its private bus. AVStream does not enable stream pointer transport for pins that are connected by using custom mediums.

2.  The driver can determine the connected pin by calling [**KsPinGetConnectedPinFileObject**](https://msdn.microsoft.com/library/windows/hardware/ff563508).

3.  The driver can then perform operations on the buffer and route it to the connected pin/filter object through its custom medium.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Using%20Hardware%20Mediums%20in%20AVStream%20Codecs%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


