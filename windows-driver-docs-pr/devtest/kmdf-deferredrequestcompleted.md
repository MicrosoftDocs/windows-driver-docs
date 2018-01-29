---
title: DeferredRequestCompleted rule (kmdf)
description: The DeferredRequestCompleted rule specifies that if an I/O request presented to a driver's default I/O queue is not completed in the callback function but is deferred for later processing, the request must be completed in a deferred processing callback function, unless the request is forwarded and delivered to the framework, or unless the WdfRequestStopAcknowledge method is called.
ms.assetid: 14ed0dda-8acb-48fe-933f-e498c41f5403
keywords: ["DeferredRequestCompleted rule (kmdf)"]
topic_type:
- apiref
api_name:
- DeferredRequestCompleted
api_type:
- NA
---

# DeferredRequestCompleted rule (kmdf)


The **DeferredRequestCompleted** rule specifies that if an I/O request presented to a driver's default I/O queue is not completed in the callback function but is deferred for later processing, the request must be completed in a deferred processing callback function, unless the request is forwarded and delivered to the framework, or unless the [**WdfRequestStopAcknowledge**](https://msdn.microsoft.com/library/windows/hardware/ff550033) method is called.

The **DeferredRequestCompleted** rule requires that you identify the deferred requests using the **\_\_sdv\_save\_request** and **\_\_sdv\_retrieve\_request** macros. For information about how to use these macros, see [Using \_\_sdv\_save\_request and \_\_sdv\_retrieve\_request for Deferred Procedure Calls](https://msdn.microsoft.com/library/windows/hardware/ff556071). The precondition rule **AliasWithinTimerDpc** checks for the presence of these macros.

A request presented to the driver's default queue through one of the queue callback functions and deferred, must be completed before it exits from the I/O request callback functions, except in the following cases:

-   The I/O request was forwarded to an I/O target or to another queue

-   The I/O request was delivered to the framework (by calling [**WdfDeviceEnqueueRequest**](https://msdn.microsoft.com/library/windows/hardware/ff545945))

-   The **WdfRequestStopAcknowledge** method was called

The rule is verified when the driver exits from the following callback functions:

-   **EvtIoStop**, **EvtCleanupCallback** or **EvtDestroyCallback** for the queue

-   **EvtCleanupCallback** or **EvtDestroyCallback** for the file object

-   **EvtFileClose**, **EvtFileCleanup**, **EvtDeviceSelfManagedIoSuspend**, **EvtDeviceSelfManagedIoFlush**, **EvtDeviceSelfManagedIoCleanup**, **EvtDeviceShutdownNotification**, **EvtDeviceSurpriseRemoval**, **EvtCleanupCallback** or **EvtDestroyCallback** for the device

-   **EvtDriverUnload**

The I/O queue callback functions for the I/O request presentation are **EvtIoDefault**, **EvtIoRead**, **EvtIoWrite**, **EvtIoDeviceControl**, and **EvtIoInternalDeviceControl**.

The deferred processing callback functions for an I/O request are **EvtTimerFunc**, **EvtDpcFunc**, **EvtInterruptDpc**, **EvtInterruptEnable**, **EvtInterruptDisable**, and **EvtWorkItem**.

The **DeferredRequestCompleted** rule uses calls to the **WdfRequestMarkCancelable**, **WdfDmaTransactionInitializeUsingRequest**, **WdfDmaTransactionInitialize**, or **WdfWorkItemEnqueue** methods to indicate that the I/O request is being deferred.

|              |      |
|--------------|------|
| Driver model | KMDF |

How to test
-----------

<table>
<colgroup>
<col width="100%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">At compile time</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>DeferredRequestCompleted</strong> rule.</p>
Use the following steps to run an analysis of your code:
<ol>
<li>[Prepare your code (use role type declarations).](https://msdn.microsoft.com/library/windows/hardware/hh454281#preparing-your-source-code)</li>
<li>[Run Static Driver Verifier.](https://msdn.microsoft.com/library/windows/hardware/hh454281#running-static-driver-verifier)</li>
<li>[View and analyze the results.](https://msdn.microsoft.com/library/windows/hardware/hh454281#viewing-and-analyzing-the-results)</li>
</ol>
<p>For more information, see [Using Static Driver Verifier to Find Defects in Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454281).</p></td>
</tr>
</tbody>
</table>

Applies to
----------

[**WdfDeviceEnqueueRequest**](https://msdn.microsoft.com/library/windows/hardware/ff545945)
[**WdfDmaTransactionInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff547099)
[**WdfDmaTransactionInitializeUsingRequest**](https://msdn.microsoft.com/library/windows/hardware/ff547107)
[**WdfIoTargetSendInternalIoctlOthersSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff548651)
[**WdfIoTargetSendInternalIoctlSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff548656)
[**WdfIoTargetSendIoctlSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff548660)
[**WdfIoTargetSendReadSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff548669)
[**WdfIoTargetSendWriteSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff548672)
[**WdfRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff549945)
[**WdfRequestCompleteWithInformation**](https://msdn.microsoft.com/library/windows/hardware/ff549948)
[**WdfRequestCompleteWithPriorityBoost**](https://msdn.microsoft.com/library/windows/hardware/ff549949)
[**WdfRequestForwardToIoQueue**](https://msdn.microsoft.com/library/windows/hardware/ff549958)
[**WdfRequestMarkCancelable**](https://msdn.microsoft.com/library/windows/hardware/ff549983)
[**WdfRequestMarkCancelableEx**](https://msdn.microsoft.com/library/windows/hardware/ff549984)
[**WdfRequestSend**](https://msdn.microsoft.com/library/windows/hardware/ff550027)
[**WdfRequestStopAcknowledge**](https://msdn.microsoft.com/library/windows/hardware/ff550033)
[**WdfRequestUnmarkCancelable**](https://msdn.microsoft.com/library/windows/hardware/ff550035)
[**WdfWorkItemEnqueue**](https://msdn.microsoft.com/library/windows/hardware/ff551203)
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20DeferredRequestCompleted%20rule%20%28kmdf%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




