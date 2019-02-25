---
title: Standard USB Identifiers
description: Standard USB Identifiers
ms.assetid: 39acb62b-83f2-4d14-a678-c37817193f01
keywords:
- USB identifiers WDK device installations
- single-interface devices WDK USB
- multiple-interface devices WDK USB
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Standard USB Identifiers





<a href="" id="the-set-of-identifiers-generated-for-usb-devices-depends-on-whether-the-device-is-a-single-interface-device-or-a-multiple-interface-device-"></a>The set of identifiers generated for USB devices depends on whether the device is a single-interface device or a multiple-interface device.  

### Single-Interface USB Devices

When a new USB device is plugged in, the system-supplied USB hub driver composes the following device ID by using information extracted from the device's device descriptor:

USB\\VID_v(4)&PID_d(4)&REV_r(4)

Where:

-   *v(4)* is the 4-digit vendor code that the USB committee assigns to the vendor.

-   *d(4)* is the 4-digit product code that the vendor assigns to the device.

-   *r(4)* is the revision code.

The hub driver extracts the vendor and product codes from the *idVendor* and *idProduct* fields of the device descriptor, respectively.

An INF model section can also specify the following hardware ID:

USB\\VID_v(4)&PID_d(4)

and the following compatible IDs:

USB\\CLASS_c(2)&SUBCLASS_s(2)&PROT_p(2)

USB\\CLASS_c(2)&SUBCLASS_s(2)

USB\\CLASS_c(2)

Where:

-   *c(2)* is the device class code taken from the device descriptor.

-   *s(2)* is the device subclass code.

-   *p(2)* is the protocol code.

The device class code, subclass code, and protocol code are determined by the *bDeviceClass, bDeviceSubClass,* and *bDeviceProtocol* fields of the device descriptor, respectively. These are 2-digit numbers.

### Multiple-Interface USB Devices

Devices with multiple interfaces are called *composite* devices. Starting with Windows 2000, when a new [USB composite device](https://msdn.microsoft.com/library/windows/hardware/ff537109) is plugged into a computer, the USB hub driver creates a physical device object (PDO) and notifies the operating system that its set of child devices has changed. After querying the hub driver for the hardware identifiers associated with the new PDO, the operating system searches the appropriate INF files to find a match for the identifiers. If it finds a match other than *USB\\COMPOSITE*, it loads the driver indicated in the INF file. However, if no other match is found, the operating system uses the compatible ID *USB\\COMPOSITE*, for which it loads the USB Generic Parent driver. The Generic Parent driver then creates a separate PDO and generates a separate set of hardware identifiers for each interface of the composite device.

Each interface has a device ID of the following form:

USB\\ VID_v(4)&PID_d(4)&MI_z(2)

Where:

-   *v(4)* is the 4-digit vendor code that the USB committee assigns to the vendor.

-   *d(4)* is the 4-digit product code that the vendor assigns to the device.

-   *z(2)* is the interface number that is extracted from the *bInterfaceNumber* field of the interface descriptor.

An INF model section can also specify the following compatible IDs:

USB\\CLASS_d(2)&SUBCLASS_s(2)&PROT_p(2)

USB\\CLASS_d(2)&SUBCLASS_s(2)

USB\\CLASS_d(2)

USB\\COMPOSITE

Where:

-   *d(2)* is the device class code taken from the device descriptor.

-   *s(2)* is the subclass code.

-   *p(2)* is the protocol code.

The device class code, subclass code, and protocol code are determined by the *bInterfaceClass, bInterfaceSubClass, and bInterfaceProtocol* fields of the interface descriptor, respectively. These are 2-digit numbers.

 

 





