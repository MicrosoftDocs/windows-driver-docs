---
title: Testing a WDF Driver (KMDF or UMDF)
description: This topic describes recommendations for testing a Kernel-Mode Driver Framework (KMDF) or User-Mode Driver Framework (UMDF) version 2 driver.
keywords:
- kernel-mode drivers WDK KMDF , testing
- KMDF WDK , testing drivers
- Kernel-Mode Driver Framework WDK , testing drivers
- framework-based drivers WDK KMDF , testing
- testing drivers WDK , framework-based drivers
- VerifierOn registry value WDK KMDF
ms.date: 04/20/2017
---

# Testing a WDF Driver (KMDF or UMDF)


This topic describes recommendations for testing a Kernel-Mode Driver Framework (KMDF) or User-Mode Driver Framework (UMDF) version 2 driver.

When testing your driver, you should:

-   Set the **VerifierOn** registry value to enable the framework's driver verification features. For more information about **VerifierOn** and other registry values that you can use when you are debugging and testing your driver, see [Using KMDF Verifier](using-kmdf-verifier.md) and [Using UMDF Verifier](using-umdf-verifier.md). For information about an application that helps you to use the framework's driver verification features, see [WDF Verifier Control Application](../devtest/wdf-verifier-control-application.md).

-   For both UMDF versions 1 and 2, enable [Application Verifier (AppVerif.exe)] on Wudfhost.exe. You can download the AppVerif tool as part of [Download Debugging Tools for Windows](../debugger/debugger-download-tools.md).  For example:
    ```cpp
    appverif -enable handles locks heaps memory exceptions TLS -for WudfHost.exe
    ```

    Doing so automatically turns on the framework's built-in verification.
-   Use the driver verification tools that are described in this documentation. For more information about these important tools, see:
    -   [WdfTester: WDF Driver Testing Toolset](../devtest/wdftester--wdf-driver-testing-toolset.md)
    -   [Tools for Verifying Drivers](../devtest/tools-for-verifying-drivers.md)
    -   [Tools for Testing Drivers](../devtest/tools-for-testing-drivers.md)

To thoroughly test your driver, you must use both the framework's driver verification features and the driver verification tools. 
