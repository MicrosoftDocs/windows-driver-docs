---
Description: Interfaces on a composite USB device can be grouped in collections or represent one USB function individually.
title: Enumeration of Interfaces on USB Composite Devices
ms.date: 04/20/2017
ms.localizationpriority: medium
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



