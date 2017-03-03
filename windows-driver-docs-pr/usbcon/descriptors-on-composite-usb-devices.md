---
Description: Descriptors on USB Composite Devices
MS-HAID:
- 'usbsystem\_c2ef6fcf-aadf-4411-a58d-335a0fd56803.xml'
- 'buses.descriptors\_on\_composite\_usb\_devices'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
title: Descriptors on USB Composite Devices
author: windows-driver-content
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

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20Descriptors%20on%20USB%20Composite%20Devices%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


