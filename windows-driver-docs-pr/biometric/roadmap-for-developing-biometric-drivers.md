---
title: Roadmap for Developing Biometric Drivers
description: Roadmap for Developing Biometric Drivers
ms.assetid: 8ed13c75-86d1-4ac0-9f44-05162521b915
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Roadmap for Developing Biometric Drivers


To create a biometric driver, follow these steps:

-   Step 1: Learn about Windows architecture and drivers.

    You must understand the fundamentals of how drivers work in Windows operating systems. Knowing the fundamentals will help you make appropriate design decisions and let you streamline your development process. For more information about driver fundamentals, see [Understanding Driver and Operating System Basics](https://msdn.microsoft.com/library/windows/hardware/ff554731).

-   Step 2: Learn how Windows supports biometric drivers.

    Windows 7 and later operating system versions include the Windows Biometric Driver Interface (WBDI). WBDI is an IOCTL-based driver interface that is part of the Windows Biometric Framework (WBF). To learn more about WBDI, see [Getting Started with Biometric Drivers](getting-started-with-biometric-drivers.md).

-   Step 3: Review the biometric driver sample in the WDK.

    For Windows 7 and later operating systems, the driver code gallery includes a sample called [WudfBioUsbSample](https://github.com/Microsoft/Windows-driver-samples/tree/master/biometrics/driver). This sample WBDI driver is UMDF-based, and uses the [USB I/O Target](https://msdn.microsoft.com/library/windows/hardware/ff561358).

    For more information about the WudfBioUsbSample sample, see the [sample description](https://github.com/Microsoft/Windows-driver-samples/tree/master/biometrics).

-   Step 4: Select a driver model for your biometric driver.

    Microsoft recommends that WBDI drivers are UMDF-based and use the USB I/O target. For information about UMDF, see [Introduction to UMDF](https://msdn.microsoft.com/library/windows/hardware/ff554928). For information about the USB I/O target, see [Handling a USB I/O Target](https://msdn.microsoft.com/library/windows/hardware/ff561358).

    [WudfBioUsbSample](https://github.com/Microsoft/Windows-driver-samples/tree/master/biometrics/driver) demonstrates how to implement a UMDF-based WBDI driver that uses a USB I/O target.

    If you use UMDF, Microsoft recommends that you develop your biometric driver in C++.

-   Step 5: Learn about the Windows driver build, test, and debug processes and tools.

    Building a driver differs from building a user-mode application. For information see [Building a Driver](https://msdn.microsoft.com/windows-drivers/develop/building_a_driver). For information about how to build a framework-based driver, see [Building and Loading a Framework-based Driver](https://msdn.microsoft.com/library/windows/hardware/ff540730).

-   Step 6: Make design decisions about your biometric driver.

    For information about how to handle IOCTLs, see [Supporting Biometric IOCTL Calling Sequence](supporting-biometric-ioctl-calling-sequence.md). For information about how to use the USB I/O target in a WBDI driver, see [Using WinUSB in a WBDI Driver](using-winusb-in-a-wbdi-driver.md).

-   Step 7: Develop, build, test, and debug your biometric driver.

    For more information about how to manage request queues in a WBDI driver, see [Managing Queues in a WBDI Driver](managing-queues-in-a-wbdi-driver.md).

    For more information about IOCTLs, structures, and error codes related to WBDI, see [Biometric Devices Reference](https://msdn.microsoft.com/library/windows/hardware/ff536410).

    For information about how to test biometric drivers, see [Testing Biometric Drivers](testing-biometric-drivers.md).

    For information about iterative building, testing, and debugging, see [Overview of Build, Debug, and Test Process](https://msdn.microsoft.com/windows-drivers/develop/visual_studio_driver_development_environment). This process helps to ensure that you create a driver that works.

-   Step 8: Create a driver package for your biometric driver.

    For more information, see [Providing a Driver Package](https://msdn.microsoft.com/windows-drivers/develop/creating_a_driver_package).

    For information about how to install biometric drivers, see [Installing a Biometric Driver](installing-a-biometric-driver.md).

-   Step 9: Sign and distribute your biometric driver.

    The final step is to sign and distribute the driver. You must sign your engine adapter on both 32-bit and 64-bit platforms.

    If your driver meets the quality standards that are defined for the Microsoft Hardware Certification Program, you can distribute it through the Microsoft Windows Update program. For more information about how to distribute a driver, see [Distributing a Driver](https://msdn.microsoft.com/windows-drivers/develop/distributing_a_driver_package_win8).

These are the basic steps. Additional steps might be necessary based on the needs of your individual driver.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[biometric\biometric]:%20Roadmap%20for%20Developing%20Biometric%20Drivers%20%20RELEASE:%20%288/24/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




