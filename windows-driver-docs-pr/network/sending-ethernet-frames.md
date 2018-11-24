---
title: Sending Ethernet Frames
description: Sending Ethernet Frames
ms.assetid: 9d1037b9-ef5c-4ed8-9204-5729eff2cea3
keywords:
- Ethernet WDK networking
- frames WDK networking
- TCP/IP transport of Ethernet frames WDK networking
- sending Ethernet frames
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Sending Ethernet Frames





The Windows TCP/IP transport supports a set of requirements for sending Ethernet frames. Any driver (for example, a MUX intermediate driver or filter driver) that originates send requests or modifies the send requests of overlying drivers must support the requirements that the TCP/IP transport implements.

**Note**  If any driver in a driver stack does not follow these requirements, underlying miniport drivers, MUX intermediate drivers, and filter drivers might behave unpredictably.

 

For Ethernet send requests, drivers must support these requirements:

-   If a driver originates a send request, the driver should allocate a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure for the Ethernet frames. The **NetBufferListInfo** member in each NET\_BUFFER\_LIST structure must include the out-of-band (OOB) data that is required for the particular use. The OOB data applies to all of the [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structures that are associated with a NET\_BUFFER\_LIST structure.

-   If a driver originates a send request, the driver should allocate one or more NET\_BUFFER structures for the Ethernet frames and link these structures to the NET\_BUFFER\_LIST structure. Each NET\_BUFFER structure that is linked to a NET\_BUFFER\_LIST structure describes a single Ethernet frame. The driver may chain multiple NET\_BUFFER\_LIST structures in a send request. 

-   All NET\_BUFFER structures that are associated with a NET\_BUFFER\_LIST structure must have the same Ethernet frame type and IP protocol version (IPv4 or IPv6).

-   All NET\_BUFFER structures that are associated with a NET\_BUFFER\_LIST structure must have the same source and destination MAC addresses.

-   If a driver is sending TCP or UDP frames, all of the NET\_BUFFER structures that are associated with a NET\_BUFFER\_LIST structure must be associated with same TCP or UDP connection.
    **Note**  Subject to the following requirements, transmitted Ethernet frames can be split. That is, multiple memory descriptor lists (MDLs) can be associated with a NET\_BUFFER structure in a send request.

     

-   Do not split the MAC header of the transmit Ethernet frame across multiple MDLs. Treat the Virtual LAN (VLAN) (or Priority) flag, if present, as part of the MAC header. Therefore, this flag must be in the same MDL as the rest of the MAC header.

-   If a driver changes the links in the MDL chain in a NET\_BUFFER structure or the NET\_BUFFER chain in a NET\_BUFFER\_LIST structure, the driver must restore the links to the original configuration before it returns ownership of the NET\_BUFFER\_LIST to an overlying driver. However, drivers are not required to restore the links between NET\_BUFFER\_LIST structures.

 

 





