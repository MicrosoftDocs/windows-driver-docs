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

-   Set the **VerifierOn** registry value to enable the framework's driver verification features. For more information about **VerifierOn** and other registry values that you can use when you are debugging and testing your driver, see [Using KMDF Verifier](using-kmdf-verifier.md) and [Using UMDF Verifier](using-umdf-verifier.md). For information about an application that helps you to use the framework's driver verification features, see [WDF Verifier Control Application](https://msdn.microsoft.com/library/windows/hardware/ff556129).

-   For both UMDF versions 1 and 2, enable [Application Verifier (AppVerif.exe)](http://www.microsoft.com/download/details.aspx?id=20028) on Wudfhost.exe. For example:
    ```cpp
    appverif -enable handles locks heaps memory exceptions TLS -for WudfHost.exe
    ```

    Doing so automatically turns on the framework's built-in verification.
-   Use the driver verification tools that are described in this documentation. For more information about these important tools, see:
    -   [WdfTester: WDF Driver Testing Toolset](https://msdn.microsoft.com/library/windows/hardware/ff556110)
    -   [Tools for Verifying Drivers](https://msdn.microsoft.com/library/windows/hardware/ff552969)
    -   [Tools for Testing Drivers](https://msdn.microsoft.com/library/windows/hardware/ff552966)

To thoroughly test your driver, you must use both the framework's driver verification features and the driver verification tools.

For general information about testing your driver using Microsoft Visual Studio and the Windows Driver Kit (WDK), see [Testing a Driver](https://msdn.microsoft.com/windows-drivers/develop/testing_a_driver).

 

 





