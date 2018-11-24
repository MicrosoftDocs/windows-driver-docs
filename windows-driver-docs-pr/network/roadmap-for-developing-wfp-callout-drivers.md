---
title: Roadmap for Developing WFP Callout Drivers
description: Roadmap for Developing WFP Callout Drivers
ms.assetid: 98c857d9-e4a6-4a7f-8427-642763864f3e
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Roadmap for Developing WFP Callout Drivers


To create a Windows Filtering Platform (WFP) callout driver, follow these steps:

-   Step 1: Learn about WFP architecture.

    For information about WFP, see [Windows Filtering Platform](https://msdn.microsoft.com/library/windows/desktop/aa366510). You may find that you can develop a WFP user-mode application and avoid writing a WFP callout driver.

-   Step 2: Learn about Windows architecture and drivers.

    You must understand the fundamentals of how drivers work in Windows operating systems. Knowing the fundamentals will help you make appropriate design decisions and let you streamline your development process. For more information about driver fundamentals, see [Concepts for all driver developers](https://msdn.microsoft.com/library/windows/hardware/ff554731).

-   Step 3: Determine the Windows driver model for your WFP callout driver.

    WFP callout drivers can be written either by using the Windows Driver Model (WDM) or the Kernel Mode Driver Framework (KMDF). For more information about how to select a driver model, see [Choosing a Driver Model](https://msdn.microsoft.com/library/windows/hardware/ff554652). For more information about WDM, see [Introduction to Windows Drivers](https://msdn.microsoft.com/library/windows/hardware/ff548173) and [Writing WDM Drivers](https://msdn.microsoft.com/library/windows/hardware/ff566412). For more information about KMDF, see [WDF Driver Development Guide](https://msdn.microsoft.com/library/windows/hardware/dn265580).

-   Step 4: Determine additional Windows driver design decisions.

    For information about how to make additional Windows design decisions, see [Creating Reliable Kernel-Mode Drivers](https://msdn.microsoft.com/library/windows/hardware/ff542904), [Programming Issues for 64-Bit Drivers](https://msdn.microsoft.com/library/windows/hardware/ff559923), and [Creating International INF Files](https://msdn.microsoft.com/library/windows/hardware/ff540208).

-   Step 5: Learn about the Windows driver build, test, and debug processes and tools.

    Building a driver differs from building a user-mode application. For information about Windows driver build, debug, and test processes, driver signing, and [Windows Hardware Certification Kit (HCK)](https://go.microsoft.com/fwlink/p/?LinkId=733613) testing, see [Building, Debugging, and Testing Drivers](https://msdn.microsoft.com/windows-drivers/develop/visual_studio_driver_development_environment). For information about building, testing, verifying, and debugging tools, see [Driver Development Tools](https://msdn.microsoft.com/library/windows/hardware/ff545440).

-   Step 6: Review the [Windows Filtering Platform (WFP) driver samples](http://go.microsoft.com/fwlink/p/?LinkId=618680) in the [Windows driver samples](http://go.microsoft.com/fwlink/p/?LinkId=616507) repository on GitHub.

-   Step 7: Make design decisions about your WFP callout driver.

    For information about how to design WFP callout drivers, see [Callout Driver Programming Considerations](callout-driver-programming-considerations.md).

-   Step 8: Develop, build, test, and debug your WFP callout driver.

    For information about WFP callout driver specifics, see [Callout Driver Operations](callout-driver-operations.md) and [Callout Driver Installation](callout-driver-installation.md). For information about functions, structures, enumerations, or constants that are specific to WFP, see [Windows Filtering Platform Callout Drivers Reference](https://msdn.microsoft.com/library/windows/hardware/ff571067). For information about iterative building, testing, and debugging, see [Overview of Build, Debug, and Test Process](https://msdn.microsoft.com/windows-drivers/develop/visual_studio_driver_development_environment). This process will help ensure that you build a driver that works.

-   Step 9: Create a driver package for your WFP callout driver.

    For more information, see [Providing a Driver Package](https://msdn.microsoft.com/windows-drivers/develop/creating_a_driver_package) and [Callout Driver Installation](callout-driver-installation.md).

-   Step 10: Sign and distribute your WFP callout driver.

    The final step is to sign (optional) and distribute the driver. If your driver meets the quality standards that are defined for the [Windows Hardware Certification Kit (HCK)](https://go.microsoft.com/fwlink/p/?LinkId=733613), you can distribute it through the Microsoft Windows Update program. For more information about how to distribute a driver, see [Distributing a Driver](https://msdn.microsoft.com/windows-drivers/develop/distributing_a_driver_package_win8).

These are the basic steps. Additional steps might be necessary based on the needs of your individual driver.

 

 





