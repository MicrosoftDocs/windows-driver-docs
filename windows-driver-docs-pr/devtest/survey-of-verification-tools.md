---
title: Survey of Verification Tools
description: Survey of Verification Tools
ms.assetid: d36e041f-efa5-450f-b4de-c84c4880e44d
keywords:
- dynamic verification tools WDK
- static verification tools WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Survey of Verification Tools


The following verification tools are described in the WDK and recommended for use by driver developers and testers. They are listed in the order in which they are typically used.

### <span id="as_soon_as_the_code_compiles"></span><span id="AS_SOON_AS_THE_CODE_COMPILES"></span>As soon as the code compiles

-   [Code Analysis for Drivers](code-analysis-for-drivers.md) is a static verification tool that runs at compile time. The Windows Driver Kit provides a driver-specific extension to the [Code Analysis tool](http://go.microsoft.com/fwlink/p/?linkid=226836) in Microsoft Visual Studio Ultimate 2012.

    [Code Analysis for Drivers](code-analysis-for-drivers.md) can verify drivers written in C/C++ and managed code. It examines the code in each function of a driver independently, so you can run it as soon as you can build your driver. It runs relatively quickly and uses few resources.

    The basic features of the [Code Analysis tool](http://go.microsoft.com/fwlink/p/?linkid=226836) detect general coding errors, such as not checking return values. The driver-specific features detect more subtle driver coding errors, such as leaving uninitialized fields in a copied IRP and failing to restore a changed IRQL by the end of a routine.

<!-- -->

-   [Static Driver Verifier](static-driver-verifier.md) (SDV) is a static verification tool that runs at compile time and verifies kernel-mode driver code written in C/C++. It is included in the WDK and can be started from Visual Studio Ultimate 2012 or from a Visual Studio Command prompt window using MSBuild.

    Based on a set of interface rules and a model of the operating system, Static Driver Verifier determines whether the driver properly interacts with the Windows operating system kernel. Static Driver Verifier is extremely thorough -- it explores all reachable paths in the driver source code and executes them symbolically. As such, it finds bugs that are not detected by using any other conventional method of driver testing.

### <span id="when_the_driver_runs"></span><span id="WHEN_THE_DRIVER_RUNS"></span>When the driver runs

Use the following dynamic verification tools as soon as the driver is built and is running without obvious errors.

-   [Checked Build of Windows](checked-build-of-windows.md). Although not technically a verification tool, running your driver on the checked build of Windows will help you to detect errors that are not evident in testing with other tools. Running with the checked build in conjunction with a kernel debugger should be a standard part of developing and testing your driver.

-   [Driver Verifier](driver-verifier.md) is a dynamic verification tool written especially for Windows drivers. It includes multiple tests that can be run on several drivers simultaneously. Driver Verifier is so effective at finding serious bugs in drivers that experienced driver developers and testers configure Driver Verifier to run whenever their driver runs in a development or test environment. Driver Verifier is included in Windows 2000 and later versions of Windows. When you enable Driver Verifier for a driver, you must also run multiple tests on the driver. Driver Verifier can detect certain driver bugs that are difficult to detect by using static verification tools alone. Examples of these types of bugs include the following:
    -   **Kernel pool buffer overruns.** When the verified driver allocates pool memory buffers, Driver Verifier guards them with a non-accessible memory page. If the driver tries to use memory past the end of the buffer, the Driver Verifier will issue a bug check.
    -   **Using memory after freeing it.** Special pool memory blocks use their own memory page, and do not share memory pages with other allocations. When the driver is freeing the block of pool memory, the corresponding memory page becomes non-accessible. If the driver attempts to use that memory after freeing it, the driver will crash instantly.
    -   **Using pageable memory while running at elevated IRQL.** When a verified driver raises the IRQL at DISPATCH\_LEVEL or higher, Driver Verifier trims all pageable memory from the system working set, simulating a system under memory pressure. The driver crashes if it tries to use one of these pageable virtual addresses.
    -   **Low Resources Simulation.** To simulate a system under low resources conditions, Driver Verifier can fail various operating system kernel APIs called by drivers.
    -   **Memory leaks.** Driver Verifier tracks memory allocations made by a driver and makes sure the memory is freed before the driver gets unloaded.
    -   **I/O operations that take too much time to complete or to be canceled.** The Driver Verifier can test the driver's logic for responding to STATUS\_PENDING return values from [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336).
    -   **DDI Compliance Checking.** (Available starting with Windows 8) Driver Verifier applies a set of device driver interface (DDI) rules that check for the proper interaction between a driver and the kernel interface of the operating system. These rules correspond to rules that Static Driver Verifier uses in analyzing driver source code. If Driver Verifier finds an error when DDI Compliance Checking is enabled, run [Static Driver Verifier](static-driver-verifier.md) and select the same rule that caused the error. Static Driver Verifier can help you locate the cause of the defect in the driver source code.
-   [Application Verifier](application-verifier.md) is a dynamic verification tool for user-mode applications and drivers written in C/C++. It does not verify managed code. Application Verifier is not included in the WDK, but you can download and install it from the [Microsoft Download Center website](http://go.microsoft.com/fwlink/p/?linkid=11573).

 

 





