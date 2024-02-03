---
title: Introduction to Plug and Play
description: Introduction to Plug and Play
keywords: ["PnP WDK kernel , about Plug and Play", "Plug and Play WDK kernel , about Plug and Play"]
ms.date: 03/10/2021
---

# Introduction to Plug and Play

This section contains the following additional topics:

[PnP Components](pnp-components.md)

[PnP Driver Design Guidelines](pnp-driver-design-guidelines.md)

[Hardware Resources](hardware-resources.md)

Plug and Play (PnP) is the part of Windows that enables a computer system to adapt to hardware changes with minimal intervention by the user. A user can add and remove devices without having to do manual configuration, and without knowledge of computer hardware. For example, a user can dock a portable computer and use the docking station keyboard, mouse, and monitor without making manual configuration changes.

PnP requires support from device hardware, system software, and drivers. Initiatives in the hardware industry define standards for easy identification of add-in boards and system components. This Windows Driver Kit (WDK) documentation focuses on the system software support for PnP and how drivers use that support to implement PnP.

The system software support for PnP, together with PnP drivers provides the following:

-   Automatic and dynamic recognition of installed hardware

-   Hardware resource allocation (and reallocation)

    The PnP manager determines the hardware resources requested by each device (for example, input/output ports, interrupt requests, direct memory access channels, and memory locations) and assigns hardware resources appropriately. The PnP manager reconfigures resource assignments when necessary, such as when a new device is added to the system that requires resources already in use.

    Drivers for PnP devices do not assign resources; instead, the requested resources for a device are identified when the device is enumerated. The PnP manager retrieves the requirements for each device during resource allocation. Resources are not dynamically configurable for legacy devices, so the PnP manager assigns resources to legacy devices first.

-   Loading of appropriate drivers

-   A programming interface for drivers to interact with the PnP system

    The interface includes I/O manager routines, Plug and Play minor IRPs, required [standard driver routines](./introduction-to-standard-driver-routines.md), and information in the registry.

-   Mechanisms for drivers and applications to learn of changes in the hardware environment and take appropriate actions

    PnP enables drivers and user-mode code to register for, and be notified of, certain hardware events.

For a driver to qualify as PnP it must provide the required PnP entry points, handle the required PnP IRPs, and follow PnP guidelines.
