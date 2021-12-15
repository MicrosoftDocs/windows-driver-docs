---
title: Roadmap to Develop MB Miniport Drivers
description: Roadmap to Develop MB Miniport Drivers
ms.date: 04/20/2017
---

# Roadmap to Develop MB Miniport Drivers


To create an MB miniport driver, follow these steps:

-   **Step 1**: Learn about Windows architecture and miniport drivers.

    You must understand the fundamentals of how drivers work in Windows operating systems. Knowing the fundamentals will help you make appropriate design decisions and let you streamline your development process. For more information about driver fundamentals, see [Concepts for all driver developers](../gettingstarted/concepts-and-knowledge-for-all-driver-developers.md).

-   **Step 2**: Learn the fundamentals of MB miniport drivers.

    MB miniport drivers are supported in Windows 7 and later versions of Windows and conform to the *NDIS 6.20 Specification*. To understand the miniport driver design decisions you must make, see [Introduction to NDIS 6.20](introduction-to-ndis-6-20.md).

-   **Step 3**: Determine additional Windows driver design decisions.

    For information about how to make additional Windows design decisions, see [Creating Reliable Kernel-Mode Drivers](../kernel/creating-reliable-kernel-mode-drivers.md), [Programming Issues for 64-Bit Drivers](../kernel/porting-your-driver-to-64-bit-windows.md), and [Creating International INF Files](../install/creating-international-inf-files.md).

-   **Step 4**: Learn about the Windows driver build, test, and debug processes and tools.

    Building a driver differs from building a user mode application. For information about Windows driver build, debug, and test processes, driver signing, and [Windows Hardware Certification Kit (HCK)](https://go.microsoft.com/fwlink/p/?LinkId=733613) testing, see [Building, Debugging, and Testing Drivers](/windows-hardware/drivers). For information about building, testing, verifying, and debugging tools, see [Driver Development Tools](../devtest/index.md).

-   **Step 5**: Make design decisions about your MB miniport driver.

    For more information, see [MB Interface Overview](mb-interface-overview.md). You can also learn more about how to develop Mobile Broadband miniport drivers by reviewing the [Mobile Broadband Driver Development](https://go.microsoft.com/fwlink/p/?linkid=144416) whitepaper.

-   **Step 6**: Develop, build, test, and debug your MB miniport driver.

    For information about iterative building, testing, and debugging, see [Overview of Build, Debug, and Test Process](/windows-hardware/drivers). This process will help ensure that you build a miniport driver that works.

-   **Step 7**: Create a driver package for your MB miniport driver.

    For more information, see [Providing a Driver Package](/windows-hardware/drivers).

-   **Step 8**: Sign and distribute your MB miniport driver.

    The final step is to sign (optional) and distribute the miniport driver. If your miniport driver meets the quality standards that are defined for the [Windows Hardware Certification Kit (HCK)](https://go.microsoft.com/fwlink/p/?LinkId=733613), you can distribute it through the Microsoft Windows Update program. For more information about how to distribute a driver, see [Distributing a Driver](/windows-hardware/drivers).

These are the basic steps. Additional steps might be necessary based on the needs of your individual miniport driver.

