---
title: Setting and Canceling Battery Notification
description: Setting and Canceling Battery Notification
keywords:
- battery notifications WDK
- battery miniclass drivers WDK , notifications
- notifications WDK battery
- battery class drivers WDK , notifications
- canceling battery notifications
- stopping battery notifications
ms.date: 04/20/2017
---

# Setting and Canceling Battery Notification


## <span id="ddk_setting_and_canceling_battery_notification_dg"></span><span id="DDK_SETTING_AND_CANCELING_BATTERY_NOTIFICATION_DG"></span>


A miniclass driver provides a [*BatteryMiniSetStatusNotify*](/windows/win32/api/batclass/nc-batclass-bclass_set_status_notify_callback) routine so that the class driver can request notification of specific conditions. The routine is declared as follows:

```cpp
typedef
NTSTATUS
(*BCLASS_SET_STATUS_NOTIFY)(
    IN PVOID Context,
    IN ULONG BatteryTag,
    IN PBATTERY_NOTIFY BatteryNotify
    );
```

The *Context* parameter is a pointer to the context area that is allocated by the miniclass driver and passed to the class driver in the BATTERY\_MINIPORT\_INFO structure at device initialization. The *BatteryTag* parameter is a value previously returned by [*BatteryMiniQueryTag*](/windows/win32/api/batclass/nc-batclass-bclass_query_tag_callback).

The *BatteryNotify* parameter contains a set of flags indicating the battery power condition, and a pair of ULONG values that define a range of acceptable battery capacities. When the battery no longer satisfies the specified power conditions or its capacity goes above or below the specified range, the miniclass driver should call [**BatteryClassStatusNotify**](/windows/win32/api/batclass/nf-batclass-batteryclassstatusnotify).

*BatteryMiniSetStatusNotify* should return STATUS\_NOT\_SUPPORTED for any conditions or trigger values that cannot be determined for this battery.

The class driver calls the [*BatteryMiniDisableStatusNotify*](/windows/win32/api/batclass/nc-batclass-bclass_disable_status_notify_callback) routine to cancel notification of battery status changes previously requested by BatteryMiniSetStatusNotify. This routine is declared as follows:

```cpp
typedef
NTSTATUS
(*BCLASS_DISABLE_STATUS_NOTIFY)(
    IN PVOID Context
    );
```

The *Context* parameter is a pointer to the context area allocated by the miniclass driver and passed to the class driver in the BATTERY\_MINIPORT\_INFO structure at device initialization.

Miniclass drivers can omit functionality for both routines and return STATUS\_NOT\_SUPPORTED. However, a miniclass driver that provides a *BatteryMiniSetStatusNotify* routine must provide a corresponding *BatteryMiniDisableStatusNotify* routine, and vice versa.

 

