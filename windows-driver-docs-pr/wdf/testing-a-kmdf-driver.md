---
title: "Test a WDF Driver: KMDF and UMDF Guide"
description: Learn how to test KMDF and UMDF drivers using WDF verification tools, registry settings, and Application Verifier. Follow best practices to ensure driver quality.
keywords:
- kernel-mode drivers WDK KMDF , testing
- KMDF WDK , testing drivers
- Kernel-Mode Driver Framework WDK , testing drivers
- framework-based drivers WDK KMDF , testing
- testing drivers WDK , framework-based drivers
- VerifierOn registry value WDK KMDF
ms.date: 12/15/2025
ms.topic: concept-article
---

# Testing a WDF Driver (KMDF or UMDF)

This article describes recommendations for testing a Kernel-Mode Driver Framework (KMDF) or User-Mode Driver Framework (UMDF) version 2 driver.

When testing your driver, use the following recommendations:

- Set the **VerifierOn** registry value to enable the framework's driver verification features. For more information about **VerifierOn** and other registry values that you can use when you're debugging and testing your driver, see [Using KMDF Verifier](using-kmdf-verifier.md) and [Using UMDF Verifier](using-umdf-verifier.md). For information about an application that helps you use the framework's driver verification features, see [WDF Verifier Control Application](/windows-hardware/drivers/devtest/wdf-verifier-control-application).
- For both UMDF versions 1 and 2, enable [Application Verifier (AppVerif.exe)] on Wudfhost.exe. You can download the AppVerif tool as part of [Download Debugging Tools for Windows](/windows-hardware/drivers/debugger/debugger-download-tools).  For example:

    ```cpp
    appverif -enable handles locks heaps memory exceptions TLS -for WudfHost.exe
    ```

    Doing this step automatically turns on the framework's built-in verification.

- Use the driver verification tools that are described in this documentation. For more information about these important tools, see:
  - [WdfTester: WDF Driver Testing Toolset](/windows-hardware/drivers/devtest/wdftester--wdf-driver-testing-toolset)
  - [Tools for Verifying Drivers](/windows-hardware/drivers/devtest/static-and-dynamic-verification-tools)
  - [Tools for Testing Drivers](/windows-hardware/drivers/devtest/tools-for-testing-drivers)

To thoroughly test your driver, use both the framework's driver verification features and the driver verification tools.
