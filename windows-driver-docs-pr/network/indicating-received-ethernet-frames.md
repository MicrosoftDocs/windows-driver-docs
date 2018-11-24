---
title: Indicating Received Ethernet Frames
description: Indicating Received Ethernet Frames
ms.assetid: 39f35a54-1d80-4a14-b48c-2dbbfde9c86f
keywords:
- Ethernet WDK networking
- frames WDK networking
- TCP/IP transport of Ethernet frames WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Indicating Received Ethernet Frames





The Windows TCP/IP protocol driver imposes a set of requirements for receiving Ethernet frames. Any driver that originates receive indications of Ethernet frames or modifies receive indications of underlying drivers must support the general requirements that TCP/IP imposes. These drivers include Ethernet miniport drivers, MUX intermediate drivers, and filter drivers.

**Note**  If a driver does not follow these requirements, overlying drivers (such as the TCP/IP transport, MUX intermediate drivers, and filter drivers) might behave unpredictably.

 

Drivers that originate Ethernet receive indications must support the following requirements:

-   The driver must allocate a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure for the received Ethernet frame. Each **NET\_BUFFER\_LIST** structure must include the out-of-band (OOB) data that is defined in the **NetBufferListInfo** member of the **NET\_BUFFER\_LIST** required for the particular use.

-   The driver must allocate a [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structure for the frame and link it to a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure. The Ethernet miniport must assign exactly one **NET\_BUFFER** structure to a **NET\_BUFFER\_LIST** structure when indicating received data. This restriction applies only to the Ethernet receive path. It is not applicable to the other media types, such as the native 802.11 wireless LAN interface. or NDIS in general.

-   Starting with NDIS 6.1, under certain scenarios, a [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structure can be associated with multiple memory descriptor lists (MDLs) for the received Ethernet frame. Even though a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure must contain a single **NET\_BUFFER** structure, using multiple MDLs allows the driver to split the received packet data into separate buffers.

    For example, Ethernet drivers that support the header-data split interface split a received Ethernet frame by using a linked list of multiple MDLs that are associated with a single [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structure. For more information, see [Header-Data Split](header-data-split.md).

    For simplicity and performance reasons, we highly recommend that drivers that don't support header-data split use only one MDL for each [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structure.

    **Note**  In NDIS 6.0 for Windows Vista, each [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structure must contain only one MDL.

     

-   Drivers must not split received Ethernet frames in the middle of the IP header, IPv4 options, IPsec headers, IPv6 extension headers, or upper-layer protocol headers, unless the first MDL contains at least as many bytes as NDIS specified for the lookahead size.

NDIS protocol and filter drivers must support split Ethernet frames in receive indications if such split frames comply with the restrictions that are defined in the preceding list item. The restrictions ensure that the protocol and filter drivers are compatible with future Windows versions.

 

 





