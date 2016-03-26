---
title: Revise Canceled Request Logic
description: Revise Canceled Request Logic
ms.assetid: 8246826A-BDBD-4A9B-9FFC-B813033E0FDC
---

# Revise Canceled Request Logic


When an I/O request is canceled, a WDM driver must manage several difficult race conditions. A request might be canceled while it is in a queue or while the driver is processing it. In each case the driver must use a combination of locks to ensure that it cancels and completes the request only once.

The WDF queuing mechanism greatly simplifies cancellation. If a request is canceled while it is on a queue, the framework handles cancellation without notifying the driver. The driver can request notification by registering an [*EvtIoCanceledOnQueue*](https://msdn.microsoft.com/library/windows/hardware/ff541756) callback function. After the framework has delivered a request to the driver, the request is not cancelable by default. A driver can call [**WdfRequestIsCanceled**](https://msdn.microsoft.com/library/windows/hardware/ff549976) at any time to find out whether the request has been canceled.

For more information, see [Canceling I/O Requests](canceling-i-o-requests.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Revise%20Canceled%20Request%20Logic%20%20RELEASE:%20%283/25/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




