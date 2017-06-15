---
title: System Power Policy
author: windows-driver-content
description: System Power Policy
MS-HAID:
- 'PwrMgmt\_7346a77a-0a37-43e7-9bee-149c3fdd93ad.xml'
- 'kernel.system\_power\_policy'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 98b1a777-3ac1-40c2-a902-cb5326c20621
keywords: ["system-wide power policy WDK kernel", "power policy WDK kernel", "power supply WDK kernel", "system power policy WDK kernel", "AC power WDK kernel", "DC power WDK kernel"]
---

# System Power Policy


## <a href="" id="ddk-system-power-policy-kg"></a>


In its role as system power policy manager, the power manager keeps track of system activity, determines the appropriate system power state, and sends [**IRP\_MJ\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff550784) requests to query or change the system power state. It also provides interfaces through which applications can read and write power policy settings (see the Microsoft Windows SDK).

The power manager maintains two separate power policies — one for AC (wall current) and one for DC (battery or UPS) — and automatically switches between these two policies depending on the current power source. Typically, AC power policy emphasizes performance over conservation, while DC power policy emphasizes conservation over performance. To find out when the system changes from one policy to the other, a driver can register for notification with the system's \\Callback\\PowerState callback object. For further information, see [**ExCreateCallback**](https://msdn.microsoft.com/library/windows/hardware/ff544560) and [Callback Objects](callback-objects.md).

Computers that comply with the APCI specification automatically switch from AC to battery power, and from one battery to another, as each such power source goes off line. If the computer hardware allows the operating system to select the power source, the power manager tracks which battery is the least charged but still functional and selects it to power the computer.

As soon as AC power becomes available, the computer hardware automatically starts to charge a battery. If the hardware allows the operating system to select which battery to charge, the power manager selects the least discharged battery for recharging; this increases the chances that the system will have at least one well-charged battery at all times.

Regardless of any other settings, the power manager carries out the DC power policy for a critical battery if a battery that is rechargeable or supplies system power reports the hardware condition "critical" and is in the discharging state for two seconds or longer. Power policy in this situation typically requires a transition to the hibernate or shutdown state.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20System%20Power%20Policy%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


