---
title: Connection-Oriented NDIS Miniport Drivers
description: Connection-Oriented NDIS Miniport Drivers
keywords:
- miniport drivers WDK networking , types
- NDIS miniport drivers WDK , types
- connection-oriented drivers WDK networking , miniport drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Connection-Oriented NDIS Miniport Drivers





A *connection-oriented miniport driver* controls one or more miniport adapters for connection-oriented media. Connection-oriented miniport drivers must be deserialized. For more information about deserialized drivers, see [Deserialized NDIS Miniport Drivers](deserialized-ndis-miniport-drivers.md).

A connection-oriented miniport driver provides an interface between connection-oriented protocol drivers (connection-oriented clients and call managers) and NIC hardware (for example, physical miniport adapters). For a summary of connection-oriented operations performed by a connection-oriented miniport driver, see [Connection-Oriented Operations Performed by Miniport Drivers](connection-oriented-operations-performed-by-miniport-drivers.md).

A connection-oriented miniport driver must register the following *MiniportXxx* functions that are specific to connection-oriented operations:

-   [**MiniportCoCreateVc**](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_co_create_vc)

-   [**MiniportCoDeleteVc**](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_co_delete_vc)

-   [**MiniportCoActivateVc**](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_co_activate_vc)

-   [**MiniportCoDeactivateVc**](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_co_deactivate_vc)

-   [**MiniportCoSendNetBufferLists**](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_co_send_net_buffer_lists)

-   [**MiniportCoOidRequest**](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_co_oid_request)

For more information about registering these functions, see [**NdisMRegisterMiniportDriver**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismregisterminiportdriver).

 

