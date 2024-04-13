---
title: Interaction of Battery Status and Notification Routines
description: Interaction of Battery Status and Notification Routines
keywords:
- battery notifications WDK
- battery miniclass drivers WDK , notifications
- notifications WDK battery
- battery class drivers WDK , notifications
ms.date: 04/20/2017
---

# Interaction of Battery Status and Notification Routines

The class driver can request and receive battery status -- and the miniclass driver can provide battery status -- in several ways.

If the miniclass driver provides a [*BatteryMiniSetStatusNotify*](/windows/win32/api/batclass/nc-batclass-bclass_set_status_notify_callback) routine, the class driver can register to be notified when the battery's capacity exceeds or drops below a specified range, or when its power state changes. When any of the registered conditions occurs, the miniclass driver calls [**BatteryClassStatusNotify**](/windows/win32/api/batclass/nf-batclass-batteryclassstatusnotify).

Note that **BatteryClassStatusNotify** does not supply status information; its only parameter is the context of the battery that triggered the notification. It merely informs the class driver that the battery's status has changed. In turn, the class driver calls [*BatteryMiniQueryStatus*](/windows/win32/api/batclass/nc-batclass-bclass_query_status_callback) if it requires details.

If the miniclass driver does not support *BatteryMiniSetStatusNotify*, the class driver polls for status by calling the *BatteryMiniQueryStatus* routine at regular but infrequent intervals.

Independent of any notification requests, a miniclass driver must call **BatteryClassStatusNotify** whenever any of the following occurs:

- The battery goes online or offline.

- The capacity of the battery becomes critically low.

- The power state of the battery changes: it starts charging, starts discharging, stops charging, or stops discharging.

Before reporting a critically low, discharging battery, the miniclass driver should attempt to solve the problem, as described previously in [Responding to Battery Status Queries](responding-to-battery-status-queries.md).
