---
title: Testing a WDF Driver (KMDF or UMDF)
description: This topic describes recommendations for testing a Kernel-Mode Driver Framework (KMDF) or User-Mode Driver Framework (UMDF) version 2 driver.
ms.assetid: 05545488-0114-49f5-bf8a-006a868911e8
keywords:
- kernel-mode drivers WDK KMDF , testing
- KMDF WDK , testing drivers
- Kernel-Mode Driver Framework WDK , testing drivers
- framework-based drivers WDK KMDF , testing
- testing drivers WDK , framework-based drivers
- VerifierOn registry value WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Testing a WDF Driver (KMDF or UMDF)


This topic describes recommendations for testing a Kernel-Mode Driver Framework (KMDF) or User-Mode Driver Framework (UMDF) version 2 driver.

When testing your driver, you should:

-   Set the **VerifierOn** registry value to enable the framework's driver verification features. For more information about **VerifierOn** and other registry values that you can use when you are debugging and testing your driver, see [Using KMDF Verifier](using-kmdf-verifier.md) and [Using UMDF Verifier](using-umdf-verifier.md). For information about an application that helps you to use the framework's driver verification features, see [WDF Verifier Control Application](https://docs.microsoft.com/windows-hardware/drivers/devtest/wdf-verifier-control-application).

-   For both UMDF versions 1 and 2, enable [Application Verifier (AppVerif.exe)] on Wudfhost.exe. You can download the AppVerif tool as part of [Download Debugging Tools for Windows](https://docs.microsoft.com/windows-hardware/drivers/debugger/debugger-download-tools).  For example:
    ```cpp
    appverif -enable handles locks heaps memory exceptions TLS -for WudfHost.exe
    ```

    Doing so automatically turns on the framework's built-in verification.
-   Use the driver verification tools that are described in this documentation. For more information about these important tools, see:
    -   [WdfTester: WDF Driver Testing Toolset](https://docs.microsoft.com/windows-hardware/drivers/devtest/wdftester--wdf-driver-testing-toolset)
    -   [Tools for Verifying Drivers](https://docs.microsoft.com/windows-hardware/drivers/devtest/tools-for-verifying-drivers)
    -   [Tools for Testing Drivers](https://docs.microsoft.com/windows-hardware/drivers/devtest/tools-for-testing-drivers)

To thoroughly test your driver, you must use both the framework's driver verification features and the driver verification tools.

For general information about testing your driver using Microsoft Visual Studio and the Windows Driver Kit (WDK), see [Testing a Driver](https://docs.microsoft.com/windows-hardware/drivers/develop/testing-a-driver) and [Testing a WDF Driver](https://docs.microsoft.com/windows-hardware/drivers/wdf/testing-a-kmdf-driver).

 

 





