---
title: Overview of Remote NDIS (RNDIS)
description: Learn how Remote NDIS (RNDIS) eliminates the need to write NDIS miniport drivers for USB network devices. Discover the architecture, benefits, and implementation details.
ms.date: 11/05/2025
ms.topic: concept-article
---

# Overview of Remote NDIS (RNDIS)

Remote NDIS (RNDIS) eliminates the need for hardware vendors to write an NDIS miniport device driver for a network device attached to the USB bus. 

Key benefits:

- Reduces development burden on device manufacturers
- Improves system stability (no new drivers required)
- Better end-user experience (no driver installation needed)
- Supports multiple USB networking devices with one driver set

Remote NDIS defines a standardized bus-independent message set that operates over the USB bus. Microsoft Windows provides support for Remote NDIS over USB.

The diagram below shows how Remote NDIS replaces custom NDIS miniport drivers. As a device manufacturer, you can focus on device implementation instead of developing Windows NDIS device drivers.

:::image type="content" source="images/remote-ndis-architecture.png" alt-text="Screenshot of Remote NDIS architecture diagram showing NDIS miniport replacement with Remote NDIS miniport driver and USB transport driver.":::

Microsoft provides an NDIS miniport driver, Rndismp.sys, which implements the Remote NDIS message set and communicates with generic bus transport drivers, which in turn communicate with the appropriate bus driver. Microsoft implements and maintains this NDIS miniport driver and distributes it as part of Windows.

The following Remote NDIS message set mirrors the semantics of the NDIS miniport driver interface:

- Initializing, resetting, and halting device operation
- Transmitting and receiving networking data packets
- Setting and querying device operational parameters
- Indicating media link status and monitoring device status

Microsoft also provides a USB bus transport driver that implements a mechanism for carrying the Remote NDIS messages across the USB bus. This driver transports standardized Remote NDIS messages between the Remote NDIS miniport driver and the bus-specific driver, such as USB. The bus-specific drivers are also required to map any bus-specific requirements, such as power management, into standardized Remote NDIS messages. Microsoft implements and maintains the transport driver for USB 1.1 and 2.0 and distributes it as part of Windows.

This structure allows a single device driver to be used for any Remote NDIS device for which there's a bus-specific transport layer. In addition, only one bus transport layer is required for all network devices on a specific bus.

## Next steps

- [Benefits of Remote NDIS](benefits-of-remote-ndis.md)
- [Remote NDIS Concepts and Definitions](remote-ndis-concepts-and-definitions.md)
- [Remote NDIS File Naming Conventions](remote-ndis-file-naming-conventions.md)
- [Remote NDIS Messaging](remote-ndis-messaging.md)
- [Remote NDIS Device Control](remote-ndis-device-control.md)
- [Remote NDIS INF Template](remote-ndis-inf-template.md)
- [Types of Remote NDIS Devices](types-of-remote-ndis-devices.md)
- [USB class drivers included in Windows](../usbcon/supported-usb-classes.md)
