---
title: Interaction of Battery Status and Notification Routines
description: Interaction of Battery Status and Notification Routines
ms.assetid: 1f9a3785-4ea4-4b56-bc66-247dfe222377
keywords: ["battery notifications WDK", "battery miniclass drivers WDK , notifications", "notifications WDK battery", "battery class drivers WDK , notifications"]
---

# Interaction of Battery Status and Notification Routines


## <span id="ddk_interaction_of_battery_status_and_notification_routines_dg"></span><span id="DDK_INTERACTION_OF_BATTERY_STATUS_AND_NOTIFICATION_ROUTINES_DG"></span>


The class driver can request and receive battery status -- and the miniclass driver can provide battery status -- in several ways.

If the miniclass driver provides a [*BatteryMiniSetStatusNotify*](https://msdn.microsoft.com/library/windows/hardware/ff536277) routine, the class driver can register to be notified when the battery's capacity exceeds or drops below a specified range, or when its power state changes. When any of the registered conditions occurs, the miniclass driver calls [**BatteryClassStatusNotify**](https://msdn.microsoft.com/library/windows/hardware/ff536269).

Note that **BatteryClassStatusNotify** does not supply status information; its only parameter is the context of the battery that triggered the notification. It merely informs the class driver that the battery's status has changed. In turn, the class driver calls [*BatteryMiniQueryStatus*](https://msdn.microsoft.com/library/windows/hardware/ff536274) if it requires details.

If the miniclass driver does not support *BatteryMiniSetStatusNotify*, the class driver polls for status by calling the *BatteryMiniQueryStatus* routine at regular but infrequent intervals.

Independent of any notification requests, a miniclass driver must call **BatteryClassStatusNotify** whenever any of the following occurs:

-   The battery goes online or offline.

-   The capacity of the battery becomes critically low.

-   The power state of the battery changes: it starts charging, starts discharging, stops charging, or stops discharging.

Before reporting a critically low, discharging battery, the miniclass driver should attempt to solve the problem, as described previously in [Responding to Battery Status Queries](responding-to-battery-status-queries.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[battery\battery]:%20Interaction%20of%20Battery%20Status%20and%20Notification%20Routines%20%20RELEASE:%20%286/7/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


