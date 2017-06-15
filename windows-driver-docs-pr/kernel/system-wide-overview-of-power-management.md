---
title: System-Wide Overview of Power Management
author: windows-driver-content
description: System-Wide Overview of Power Management
MS-HAID:
- 'PwrMgmt\_290d44a8-54a7-4260-ace4-1b9bad3f11c2.xml'
- 'kernel.system\_wide\_overview\_of\_power\_management'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 16313152-3fe2-49d7-8cf1-b369e39e4130
keywords: ["power management WDK kernel , about power management", "power management WDK kernel , system-wide overview", "software WDK power management", "Control Panel WDK power management", "system-wide power policy WDK kernel", "power policy WDK kernel", "conserving power WDK kernel"]
---

# System-Wide Overview of Power Management


## <a href="" id="ddk-system-wide-overview-of-power-management-kg"></a>


Power management requires support from system and device hardware and from system software and drivers. Required hardware support is covered in the industry specifications, as described in the previous section. This topic covers the software support—specifically, what drivers must do to conform to operating system requirements and to manage power as appropriate for their devices.

The following figure shows a system-wide overview of power management.

![diagram illustrating a system-wide overview of power management](images/power-comp.png)

Applications and users can affect power management decisions through Control Panel and by calling power management routines. Users can use Control Panel to set system and device power options, including custom power settings. Control Panel notifies the power manager and drivers of changes to the active power policy and associated power settings. Beginning with Windows Vista, the power manager notifies a driver by calling the [**power setting callback**](https://msdn.microsoft.com/library/windows/hardware/ff559727) that a driver registers to receive notifications. In Windows Server 2003, Windows XP, and Windows 2000, this notification is performed through WMI.

The power manager administers the system-wide *power policy*, the rules that govern the system's power usage. (For more information, see [System Power Policy](system-power-policy.md).) Using information from Control Panel and APIs, the power manager can determine when applications are using, or might need to use, various devices, so that it can adjust the system's power policy appropriately.

The power manager also provides an interface for drivers, comprising [power management support routines](https://msdn.microsoft.com/library/windows/hardware/ff559835), [power management minor IRPs](https://msdn.microsoft.com/library/windows/hardware/ff559822), and required driver entry points.

When the power manager requests a change to the system power state, drivers respond by putting their devices in an appropriate device power state. In addition, drivers can perform idle detection for their devices and put unused devices in a sleep state. Bus-specific mechanisms report device power capabilities, set and report device status, and change device power. Exactly how and when device power is changed depends on the type of device and the capabilities of the device hardware.

Although ACPI hardware realizes the greatest power savings, the hardware need not be ACPI-compliant for power management in drivers to be effective.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20System-Wide%20Overview%20of%20Power%20Management%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


