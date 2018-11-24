---
title: Guidelines for Managing Packet Coalescing Receive Filters
description: Guidelines for Managing Packet Coalescing Receive Filters
ms.assetid: 7FA44368-1641-478A-927B-020619F39A0D
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Guidelines for Managing Packet Coalescing Receive Filters


If the miniport driver supports NDIS packet coalescing, it must follow these guidelines for managing packet coalescing receive filters:

-   The miniport driver and underlying network adapter must be able to handle the setting and clearing of receive filters dynamically. Individual receive filters may be set or cleared at any time.

-   The miniport driver must maintain a coalesced packet counter. This 64-bit counter contains a value for the number of received packets that have matched a packet coalescing filter. NDIS queries this counter through an OID query request of [OID\_PACKET\_COALESCING\_FILTER\_MATCH\_COUNT](https://msdn.microsoft.com/library/windows/hardware/hh451826).

    **Note**  The miniport driver clears this counter when it transitions to a full-power state by handling an OID set request of [OID\_PNP\_SET\_POWER](https://msdn.microsoft.com/library/windows/hardware/ff569780). The miniport driver also clears the counter when its [*MiniportResetEx*](https://msdn.microsoft.com/library/windows/hardware/ff559432) function is called.

     

-   The miniport driver must not discard the packet coalescing receive filters when it transitions to a low-power state. However, while the network adapter is in a low-power state, it must only filter received packets based on wake-up patterns that have been offloaded to the adapter through OID set requests of [OID\_PNP\_ENABLE\_WAKE\_UP](https://msdn.microsoft.com/library/windows/hardware/ff569775).

    The miniport driver must configure the network adapter with the packet coalescing receive filters when the adapter transitions to a full-power state.

-   The miniport driver must not discard the packet coalescing receive filters when NDIS calls the driver's [*MiniportResetEx*](https://msdn.microsoft.com/library/windows/hardware/ff559432) function. After the driver resets the network adapter, it must configure the adapter with the packet coalescing filters. Also, the driver *must clear* the coalesced packet counter.

    **Note**  The miniport driver must perform this operation regardless of whether the driver sets the *AddressingReset* parameter to TRUE.

     

-   If the miniport driver is operating in the Native 802.11 extensible station (ExtSTA) mode, it must not discard the packet coalescing receive filters when it handles an OID method request of [OID\_DOT11\_RESET\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569409). After the miniport driver performs the 802.11 reset operation, it must configure the network adapter with the packet coalescing receive filters. Also, the driver *must not clear* the coalesced packet counter.

    For more information about the Native 802.11 extensible station mode, see [Extensible Station Operation Mode](https://docs.microsoft.com/previous-versions/windows/hardware/wireless/extensible-station-operation-mode).

    **Note**  NDIS does not support packet coalescing for native 802.11 miniport drivers that operate in extensible access point (ExtAP) mode. For more information about the ExtAP operation mode, see [Extensible Access Point Operation Mode](https://docs.microsoft.com/previous-versions/windows/hardware/wireless/extensible-access-point-operation-mode).

     

 

 





