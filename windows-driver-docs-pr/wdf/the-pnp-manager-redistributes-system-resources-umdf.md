---
title: The PnP Manager Redistributes System Resources
description: The PnP Manager Redistributes System Resources
ms.assetid: c8e6277b-b1e5-449f-b5a0-f5a46b46e56e
keywords: ["power management scenarios WDK UMDF , PnP manager redistributes system resources", "redistribution of system resources scenario WDK UMDF"]
---

# The PnP Manager Redistributes System Resources


\[This topic applies to UMDF 1.*x*.\]

If a user adds a device to a system, and if the device requires system resources that the PnP manager has already assigned to another device, the PnP manager attempts to reassign resources.

During this process, the PnP manager stops devices and takes them out of their working (D0) states. It then delivers new resource lists to the devices so that they can restart, using the new resources.

When redistributing resources, the PnP manager will not alter a device's resource assignment if one of the device's UMDF-based drivers has supplied an [**IPnpCallback::OnQueryStop**](https://msdn.microsoft.com/library/windows/hardware/ff556811) callback function, and the callback function has vetoed the reassignment.

<a href="" id="power-down-sequence"></a>**Power-Down Sequence**  
For each UMDF-based function and filter driver that supports the device being stopped, the framework does the following, in sequence, one driver at a time, starting with the driver that is highest in the driver stack:

1.  If the driver is using self-managed I/O, the framework calls the driver's [**IPnpCallbackSelfManagedIo::OnSelfManagedIoSuspend**](https://msdn.microsoft.com/library/windows/hardware/ff556790) callback function.

2.  The framework stops all of the device's power-managed I/O queues.

3.  The framework calls the driver's [**IPnpCallback::OnD0Exit**](https://msdn.microsoft.com/library/windows/hardware/ff556803) callback function (if it exists).

4.  The framework calls the driver's [**IPnpCallbackHardware::OnReleaseHardware**](https://msdn.microsoft.com/library/windows/hardware/ff556768) callback function (if it exists) passing the list of hardware resources that the PnP manager has assigned to the device.

To see a diagram that shows these steps, see the orderly removal figure in [A User Unplugs a Device](a-user-unplugs-a-device.md).

<a href="" id="power-up-sequence-------"></a>**Power-Up Sequence**   
For each UMDF-based function and filter driver that supports the device, the framework does the following, in sequence, one driver at a time, starting with the driver that is lowest in the driver stack:

1.  The framework calls the driver's [**IPnpCallbackHardware::OnPrepareHardware**](https://msdn.microsoft.com/library/windows/hardware/ff556766) callback function (if it exists), passing the list of hardware resources that the PnP manager has assigned to the device.

2.  The framework calls the driver's [**IPnpCallback::OnD0Entry**](https://msdn.microsoft.com/library/windows/hardware/ff556799) callback function (if it exists).

3.  The framework restarts all of the device's power-managed I/O queues.

4.  If the driver is using self-managed I/O, the framework calls the driver's [**IPnpCallbackSelfManagedIo::OnSelfManagedIoRestart**](https://msdn.microsoft.com/library/windows/hardware/ff556785) callback function.

To see a diagram that shows these steps, see [A User Plugs in a Device](a-user-plugs-in-a-device.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20The%20PnP%20Manager%20Redistributes%20System%20Resources%20%20RELEASE:%20%283/24/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




