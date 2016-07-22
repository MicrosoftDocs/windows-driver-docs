---
title: Device Installations and System Restarts
description: Device Installations and System Restarts
ms.assetid: c09d2150-60ae-4912-86f5-6489c818853e
keywords: ["device installations WDK , reboots", "installing devices WDK , reboots", "Device setup WDK device installations , reboots", "rebooting WDK device installations", "initiating reboots during device installations", "restarting during device installations"]
---

# Device Installations and System Restarts


## <a href="" id="ddk-device-installations-requiring-a-reboot-dg"></a>


Device installations should not force the user to restart the system unless absolutely necessary. The following circumstances are the only ones for which a system restart should be necessary:

<a href="" id="installing-or-removing-a-non-plug-and-play-device--"></a>Installing or removing a non-Plug and Play device.   
For these earlier devices, a user typically must shut down the system before physically adding or removing the device. After the power is turned back on, the system starts.

**Note**  The device's setup files should not initiate a system restart, regardless of whether the user installs the drivers before or after plugging in the hardware.

 

<a href="" id="updating-a-driver-for-a-system-boot-device--"></a>Updating a driver for a system boot device.   
If a device can potentially hold the system's paging, hibernation, or crash dump file, its drivers must service [**IRP\_MN\_DEVICE\_USAGE\_NOTIFICATION**](https://msdn.microsoft.com/library/windows/hardware/ff550841) requests. The system sends this request before putting one of these files on the disk. If the drivers succeed the request, they must fail any subsequent [**IRP\_MN\_QUERY\_REMOVE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551705) requests. When a driver for the device fails an IRP\_MN\_QUERY\_REMOVE\_DEVICE request, the system prompts the user to restart the system.

**Note**  The device's setup files should not initiate a system restart.

 

<a href="" id="installing-a-non-wdm-filter-driver-"></a>Installing a non-WDM filter driver.  
If a filter driver is added to a non-WDM driver stack, the system must be restarted. In this case, the driver's installer or co-installer should request a system restart (see [Initiating System Restarts During Device Installations](initiating-system-restarts-during-device-installations.md)).

**Note**   Adding a filter driver to a WDM driver stack does not require a system restart, unless an underlying device is a system boot device.

 

The section includes the following topics:

[Avoiding System Restarts during Device Installations](avoiding-system-restarts-during-device-installations.md)

[Initiating System Restarts During Device Installations](initiating-system-restarts-during-device-installations.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Device%20Installations%20and%20System%20Restarts%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




