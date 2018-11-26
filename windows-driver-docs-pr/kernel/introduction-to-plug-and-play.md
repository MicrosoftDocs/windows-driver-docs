---
title: Introduction to Plug and Play
description: Introduction to Plug and Play
ms.assetid: 2ad9663b-ea47-4f7a-a382-53de3719214b
keywords: ["PnP WDK kernel , about Plug and Play", "Plug and Play WDK kernel , about Plug and Play"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Introduction to Plug and Play





Plug and Play (PnP) is a combination of hardware and software support that enables a computer system to recognize and adapt to hardware configuration changes with little or no intervention by a user. A user can add devices to, and remove devices from, a computer system without having to do awkward and confusing manual configuration, and without having knowledge of intricate computer hardware. For example, a user can dock a portable computer and use the docking station keyboard, mouse, and monitor without making manual configuration changes.

PnP requires support from device hardware, system software, and drivers. Initiatives in the hardware industry define standards (such as the PnP ISA definition and the PC Card standard) for easy identification of add-in boards and basic system components. This Windows Driver Kit (WDK) documentation focuses on the system software support for PnP and how drivers use that support to implement PnP.

The system software support for PnP, together with PnP drivers provides the following:

-   Automatic and dynamic recognition of installed hardware

    The system software recognizes hardware during initial system installation, recognizes PnP hardware changes that occur between system boots, and responds to run-time hardware events such as docking or undocking and device insertion or removal.

-   Hardware resource allocation (and reallocation)

    The PnP manager determines the hardware resources requested by each device (for example, input/output ports \[I/O\], interrupt requests \[IRQs\], direct memory access \[DMA\] channels, and memory locations) and assigns hardware resources appropriately. The PnP manager reconfigures resource assignments when necessary, such as when a new device is added to the system that requires resources already in use.

    Drivers for PnP devices do not assign resources; instead, the requested resources for a device are identified when the device is enumerated. The PnP manager retrieves the requirements for each device during resource allocation. Resources are not dynamically configurable for legacy devices, so the PnP manager assigns resources to legacy devices first.

-   Loading of appropriate drivers

    The PnP manager determines which drivers are required to support each device and loads those drivers.

-   A programming interface for drivers to interact with the PnP system

    The interface includes [I/O manager routines](https://msdn.microsoft.com/library/windows/hardware/ff551797), [Plug and Play minor IRPs](https://msdn.microsoft.com/library/windows/hardware/ff558807), required [standard driver routines](https://msdn.microsoft.com/library/windows/hardware/ff563842), and information in the registry.

-   Mechanisms for drivers and applications to learn of changes in the hardware environment and take appropriate actions

    PnP enables drivers and user-mode code to register for, and be notified of, certain hardware events.

PnP drivers are an important part of PnP support. For a driver to qualify as PnP it must provide the required PnP entry points, handle the required PnP IRPs, and follow PnP guidelines.

This section contains the following additional topics:

[PnP Components](pnp-components.md)

[Levels of Support for PnP](levels-of-support-for-pnp.md)

[PnP Driver Design Guidelines](pnp-driver-design-guidelines.md)

[Device Tree](device-tree.md)

[Hardware Resources](hardware-resources.md)

[State Transitions for PnP Devices](state-transitions-for-pnp-devices.md)

 

 




