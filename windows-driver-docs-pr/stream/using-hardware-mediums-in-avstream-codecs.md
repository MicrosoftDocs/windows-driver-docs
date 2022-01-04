---
title: Using Hardware Mediums in AVStream Codecs
description: Using Hardware Mediums in AVStream Codecs
keywords:
- AVStream hardware codec support WDK , using hardware mediums
ms.date: 04/20/2017
---

# Using Hardware Mediums in AVStream Codecs


An AVStream minidriver that supports private mediums can transfer data in the device hardware, without an intermediate transfer to system memory.

Specifically, if two filters share the same private medium and medium instance, Media Foundation transfers media exclusively in device hardware. This transfer happens without bringing the functions to the system memory. For example, a decoder and an encoder from the same device can share a private medium, which results in significantly improved performance.

To use private mediums, the minidriver should do the following in the pin's [*AVStrMiniPinProcess*](/windows-hardware/drivers/ddi/ks/nc-ks-pfnkspin) function:

1.  If a driver's custom medium is selected for the pin connection (for example, the pin's medium is not KSMEDIUMSETID\_Standard), the driver should route the data through its private bus. AVStream does not enable stream pointer transport for pins that are connected by using custom mediums.

2.  The driver can determine the connected pin by calling [**KsPinGetConnectedPinFileObject**](/windows-hardware/drivers/ddi/ks/nf-ks-kspingetconnectedpinfileobject).

3.  The driver can then perform operations on the buffer and route it to the connected pin/filter object through its custom medium.

 

