---
title: Determining the Parent of a Device
description: Determining the Parent of a Device
keywords:
- SetupAPI functions WDK , determining parents
- parent device determining WDK SetupAPI
- device parents WDK
ms.date: 03/30/2022
---

# Determining the Parent of a Device

Sometimes it is necessary to access the parent of a device. For example, the operation of some types of hardware devices depends on a fixed relationship between a specific parent and set of child devices. To uninstall such a hardware device, you must uninstall the parent in addition to all the child devices. To uninstall the parent, you must obtain a [**SP_DEVINFO_DATA**](/windows/win32/api/setupapi/ns-setupapi-sp_devinfo_data) structure for the parent. A Universal Serial Bus (USB) composite device, such as, a multifunction printer, is such a device. It is represented in the system by a parent composite device and one or more child interface devices (see [USB Driver Stack Architecture](../usbcon/usb-3-0-driver-stack-architecture.md)). To uninstall a multifunction printer, you must uninstall its parent composite device in addition to all its child interface devices.

When the [Plug and Play](../kernel/introduction-to-plug-and-play.md) (PnP) manager configures a device in the system, it adds a device node (*devnode*) for the device to the [device tree](../kernel/device-tree.md). When the PnP manager removes a device from the system, it removes the devnode for the device from the device tree, and the device becomes a *non-present device*. 

To determine the [device instance ID](device-instance-ids.md) of the parent of a device, you can query the [**DEVPKEY_Device_Parent**](devpkey-device-parent.md) property on the device using [**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw).  For a *present* device, this will provide you the device instance ID of the parent of that device.  For a *non-present* device:
-  On Windows 8 and later:
    -  If the parent of the *non-present* device from the last time the *non-present* device was a *present* device still exists as a device on the system (*present* or *non-present* device), [**DEVPKEY_Device_Parent**](devpkey-device-parent.md) will provide the device instance ID of that parent device.
    -  If the parent of the *non-present* device from the last time the *non-present* device was a *present* device does not still exist as a device on the system, [**DEVPKEY_Device_Parent**](devpkey-device-parent.md) will return the device instance ID of the device that is at the root of the device tree.
-  Prior to Windows 8:
    -  Retrieving [**DEVPKEY_Device_Parent**](devpkey-device-parent.md) will return an error that the property is not found.

Once you have the device instance ID of the parent device, you can use [**SetupDiOpenDeviceInfo**](/windows/win32/api/setupapi/nf-setupapi-setupdiopendeviceinfow) to obtain a [**SP_DEVINFO_DATA**](/windows/win32/api/setupapi/ns-setupapi-sp_devinfo_data) structure for the parent.
