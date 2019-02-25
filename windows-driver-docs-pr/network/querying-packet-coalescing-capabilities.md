---
title: Querying Packet Coalescing Capabilities
description: Querying Packet Coalescing Capabilities
ms.assetid: CD1839B5-2279-4E8C-ADD8-7869A3123B86
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Querying Packet Coalescing Capabilities


Once the miniport driver is initialized, overlying drivers and applications can issue the following OID query requests to obtain the packet coalescing capabilities of the network adapter:

-   [OID\_RECEIVE\_FILTER\_HARDWARE\_CAPABILITIES](https://msdn.microsoft.com/library/windows/hardware/ff569791)

-   [OID\_RECEIVE\_FILTER\_CURRENT\_CAPABILITIES](https://msdn.microsoft.com/library/windows/hardware/ff569786)

-   [OID\_RECEIVE\_FILTER\_GLOBAL\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff569790)

NDIS handles these OID query requests for miniport drivers and returns the packet coalescing capabilities that the miniport driver registered when NDIS called the driver's [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function. Therefore, these OID query requests are not handled by miniport drivers.

For more information about how the miniport driver registers its packet coalescing capabilities, see [Determining Receive Filtering Capabilities](determining-receive-filtering-capabilities.md).

 

 





