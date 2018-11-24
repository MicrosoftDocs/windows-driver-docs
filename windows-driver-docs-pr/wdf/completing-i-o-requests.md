---
title: Completing I/O Requests
description: Completing I/O Requests
ms.assetid: ec5aef7a-110e-430c-902d-669ccc7095ac
keywords:
- I/O requests WDK KMDF , completing
- completing I/O requests WDK KMDF
- request processing WDK KMDF , completing requests
- status information WDK KMDF , completing I/O requests
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Completing I/O Requests





Every framework-based driver must eventually complete every I/O request that it receives from the framework. Drivers complete requests by calling the request object's [**WdfRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff549945), [**WdfRequestCompleteWithInformation**](https://msdn.microsoft.com/library/windows/hardware/ff549948), or [**WdfRequestCompleteWithPriorityBoost**](https://msdn.microsoft.com/library/windows/hardware/ff549949) method.

### When to Complete a Request

A driver must complete a request when it determines that one of the following cases is true:

-   The requested I/O operation has finished successfully.

-   The requested I/O operation was started but failed before it finished.

-   The requested I/O operation is not supported, or was not valid at the time it was received, and could not be started.

-   The requested I/O operation was canceled.

If the driver services the I/O request by creating I/O activity on the device, the driver typically calls [**WdfRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff549945) from its [*EvtInterruptDpc*](https://msdn.microsoft.com/library/windows/hardware/ff541721) or [*EvtDpcFunc*](https://msdn.microsoft.com/library/windows/hardware/ff541683) callback function.

If the driver receives an unsupported or otherwise invalid request, it typically calls [**WdfRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff549945) from the [request handler](request-handlers.md) that received the request.

If the I/O operation was [canceled](canceling-i-o-requests.md), the driver typically calls [**WdfRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff549945) from its [*EvtRequestCancel*](https://msdn.microsoft.com/library/windows/hardware/ff541817) callback function.

If the driver [forwards](forwarding-i-o-requests.md) the I/O request to an [I/O target](using-i-o-targets.md), the driver completes the request after the I/O target completes the request, as follows:

-   If your driver forwards the I/O request [synchronously](sending-i-o-requests-synchronously.md) to the I/O target, the driver's call to the I/O target returns only after a lower-level driver has completed the request (unless an error occurs). After the I/O target returns, your driver must call [**WdfRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff549945).

-   If your driver forwards the I/O request [asynchronously](sending-i-o-requests-asynchronously.md), you will want your driver to be notified when a lower-level driver completes the request. If your driver registers a [*CompletionRoutine*](https://msdn.microsoft.com/library/windows/hardware/ff540745) callback function, the framework calls this callback function after the I/O target completes the request. The *CompletionRoutine* callback function typically calls [**WdfRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff549945).

To register a [*CompletionRoutine*](https://msdn.microsoft.com/library/windows/hardware/ff540745) callback function, the driver must call [**WdfRequestSetCompletionRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff550030) before it forwards the I/O request to an I/O target.

If your driver does not need to be notified when an I/O target completes an asynchronously forwarded I/O request, the driver does not have to register a [*CompletionRoutine*](https://msdn.microsoft.com/library/windows/hardware/ff540745) callback function. Instead, the driver can set the [**WDF\_REQUEST\_SEND\_OPTION\_SEND\_AND\_FORGET**](https://msdn.microsoft.com/library/windows/hardware/ff552493) flag when calling [**WdfRequestSend**](https://msdn.microsoft.com/library/windows/hardware/ff550027). In this case the driver does not call [**WdfRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff549945).

A driver does not complete an I/O request that it has created by calling [**WdfRequestCreate**](https://msdn.microsoft.com/library/windows/hardware/ff549951) or [**WdfRequestCreateFromIrp**](https://msdn.microsoft.com/library/windows/hardware/ff549953). Instead, the driver must call [**WdfObjectDelete**](https://msdn.microsoft.com/library/windows/hardware/ff548734) to delete the request object, typically after an I/O target has completed the request.

For example, a driver might receive a read or write request for an amount of data that is larger than the driver's I/O targets can handle at one time. The driver must divide the data into several smaller requests and send these smaller requests to one or more I/O targets. Techniques for handling this situation include:

-   Calling [**WdfRequestCreate**](https://msdn.microsoft.com/library/windows/hardware/ff549951) to create a single additional request object that represents a smaller request.

    The driver can send this request synchronously to an I/O target. The smaller request's [*CompletionRoutine*](https://msdn.microsoft.com/library/windows/hardware/ff540745) callback function can call [**WdfRequestReuse**](https://msdn.microsoft.com/library/windows/hardware/ff550026) so that the driver can reuse the request and send it to the I/O target again. After the I/O target completes the last of the smaller requests, the *CompletionRoutine* callback function can call [**WdfObjectDelete**](https://msdn.microsoft.com/library/windows/hardware/ff548734) to delete the driver-created request object and the driver can call [**WdfRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff549945) to complete the original request.

-   Calling [**WdfRequestCreate**](https://msdn.microsoft.com/library/windows/hardware/ff549951) to create several additional request objects that represent the smaller requests.

    The driver's I/O targets can process these multiple smaller requests asynchronously. The driver can register a [*CompletionRoutine*](https://msdn.microsoft.com/library/windows/hardware/ff540745) callback function for each of the smaller requests. Each time that the *CompletionRoutine* callback function is called, it can call [**WdfObjectDelete**](https://msdn.microsoft.com/library/windows/hardware/ff548734) to delete a driver-created request object. After the I/O target completes all of the smaller requests, the driver can call [**WdfRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff549945) to complete the original request.

### <a href="" id="providing-completion-information"></a> Providing Completion Information

When a driver completes a request, it can optionally provide some additional information that other drivers can access. For example, a driver might provide the number of bytes that were transferred for a read or write request. To provide this information, the driver can do either of the following:

-   Call [**WdfRequestSetInformation**](https://msdn.microsoft.com/library/windows/hardware/ff550032) before calling [**WdfRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff549945).

-   Call [**WdfRequestCompleteWithInformation**](https://msdn.microsoft.com/library/windows/hardware/ff549948).

### <a href="" id="obtaining-completion-information"></a> Obtaining Completion Information

To obtain information about an I/O request that another driver has completed, a driver can:

-   Call [**WdfRequestGetStatus**](https://msdn.microsoft.com/library/windows/hardware/ff549974) to obtain the completion status value that the lower-level driver specified when it called [**WdfRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff549945).

-   Call [**WdfRequestGetCompletionParams**](https://msdn.microsoft.com/library/windows/hardware/ff549961) to obtain a [**WDF\_REQUEST\_COMPLETION\_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff552454) structure that contains additional information about the completed request, such as handles to memory objects that represent the request's buffers, or bus-specific information.

    A driver can call [**WdfRequestGetCompletionParams**](https://msdn.microsoft.com/library/windows/hardware/ff549961) only after it calls [**WdfRequestSend**](https://msdn.microsoft.com/library/windows/hardware/ff550027) to send the I/O request synchronously or asynchronously to an I/O target. The driver must not call **WdfRequestGetCompletionParams** after it calls one of the methods that send I/O requests to I/O targets only synchronously (such as [**WdfIoTargetSendReadSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff548669)).

-   Call [**WdfRequestGetInformation**](https://msdn.microsoft.com/library/windows/hardware/ff549965) to obtain additional I/O completion information that the lower-level driver specified when it called [**WdfRequestSetInformation**](https://msdn.microsoft.com/library/windows/hardware/ff550032) or [**WdfRequestCompleteWithInformation**](https://msdn.microsoft.com/library/windows/hardware/ff549948), if drivers in the driver stack provide such information.

If a driver sends an I/O request synchronously, it typically calls [**WdfRequestGetStatus**](https://msdn.microsoft.com/library/windows/hardware/ff549974), [**WdfRequestGetCompletionParams**](https://msdn.microsoft.com/library/windows/hardware/ff549961), and [**WdfRequestGetInformation**](https://msdn.microsoft.com/library/windows/hardware/ff549965) after the synchronous call returns. If a driver sends an I/O request asynchronously, it typically calls these methods from within a [*CompletionRoutine*](https://msdn.microsoft.com/library/windows/hardware/ff540745) callback function.

For more information about completing I/O requests, see [Synchronizing Cancel and Completion Code](synchronizing-cancel-and-completion-code.md).

 

 





