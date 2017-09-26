---
title: Ws2def.h
author: windows-driver-content
description: This section contains kernel mode network driver topics for the Ws2def.h header.
ms.assetid: D84A448E-5810-485F-9CAC-4366E4223DBE
keywords:
- Ws2def.h network drivers
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Ws2def.h

This section contains kernel mode network driver topics for the Ws2def.h header. This header is included in the Windows SDK as it is also shared with user mode networking applications.

The Ws2def.h header contains definitions for the Winsock2 specification. It is included in Winsock2.h. User mode applications should include Winsock2.h rather than including Ws2def.h directly. Ws2def.h cannot be included by a module that also includes Winsock.h.

> [!IMPORTANT]
> This section's topics contains pages for definitions, macros, OIDs, status indications, and other data structures that are not part of network driver reference (structures, enumerations, functions, and callbacks). 
>
> For more information about network driver reference for this header, see [Ws2def.h (reference)](https://msdn.microsoft.com/library/windows/hardware/mt808757).

## In this section

* [AF_INET](af-inet.md)
* [AF_INET6](af-inet6.md)
* [SIO_ADDRESS_LIST_CHANGE](sio-address-list-change.md)
* [SIO_ADDRESS_LIST_QUERY](sio-address-list-query.md)
* [SO_BROADCAST](so-broadcast.md)
* [SO_CONDITIONAL_ACCEPT](so-conditional-accept.md)
* [SO_EXCLUSIVEADDRUSE](so-exclusiveaddruse.md)
* [SO_KEEPALIVE](so-keepalive.md)
* [SO_RCVBUF](so-rcvbuf.md)
* [SO_REUSEADDR](so-reuseaddr.md)

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20Ws2def.h%20%20RELEASE:%20%288/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


