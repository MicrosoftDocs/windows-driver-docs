---
title: Support for Power Management
author: windows-driver-content
description: Support for Power Management
ms.assetid: 77e8be50-9623-4085-8d38-44db676a9a1f
keywords: ["power management WDK kernel , support requirements", "power management WDK kernel , about power management", "PnP WDK power management", "Plug and Play WDK power management"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Support for Power Management


## <a href="" id="ddk-levels-of-support-for-power-management-kg"></a>


To support power management, drivers must also support [Plug and Play](implementing-plug-and-play.md) (PnP). Driver support for PnP is required because many power management operations are associated with installing and removing devices, and the PnP manager notifies drivers of these events by means of PnP IRPs. Additionally, drivers report device support for power management in response to PnP queries for device capabilities.

Power management works on two levels: one applies to individual devices and the other to the system as a whole.

The power manager, part of the operating system kernel, manages the power level of the entire system. If all drivers in the system support power management, the power manager can manage power consumption on a system-wide basis, utilizing not only the fully on and fully off states, but also various intermediate system sleep states.

Legacy drivers that were written before the operating system supported power management continue to work as they did previously. However, systems that include legacy drivers cannot enter any of the intermediate system sleep states; they can operate only in the fully on or fully off states as before.

Device power management applies to individual devices. A driver that supports power management can turn its device on when it is needed and off when it is not in use. Devices that have the hardware capability can enter intermediate device power states. The presence of legacy drivers in the system does not affect the ability of newer drivers to manage power for their devices.

Beginning with Windows Vista, the operating system also supports driver performance states. Drivers that support device performance states can choose to tradeoff performance or features with a reduction in power consumption. Windows Vista provides a framework for devices to retrieve their power settings and information about the system power state. This mechanism is extendable, allowing driver vendors to define and install new custom power settings for their device. For more information, see [System Power Policy](system-power-policy.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Support%20for%20Power%20Management%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


