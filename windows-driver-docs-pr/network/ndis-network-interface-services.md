---
title: NDIS Network Interface Services
description: NDIS Network Interface Services
ms.assetid: c37d9b7e-bc56-41e6-b41f-92a6df890e8e
keywords:
- NDIS network interfaces WDK , services
- network interfaces WDK , services
- services WDK network interface
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# NDIS Network Interface Services





The NDIS network interfaces programming interface provides services to:

-   Generate a locally unique identifier ( [**NET\_LUID**](https://msdn.microsoft.com/library/windows/hardware/ff568747)) for each interface. NET\_LUID values:
    -   Must persist when the computer restarts. Interface providers must make NET\_LUIDs persistent even if the associated interface is not persistent. For example, this persistence allows the interface provider to free the NET\_LUID index if there is a computer power failure.
    -   Must be associated with an interface type ( *IfType* in RFC 2863).
    -   Must be unique on a local computer.
    -   Can be converted to a text representation because a NET\_LUID is equivalent to the interface name (*ifName* in RFC 2863).
-   Generate a locally unique interface index (a 24-bit value that is also referred to as *IfIndex* ) for each interface. *IfIndex* values have the following properties:
    -   Low numbers are preferred. For example, NDIS reuses the lowest available interface index.
    -   *IfIndex* values do not persist when the computer restarts.
    -   There is a one-to-one correspondence between a [**NET\_LUID**](https://msdn.microsoft.com/library/windows/hardware/ff568747) value and an *IfIndex* value.
-   Map between interface indexes, NET\_LUID values, and "friendly names" (For example, a friendly name as displayed in the network connections folder).

-   Define the layering order of interfaces in a driver stack.

-   Query and set interface properties and tables that NDIS drivers manage and that RFCs 2863 and 2864 specify.

 

 





