---
title: Exporting a MiniportDevicePnPEventNotify Function
description: Exporting a MiniportDevicePnPEventNotify Function
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





NDIS calls a miniport driver's [*MiniportDevicePnPEventNotify*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_device_pnp_event_notify) function to notify the miniport driver of the following Plug and Play (PnP) events:

-   The surprise removal of a NIC that the miniport driver controls.

-   A change in the system's power source.

If a miniport driver does not export a *MiniportDevicePnPEventNotify* function, NDIS cannot notify the driver of these PnP events.

All NDIS 6.0 and later miniport drivers *must* export a *MiniportDevicePnPEventNotify* function. In addition, all miniport drivers that have a WDM lower edge *should* export a *MiniportDevicePnPEventNotify* function.

 

