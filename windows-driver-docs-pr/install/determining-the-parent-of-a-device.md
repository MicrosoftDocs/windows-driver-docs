---
title: Determining the Parent of a Device
description: Determining the Parent of a Device
ms.assetid: 61458911-222f-46aa-bc0e-a61ee25337bb
keywords:
- SetupAPI functions WDK , determining parents
- parent device determining WDK SetupAPI
- device parents WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Determining the Parent of a Device





Sometimes it is necessary to access the parent of a device. For example, the operation of some types of hardware devices depends on a fixed relationship between a specific parent and set of child devices. To uninstall such a hardware device, you must uninstall the parent in addition to all the child devices. To uninstall the parent, you must obtain a [**SP_DEVINFO_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552344) structure for the parent. A Universal Serial Bus (USB) composite device, such as, a multifunction printer, is such a device. It is represented in the system by a parent composite device and one or more child interface devices (see [USB Driver Stack Architecture](https://msdn.microsoft.com/library/windows/hardware/hh406256)). To uninstall a multifunction printer, you must uninstall its parent composite device in addition to all its child interface devices.

When the [Plug and Play](https://msdn.microsoft.com/library/windows/hardware/ff547125) (PnP) manager configures a device in the system, it adds a device node ([*devnode*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)) for the device to the [device tree](https://msdn.microsoft.com/library/windows/hardware/ff543194). When the PnP manager removes a device from the system, it deletes the devnode for the device from the device tree, and the device becomes a [*nonpresent device*](https://msdn.microsoft.com/library/windows/hardware/ff556313#wdkgloss-nonpresent-device). The approach that you use to determine the parent of a device depends on how the device is currently configured in the system, as follows:

-   If a device has a devnode in the device tree, use [**CM_Get_Parent**](https://msdn.microsoft.com/library/windows/hardware/ff538610) to obtain a device instance handle for its parent. Given a device instance handle, you can obtain a [device instance ID](device-instance-ids.md) and an [**SP_DEVINFO_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552344) structure for a device. For more information, see [Obtaining the Parent of a Device in the Device Tree](obtaining-the-parent-of-a-device-in-the-device-tree.md).

-   If a device has a fixed relationship with its parent, you can save and retrieve the device instance ID of its parent. When a device becomes nonpresent, you can use its device instance handle to obtain an SP_DEVINFO_DATA structure for the device. For more information, see [Determining the Parent of a Nonpresent Device](determining-the-parent-of-a-nonpresent-device.md).

 

 





