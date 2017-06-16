---
title: Power Manager
author: windows-driver-content
description: Power Manager
ms.assetid: f7727368-6edd-427b-9fb3-02f80538807b
keywords: ["power manager WDK kernel", "usage manager WDK power management", "power IRPs WDK kernel , power manager", "system-wide power policy WDK kernel", "power policy WDK kernel", "sleep power management WDK kernel", "hibernation power management WDK kernel", "shutdown power management WDK kernel"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Power Manager


## <a href="" id="ddk-power-manager-kg"></a>


The power manager is responsible for managing power usage for the system. It administers the system-wide power policy and tracks the path of power IRPs through the system.

The power manager requests power operations by sending [**IRP\_MJ\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff550784) requests to drivers. A request can specify a new power state or can query whether a change in power state is feasible.

When sleep, hibernation, or shutdown is required, the power manager requests the appropriate power action by sending an **IRP\_MJ\_POWER** request to each leaf node in the device tree. The power manager considers the following in determining whether the system should sleep, hibernate, or shut down:

-   System activity level

-   System battery level

-   Shutdown, hibernate, or sleep requests from applications

-   User actions, such as pressing the power button

-   Control panel settings

For more information, see [Windows Kernel-Mode Power Manager](windows-kernel-mode-power-manager.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Power%20Manager%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


