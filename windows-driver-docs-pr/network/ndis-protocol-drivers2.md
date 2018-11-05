---
title: Protocol drivers
description: Protocol drivers
ms.assetid: e144f9a6-97fc-46ac-82f8-4a1745d280c7
keywords:
- protocol drivers WDK networking , architecture
- NDIS protocol drivers WDK , architecture
- transport protocol drivers WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Protocol drivers





A network protocol, which is the highest driver in the NDIS hierarchy of drivers, is often used as the lowest-level driver in a transport driver that implements a transport protocol stack, such as a TCP/IP stack. A *transport protocol driver* allocates packets, copies data from the sending application into the packet, and sends the packets to the lower-level driver by calling NDIS functions. A protocol driver also provides a protocol interface to receive incoming packets from the next lower-level driver. A transport protocol driver transfers received data to the appropriate client application.

At its lower edge, a protocol driver interfaces with intermediate network drivers and miniport drivers. The protocol driver calls **Ndis*Xxx*** functions to send packets, read and set information that is maintained by lower-level drivers, and use operating system services. The protocol driver also exports a set of entry points (*ProtocolXxx* functions) that NDIS calls for its own purposes or on behalf of lower-level drivers to indicate up receive packets, indicate the status of lower-level drivers, and to otherwise communicate with the protocol driver.

At its upper edge, a transport protocol driver has a private interface to a higher-level driver in the protocol stack.

## Related topics


[NDIS Protocol Drivers](ndis-protocol-drivers.md)

[NDIS Protocol Driver Reference](https://msdn.microsoft.com/library/windows/hardware/ff566829)

 

 






