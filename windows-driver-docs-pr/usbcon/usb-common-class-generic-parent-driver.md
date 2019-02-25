---
Description: This section describes the Usbccgp.sys driver provided by Microsoft for composite devices.
title: USB Generic Parent Driver (Usbccgp.sys)
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# USB Generic Parent Driver (Usbccgp.sys)


This section describes the Usbccgp.sys driver provided by Microsoft for composite devices.

Many USB devices expose multiple *USB interfaces*. In USB terminology, these devices are called *composite devices*. Microsoft Windows 2000 and Windows 98 operating systems include a generic parent facility in the USB bus driver (Usbhub.sys) that exposes each interface of the composite device as a separate device. In Microsoft Windows XP and Windows Me, this facility is streamlined and improved by transferring it to an independent driver called the *USB generic parent driver* (Usbccgp.sys). Using the features of the generic parent driver, device vendors can make selective use of Microsoft-supplied driver support for some interfaces.

The interfaces of some composite device operate independently. For example, a composite USB keyboard with power buttons might have one interface for the keyboard and another interface for the power buttons. The USB generic parent driver enumerates each of these interfaces as a separate device. The operating system loads the Microsoft-supplied keyboard driver to manage the keyboard interface, and the Microsoft-supplied power keys driver to manage the power keys interface.

If the composite device has an interface that is not supported by native Windows drivers, the vendor of the device should provide a driver for the interfaces and an INF file. The INF file should have an INF *DDInstall* section that matches the device ID of interface. The INF file must not match the device ID for the composite device itself, because this prevents the generic parent driver from loading. For an explanation of how the operating system loads the USB generic parent driver, see [Enumeration of USB Composite Devices](enumeration-of-the-composite-parent-device.md).

Some devices group interfaces into *interface collections* that work together to perform a particular *function*. When interfaces are grouped in interface collections, the generic parent driver treats each collection, rather than each individual interfaces, as a device. For more information on how the generic parent driver manages interface collections, see [Enumeration of Interface Collections on USB Composite Devices](support-for-interface-collections.md).

After the operating system loads the client drivers for the interfaces of a composite device, the generic parent driver multiplexes the data flow from the client drivers, combining these separate interactions into a single data stream for the composite device. The generic parent is power policy owner for the entire composite device and all of its interfaces. It also manages synchronization and PnP requests.

The generic parent driver can simplify the task for vendors of composite hardware, if Microsoft-supplied drivers support some interfaces but not others. Vendors of such devices need only supply drivers for the unsupported interfaces, because the generic parent driver facilitates the use of Microsoft-supplied drivers for the supported interfaces.

The following sections describe the features and functions of the generic parent driver:

[Enumeration of USB Composite Devices](enumeration-of-the-composite-parent-device.md)

[Descriptors on USB Composite Devices](descriptors-on-composite-usb-devices.md)

[Enumeration of Interfaces on USB Composite Devices](enumeration-of-interfaces-not-grouped-in-collections.md)

[Enumeration of Interface Collections on USB Composite Devices](support-for-interface-collections.md)

[Content Security Features in Usbccgp.sys](content-security-features-in-the-composite-client-generic-parent-drive.md)

## Related topics
[Microsoft-provided USB drivers](system-supplied-usb-drivers.md)  



