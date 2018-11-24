---
title: Porting miniport driver PnP event handling to NDIS 6.0
description: Porting Miniport Driver Plug and Play Event Notification Handling to NDIS 6.0
ms.assetid: a7118a0a-a6dd-4db3-8108-fff473355438
keywords:
- NDIS miniport drivers WDK networking , Plug and Play
- miniport drivers WDK networking , Plug and Play
- Plug and Play WDK networking , porting event notifications
- event notifications WDK networking
- porting miniport drivers WDK networking , Plug and
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting Miniport Driver Plug and Play Event Notification Handling to NDIS 6.0





In NDIS 6.0 miniport drivers, replace the NDIS 5.x [**MiniportPnPEventNotify**](https://msdn.microsoft.com/library/windows/hardware/ff550487) function with the [*MiniportDevicePnPEventNotify*](https://msdn.microsoft.com/library/windows/hardware/ff559369) function.

For more information about NDIS 6.0 Plug and Play notifications, see [Adapter PnP Event Notifications](miniport-adapter-device-pnp-event-notifications.md).

 

 





