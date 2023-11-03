---
title: Overview of system battery management
description: Learn about the components and roles involved in system battery management, including battery GUI, power manager, and various drivers.
ms.date: 11/01/2023
---

# Overview of system battery management

## System components

Battery management involves the following system components:

- Battery GUI: Presents status information to users and allows them to set battery options
- Power manager
- Composite battery driver: A kernel-mode driver supplied by Microsoft
- Battery class driver: A kernel-mode driver supplied by Microsoft
- Battery miniclass drivers: For individual battery devices
- Devices: Including batteries and some Uninterruptible Power Supplies (UPS)

:::image type="content" source="images/compbatt.png" alt-text="Diagram showing the components of a battery management system, including Battery GUI, Power manager, Composite battery driver, Battery class driver, Battery miniclass drivers, and Devices.":::

Devices controlled by battery miniclass drivers include batteries and some UPS devices. Batteries can be primary (nonrechargeable) or secondary (rechargeable) cells. A UPS is essentially a system battery with a much larger capacity and a different alert threshold than a laptop battery.

**Note**: For UPS units connected to COM ports, [writing a UPS minidriver](writing-ups-minidrivers.md) is preferable to writing a battery miniclass driver for operating systems prior to Windows Vista.

## Component roles

As shown in the diagram, the role of each component in battery operations is as follows:

- Bus driver and optional filter drivers: Layered between the device and its miniclass driver.

- Battery miniclass driver: Function driver for a specific type of battery or UPS device.

- Composite battery driver: Tracks the status of all batteries in the system and acts as an intermediary between the power manager and the battery class/miniclass drivers. The composite battery driver receives IRPs from the power manager and notifies the power manager when the battery status changes (for example, when system battery power becomes critically low). The composite battery driver interacts with the battery class driver in much the same way that a battery miniclass driver does, but it is transparent to other miniclass drivers. The system has one composite battery driver, supplied by Microsoft.

- Battery class driver: Supports all battery miniclass drivers and the composite battery driver. The system has one battery class driver, supplied by Microsoft.

- Power manager: Sends power and Plug and Play (PnP) IRPs to battery device stacks through the composite battery driver. The power manager does not interact directly with the battery class or miniclass drivers; all IRPs are sent through the composite battery driver.

- Battery GUI: Gets system battery status from the composite battery driver through the power manager and presents the information to the user. The GUI also sends IRPs to the battery miniclass drivers for device-specific information. The system has one battery GUI, supplied by the hardware vendor.
