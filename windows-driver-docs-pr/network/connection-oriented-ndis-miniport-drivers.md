---
title: Connection-Oriented NDIS Miniport Drivers
description: Connection-Oriented NDIS Miniport Drivers
ms.assetid: 58f9bed1-274c-4f60-87cd-f0b44871eb60
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

-   [**MiniportCoCreateVc**](https://msdn.microsoft.com/library/windows/hardware/ff559354)

-   [**MiniportCoDeleteVc**](https://msdn.microsoft.com/library/windows/hardware/ff559358)

-   [**MiniportCoActivateVc**](https://msdn.microsoft.com/library/windows/hardware/ff559351)

-   [**MiniportCoDeactivateVc**](https://msdn.microsoft.com/library/windows/hardware/ff559356)

-   [**MiniportCoSendNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff559365)

-   [**MiniportCoOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff559362)

For more information about registering these functions, see [**NdisMRegisterMiniportDriver**](https://msdn.microsoft.com/library/windows/hardware/ff563654).

 

 





