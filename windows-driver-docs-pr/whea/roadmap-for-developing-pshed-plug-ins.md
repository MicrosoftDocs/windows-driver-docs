---
title: Roadmap for Developing PSHED Plug-Ins
description: Roadmap for Developing PSHED Plug-Ins
ms.assetid: 3e1eb744-e480-4478-9705-94da8029c382
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Roadmap for Developing PSHED Plug-Ins


![figure of a compass, a map, and a finger pointing at the map](images/map-hand-sml.png)

The platform-specific hardware error driver (PSHED) is a component of Windows Hardware Error Architecture (WHEA) that is used to collect platform-specific error information. The PSHED provides an abstraction layer above the hardware error reporting capabilities of the underlying platform, By providing this layer, the PSHED hides the details of a platform's error handling capabilities from the operating system, and exposes a consistent error handling interface to the Windows operating system.

On platforms that involve a system firmware interface to hardware error handling resources, the PSHED manages the interface with the firmware. It does this by using a PSHED plug-in that is implemented by platform vendors.

A PSHED plug-in is a driver that is based on the Windows driver model (WDM), and provides a software interface to the error reporting and recovery capabilities of the hardware platform.

A PSHED plug-in can also interface with the platform firmware by using the private interfaces that are defined by the platform vendor. This allows the platform vendor to continue using existing firmware for hardware error handling.

To create a PSHED plug-in driver for Windows Vista and later versions of Windows, follow these steps:

-   Step 1: Learn about Windows architecture and drivers.

    You must first understand the fundamentals of how drivers work in Windows operating systems. Knowing the fundamentals will help you make appropriate design decisions and let you streamline your development process.

    For more information about driver fundamentals, see [Understanding Driver and Operating System Basics](https://msdn.microsoft.com/library/windows/hardware/ff554731).

-   Step 2: Learn the fundamentals of the Windows Hardware Error Architecture (WHEA).

    WHEA, which was introduced with Windows Vista, extends the hardware error reporting functionality of previous versions of Windows, and brings these mechanisms together as components of a coherent hardware error infrastructure. WHEA uses the additional hardware error information that is available in today's hardware devices and integrates much more closely with the system firmware.

    You must understand the fundamentals of WHEA in Windows Vista and later versions of Windows. This will help you understand the functional components of WHEA, which will also help you make appropriate design decisions.

    For more information about WHEA, see [Introduction to the Windows Hardware Error Architecture](introduction-to-the-windows-hardware-error-architecture.md) and [Windows Hardware Error Architecture Overview](windows-hardware-error-architecture-overview.md).

-   Step 3: Learn about the Windows driver build, test, and debug processes and tools.

    Building a driver is not the same as building a user-mode application.

    For information about Windows driver build, debug, and test processes, driver signing, and Windows Logo testing, see [Building, Debugging, and Testing Drivers](https://msdn.microsoft.com/windows-drivers/develop/visual_studio_driver_development_environment).

    For information about building, testing, verifying, and debugging tools, see [Driver Development Tools](https://msdn.microsoft.com/library/windows/hardware/ff545440).

-   Step 4: Make design decisions about your PSHED plug-in.

    Before you start the design of your PSHED plug-in, you must first understand the following:

    -   The functional requirements and operations of PSHED plug-ins for Windows Vista and later versions of Windows.

        For more information, see [Platform-Specific Hardware Error Driver Plug-Ins](platform-specific-hardware-error-driver-plug-ins2.md).

    -   The changes to WHEA that have been made since Windows Vista.

        For more information about these changes, see [New Information for Windows Hardware Error Architecture](new-information-for-windows-hardware-error-architecture.md).

-   Step 5: Develop, build, test and debug your PSHED plug-in.

    The information in the following topics will help you build a PSHED plug-in that works correctly:

    -   For guidelines on developing a PSHED plug-in, see [PSHED Plug-In Guidelines](pshed-plug-in-guidelines.md).
    -   For information about how to build a PSHED plug-in, see [Building a PSHED Plug-In](building-a-pshed-plug-in.md).
    -   For information about WHEA debugger extensions that can be used to debug a PSHED plug-in, see [Windows Hardware Error Architecture Debugger Extensions](windows-hardware-error-architecture-debugger-extensions.md).
    -   For information about iterative building, testing, and debugging, see [Overview of Build, Debug, and Test Process](https://msdn.microsoft.com/windows-drivers/develop/visual_studio_driver_development_environment).
-   Step 6: Create a driver package for your PSHED Plug-In.

    A PSHED plug-in is a WDM driver. As with other WDM drivers, the PSHED plug-in is installed by using a [driver package](https://msdn.microsoft.com/library/windows/hardware/ff544840).

    For more information about driver packages, see [Providing a Driver Package](https://msdn.microsoft.com/windows-drivers/develop/creating_a_driver_package).

    For more information about how to install a driver package for a PSHED plug-in, see [PSHED Plug-In Installation](pshed-plug-in-installation.md).

-   Step 7: Sign and distribute your PSHED plug-in.

    The final step is to digitally sign and distribute your PSHED plug-in. PSHED plug-ins do not fit into any of the existing Windows Hardware Quality Labs (WHQL) test programs. Therefore, PSHED plug-ins must be digitally signed by using an Authenticode Signature.

    For more information about signing and distributing your PSHED plug-in, see [Qualifying and Distributing PSHED Plug-Ins](qualifying-and-distributing-pshed-plug-ins.md).

These are the basic steps. Additional steps might be necessary based on the needs of your individual PSHED plug-in.

 

 




