---
title: Roadmap for Developing NDIS Intermediate Drivers
description: Roadmap for Developing NDIS Intermediate Drivers
ms.date: 03/02/2023
---

# Roadmap for Developing NDIS Intermediate Drivers

To create a Network Driver Interface Specification (NDIS) intermediate driver package, follow these steps:

- Step 1: Learn about Windows architecture and drivers.

    You must understand the fundamentals of how drivers work in Windows operating systems. Knowing the fundamentals will help you make appropriate design decisions and let you streamline your development process. For more information about driver fundamentals, see [Concepts for all driver developers](../gettingstarted/concepts-and-knowledge-for-all-driver-developers.md).

- Step 2: Learn about NDIS.

    For general information about NDIS and NDIS drivers, see the following topics:

    [Windows Network Architecture and the OSI Model](windows-network-architecture-and-the-osi-model.md)

    [Network Driver Programming Considerations](network-driver-programming-considerations.md)

    [Driver Stack Management](driver-stack-management.md)

    [NET\_BUFFER Architecture](net-buffer-architecture.md)

- Step 3: Determine additional Windows driver design decisions.

    For more information about how to make additional Windows design decisions, see [Creating Reliable Kernel-Mode Drivers](../kernel/creating-reliable-kernel-mode-drivers.md), [Programming Issues for 64-Bit Drivers](../kernel/porting-your-driver-to-64-bit-windows.md), and [Creating International INF Files](../install/creating-international-inf-files.md).

- Step 4: Learn about the Windows driver build, test, and debug processes and tools.

    Building a driver differs from building a user-mode application. For more information about Windows driver build, debug, and test processes, driver signing, and [Windows Hardware Lab Kit (HLK)](/windows-hardware/test/hlk/) testing, see [Building, Debugging, and Testing Drivers](/windows-hardware/drivers). For more information about building, testing, verifying, and debugging tools, see [Driver Development Tools](../devtest/index.md).

- Step 5: Read the intermediate driver, miniport driver, and protocol driver introduction topics.
    [Introduction to NDIS Intermediate Drivers](introduction-to-ndis-intermediate-drivers.md)
    [Introduction to NDIS Miniport Drivers](deserialized-ndis-miniport-drivers.md)
    [NDIS Protocol Drivers](./roadmap-for-developing-ndis-protocol-drivers.md)
- Step 6: Read the [writing intermediate drivers section](writing-ndis-intermediate-drivers.md).

    Intermediate drivers use a combination of protocol driver and miniport driver interfaces in addition to some intermediate driver specific interfaces. As an option, you can also read the miniport driver and protocol driver design guides.

- Step 7: Review the [NDIS intermediate driver sample](https://go.microsoft.com/fwlink/p/?LinkId=617916) in the [Windows driver samples](https://go.microsoft.com/fwlink/p/?LinkId=616507) repository on GitHub.

- Step 8: Develop (or port), build, test, and debug your NDIS driver.

    See the porting guides if you are porting an existing driver:

  - [Porting NDIS 5.x Drivers to NDIS 6.0](/previous-versions/windows/hardware/network/porting-ndis-5-x-drivers-to-ndis-6-0)
  - [Porting NDIS 6.x Drivers to NDIS 6.20](porting-ndis-6-x-drivers-to-ndis-6-20.md)
  - [Porting NDIS 6.x Drivers to NDIS 6.30](porting-ndis-6-x-drivers-to-ndis-6-30.md)

    For more information about iterative building, testing, and debugging, see [Overview of Build, Debug, and Test Process](/windows-hardware/drivers). This process will help ensure that you build a driver that works.

- Step 9: Create a driver package for your driver.

    For more information about how to install drivers, see [Providing a Driver Package](../install/driver-packages.md). For more information about how to install an NDIS driver, see [Components and Files Used for Network Component Installation](components-and-files-used-for-network-component-installation.md) and [Notify Objects for Network Components](notify-objects-for-network-components.md).

- Step 10: Sign and distribute your driver.

    The final step is to sign (optional) and distribute the driver. If your driver meets the quality standards that are defined for the [Windows Hardware Lab Kit (HLK)](/windows-hardware/test/hlk/), you can distribute it through the Microsoft Windows Update program. For more information about how to distribute a driver, see [Get started with the hardware submission process](../dashboard/get-started-dashboard-submissions.md).

These are the basic steps. Additional steps might be necessary based on the needs of your individual driver.
