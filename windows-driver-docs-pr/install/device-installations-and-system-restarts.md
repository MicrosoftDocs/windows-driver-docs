---
title: Device Installations and System Restarts
description: Device Installations and System Restarts
ms.assetid: c09d2150-60ae-4912-86f5-6489c818853e
keywords:
- device installations WDK , reboots
- installing devices WDK , reboots
- Device setup WDK device installations , reboots
- rebooting WDK device installations
- initiating reboots during device installations
- restarting during device installations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Device Installations and System Restarts





Device installations should not force the user to restart the system unless absolutely necessary. The following circumstances are the only ones for which a system restart should be necessary:

<a href="" id="installing-or-removing-a-non-plug-and-play-device--"></a>Installing or removing a non-Plug and Play device.   
For these earlier devices, a user typically must shut down the system before physically adding or removing the device. After the power is turned back on, the system starts.

**Note**  The device's setup files should not initiate a system restart, regardless of whether the user installs the drivers before or after plugging in the hardware.

 

<a href="" id="updating-a-driver-for-a-system-boot-device--"></a>Updating a driver for a system boot device.   
If a device can potentially hold the system's paging, hibernation, or crash dump file, its drivers must service [**IRP_MN_DEVICE_USAGE_NOTIFICATION**](https://msdn.microsoft.com/library/windows/hardware/ff550841) requests. The system sends this request before putting one of these files on the disk. If the drivers succeed the request, they must fail any subsequent [**IRP_MN_QUERY_REMOVE_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551705) requests. When a driver for the device fails an IRP_MN_QUERY_REMOVE_DEVICE request, the system prompts the user to restart the system.

**Note**  The device's setup files should not initiate a system restart.

 

<a href="" id="installing-a-non-wdm-filter-driver-"></a>Installing a non-WDM filter driver.  
If a filter driver is added to a non-WDM driver stack, the system must be restarted. In this case, the driver's installer or co-installer should request a system restart (see [Initiating System Restarts During Device Installations](initiating-system-restarts-during-device-installations.md)).

**Note**   Adding a filter driver to a WDM driver stack does not require a system restart, unless an underlying device is a system boot device.

 

The section includes the following topics:

[Avoiding System Restarts during Device Installations](avoiding-system-restarts-during-device-installations.md)

[Initiating System Restarts During Device Installations](initiating-system-restarts-during-device-installations.md)

 

 





