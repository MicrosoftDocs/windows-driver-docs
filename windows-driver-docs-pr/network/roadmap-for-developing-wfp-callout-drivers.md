---
title: Roadmap for Developing WFP Callout Drivers
description: Roadmap for Developing WFP Callout Drivers
ms.date: 04/20/2017
---

# Roadmap for Developing WFP Callout Drivers


To create a Windows Filtering Platform (WFP) callout driver, follow these steps:

-   Step 1: Learn about WFP architecture.

    For information about WFP, see [Windows Filtering Platform](/windows/desktop/FWP/windows-filtering-platform-start-page). You may find that you can develop a WFP user-mode application and avoid writing a WFP callout driver.

-   Step 2: Learn about Windows architecture and drivers.

    You must understand the fundamentals of how drivers work in Windows operating systems. Knowing the fundamentals will help you make appropriate design decisions and let you streamline your development process. For more information about driver fundamentals, see [Concepts for all driver developers](../gettingstarted/concepts-and-knowledge-for-all-driver-developers.md).

-   Step 3: Determine the Windows driver model for your WFP callout driver.

    WFP callout drivers can be written either by using the Windows Driver Model (WDM) or the Kernel Mode Driver Framework (KMDF). For more information about how to select a driver model, see [Choosing a Driver Model](../gettingstarted/choosing-a-driver-model.md). For more information about WDM, see [Introduction to Windows Drivers](../kernel/overview-of-windows-components.md) and [Writing WDM Drivers](../kernel/writing-wdm-drivers.md). For more information about KMDF, see [WDF Driver Development Guide](../wdf/index.md).

-   Step 4: Determine additional Windows driver design decisions.

    For information about how to make additional Windows design decisions, see [Creating Reliable Kernel-Mode Drivers](../kernel/creating-reliable-kernel-mode-drivers.md), [Programming Issues for 64-Bit Drivers](../kernel/porting-your-driver-to-64-bit-windows.md), and [Creating International INF Files](../install/creating-international-inf-files.md).

-   Step 5: Learn about the Windows driver build, test, and debug processes and tools.

    Building a driver differs from building a user-mode application. For information about Windows driver build, debug, and test processes, driver signing, and [Windows Hardware Certification Kit (HCK)](https://go.microsoft.com/fwlink/p/?LinkId=733613) testing, see [Building, Debugging, and Testing Drivers](/windows-hardware/drivers). For information about building, testing, verifying, and debugging tools, see [Driver Development Tools](../devtest/index.md).

-   Step 6: Review the [Windows Filtering Platform (WFP) driver samples](https://go.microsoft.com/fwlink/p/?LinkId=618680) in the [Windows driver samples](https://go.microsoft.com/fwlink/p/?LinkId=616507) repository on GitHub.

-   Step 7: Make design decisions about your WFP callout driver.

    For information about how to design WFP callout drivers, see [Callout Driver Programming Considerations](callout-driver-programming-considerations.md).

-   Step 8: Develop, build, test, and debug your WFP callout driver.

    For information about WFP callout driver specifics, see [Callout Driver Operations](callout-driver-operations.md) and [Callout Driver Installation](callout-driver-installation.md). For information about functions, structures, enumerations, or constants that are specific to WFP, see [Windows Filtering Platform Callout Drivers Reference](/windows-hardware/drivers/ddi/_netvista/). For information about iterative building, testing, and debugging, see [Overview of Build, Debug, and Test Process](/windows-hardware/drivers). This process will help ensure that you build a driver that works.

-   Step 9: Create a driver package for your WFP callout driver.

    For more information, see [Providing a Driver Package](/windows-hardware/drivers) and [Callout Driver Installation](callout-driver-installation.md).

-   Step 10: Sign and distribute your WFP callout driver.

    The final step is to sign (optional) and distribute the driver. If your driver meets the quality standards that are defined for the [Windows Hardware Certification Kit (HCK)](https://go.microsoft.com/fwlink/p/?LinkId=733613), you can distribute it through the Microsoft Windows Update program. For more information about how to distribute a driver, see [Distributing a Driver](/windows-hardware/drivers).

These are the basic steps. Additional steps might be necessary based on the needs of your individual driver.

