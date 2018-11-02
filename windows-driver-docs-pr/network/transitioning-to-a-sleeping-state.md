---
title: Transitioning to a Sleeping State
description: Transitioning to a Sleeping State
ms.assetid: cea326dd-7235-41a3-ad37-19549533a8dd
keywords:
- network interface cards WDK networking , transitioning power states
- NICs WDK networking , transitioning power states
- sleeping states WDK networking
- power management WDK NDIS miniport , transitioning power states
- device power states WDK networking
- power states WDK networking
- transitioning power states WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Transitioning to a Sleeping State





If a miniport driver supports wake-up events, NDIS sends the driver an [OID\_PNP\_ENABLE\_WAKE\_UP](https://msdn.microsoft.com/library/windows/hardware/ff569775) request before sending an [OID\_PNP\_SET\_POWER](https://msdn.microsoft.com/library/windows/hardware/ff569780) request. For more information, see [Enabling Wake-Up Events](enabling-wake-up-events.md). A miniport driver must not fail an OID\_PNP\_SET\_POWER request.

Before returning NDIS\_STATUS\_SUCCESS in response to an OID\_PNP\_SET\_POWER request, the miniport driver must:

-   Perform the device-dependent operations that are needed to prepare the network adapter for the sleeping state.

-   Save any packet filters, multicast addresses, the current MAC address, wake-up patterns, and any other hardware context that the network adapter cannot preserve in a sleeping state.

-   Disable interrupts and the network adapter's DMA engine. A miniport driver cannot access the network adapter hardware after the network adapter has been set to the D3 state by the bus driver.

 

 





