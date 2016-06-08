---
title: Responding to Battery Status Queries
description: Responding to Battery Status Queries
ms.assetid: 756d7dd3-c4cc-4185-95cf-5a28ce86cacc
keywords: ["battery status WDK", "low batteries WDK", "discharging batteries WDK", "power states WDK battery", "failed batteries WDK", "battery failures WDK"]
---

# Responding to Battery Status Queries


## <span id="ddk_responding_to_battery_status_queries_dg"></span><span id="DDK_RESPONDING_TO_BATTERY_STATUS_QUERIES_DG"></span>


The battery class driver calls the miniclass driver's [*BatteryMiniQueryStatus*](https://msdn.microsoft.com/library/windows/hardware/ff536274) routine to get the power state, capacity, voltage, and discharge rate of a battery. The following is the prototype for this routine:

```
typedef
NTSTATUS
(*BCLASS_QUERY_STATUS)(
    IN PVOID Context,
    IN ULONG BatteryTag,
    OUT PBATTERY_STATUS BatteryStatus
    );
```

The *Context* parameter is a pointer to the context area that is allocated by the miniclass driver and passed to the class driver in the [**BATTERY\_MINIPORT\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff536287) structure at device initialization. The *BatteryTag* parameter is a value previously returned by BatteryMiniQueryTag.

In the buffered BATTERY\_STATUS structure, the miniclass driver reports the battery's voltage, capacity, and charge/discharge rate to the extent that the miniclass driver can determine them. The miniclass driver also reports one or more of the following constants that describe the battery's power condition:

-   BATTERY\_CHARGING

-   BATTERY\_DISCHARGING

-   BATTERY\_POWER\_ON\_LINE

-   BATTERY\_CRITICAL

The miniclass driver should not report a critically low, discharging battery (BATTERY\_CRITICAL and BATTERY\_DISCHARGING) until it has ascertained that the condition is not merely a transitory fluctuation and has exhausted all other means of remedying the situation. Such remedies might include switching to AC power or to another battery, if the miniclass driver can do so.

When the miniclass driver reports a critically low, discharging battery, the power manager assumes that battery failure is imminent. If the battery supplies system power or is a secondary (rechargeable) cell, the system carries out the DC power policy for a critical battery. The details of the power policy vary from system to system, depending on hardware capabilities, application settings, and user preferences. Typically, the system attempts to enter a sleeping state or powers off the computer. For more information, see [System Power Policy](https://msdn.microsoft.com/library/windows/hardware/ff564559).

The class driver's [**BatteryClassStatusNotify**](https://msdn.microsoft.com/library/windows/hardware/ff536269) routine and the miniclass driver's [*BatteryMiniQueryStatus*](https://msdn.microsoft.com/library/windows/hardware/ff536274), [*BatteryMiniSetStatusNotify*](https://msdn.microsoft.com/library/windows/hardware/ff536277), and [*BatteryMiniDisableStatusNotify*](https://msdn.microsoft.com/library/windows/hardware/ff536272) routines are used in sequence by the two drivers to provide timely status information. For details, see [Interaction of Battery Status and Notification Routines](interaction-of-battery-status-and-notification-routines.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[battery\battery]:%20Responding%20to%20Battery%20Status%20Queries%20%20RELEASE:%20%286/7/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




