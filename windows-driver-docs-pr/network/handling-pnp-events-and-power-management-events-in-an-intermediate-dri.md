---
title: Handling PnP Events and Power Management Events in an Intermediate Driver
description: Handling PnP Events and Power Management Events in an Intermediate Driver
ms.assetid: 0b4cf76f-a31d-4cf6-8486-090393404af9
keywords:
- intermediate drivers WDK networking , events
- NDIS intermediate drivers WDK , events
- Plug and Play WDK networking , intermediate drivers
- power management WDK networking , intermediate drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling PnP Events and Power Management Events in an Intermediate Driver





An intermediate driver must be able to handle Plug and Play (PnP) events and power management events. Specifically:

-   An intermediate driver must set the NDIS\_MINIPORT\_ATTRIBUTES\_NO\_HALT\_ON\_SUSPEND flag in the **AttributeFlags** member of the [**NDIS\_MINIPORT\_ADAPTER\_REGISTRATION\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565934) structure that is passed to [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672). For more information, see [Initializing as a Miniport](initializing-virtual-miniports.md).

-   The virtual miniport of an intermediate driver must handle OID\_PNP\_*Xxx* requests.

-   The protocol section of an intermediate driver should propagate appropriate OID\_PNP\_*Xxx* requests to the underlying miniport drivers. The virtual miniport of the intermediate driver should pass the underlying miniport driver's responses to these requests back to the protocol driver that originated the requests. The intermediate driver does not have to pass requests that are not required by design. For example, when there is not a one-to-one relationship between virtual miniports and underlying miniport adapters as in Load Balancing Failover (LBFO) applications.

-   The protocol portion of an intermediate driver must supply a [*ProtocolNetPnPEvent*](https://msdn.microsoft.com/library/windows/hardware/ff570263) function.

Intermediate driver protocol and miniport event handlers are not called in any particular order. Event handlers for intermediate drivers should be implemented accordingly.

This section includes the following topics:

[Initializing Intermediate Drivers to Handle PnP and Power Management Events](initializing-intermediate-drivers-to-handle-pnp-and-power-management-events.md)

[Handling OID\_PNP\_Xxx Queries and Sets](handling-oid-pnp-xxx-queries-and-sets.md)

[Implementing a ProtocolNetPnPEvent Handler in an Intermediate Driver](implementing-a-protocolnetpnpevent-handler-in-an-intermediate-driver.md)

[Handling a Set Power Request](handling-a-set-power-request.md)

 

 





