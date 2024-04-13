---
title: USB Descriptors
description: A USB device provides information about itself in data structures called USB descriptors. This section provides information about various descriptors that a client driver can obtain from a USB device.
ms.date: 01/17/2024
---

# USB descriptors

A USB device provides information about itself in data structures called *USB descriptors*. This section provides information about various descriptors that a client driver can obtain from a USB device.

The host obtains descriptors from an attached device by sending various standard control requests (GET\_DESCRIPTOR requests) to the default endpoint. Those requests specify the type of descriptor to retrieve. In response to such requests, the device sends descriptors that include information about the device, its configurations, interfaces and the related endpoints. *Device descriptors* contain information about the whole device. *Configuration descriptors* contain information about each device configuration. *String descriptors* contain Unicode text strings.

Every USB device exposes a device descriptor that indicates the device's class information, vendor and product identifiers, and number of configurations. Each configuration exposes its configuration descriptor that indicates number of interfaces and power characteristics. Each interface exposes an interface descriptor for each of its alternate settings that contains information about the class and the number of endpoints. Each endpoint within each interface exposes endpoint descriptors that indicate the endpoint type and the maximum packet size.

For example, consider the OSR FX2 board device layout described in [USB Device Layout](usb-device-layout.md). At device level, the device exposes a device descriptor and an endpoint descriptor for the default endpoint. At configuration level, the device exposes a configuration descriptor for Configuration 0. At interface level, it exposes one interface descriptor for Alternate Setting 0. At the endpoint level, it exposes three endpoint descriptors.

## In this section

| Article | Description |
|---|---|
| [USB device descriptors](usb-device-descriptors.md) | The device descriptor contains information about a USB device as a whole. This article describes the **[USB_DEVICE_DESCRIPTOR](/windows-hardware/drivers/ddi/usbspec/ns-usbspec-_usb_device_descriptor)** structure and includes information about how a client driver can send a get-descriptor request to obtain the device descriptor. |
| [USB configuration descriptors](usb-configuration-descriptors.md) | A USB device exposes its capabilities in the form of a series of interfaces called a USB configuration. Each interface consists of one or more alternate settings, and each alternate setting is made up of a set of endpoints. This article describes the various descriptors associated with a USB configuration. |
| [USB String Descriptors](usb-string-descriptors.md) | Device, configuration, and interface descriptors may contain references to string descriptors. This article describes how to get a particular string descriptor from the device. |
| [USB Interface Association Descriptor](usb-interface-association-descriptor.md) | USB interface association descriptor (IAD) allows the device to group interfaces that belong to a function. This article describes how a client driver can determine whether the device contains an IAD for a function. |

## Related topics

- [USB Device Layout](usb-device-layout.md)
- [USB Driver Development Guide](usb-driver-development-guide.md)
