---
title: Handling PnP Event Notifications in a Protocol Driver
description: Handling PnP Event Notifications in a Protocol Driver
ms.assetid: 7c6c9bc5-37ce-49f4-8e39-5f51a266836a
keywords:
- Plug and Play WDK NDIS protocol
- notifications WDK PnP , NDIS protocol drivers
- event notifications WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling PnP Event Notifications in a Protocol Driver





NDIS 6.0 and later protocol drivers handle the same Plug and Play (PnP) event notifications as NDIS 5.x drivers in addition to event notifications that are specific to NDIS 6.0 and later. The handling of PnP event notifications is driver specific.

To notify a protocol driver of a network PnP event, NDIS calls the driver's [*ProtocolNetPnPEvent*](https://msdn.microsoft.com/library/windows/hardware/ff570263) function. To define the type of event and characteristics of the event, NDIS passes a [**NET\_PNP\_EVENT\_NOTIFICATION**](https://msdn.microsoft.com/library/windows/hardware/ff568752) structure at the *NetPnPEvent* event parameter of *ProtocolNetPnPEvent*.

Protocol drivers should handle driver stack changes. For more information about driver stack changes, see [Modifying a Running Driver Stack](modifying-a-running-driver-stack.md).

Protocol drivers that do not handle stack change notifications are unbound from the adapter and rebound. Bindings for protocol drivers that handle driver stack notifications successfully are not affected.

Protocol drivers should handle driver stack pause notifications. For more information about these notifications, see [Pausing a Driver Stack](pausing-a-driver-stack.md).

Protocol drivers should handle driver stack restart notifications. For more information about these notifications, see [Restarting a Driver Stack](restarting-a-driver-stack.md).

 

 





