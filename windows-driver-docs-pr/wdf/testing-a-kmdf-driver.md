---
title: Testing a WDF Driver (KMDF or UMDF)
author: windows-driver-content
description: This topic describes recommendations for testing a Kernel-Mode Driver Framework (KMDF) or User-Mode Driver Framework (UMDF) version 2 driver.
ms.assetid: 05545488-0114-49f5-bf8a-006a868911e8
keywords: ["kernel-mode drivers WDK KMDF , testing", "KMDF WDK , testing drivers", "Kernel-Mode Driver Framework WDK , testing drivers", "framework-based drivers WDK KMDF , testing", "testing drivers WDK , framework-based drivers", "VerifierOn registry value WDK KMDF"]
---

# Testing a WDF Driver (KMDF or UMDF)


This topic describes recommendations for testing a Kernel-Mode Driver Framework (KMDF) or User-Mode Driver Framework (UMDF) version 2 driver.

When testing your driver, you should:

-   Set the **VerifierOn** registry value to enable the framework's driver verification features. For more information about **VerifierOn** and other registry values that you can use when you are debugging and testing your driver, see [Using KMDF Verifier](using-kmdf-verifier.md) and [Using UMDF Verifier](using-umdf-verifier.md). For information about an application that helps you to use the framework's driver verification features, see [WDF Verifier Control Application](https://msdn.microsoft.com/library/windows/hardware/ff556129).

-   For both UMDF versions 1 and 2, enable [Application Verifier (AppVerif.exe)](http://www.microsoft.com/download/details.aspx?id=20028) on Wudfhost.exe. For example:
    ```
    appverif -enable handles locks heaps memory exceptions TLS -for WudfHost.exe
    ```

    Doing so automatically turns on the framework's built-in verification.
-   Use the driver verification tools that are described in this documentation. For more information about these important tools, see:
    -   [WdfTester: WDF Driver Testing Toolset](https://msdn.microsoft.com/library/windows/hardware/ff556110)
    -   [Tools for Verifying Drivers](https://msdn.microsoft.com/library/windows/hardware/ff552969)
    -   [Tools for Testing Drivers](https://msdn.microsoft.com/library/windows/hardware/ff552966)

To thoroughly test your driver, you must use both the framework's driver verification features and the driver verification tools.

For general information about testing your driver using Microsoft Visual Studio and the Windows Driver Kit (WDK), see [Testing a Driver](https://msdn.microsoft.com/windows-drivers/develop/testing_a_driver).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Testing%20a%20WDF%20Driver%20%28KMDF%20or%20UMDF%29%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




