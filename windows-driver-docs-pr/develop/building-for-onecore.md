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

When you use Visual Studio to build user-mode code for Windows 10, you can customize linker options to target specific versions of Windows.  To build a binary that works on the desired platforms, consider the following factors:

* Should the built binary run on only the most recent version of Windows?  Or should it run on *downlevel* versions, meaning Windows 7 and later?  

* Does your project have any UWP dependencies?

By default, when you create a new UMDF v2 driver project, Visual Studio links to `OneCoreUAP.lib`.  This is the correct choice if your binary only needs to run on the most recent version of Windows, and it also permits addition of UWP functionality.

If your answers to the questions above are different, however, you can change the default to link to one of the following libraries:

|Library|Scenario|
|-|-|
|onecore.lib|For building a binary to run on the latest OS version, targeting all SKUs, but with no UWP support|
|onecoreuap.lib|For building a binary to run on the latest OS version, targeting SKUs with UWP support (Desktop, IoT, HoloLens, but not Nano Server)|
|onecore_downlevel.lib|For building a binary to run on Windows 7 and later, targeting all SKUs, but with no UWP support|
|onecoreuap_downlevel.lib|For building a binary to run on Windows 7 and later, targeting those SKUs with UWP support (Desktop, IoT, HoloLens, but not Nano Server)|

When you use a downlevel option, a subset of APIs compile fine but return immediately on non-Desktop OneCore SKUs (for example Mobile or IoT).  For example, the [**MessageBox**](https://msdn.microsoft.com/library/windows/desktop/ms645505) function returns ERROR_CALL_NOT_IMPLEMENTED on non-Desktop OneCore SKUs.  The documentation for these APIs describes this behavior, including applicable error codes, in the Requirements section of the page.
<!--Link to list of apis with stub functionality, include example screenshot-->

If you link to `onecoreuap.lib` or `onecore.lib`, you will get a slight load time performance boost over the downlevel options.

To change specified libraries in a Visual Studio project, choose project properties and navigate to **Linker->Input->Additional Dependencies**.

## Recommended actions

Use the [ApiValidator](validating-universal-drivers.md) tool in the WDK to verify that the built binary will load and run on non-Desktop OneCore SKUs.  This tool runs automatically when you build a driver in Visual Studio.

Use runtime testing to verify that your user-mode code runs as you expect on non-Desktop OneCore SKUs.  Note that stubbed APIs may generate different error codes.

Related
---
[OneCore](https://docs.microsoft.com/windows-hardware/get-started/what-s-new-in-windows)

<!--API BOILERPLATE: Compiles using onecore_downlevel.lib, but always returns ERROR_CALL_NOT_IMPLEMENTED on non-Desktop OneCore SKUs.-->
