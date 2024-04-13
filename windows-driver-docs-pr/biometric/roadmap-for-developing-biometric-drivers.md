---
title: Roadmap for Developing Biometric Drivers
description: Roadmap for Developing Biometric Drivers
ms.date: 03/03/2023
---

# Roadmap for Developing Biometric Drivers

To create a biometric driver, follow these steps:

- Step 1: Learn about Windows architecture and drivers.

    You must understand the fundamentals of how drivers work in Windows operating systems. Knowing the fundamentals will help you make appropriate design decisions and let you streamline your development process. For more information about driver fundamentals, see [Understanding Driver and Operating System Basics](../gettingstarted/concepts-and-knowledge-for-all-driver-developers.md).

- Step 2: Learn how Windows supports biometric drivers.

    Windows 7 and later operating system versions include the Windows Biometric Driver Interface (WBDI). WBDI is an IOCTL-based driver interface that is part of the Windows Biometric Framework (WBF). To learn more about WBDI, see [Getting Started with Biometric Drivers](getting-started-with-biometric-drivers.md).

- Step 3: Review the biometric driver sample in the WDK.

    For Windows 7 and later operating systems, the driver code gallery includes a sample called [WudfBioUsbSample](https://github.com/Microsoft/Windows-driver-samples/tree/main/biometrics/driver). This sample WBDI driver is UMDF-based, and uses the [USB I/O Target](../wdf/usb-i-o-targets-in-umdf.md).

    For more information about the WudfBioUsbSample sample, see the [sample description](https://github.com/Microsoft/Windows-driver-samples/tree/main/biometrics).

- Step 4: Select a driver model for your biometric driver.

    Microsoft recommends that WBDI drivers are UMDF-based and use the USB I/O target. For information about UMDF, see [Introduction to UMDF](/previous-versions/ff554928(v=vs.85)). For information about the USB I/O target, see [Handling a USB I/O Target](../wdf/usb-i-o-targets-in-umdf.md).

    [WudfBioUsbSample](https://github.com/Microsoft/Windows-driver-samples/tree/main/biometrics/driver) demonstrates how to implement a UMDF-based WBDI driver that uses a USB I/O target.

    If you use UMDF, Microsoft recommends that you develop your biometric driver in C++.

- Step 5: Learn about the Windows driver build, test, and debug processes and tools.

    Building a driver differs from building a user-mode application. For information see [Building a Driver](../develop/building-a-driver.md). For information about how to build a framework-based driver, see [Building and Loading a Framework-based Driver](../wdf/building-and-loading-a-kmdf-driver.md).

- Step 6: Make design decisions about your biometric driver.

    For information about how to handle IOCTLs, see [Supporting Biometric IOCTL Calling Sequence](supporting-biometric-ioctl-calling-sequence.md). For information about how to use the USB I/O target in a WBDI driver, see [Using WinUSB in a WBDI Driver](using-winusb-in-a-wbdi-driver.md).

- Step 7: Develop, build, test, and debug your biometric driver.

    For more information about how to manage request queues in a WBDI driver, see [Managing Queues in a WBDI Driver](managing-queues-in-a-wbdi-driver.md).

    For more information about IOCTLs, structures, and error codes related to WBDI, see [Biometric Devices Reference](/windows-hardware/drivers/ddi/_biometric).

    For information about how to test biometric drivers, see [Testing Biometric Drivers](testing-biometric-drivers.md).

    For information about iterative building, testing, and debugging, see [Developing, Testing, and Deploying Drivers](../develop/index.md). This process helps to ensure that you create a driver that works.

- Step 8: Create a driver package for your biometric driver.

    For more information, see [Driver Packages](../install/driver-packages.md).

    For information about how to install biometric drivers, see [Installing a Biometric Driver](installing-a-biometric-driver.md).

- Step 9: Sign and distribute your biometric driver.

    The final step is to sign and distribute the driver. You must sign your engine adapter on both 32-bit and 64-bit platforms.

    If your driver meets the quality standards that are defined for the Microsoft Hardware Certification Program, you can distribute it through the Microsoft Windows Update program. For more information about how to distribute a driver, see [Manage driver distribution with shipping labels](../dashboard/manage-driver-distribution-by-submission.md).

These are the basic steps. Additional steps might be necessary based on the needs of your individual driver.
