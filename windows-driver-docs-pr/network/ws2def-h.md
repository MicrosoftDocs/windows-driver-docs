---
title: Ws2def.h
description: This section contains kernel mode network driver topics for the Ws2def.h header.
ms.assetid: D84A448E-5810-485F-9CAC-4366E4223DBE
keywords:
- Ws2def.h network drivers
ms.date: 08/08/2017
ms.localizationpriority: medium
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



