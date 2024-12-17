---
title: Roadmap for developing NDIS drivers
description: Learn how to create a Network Driver Interface Specification (NDIS) driver package.
keywords:
- NDIS WDK , drivers
- NDIS WDK , drivers, developing
- developing NDIS drivers WDK
- Network Driver Interface Specification (NDIS) WDK
ms.date: 12/17/2024
---

# Roadmap for developing NDIS drivers

To create a Network Driver Interface Specification (NDIS) driver package, follow these steps:

1. Learn about Windows architecture and drivers.

    You must understand the fundamentals of how drivers work in Windows operating systems. Knowing the fundamentals helps you make appropriate design decisions and lets you streamline your development process. For more information about driver fundamentals, see [Concepts for all driver developers](../gettingstarted/concepts-and-knowledge-for-all-driver-developers.md).

1. Learn about NDIS.

    For general information about NDIS and NDIS drivers, see the following articles:

    - [Windows Network Architecture and the OSI Model](windows-network-architecture-and-the-osi-model.md)

    - [Network Driver Programming Considerations](network-driver-programming-considerations.md)

    - [Driver Stack Management](driver-stack-management.md)

    - [NET\_BUFFER Architecture](net-buffer-architecture.md)

1. Determine other Windows driver design decisions.

    For more information about making Windows design decisions, see [Creating Reliable Kernel-Mode Drivers](../kernel/creating-reliable-kernel-mode-drivers.md), [Using single source code base for 64-bit Windows](../kernel/porting-your-driver-to-64-bit-windows.md), and [Creating International INF Files](../install/creating-international-inf-files.md).

1. Learn about the Windows driver build, test, and debug processes and tools.

    Building a driver differs from building a user-mode application. For more information about Windows driver build, debug, and test processes, driver signing, and [Windows Hardware Lab Kit (HLK)](/windows-hardware/test/hlk/) testing, see [Windows hardware developer documentation](/windows-hardware/drivers). For more information about building, testing, verifying, and debugging tools, see [Driver Development Tools](../devtest/index.md).

1. Select the type of NDIS driver you want to implement.

    For more information about types of NDIS drivers, see [Navigating the Network Driver Design Guide](using-the-network-driver-design-guide.md).

    Follow the roadmaps for the type of driver.

    - [Roadmap for Developing NDIS Miniport Drivers](roadmap-for-developing-ndis-miniport-drivers.md)

    - [Roadmap for Developing NDIS Protocol Drivers](roadmap-for-developing-ndis-protocol-drivers.md)

    - [Roadmap for Developing NDIS Filter Drivers](roadmap-for-developing-ndis-filter-drivers.md)

    - [Roadmap for Developing NDIS Intermediate Drivers](roadmap-for-developing-ndis-intermediate-drivers.md)

    - [Roadmap to Develop Mobile Broadband Miniport Drivers](roadmap-to-develop-mb-miniport-drivers.md)

    - [Roadmap for Developing Windows Filtering Platform Callout Drivers](roadmap-for-developing-wfp-callout-drivers.md)

1. Review the [Network driver samples](https://github.com/microsoft/Windows-driver-samples/tree/95037b3f77f3a745f7682f991ac80e81f91f5362/network) in the [Windows driver samples](https://github.com/Microsoft/Windows-driver-samples/tree/develop) repository on GitHub.

1. Develop (or port), build, test, and debug your NDIS driver.

    See the porting guides if you're porting an existing driver:

    - [Porting NDIS 6.x Drivers to NDIS 6.40](porting-ndis-6-x-drivers-to-ndis-6-40.md)

    - [Porting NDIS 6.x Drivers to NDIS 6.30](porting-ndis-6-x-drivers-to-ndis-6-30.md)

    - [Porting NDIS 6.x Drivers to NDIS 6.20](porting-ndis-6-x-drivers-to-ndis-6-20.md)

    - [Porting NDIS 5.x Drivers to NDIS 6.0](/previous-versions/windows/hardware/network/porting-ndis-5-x-drivers-to-ndis-6-0)

    For more information about iterative building, testing, and debugging, see [Windows hardware developer documentation](/windows-hardware/drivers). This process helps ensure that you build a driver that works.

1. Create a driver package for your driver.

    For more information about how to install drivers, see [Driver Packages](../install/driver-packages.md). For more information about how to install an NDIS driver, see [Components and Files Used for Network Component Installation](components-and-files-used-for-network-component-installation.md) and [Notify Objects for Network Components](notify-objects-for-network-components.md).

1. Sign and distribute your driver.

    The final step is to sign and distribute the driver. If your driver meets the quality standards that are defined for the [Windows Hardware Lab Kit (HLK)](/windows-hardware/test/hlk/), you can distribute it through the Microsoft Windows Update program. For more information about how to distribute a driver, see [Partner Center for Windows Hardware](../dashboard/get-started-dashboard-submissions.md).

These are the basic steps. Your individual driver might require more steps.
