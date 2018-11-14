---
title: Exporting a MiniportDevicePnPEventNotify Function
description: Exporting a MiniportDevicePnPEventNotify Function
ms.assetid: 1c6dce4e-c452-48ce-b3c9-a3fb7842f060
keywords:
- Plug and Play WDK NDIS miniport , event notifications
- MiniportDevicePnPEventNotify
- notifications
- notifications WDK PnP , NDIS miniport drivers
- event notifications WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Exporting a MiniportDevicePnPEventNotify Function





NDIS calls a miniport driver's [*MiniportDevicePnPEventNotify*](https://msdn.microsoft.com/library/windows/hardware/ff559369) function to notify the miniport driver of the following Plug and Play (PnP) events:

-   The surprise removal of a NIC that the miniport driver controls.

-   A change in the system's power source.

If a miniport driver does not export a *MiniportDevicePnPEventNotify* function, NDIS cannot notify the driver of these PnP events.

All NDIS 6.0 and later miniport drivers *must* export a *MiniportDevicePnPEventNotify* function. In addition, all miniport drivers that have a WDM lower edge *should* export a *MiniportDevicePnPEventNotify* function.

 

 





