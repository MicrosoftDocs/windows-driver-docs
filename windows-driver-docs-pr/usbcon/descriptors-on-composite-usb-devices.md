---
Description: Descriptors on USB Composite Devices
title: Descriptors on USB Composite Devices
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Descriptors on USB Composite Devices


As described by the USB specification, every USB device provides a set of hierarchical descriptors that define its functionality. At the top level, each device has one or more USB configuration descriptors, each of which has one or more interface descriptors. For further information about USB configuration descriptors, see [USB Configuration Descriptors](usb-configuration-descriptors.md). Configurations are mutually exclusive, so only one configuration can be selected to operate at a time.

Prior to Windows Vista, Microsoft-supplied drivers only select configuration 1. In Windows Vista and the later versions of Windows, you can set a registry value to specify which configuration the [USB Generic Parent Driver (Usbccgp.sys)](usb-common-class-generic-parent-driver.md) will use. For more information about selecting the device configuration on composite devices, see [How to select a configuration for a USB device](how-to-select-a-configuration-for-a-usb-device.md).

Within a configuration, interfaces and interface collections are managed independently. Each interface is represented, at the descriptor level, by a unique value in the **bInterfaceNumber** member of its [**USB\_INTERFACE\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff540065) structure.

The function of an interface is indicated by the **bInterfaceClass**, **bInterfaceSubClass**, and **bInterfaceProtocol** members of the same structure, along with the class-specific descriptors that might follow it.

For more information on descriptors, see [USB Descriptors](usb-descriptors.md).

## Related topics
[USB Generic Parent Driver (Usbccgp.sys)](usb-common-class-generic-parent-driver.md)  
[Microsoft-provided USB drivers](system-supplied-usb-drivers.md)  



