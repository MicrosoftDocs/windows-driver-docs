---
title: Miniport Adapter Device PnP Event Notifications
description: Miniport Adapter Device PnP Event Notifications
keywords:
- Plug and Play WDK networking , handling PnP event notifications
- miniport adapters WDK networking , Plug and Play event notifications
- adapters WDK networking , Plug and Play event notifications
- MiniportDevicePnPEventNotify
- events WDK networking
ms.date: 04/20/2017
---

# Miniport Adapter Device PnP Event Notifications





NDIS calls a miniport driver's [*MiniportDevicePnPEventNotify*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_device_pnp_event_notify) function to notify the driver of Plug and Play (PnP) events.

NDIS provides an event code that describes the PnP event. The code can indicate that the adapter has been unexpectedly removed from the system or that the power profile of the host system has changed.

If the event code indicates that the power profile has changed, NDIS also indicates the type of change. Either the system is running on battery power or the system is running on AC power.

The miniport driver should adjust the adapter settings accordingly.

 

