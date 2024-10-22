---
title: Architecture and Overview for HID Over the I2C Transport
description: This article describes the driver stack for devices that support HID over the I2C transport.
ms.date: 10/22/2024
---

# Architecture and overview for HID over the I2C transport

This article describes the driver stack for devices that support HID over the I2C transport.

## Architecture and overview

The HID I2C driver stack consists of existing and new components supplied by Microsoft, and components provided by the I2C silicon manufacturer. The following illustration depicts the stack and these components.

![hid over i2c driver stack.](images/hid-i2c-arch.png)

Windows 8 provides an interface for low-power, simple buses to communicate effectively with the operating system. This interface is referred to as simple peripheral bus (SPB), and it supports buses like Inter-Integrated Circuit (I2C) and Serial Peripheral Interface (SPI). For more information about SPB, see [Simple Peripheral Buses](/windows-hardware/drivers/spb/).

Windows 8 provides a KMDF-based HID miniport driver that implements version 1.0 of the protocol specification for HID over I2C. This driver is named HIDI2C.sys. Windows loads this driver based on a compatible ID match, which is exposed by the Advanced Configuration and Power Interface (ACPI). The driver ensures that apps that use HID IOCTLs application level compatibility for software that uses the HID IOCTLs and API set. A device asserts the host when it requires attention or has data. However, before the assertion occurs, a GPIO connection must exist.

**Note**  The HIDI2C.sys device driver supports only the I2C bus. It doesn't support SPI, SMBUS, or other low-power buses in Windows 8.

## The I2C Controller Driver

The I2C controller driver exposes a Serial Peripheral Bus (SPB) IOCTL interface to perform read and write operations. This driver provides the actual controller intrinsics (for example, I2C). The SPB Class Extension, on behalf of the controller driver, handles all interaction with the resource hub and implements necessary queues to manage simultaneous targets.

**Note**  The HID I2C driver doesn't function on systems that don't have an I2C bus that is compatible with the SPB platform. Contact your system manufacturer to determine whether the I2C bus on your device system is compatible with the SPB platform.

## The GPIO Controller Driver

The General Purpose Input/Output (GPIO) controller delivers interrupts from the device over GPIO. This controller is often a simple subordinate component that uses GPIO pins to signal Windows of new data or other events. GPIO can also control the device by approaches other than the I2C channel.

## The Resource Hub

Connections on a SoC platform are typically nondiscoverable, because there are no standards for device enumeration on the buses that are used on SoC. As a result, these devices must be statically defined in the Advanced Configuration and Power Interface (ACPI). Furthermore, components often have multiple dependencies spanning multiple buses, as opposed to a strict branching tree structure.

The resource hub is a proxy that manages the connections among all devices and bus controllers. The HIDI2C driver uses the resource hub to reroute device-open requests to the appropriate controller driver. For more information about the resource hub, see [Connection IDs for SPB Connected Devices](../spb/connection-ids-for-spb-connected-peripheral-devices.md).
