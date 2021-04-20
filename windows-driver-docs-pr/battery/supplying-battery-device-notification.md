---
title: Supplying Battery Device Notification
description: Supplying Battery Device Notification
keywords:
- battery notifications WDK
- battery miniclass drivers WDK , notifications
- notifications WDK battery
- battery miniclass drivers WDK , status reporting
- status information WDK battery
- monitoring battery status
- battery class drivers WDK , notifications
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supplying Battery Device Notification


## <span id="ddk_supplying_battery_device_notification_dg"></span><span id="DDK_SUPPLYING_BATTERY_DEVICE_NOTIFICATION_DG"></span>


The miniclass driver is responsible for monitoring the status of the batteries it supports and notifying the class driver when important changes occur.

In addition to the [*BatteryMiniQueryStatus*](/windows/win32/api/batclass/nc-batclass-bclass_query_status_callback) routine, the miniclass driver also supplies the [*BatteryMiniSetStatusNotify*](/windows/win32/api/batclass/nc-batclass-bclass_set_status_notify_callback) and [*BatteryMiniDisableStatusNotify*](/windows/win32/api/batclass/nc-batclass-bclass_disable_status_notify_callback) routines. The class driver uses the *BatteryMiniSetStatusNotify* and *BatteryMiniDisableStatusNotify* routines to request and cancel notification of specific battery states. These routines interact with the class and miniclass driver status routines as described in the next section. For more information about these two miniclass routines, see [Setting and Canceling Battery Notification](setting-and-canceling-battery-notification.md).

 

