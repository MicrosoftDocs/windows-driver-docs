---
title: System Power Policy
description: System Power Policy
ms.assetid: 98b1a777-3ac1-40c2-a902-cb5326c20621
keywords: ["system-wide power policy WDK kernel", "power policy WDK kernel", "power supply WDK kernel", "system power policy WDK kernel", "AC power WDK kernel", "DC power WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# System Power Policy





In its role as system power policy manager, the power manager keeps track of system activity, determines the appropriate system power state, and sends [**IRP\_MJ\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff550784) requests to query or change the system power state. It also provides interfaces through which applications can read and write power policy settings (see the Microsoft Windows SDK).

The power manager maintains two separate power policies — one for AC (wall current) and one for DC (battery or UPS) — and automatically switches between these two policies depending on the current power source. Typically, AC power policy emphasizes performance over conservation, while DC power policy emphasizes conservation over performance. To find out when the system changes from one policy to the other, a driver can register for notification with the system's \\Callback\\PowerState callback object. For further information, see [**ExCreateCallback**](https://msdn.microsoft.com/library/windows/hardware/ff544560) and [Callback Objects](callback-objects.md).

Computers that comply with the APCI specification automatically switch from AC to battery power, and from one battery to another, as each such power source goes off line. If the computer hardware allows the operating system to select the power source, the power manager tracks which battery is the least charged but still functional and selects it to power the computer.

As soon as AC power becomes available, the computer hardware automatically starts to charge a battery. If the hardware allows the operating system to select which battery to charge, the power manager selects the least discharged battery for recharging; this increases the chances that the system will have at least one well-charged battery at all times.

Regardless of any other settings, the power manager carries out the DC power policy for a critical battery if a battery that is rechargeable or supplies system power reports the hardware condition "critical" and is in the discharging state for two seconds or longer. Power policy in this situation typically requires a transition to the hibernate or shutdown state.

 

 




