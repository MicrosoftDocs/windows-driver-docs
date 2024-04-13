---
title: Querying Packet Coalescing Capabilities
description: Querying Packet Coalescing Capabilities
ms.date: 04/20/2017
---

# Querying Packet Coalescing Capabilities


Once the miniport driver is initialized, overlying drivers and applications can issue the following OID query requests to obtain the packet coalescing capabilities of the network adapter:

-   [OID\_RECEIVE\_FILTER\_HARDWARE\_CAPABILITIES](./oid-receive-filter-hardware-capabilities.md)

-   [OID\_RECEIVE\_FILTER\_CURRENT\_CAPABILITIES](./oid-receive-filter-current-capabilities.md)

-   [OID\_RECEIVE\_FILTER\_GLOBAL\_PARAMETERS](./oid-receive-filter-global-parameters.md)

NDIS handles these OID query requests for miniport drivers and returns the packet coalescing capabilities that the miniport driver registered when NDIS called the driver's [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) function. Therefore, these OID query requests are not handled by miniport drivers.

For more information about how the miniport driver registers its packet coalescing capabilities, see [Determining Receive Filtering Capabilities](determining-receive-filtering-capabilities.md).

 

