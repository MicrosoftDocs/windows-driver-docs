---
title: Porting Protocol Driver Plug and Play Event Notification Handling to NDIS 6.0
description: Porting Protocol Driver Plug and Play Event Notification Handling to NDIS 6.0
ms.assetid: a1ee9d58-ae64-40d3-bcfc-19ea9ecca10a
keywords:
- NDIS protocol drivers WDK , Plug and Play
- protocol drivers WDK networking , Plug and Play
- porting protocol drivers WDK networking , Plug and Play event notifications
- Plug and Play WDK networking , porting event notifications
- event notifications WD
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting Protocol Driver Plug and Play Event Notification Handling to NDIS 6.0





In NDIS 6.0 protocol drivers, replace the NDIS 5.x [**ProtocolPnPEvent**](https://msdn.microsoft.com/library/windows/hardware/ff563243) function with the [*ProtocolNetPnPEvent*](https://msdn.microsoft.com/library/windows/hardware/ff570263) function.

NDIS 6.0 protocol drivers must handle pause and restart events. For more information about pause and restart events, see [Supporting NDIS 6.0 Protocol Binding Pause and Restart Operations](supporting-ndis-6-0-protocol-binding-pause-and-restart-operations.md).

For more information about NDIS 6.0 Plug and Play notifications, see [Handling PnP Event Notifications in a Protocol Driver](handling-pnp-event-notifications-in-a-protocol-driver.md).

 

 





