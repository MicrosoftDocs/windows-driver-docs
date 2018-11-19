---
title: WIA Driver Error Recovery for Windows Vista
description: WIA Driver Error Recovery for Windows Vista
ms.assetid: 7347cc02-e00e-418e-9ac4-8bfda7d02857
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WIA Driver Error Recovery for Windows Vista





There are multiple points in the WIA image acquisition process where software, hardware, or configuration errors can cause unexpected delays, failure messages, or indecipherable hangs. Most of these errors occur at the point where the application requests image data, either for preview or for the full image. This section describes a mechanism that allows applications and users to gracefully handle these errors and delays, and possibly, to recover from them. It does not address ways to improve error recovery while trying to set or get device properties, or when callback routines into a driver never return, or during other non-transfer related situations.

This section includes:

[WIA Error Handling Architecture](wia-error-handling-architecture.md)

[WIA Error Handler Cancellation of Modeless Dialogs](wia-error-handler-cancellation-of-modeless-dialogs.md)

[WIA Error Handler Return Values](wia-error-handler-return-values.md)

[WIA Device Messages](wia-device-messages.md)

[Installing a WIA Error Handling Driver Extension](installing-a-wia-error-handling-driver-extension.md)

[WIA Error Handling Examples](wia-error-handling-example.md)

For information about the Windows Vista error macros, see [WIA Diagnostic Log Macros](wia-diagnostic-log-macros.md).

 

 




