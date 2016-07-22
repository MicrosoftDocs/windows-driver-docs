---
title: Determining the Parent of a Device
description: Determining the Parent of a Device
ms.assetid: 61458911-222f-46aa-bc0e-a61ee25337bb
keywords: ["SetupAPI functions WDK , determining parents", "parent device determining WDK SetupAPI", "device parents WDK"]
---

# Determining the Parent of a Device


## <a href="" id="ddk-determining-the-parent-of-a-device-dg"></a>


Sometimes it is necessary to access the parent of a device. For example, the operation of some types of hardware devices depends on a fixed relationship between a specific parent and set of child devices. To uninstall such a hardware device, you must uninstall the parent in addition to all the child devices. To uninstall the parent, you must obtain a [**SP\_DEVINFO\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552344) structure for the parent. A Universal Serial Bus (USB) composite device, such as, a multifunction printer, is such a device. It is represented in the system by a parent composite device and one or more child interface devices (see [USB Driver Stack Architecture](https://msdn.microsoft.com/library/windows/hardware/hh406256)). To uninstall a multifunction printer, you must uninstall its parent composite device in addition to all its child interface devices.

When the [Plug and Play](https://msdn.microsoft.com/library/windows/hardware/ff547125) (PnP) manager configures a device in the system, it adds a device node ([*devnode*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)) for the device to the [device tree](https://msdn.microsoft.com/library/windows/hardware/ff543194). When the PnP manager removes a device from the system, it deletes the devnode for the device from the device tree, and the device becomes a [*nonpresent device*](https://msdn.microsoft.com/library/windows/hardware/ff556313#wdkgloss-nonpresent-device). The approach that you use to determine the parent of a device depends on how the device is currently configured in the system, as follows:

-   If a device has a devnode in the device tree, use [**CM\_Get\_Parent**](https://msdn.microsoft.com/library/windows/hardware/ff538610) to obtain a device instance handle for its parent. Given a device instance handle, you can obtain a [device instance ID](device-instance-ids.md) and an [**SP\_DEVINFO\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552344) structure for a device. For more information, see [Obtaining the Parent of a Device in the Device Tree](obtaining-the-parent-of-a-device-in-the-device-tree.md).

-   If a device has a fixed relationship with its parent, you can save and retrieve the device instance ID of its parent. When a device becomes nonpresent, you can use its device instance handle to obtain an SP\_DEVINFO\_DATA structure for the device. For more information, see [Determining the Parent of a Nonpresent Device](determining-the-parent-of-a-nonpresent-device.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Determining%20the%20Parent%20of%20a%20Device%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




