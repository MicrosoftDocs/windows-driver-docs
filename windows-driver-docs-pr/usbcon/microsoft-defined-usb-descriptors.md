---
title: Microsoft OS Descriptors for USB Devices
description: Microsoft provides a set of proprietary device classes and USB descriptors, which are called Microsoft OS Descriptors (MODs).
ms.date: 06/26/2024
ms.topic: concept-article
---

# Microsoft OS descriptors for USB devices

Microsoft provides a set of proprietary device classes and USB descriptors, which are called Microsoft OS Descriptors (MODs).

- [Microsoft OS 1.0 Descriptors Specification](./microsoft-os-1-0-descriptors-specification.md)
- [Microsoft OS 2.0 Descriptors Specification](./microsoft-os-2-0-descriptors-specification.md)

Due to the rapid emergence of devices that contain multiple hardware functions, many manufacturers find that their devices don't fit comfortably into any of the current universal serial bus (USB) device classes. This deprives such manufacturers of one of the most attractive features of USB technology: the standardization of driver software (according to the class of the device). Windows provides native class drivers for most of the devices that belong to standard USB device classes, and these drivers allow end users to easily attach such devices to the computer without needing to install special software.

To accommodate manufacturers whose devices don't fit into the current set of USB device classes, Microsoft developed a set of proprietary device classes and USB descriptors, which are called Microsoft OS Descriptors (MODs). Both applications and system software can identify the devices that belong to the Microsoft-defined device classes by querying the devices to determine whether they support MODs.

Microsoft OS Descriptors have important uses other than supporting the proprietary device classes. In particular, they provide a mechanism for deriving the maximum benefit from the device firmware. With the help of Microsoft OS Descriptors, you can use the firmware to deliver help files, special icons, Uniform Resource Locators (URLs), registry settings, and other data that is required to ease installation and enhance customer satisfaction. In some cases, you can forgo storage media such as floppy disks and CDs--which simplifies the delivery and support of upgrades.

## Operating system support

Microsoft OS 1.0 Descriptors are supported in:

- Windows 11
- Windows 10
- Windows 8.1
- Windows 8
- Windows 7
- Windows Vista, Windows Server 2008
- Windows XP with Service Pack 1 (SP1), Windows Server 2003

Microsoft OS 2.0 Descriptors are supported in:

- Windows 11
- Windows 10
- Windows 8.1

## Why does Windows issue a string descriptor request to index 0xEE?

Devices that support Microsoft OS Descriptors must store a special USB string descriptor in firmware at the fixed string index of 0xEE. This string descriptor is called a Microsoft OS String Descriptor.

- Its presence indicates that the device contains one or more OS feature descriptors.
- It contains the data that is required to retrieve the associated OS feature descriptors.
- It contains a signature field that differentiates the OS string descriptor from other strings that IHVs might choose to store at 0xEE.
- It contains a version number that allows for future revisions of Microsoft OS descriptors.

If there's no string descriptor at 0xEE, or the string descriptor at that index isn't a valid OS string descriptor, Windows assumes that the device doesn't contain any OS feature descriptors.

When a new device is attached to a computer for the first time, an operating system that supports Microsoft OS Descriptors requests the string descriptor that is at index 0xEE. The Microsoft OS String Descriptor contains an embedded signature field that the operating system uses to differentiate it from other strings that might be at index 0xEE. The presence of a string descriptor that contains the proper signature field at index 0xEE indicates to the operating system that the device supports Microsoft OS Descriptors. The Microsoft OS String Descriptor also provides the operating system with version information.

The operating system queries for the string descriptor at index 0xEE during device enumeration--before the driver for the device loads--which might cause some devices to malfunction. Such devices aren't supported by versions of the Windows operating system that support Microsoft OS Descriptors.

If a device doesn't contain a valid string descriptor at index 0xEE, it must respond with a stall packet (in other words, a packet that contains a packet identifier of type STALL), which is described in the "Request Errors" section of the Universal Serial Bus Specification. If the device doesn't respond with a stall packet, the system issues a single-ended zero reset packet to the device, to help it recover from its stalled state (Windows XP only).

After the operating system requests a Microsoft OS String Descriptor from a device, it creates the following registry key:

**HLKM\\SYSTEM\\CurrentControlSet\\Control\\UsbFlags\\*vvvvpppprrrrr***

The operating system creates a registry entry, named **osvc**, under this registry key that indicates whether the device supports Microsoft OS Descriptors. If the device doesn't provide a valid response the first time that the operating system queries it for a Microsoft OS String Descriptor, the operating system makes no further requests for that descriptor.

For registry entries under that key, see [USB Device Registry Entries](usb-device-specific-registry-settings.md).

For more information, see [Microsoft OS 1.0 Descriptors Specification](./microsoft-os-1-0-descriptors-specification.md).

## What types of OS feature descriptors does Windows support?

Any information to be stored as a feature descriptor must comply with one of the Microsoft defined standard formats. Other feature descriptors can't be defined or implemented without Microsoft consent. Microsoft defined the following feature descriptors:

- **Extended Compat ID**. Windows uses class and subclass codes to help locate the appropriate default driver for a USB device. However, the USB Device Working Group must allocate these codes. This means that devices that implement new types of features often don't yet have appropriate class and subclass codes, so Windows can't use the codes to select a default driver. IHVs can circumvent this problem by storing the information in firmware as an extended compatible ID OS feature descriptor. Windows can then retrieve this information when the device is plugged in and use it to help determine which default driver to load.
- **Extended Properties**. Currently, there are two levels at which properties can be declared for a USB device: class level or devnode level. The extended properties OS feature descriptor allows a vendor to store more properties, such as help pages, URLs, and icons-in device firmware.

## Related topics

- [Microsoft OS 1.0 Descriptors Specification](./microsoft-os-1-0-descriptors-specification.md)
- [Microsoft OS 2.0 Descriptors Specification](./microsoft-os-2-0-descriptors-specification.md)
- [Building USB devices for Windows](building-usb-devices-for-windows.md)
