---
title: Roadmap for Developing Network Drivers with Winsock Kernel
description: Roadmap for Developing Network Drivers with Winsock Kernel
ms.date: 04/20/2017
---

# Roadmap for Developing Network Drivers with Winsock Kernel


To create a networking driver package that uses the kernel-mode socket programming features of Winsock Kernel (WSK), follow these steps:

-   **Step 1:** Learn about Windows architecture and drivers.

    You must understand the fundamentals of how drivers work in Windows operating systems. Knowing the fundamentals will help you make appropriate design decisions and let you streamline your development process. For more information about driver fundamentals, see [Concepts for all driver developers](../gettingstarted/concepts-and-knowledge-for-all-driver-developers.md).

-   **Step 2:** Learn about the Network Driver Interface Specification (NDIS).

    Your driver package will typically use Network Driver Interface Specification (NDIS) interfaces. For more information about NDIS and NDIS miniport drivers, see the following topics:

    [Windows Network Architecture and the OSI Model](windows-network-architecture-and-the-osi-model.md)

    [NDIS Miniport Drivers](roadmap-for-developing-ndis-miniport-drivers.md)

    [Writing NDIS Miniport Drivers](./initializing-a-miniport-driver.md)

    [Network Driver Programming Considerations](network-driver-programming-considerations.md)

-   **Step 3:** Determine additional network components to use in your driver.

    In addition to the core NDIS features, you can use the following additional Windows network components with kernel-mode drivers, depending on the hardware configuration:

    [IP Helper](ip-helper.md)

    [Windows Filtering Platform Callout Drivers](introduction-to-windows-filtering-platform-callout-drivers.md)

    [Native 802.11 Wireless LAN](/previous-versions/windows/hardware/wireless/ff560689(v=vs.85))

    [Mobile Broadband Network Interface](mb-interface-overview.md)

-   **Step 4:** Learn the fundamentals of Winsock Kernel.

    Winsock Kernel is supported in Windows Vista and later versions of Windows. For information about how to use Winsock Kernel, see [Introduction to Winsock Kernel](introduction-to-winsock-kernel.md).

    A simpler, more generic network programming interface that you can use in network drivers is [Network Module Registrar](network-module-registrar2.md).

-   **Step 5:** Determine additional Windows driver design decisions.

    For information about how to make additional Windows design decisions, see [Creating Reliable Kernel-Mode Drivers](../kernel/creating-reliable-kernel-mode-drivers.md), [Programming Issues for 64-Bit Drivers](../kernel/porting-your-driver-to-64-bit-windows.md), and [Creating International INF Files](../install/creating-international-inf-files.md).

-   **Step 6:** Learn about the Windows driver build, test, and debug processes and tools.

    Building a driver differs from building a user-mode application. For information about Windows driver build, debug, and test processes, driver signing, and [Windows Hardware Certification Kit (HCK)](https://go.microsoft.com/fwlink/p/?LinkId=733613) testing, see [Building, Debugging, and Testing Drivers](/windows-hardware/drivers). For information about tools for building, testing, verifying, and debugging, see [Driver Development Tools](../devtest/index.md).

-   **Step 7:** Review the [Winsock Kernel (WSK TCP Echo Server) driver sample](https://go.microsoft.com/fwlink/p/?LinkId=617935) in the [Windows driver samples](https://go.microsoft.com/fwlink/p/?LinkId=616507) repository on GitHub.

-   **Step 8:** Develop, build, test, and debug your driver.

    For information about iterative building, testing, and debugging, see [Overview of Build, Debug, and Test Process](/windows-hardware/drivers). This process helps ensure that you build a driver that works.

-   **Step 9:** Create a driver package for your driver.

    For information about how to install drivers, see [Providing a Driver Package](/windows-hardware/drivers).

-   **Step 10:** Sign and distribute your driver.

    The final step is to sign (optional) and distribute the driver. If your driver meets the quality standards that are defined for the [Windows Hardware Certification Kit (HCK)](https://go.microsoft.com/fwlink/p/?LinkId=733613), you can distribute it through the Microsoft Windows Update program. For more information about how to distribute a driver, see [Distributing a Driver](/windows-hardware/drivers).

These are the basic steps. Additional steps might be necessary based on the needs of your individual driver.

