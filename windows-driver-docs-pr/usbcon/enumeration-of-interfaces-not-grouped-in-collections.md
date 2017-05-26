---
Description: Interfaces on a composite USB device can be grouped in collections or represent one USB function individually.
title: Enumeration of Interfaces on USB Composite Devices
author: windows-driver-content
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Enumeration of Interfaces on USB Composite Devices


Interfaces on a composite USB device can be grouped in collections or represent one USB function individually. When the interfaces are not grouped in collections, the generic parent driver creates a PDO for each interface and generates a set of hardware IDs for each PDO.

The [*device ID*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-id) for an interface PDO has the following form:

`USB\VID_v(4)&PID_p(4)&MI_z(2)`

In these IDs:

-   *v(4)* is the four-digit vendor code that the USB standards committee assigns to the vendor.
-   *p(4)* is the four-digit product code that the vendor assigns to the device.
-   *z(2)* is the interface number that is extracted from the **bInterfaceNumber** field of the interface descriptor.

The generic parent driver also generates the following compatible IDs by using the information from the interface descriptor ([**USB\_INTERFACE\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff540065)):

`USB\CLASS_d(2)&SUBCLASS_s(2)&PROT_p(2)`

`USB\CLASS_d(2)&SUBCLASS_s(2)`

`USB\CLASS_d(2)`

In these IDs:

-   *d(2)* is the class code (**bInterfaceClass**)
-   *s(2)* is the subclass code (**bInterfaceSubClass**)
-   *p(2)* is the protocol code (**bInterfaceProtocol**)

Each of these codes is a four-digit number.

## Related topics
[Enumeration of Interface Collections on USB Composite Devices](support-for-interface-collections.md)  
[USB Generic Parent Driver (Usbccgp.sys)](usb-common-class-generic-parent-driver.md)  
[Microsoft-provided USB drivers](system-supplied-usb-drivers.md)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20Enumeration%20of%20Interfaces%20on%20USB%20Composite%20Devices%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


