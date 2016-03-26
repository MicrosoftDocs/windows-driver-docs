---
title: How UMDF Reports Errors
description: This topic describes how User-Mode Driver Framework (UMDF) reports errors. It applies to both UMDF versions 1 and 2.
ms.assetid: 44e4e5df-d968-4973-8a36-e93c75320ff6
keywords: ["User-Mode Driver Framework WDK , errors", "UMDF WDK , errors", "user-mode drivers WDK UMDF , errors", "errors WDK UMDF", "Windows Error Reporting WDK UMDF", "WER WDK UMDF", "error reporting WDK UMDF"]
---

# How UMDF Reports Errors


This topic describes how User-Mode Driver Framework (UMDF) reports errors. It applies to both UMDF versions 1 and 2.

When a UMDF driver crashes, the framework creates a Windows Error Reporting (WER) report.

UMDF reports the following types of errors:

-   [UMDF Verifier](using-umdf-verifier.md) failures.

-   Unhandled exceptions in the host process.

-   Unexpected termination of the host process.

-   Failure or time-out of critical operations. For more information about timeouts, see [Host Process Timeouts in UMDF](how-umdf-enforces-time-outs.md).

A UMDF error report can contain the following information. The contents of the report depend on the problem that is detected.

-   A memory dump of the host process

-   A copy of the UMDF trace log

-   Configuration information about the device, which can include the device name, manufacturer, drivers that are installed, and driver binary versions

-   Analysis of the problem, which can include the address of the last driver-to-framework call (or vice versa), problem code, exception information, and so on

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20How%20UMDF%20Reports%20Errors%20%20RELEASE:%20%283/25/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




