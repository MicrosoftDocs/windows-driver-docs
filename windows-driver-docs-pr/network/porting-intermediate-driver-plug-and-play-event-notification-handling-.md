---
title: Porting Intermediate Driver PnP Event Handling to NDIS 6.0
description: Porting Intermediate Driver Plug and Play Event Notification Handling to NDIS 6.0
ms.assetid: 0ffaff9c-7ca1-4384-a2da-15586107ecdc
keywords:
- NDIS intermediate drivers WDK networking , Plug and Play
- intermediate drivers WDK networking , Plug and Play
- Plug and Play WDK networking , porting event notifications
- event notifications WDK networking
- porting intermediate drivers WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting Intermediate Driver Plug and Play Event Notification Handling to NDIS 6.0





Like NDIS 5.*x* intermediate drivers, NDIS 6.0 intermediate drivers receive network Plug and Play events and device Plug and Play events.

NDIS intermediate drivers call the [**NdisMNetPnPEvent**](https://msdn.microsoft.com/library/windows/hardware/ff563616) function to propagate a network Plug and Play or Power Management event notification to overlying drivers.

For more information about Plug and Play events in the miniport upper edge of an intermediate driver, see [Porting Miniport Adapter Shutdown Operations to NDIS 6.0](porting-miniport-adapter-shutdown-operations-to-ndis-6-0.md).

For more information about status indications in the protocol lower edge of an intermediate driver, see [Porting Protocol Driver Plug and Play Event Notification Handling to NDIS 6.0](porting-protocol-driver-plug-and-play-event-notification-handling-to-n.md).

 

 





