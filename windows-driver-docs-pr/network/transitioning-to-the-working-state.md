---
title: Transitioning to the Working State
description: Transitioning to the Working State
keywords:
- working power state WDK networking
- network interface cards WDK networking , transitioning power states
- NICs WDK networking , transitioning power states
- power management WDK NDIS miniport , transitioning power states
- device power states WDK networking
- power states WDK networking
- transitioning power states WDK networking
ms.date: 04/20/2017
---

# Transitioning to the Working State





NDIS initiates the transition to the working power state (D0) by sending the miniport driver an [OID\_PNP\_SET\_POWER](./oid-pnp-set-power.md) request that specifies state D0. The miniport driver must then perform any device-dependent operations needed to restore the network adapter to a working state. The miniport driver must also restore any hardware context--packet filters, multicast addresses, the current media access control (MAC) address, or wake-up patterns--that the network adapter might have lost.

**Note**  Starting with NDIS 6.30, the miniport driver that support [NDIS packet coalescing](ndis-packet-coalescing.md) must clear its coalesced packet counter. The driver must also configure the network adapter to flush any packets that it coalesced before the low-power transition. For more information, see [Handling Packet Coalescing Receive Filters](handling-packet-coalescing-receive-filters.md).

 

Before the miniport driver returns NDIS\_STATUS\_SUCCESS in response to the OID\_PNP\_SET\_POWER request, the miniport driver and a network adapter must be ready for normal operation.

 

