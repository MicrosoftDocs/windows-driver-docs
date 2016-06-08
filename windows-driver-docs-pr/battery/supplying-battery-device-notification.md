---
title: Supplying Battery Device Notification
description: Supplying Battery Device Notification
ms.assetid: 7104c43b-84f1-496d-9552-608101f5b379
keywords: ["battery notifications WDK", "battery miniclass drivers WDK , notifications", "notifications WDK battery", "battery miniclass drivers WDK , status reporting", "status information WDK battery", "monitoring battery status", "battery class drivers WDK , notifications"]
---

# Supplying Battery Device Notification


## <span id="ddk_supplying_battery_device_notification_dg"></span><span id="DDK_SUPPLYING_BATTERY_DEVICE_NOTIFICATION_DG"></span>


The miniclass driver is responsible for monitoring the status of the batteries it supports and notifying the class driver when important changes occur.

In addition to the [*BatteryMiniQueryStatus*](https://msdn.microsoft.com/library/windows/hardware/ff536274) routine, the miniclass driver also supplies the [*BatteryMiniSetStatusNotify*](https://msdn.microsoft.com/library/windows/hardware/ff536277) and [*BatteryMiniDisableStatusNotify*](https://msdn.microsoft.com/library/windows/hardware/ff536272) routines. The class driver uses the *BatteryMiniSetStatusNotify* and *BatteryMiniDisableStatusNotify* routines to request and cancel notification of specific battery states. These routines interact with the class and miniclass driver status routines as described in the next section. For more information about these two miniclass routines, see [Setting and Canceling Battery Notification](setting-and-canceling-battery-notification.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[battery\battery]:%20Supplying%20Battery%20Device%20Notification%20%20RELEASE:%20%286/7/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




