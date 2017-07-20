---
ms.assetid: ee46801a-4fa5-465a-aa81-5e76eb83d315
title: Building for OneCore
description: You can build a single binary that targets pre-Windows 10 and OneCore SKUs.
ms.author: windowsdriverdev
ms.date: 07/19/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Building for OneCore

If you are building user-mode code for Windows 7 and later, including [OneCore](https://docs.microsoft.com/windows-hardware/get-started/what-s-new-in-windows) SKUs, you can generate a single binary that works on all of these operating systems.
To do so, link to `onecore_downlevel.lib` or `onecoreuap_downlevel.lib`.
When you use this downlevel option, a subset of APIs compile fine but return immediately on non-Desktop OneCore SKUs.  For example, the [**MessageBox**](https://msdn.microsoft.com/library/windows/desktop/ms645505) function returns ERROR_CALL_NOT_IMPLEMENTED on non-Desktop OneCore SKUs.  The documentation for these APIs describes this behavior, including applicable error codes, in the Requirements section of the page.
<!--Link to list of apis with stub functionality, include example screenshot-->

If you are building user-mode code for only Windows 10 and later, including OneCore SKUs, link instead to `onecoreuap.lib` or `onecore.lib`.  You will get a slight load time performance boost.

The following table describes when to link to each option.

|Library|Scenario|
|-|-|
|onecore.lib|For building a binary to run on the latest OS version, targeting all SKUs, but with no UWP support|
|onecoreuap.lib|For building a binary to run on the latest OS version, targeting SKUs with UWP support (Desktop, IoT, HoloLens, but not Nano Server)|
|onecore_downlevel.lib|For building a binary to run on Windows 7 and later, targeting all SKUs, but with no UWP support|
|onecoreuap_downlevel.lib|For building a binary to run on Windows 7 and later, targeting those SKUs with UWP support (Desktop, IoT, HoloLens, but not Nano Server)|

To change specified libraries in a Visual Studio project, choose project properties and navigate to **Linker->Input**.  The **Additional Dependencies** should contain:

    ```
    %AdditionalDependencies);$(SDK_LIB_PATH)\<filename>.lib
    ```

## Recommended actions

Use the [ApiValidator](validating-universal-drivers.md) tool in the WDK to verify that the built binary will load and run on non-Desktop OneCore SKUs.  This tool runs automatically when you build a driver in Visual Studio.

Use runtime testing to verify that your user-mode code runs as you expect on non-Desktop OneCore SKUs.  Note that stubbed APIs may generate different error codes.

The first two choices are recommended due to improved performance, but note that the resulting binaries will not run on operating systems earlier than Windows 10.

<!--API BOILERPLATE: Compiles using onecore_downlevel.lib, but always returns ERROR_CALL_NOT_IMPLEMENTED on non-Desktop OneCore SKUs.-->
