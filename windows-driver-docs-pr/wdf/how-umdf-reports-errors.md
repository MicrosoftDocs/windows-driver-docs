---
title: How UMDF Reports Errors
description: This topic describes how User-Mode Driver Framework (UMDF) reports errors. It applies to both UMDF versions 1 and 2.
ms.assetid: 44e4e5df-d968-4973-8a36-e93c75320ff6
keywords:
- User-Mode Driver Framework WDK , errors
- UMDF WDK , errors
- user-mode drivers WDK UMDF , errors
- errors WDK UMDF
- Windows Error Reporting WDK UMDF
- WER WDK UMDF
- error reporting WDK UMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





