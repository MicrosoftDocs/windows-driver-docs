---
title: Setting and Canceling Battery Notification
description: Setting and Canceling Battery Notification
ms.assetid: bd0920f0-9f3f-47f7-b1a7-29ec233e93ff
keywords: ["battery notifications WDK", "battery miniclass drivers WDK , notifications", "notifications WDK battery", "battery class drivers WDK , notifications", "canceling battery notifications", "stopping battery notifications"]
---

# Setting and Canceling Battery Notification


## <span id="ddk_setting_and_canceling_battery_notification_dg"></span><span id="DDK_SETTING_AND_CANCELING_BATTERY_NOTIFICATION_DG"></span>


A miniclass driver provides a [*BatteryMiniSetStatusNotify*](https://msdn.microsoft.com/library/windows/hardware/ff536277) routine so that the class driver can request notification of specific conditions. The routine is declared as follows:

```
typedef
NTSTATUS
(*BCLASS_SET_STATUS_NOTIFY)(
    IN PVOID Context,
    IN ULONG BatteryTag,
    IN PBATTERY_NOTIFY BatteryNotify
    );
```

The *Context* parameter is a pointer to the context area that is allocated by the miniclass driver and passed to the class driver in the BATTERY\_MINIPORT\_INFO structure at device initialization. The *BatteryTag* parameter is a value previously returned by [*BatteryMiniQueryTag*](https://msdn.microsoft.com/library/windows/hardware/ff536275).

The *BatteryNotify* parameter contains a set of flags indicating the battery power condition, and a pair of ULONG values that define a range of acceptable battery capacities. When the battery no longer satisfies the specified power conditions or its capacity goes above or below the specified range, the miniclass driver should call [**BatteryClassStatusNotify**](https://msdn.microsoft.com/library/windows/hardware/ff536269).

*BatteryMiniSetStatusNotify* should return STATUS\_NOT\_SUPPORTED for any conditions or trigger values that cannot be determined for this battery.

The class driver calls the [*BatteryMiniDisableStatusNotify*](https://msdn.microsoft.com/library/windows/hardware/ff536272) routine to cancel notification of battery status changes previously requested by BatteryMiniSetStatusNotify. This routine is declared as follows:

```
typedef
NTSTATUS
(*BCLASS_DISABLE_STATUS_NOTIFY)(
    IN PVOID Context
    );
```

The *Context* parameter is a pointer to the context area allocated by the miniclass driver and passed to the class driver in the BATTERY\_MINIPORT\_INFO structure at device initialization.

Miniclass drivers can omit functionality for both routines and return STATUS\_NOT\_SUPPORTED. However, a miniclass driver that provides a *BatteryMiniSetStatusNotify* routine must provide a corresponding *BatteryMiniDisableStatusNotify* routine, and vice versa.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[battery\battery]:%20Setting%20and%20Canceling%20Battery%20Notification%20%20RELEASE:%20%286/7/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


