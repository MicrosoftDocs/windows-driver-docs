---
title: Improved Send and Receive Paths
description: Improved Send and Receive Paths
ms.assetid: 7edecb49-576f-4058-92e8-39f14268a130
keywords:
- NDIS WDK , sending and receiving data
- sending data WDK networking
- receiving data WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Improved Send and Receive Paths





The NDIS 6.0 send and receive paths have been improved as follows to enhance performance:

-   All of the NDIS 6.0 and later driver send and receive functions can transfer a linked list of [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures and their associated [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structures with a single function call. This support for true multipacket send and receive operations substantially reduces the number of function calls that drivers must make.

-   When calling a send or receive function, a driver running at DISPATCH\_LEVEL can indicate its IRQL to NDIS. When NDIS subsequently makes calls to other drivers in the stack, it is not necessary for these drivers to test the IRQL or set it to DISPATCH\_LEVEL. This reduces the overhead that is associated with testing and setting the IRQL in critical code sections.

-   When drivers pass packets up and down the driver stack, they can request NDIS to adjust the NET\_BUFFER data offsets to accommodate header information. When sending a packet, a driver can expand the used data space to accommodate the driver's header information. When indicating a receive packet, a driver can decrease the used data space after the driver is done accessing its header information. This ability to dynamically adjust the used data space in a NET\_BUFFER structure, without allocating and freeing memory or copying data, reduces the overhead that is required to process network data.

For more information about send and receive data handling in NDIS 6.0, see [NET\_BUFFER Architecture](net-buffer-architecture.md).

 

 





