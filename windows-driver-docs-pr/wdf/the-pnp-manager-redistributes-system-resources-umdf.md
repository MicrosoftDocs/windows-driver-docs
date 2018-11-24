---
title: The PnP Manager Redistributes System Resources
description: The PnP Manager Redistributes System Resources
ms.assetid: c8e6277b-b1e5-449f-b5a0-f5a46b46e56e
keywords:
- power management scenarios WDK UMDF , PnP manager redistributes system resources
- redistribution of system resources scenario WDK UMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# The PnP Manager Redistributes System Resources


[!include[UMDF 1 Deprecation](../umdf-1-deprecation.md)]

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

 

 





