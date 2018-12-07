---
title: Roadmap for Developing Network Drivers with Winsock Kernel
description: Roadmap for Developing Network Drivers with Winsock Kernel
ms.assetid: f94952c3-02b1-4bd2-bd73-e6d6d42a06fb
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Roadmap for Developing Network Drivers with Winsock Kernel


To create a networking driver package that uses the kernel-mode socket programming features of Winsock Kernel (WSK), follow these steps:

-   **Step 1:** Learn about Windows architecture and drivers.

    You must understand the fundamentals of how drivers work in Windows operating systems. Knowing the fundamentals will help you make appropriate design decisions and let you streamline your development process. For more information about driver fundamentals, see [Concepts for all driver developers](https://msdn.microsoft.com/library/windows/hardware/ff554731).

-   **Step 2:** Learn about the Network Driver Interface Specification (NDIS).

    Your driver package will typically use Network Driver Interface Specification (NDIS) interfaces. For more information about NDIS and NDIS miniport drivers, see the following topics:

    [Windows Network Architecture and the OSI Model](windows-network-architecture-and-the-osi-model.md)

    [NDIS Miniport Drivers](ndis-miniport-drivers.md)

    [Writing NDIS Miniport Drivers](writing-ndis-miniport-drivers.md)

    [Network Driver Programming Considerations](network-driver-programming-considerations.md)

-   **Step 3:** Determine additional network components to use in your driver.

    In addition to the core NDIS features, you can use the following additional Windows network components with kernel-mode drivers, depending on the hardware configuration:

    [IP Helper](ip-helper.md)

    [Windows Filtering Platform Callout Drivers](introduction-to-windows-filtering-platform-callout-drivers.md)

    [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560689)

    [Mobile Broadband Network Interface](mb-interface-overview.md)

-   **Step 4:** Learn the fundamentals of Winsock Kernel.

    Winsock Kernel is supported in Windows Vista and later versions of Windows. For information about how to use Winsock Kernel, see [Introduction to Winsock Kernel](introduction-to-winsock-kernel.md).

    A simpler, more generic network programming interface that you can use in network drivers is [Network Module Registrar](network-module-registrar2.md).

-   **Step 5:** Determine additional Windows driver design decisions.

    For information about how to make additional Windows design decisions, see [Creating Reliable Kernel-Mode Drivers](https://msdn.microsoft.com/library/windows/hardware/ff542904), [Programming Issues for 64-Bit Drivers](https://msdn.microsoft.com/library/windows/hardware/ff559923), and [Creating International INF Files](https://msdn.microsoft.com/library/windows/hardware/ff540208).

-   **Step 6:** Learn about the Windows driver build, test, and debug processes and tools.

    Building a driver differs from building a user-mode application. For information about Windows driver build, debug, and test processes, driver signing, and [Windows Hardware Certification Kit (HCK)](https://go.microsoft.com/fwlink/p/?LinkId=733613) testing, see [Building, Debugging, and Testing Drivers](https://msdn.microsoft.com/windows-drivers/develop/visual_studio_driver_development_environment). For information about tools for building, testing, verifying, and debugging, see [Driver Development Tools](https://msdn.microsoft.com/library/windows/hardware/ff545440).

-   **Step 7:** Review the [Winsock Kernel (WSK TCP Echo Server) driver sample](http://go.microsoft.com/fwlink/p/?LinkId=617935) in the [Windows driver samples](http://go.microsoft.com/fwlink/p/?LinkId=616507) repository on GitHub.

-   **Step 8:** Develop, build, test, and debug your driver.

    For information about iterative building, testing, and debugging, see [Overview of Build, Debug, and Test Process](https://msdn.microsoft.com/windows-drivers/develop/visual_studio_driver_development_environment). This process helps ensure that you build a driver that works.

-   **Step 9:** Create a driver package for your driver.

    For information about how to install drivers, see [Providing a Driver Package](https://msdn.microsoft.com/windows-drivers/develop/creating_a_driver_package).

-   **Step 10:** Sign and distribute your driver.

    The final step is to sign (optional) and distribute the driver. If your driver meets the quality standards that are defined for the [Windows Hardware Certification Kit (HCK)](https://go.microsoft.com/fwlink/p/?LinkId=733613), you can distribute it through the Microsoft Windows Update program. For more information about how to distribute a driver, see [Distributing a Driver](https://msdn.microsoft.com/windows-drivers/develop/distributing_a_driver_package_win8).

These are the basic steps. Additional steps might be necessary based on the needs of your individual driver.

 

 





