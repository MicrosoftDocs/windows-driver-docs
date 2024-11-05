---
title: Standard USB Identifiers
description: The set of identifiers generated for USB devices depends on whether the device is a single-interface device or a multiple-interface device.
keywords:
- USB identifiers WDK device installations
- single-interface devices WDK USB
- multiple-interface devices WDK USB
ms.date: 11/05/2024
---

# Standard USB identifiers

The set of identifiers generated for USB devices depends on whether the device is a single-interface device or a multiple-interface device.  

## Single-interface USB devices

When a new USB device is plugged in, the system-supplied USB hub driver composes the following device ID by using information extracted from the device's [device descriptor](/windows-hardware/drivers/ddi/usbspec/ns-usbspec-_usb_device_descriptor):

USB\\VID_v(4)&PID_d(4)&REV_r(4)

Where:

- *v(4)* is the vendor code that the [USB committee assigns to the vendor](https://www.usb.org/developers).
- *d(4)* is the product code that the vendor assigns to the device.
- *r(4)* is the revision code.

The hub driver extracts the vendor and product codes from the *idVendor*, *idProduct*, and *bcdDevice* fields of the [device descriptor](/windows-hardware/drivers/ddi/usbspec/ns-usbspec-_usb_device_descriptor), respectively. These codes are four-digit hexadecimal numbers.

An INF model section can also specify the following hardware ID:

USB\\VID_v(4)&PID_d(4)

And the following compatible IDs:

USB\\CLASS_c(2)&SUBCLASS_s(2)&PROT_p(2)

USB\\CLASS_c(2)&SUBCLASS_s(2)

USB\\CLASS_c(2)

Where:

- *c(2)* is the device class code taken from the [device descriptor](/windows-hardware/drivers/ddi/usbspec/ns-usbspec-_usb_device_descriptor).
- *s(2)* is the device subclass code.
- *p(2)* is the protocol code.

The *bDeviceClass*, *bDeviceSubClass*, and *bDeviceProtocol* fields of the [device descriptor](/windows-hardware/drivers/ddi/usbspec/ns-usbspec-_usb_device_descriptor) determine the device class code, subclass code, and protocol code, respectively. These codes are two-digit hexadecimal numbers.

## Multiple-interface USB devices

Devices with multiple interfaces are called *composite* devices. When a new [USB composite device](../usbcon/register-a-composite-driver.md) is plugged into a Windows computer, the USB hub driver creates a physical device object (PDO) and notifies the operating system to update the list of child devices. After the Windows queries the hub driver for the hardware identifiers associated with the new PDO, it searches the appropriate INF files to find a match for the identifiers. If it finds a match other than *USB\\COMPOSITE*, it loads the driver indicated in the INF file. However, if no other match is found, the operating system uses the compatible ID *USB\\COMPOSITE*, for which it loads the USB generic parent driver. The generic parent driver then creates a separate PDO and generates a separate set of hardware identifiers for each interface of the composite device.

Each interface has a device ID of the following form:

USB\\VID_v(4)&PID_d(4)&MI_z(2)

Where:

- *v(4)* is the vendor code that the [USB committee assigns to the vendor](https://www.usb.org/developers).
- *d(4)* is the product code that the vendor assigns to the device.
- *z(2)* is the interface number that is extracted from the *bInterfaceNumber* field of the corresponding [interface descriptor](/windows-hardware/drivers/ddi/usbspec/ns-usbspec-_usb_interface_descriptor).

An INF model section can also specify the following compatible IDs:

USB\\CLASS_d(2)&SUBCLASS_s(2)&PROT_p(2)

USB\\CLASS_d(2)&SUBCLASS_s(2)

USB\\CLASS_d(2)

USB\\COMPOSITE

Where:

- *d(2)* is the device class code taken from the device descriptor.
- *s(2)* is the subclass code.
- *p(2)* is the protocol code.

The *bInterfaceClass*, *bInterfaceSubClass*, and *bInterfaceProtocol* fields of the [interface descriptor](/windows-hardware/drivers/ddi/usbspec/ns-usbspec-_usb_interface_descriptor) determine the device class code, subclass code, and protocol code, respectively. These codes are two-digit hexadecimal numbers.
