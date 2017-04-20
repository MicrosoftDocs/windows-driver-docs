---
title: WIA Driver Error Recovery for Windows Vista
author: windows-driver-content
description: WIA Driver Error Recovery for Windows Vista
ms.assetid: 7347cc02-e00e-418e-9ac4-8bfda7d02857
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WIA Driver Error Recovery for Windows Vista


## <a href="" id="ddk-wia-driver-error-recovery-for-windows-longhorn-si"></a>


There are multiple points in the WIA image acquisition process where software, hardware, or configuration errors can cause unexpected delays, failure messages, or indecipherable hangs. Most of these errors occur at the point where the application requests image data, either for preview or for the full image. This section describes a mechanism that allows applications and users to gracefully handle these errors and delays, and possibly, to recover from them. It does not address ways to improve error recovery while trying to set or get device properties, or when callback routines into a driver never return, or during other non-transfer related situations.

This section includes:

[WIA Error Handling Architecture](wia-error-handling-architecture.md)

[WIA Error Handler Cancellation of Modeless Dialogs](wia-error-handler-cancellation-of-modeless-dialogs.md)

[WIA Error Handler Return Values](wia-error-handler-return-values.md)

[WIA Device Messages](wia-device-messages.md)

[Installing a WIA Error Handling Driver Extension](installing-a-wia-error-handling-driver-extension.md)

[WIA Error Handling Examples](wia-error-handling-example.md)

For information about the Windows Vista error macros, see [WIA Diagnostic Log Macros](wia-diagnostic-log-macros.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA%20Driver%20Error%20Recovery%20for%20Windows%20Vista%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


