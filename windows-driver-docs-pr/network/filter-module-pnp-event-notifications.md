---
title: Filter Module PnP Event Notifications
description: Filter Module PnP Event Notifications
ms.assetid: ca1e250a-aaa8-4fbc-abe5-c30c8913a67a
keywords:
- filter modules WDK networking , PnP event notifications
- filter drivers WDK networking , PnP event notifications
- NDIS filter drivers WDK , event notifications
- event notifications WDK networking , filter drivers
- Plug and Play WDK networking , filter
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Filter Module PnP Event Notifications





Filter drivers can receive all the device Plug and Play (PnP) notifications that underlying miniport drivers receive. Also, filter drivers can receive all the network PnP notifications that overlying protocol drivers receive.The handling of PnP notifications is driver specific.

The following figure illustrates a filtered device PnP event notification.

![diagram illustrating a filtered device plug and play event notification](images/pnpeventfilter.png)

Filter drivers provide a [*FilterDevicePnPEventNotify*](https://msdn.microsoft.com/library/windows/hardware/ff549926) function that NDIS calls to pass in device PnP and Power Management event notifications. This is similar to the [*MiniportDevicePnPEventNotify*](https://msdn.microsoft.com/library/windows/hardware/ff559369) function.

Filter drivers can forward device PnP and Power Management events to underlying drivers. To forward a device PnP or Power Management event, call the [**NdisFDevicePnPEventNotify**](https://msdn.microsoft.com/library/windows/hardware/ff561804) function.

The following figure illustrates a filtered network PnP event notification.

![diagram illustrating a filtered network device plug and play event notification](images/netpnpeventfilter.png)

Filter drivers provide a [*FilterNetPnPEvent*](https://msdn.microsoft.com/library/windows/hardware/ff549952) function that NDIS calls to pass in network PnP and Power Management event notifications. This is similar to the [*ProtocolNetPnPEvent*](https://msdn.microsoft.com/library/windows/hardware/ff570263) function.

Filter drivers can forward network PnP and Power Management events to overlying drivers. To forward a network PnP or Power Management event, call the [**NdisFNetPnPEvent**](https://msdn.microsoft.com/library/windows/hardware/ff561828) function.

Filter drivers should handle driver stack changes. For more information about driver stack changes, see [Modifying a Running Driver Stack](modifying-a-running-driver-stack.md).

If necessary to allow handling of these events, NDIS can initiate a pause operation after the PnP or Power Management notification. For more information, see [Pausing a Driver Stack](pausing-a-driver-stack.md).

 

 





