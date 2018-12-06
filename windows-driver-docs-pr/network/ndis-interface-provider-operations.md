---
title: NDIS Interface Provider Operations
description: NDIS Interface Provider Operations
ms.assetid: cd5c76b0-6b38-44ea-ac1b-02be5d073203
keywords:
- NDIS network interfaces WDK , interface providers
- network interfaces WDK , interface providers
- interface providers WDk network interface
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# NDIS Interface Provider Operations





All NDIS drivers can register as interface providers. Whenever a driver (or the NDIS proxy interface provider) detects a new interface that is being introduced to the computer, it allocates a [**NET\_LUID**](https://msdn.microsoft.com/library/windows/hardware/ff568747) index, registers the interface, and retains the associated NET\_LUID value in persistent storage (such as the registry). The following list describes several examples of how a new interface can be introduced to a computer:

-   Installing a network adapter, either a virtual adapter for an intermediate driver or a physical adapter. In this case, the NDIS proxy interface provider manages the interface.

-   Attaching a filter module. In this case, the NDIS proxy interface provider manages the interface.

-   MUX intermediate driver internal bindings. The MUX intermediate driver should implement NDIS provider services to handle this case because the internal interfaces are not visible to NDIS.

When the computer subsequently restarts, the interface provider should not allocate a new [**NET\_LUID**](https://msdn.microsoft.com/library/windows/hardware/ff568747) for the same interface if the interface is persistent; instead, the interface provider should use the previously stored NET\_LUID value to register the same interface. Also, even if the interface is not persistent, the interface provider must free the NET\_LUID index if there is a computer power failure. Therefore, the interface provider should store the NET\_LUID in persistent storage (for example, the registry).

If an interface provider detects that an interface is being shut down, it should deregister the interface.

**Note**  The NDIS proxy provider deregisters interfaces for miniport adapters when they are uninstalled and filter modules when they are detached.

 

If an interface provider detects that an interface is being removed completely (for example, the NDIS proxy provider is notified that a miniport adapter is being uninstalled), the interface provider deregisters the interface and releases the NET\_LUID index. The NDIS proxy provider also releases the NET\_LUID index when a filter module is detached.

During run time, interface providers handle OID requests for the interfaces that they registered. The NDIS proxy interface provider might issue OID requests to underlying drivers to obtain interface information.

 

 





