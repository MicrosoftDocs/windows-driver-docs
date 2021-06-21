---
title: Architecture and overview for HID over the SPI transport
description: Describes the driver stack for devices that support HID over the SPI transport.
ms.date: 06/18/2021
ms.localizationpriority: medium
---

# Architecture and overview for HID over the SPI transport

This section describes the driver stack for devices that support HID over the SPI transport.

## Architecture and overview

The HID SPI driver stack consists of existing and new components supplied by Microsoft, as well as components provided by the SPI silicon manufacturer. The following illustration depicts the stack and these components.

:::image type="content" source="images/hid-spi-arch.png" alt-text="The HID over SPI driver stack.":::

Windows provides an interface for low-power, simple buses to communicate effectively with the operating system. This interface is referred to as simple peripheral bus (SPB), and it supports buses like Inter-Integrated Circuit (I²C) and Serial Peripheral Interface (SPI). For additional details about SPB, refer to the [Simple peripheral bus (SPB)](../bringup/simple-peripheral-bus--spb-.md) topic.

Windows provides a KMDF-based HID miniport driver that implements version 1.0 of the protocol specification for HID over SPI. This driver is named HIDSPI.sys. Windows loads this driver based on a compatible ID match, which is exposed by the Advanced Configuration and Power Interface (ACPI). The driver ensures that apps that use HID IOCTLs application level compatibility for software that leverages the HID IOCTLs and API set. A device will assert the host when it requires attention or has data. However, before the assertion occurs, a GPIO connection must exist.

> [!NOTE]
> The HIDSPI.sys device driver supports only the SPI bus. It does not support I²C, SMBUS, or other low-power buses in Windows.

## The SPI Controller Driver

The SPI controller driver exposes a Serial Peripheral Bus (SPB) IOCTL interface to perform read and write operations. This driver provides the actual controller intrinsics (for example, SPI). The SPB Class Extension, on behalf of the controller driver, handles all interaction with the resource hub and implements necessary queues to manage simultaneous targets.

> [!NOTE]
> The HID SPI driver will not function on systems that do not have an SPI bus that is compatible with the SPB platform. Contact your system manufacturer to determine whether the SPI bus on your device system is compatible with the SPB platform.

## The GPIO Controller Driver

The General Purpose Input/Output (GPIO) controller delivers interrupts from the device over GPIO. This is often a simple subordinate component that uses GPIO pins to signal Windows of new data or other events. GPIO can also control the device by approaches other than the SPI channel.

## The Resource Hub

Connections on a SoC platform are typically non-discoverable, because there are no standards for device enumeration on the buses that are used on SoC. As a result, these devices must be statically defined in the Advanced Configuration and Power Interface (ACPI). Furthermore, components often have multiple dependencies spanning multiple buses, as opposed to a strict branching tree structure.

The resource hub is a proxy that manages the connections among all devices and bus controllers. The HIDSPI driver uses the resource hub to reroute device-open requests to the appropriate controller driver. For more information about the resource hub, refer to the [Connection IDs for SPB Connected Devices](../spb/connection-ids-for-spb-connected-peripheral-devices.md) topic.
