---
title: RequestCompleted rule (kmdf)
description: The DeferredRequestCompleted rule specifies that for a non-filter driver each request presented to the driver's default I/O queue must be completed, unless the request is deferred or forwarded, or if WdfRequestStopAcknowledge is called.
ms.assetid: fb034d81-d49d-43a5-92b9-9b4e3f3056ee
ms.date: 05/21/2018
keywords: ["RequestCompleted rule (kmdf)"]
topic_type:
- apiref
api_name:
- RequestCompleted
api_type:
- NA
ms.localizationpriority: medium
---

# RequestCompleted rule (kmdf)


The [**DeferredRequestCompleted**](kmdf-deferredrequestcompleted.md) rule specifies that for a non-filter driver each request presented to the driver's default I/O queue must be completed, unless the request is deferred or forwarded, or if [**WdfRequestStopAcknowledge**](https://msdn.microsoft.com/library/windows/hardware/ff550033) is called.

An I/O request presented to the driver's default queue through one of the queue callback functions must be completed before it exits from the I/O request callback functions, except in the following cases:

-   The request was deferred (to a DPC or work item, for example). In this case, you can use the [DeferredRequestCompleted](kmdf-deferredrequestcompleted.md) rule.

-   The request was forwarded to an I/O target or to another queue

-   The request was delivered to the framework (by calling [**WdfDeviceEnqueueRequest**](https://msdn.microsoft.com/library/windows/hardware/ff545945))

-   [**WdfRequestStopAcknowledge**](https://msdn.microsoft.com/library/windows/hardware/ff550033) was called

The rule is verified when the driver exits from the following callback functions:

-   [*EvtIoStop*](https://msdn.microsoft.com/library/windows/hardware/ff541788), [*EvtCleanupCallback*](https://msdn.microsoft.com/library/windows/hardware/ff540840) or [*EvtDestroyCallback*](https://msdn.microsoft.com/library/windows/hardware/ff540841) for the queue

-   [*EvtCleanupCallback*](https://msdn.microsoft.com/library/windows/hardware/ff540840) or [*EvtDestroyCallback*](https://msdn.microsoft.com/library/windows/hardware/ff540841) for the file object

-   [*EvtFileClose*](https://msdn.microsoft.com/library/windows/hardware/ff541702), [*EvtFileCleanup*](https://msdn.microsoft.com/library/windows/hardware/ff541700), [*EvtDeviceSelfManagedIoSuspend*](https://msdn.microsoft.com/library/windows/hardware/ff540907), [*EvtDeviceSelfManagedIoFlush*](https://msdn.microsoft.com/library/windows/hardware/ff540901), [*EvtDeviceSelfManagedIoCleanup*](https://msdn.microsoft.com/library/windows/hardware/ff540898), [*EvtDeviceShutdownNotification*](https://msdn.microsoft.com/library/windows/hardware/ff540911), [*EvtDeviceSurpriseRemoval*](https://msdn.microsoft.com/library/windows/hardware/ff540913), [*EvtCleanupCallback*](https://msdn.microsoft.com/library/windows/hardware/ff540840) or [*EvtDestroyCallback*](https://msdn.microsoft.com/library/windows/hardware/ff540841) for the device

-   [*EvtDriverUnload*](https://msdn.microsoft.com/library/windows/hardware/ff541694)

The I/O queue callback functions for request presentation are [*EvtIoDefault*](https://msdn.microsoft.com/library/windows/hardware/ff541757), [*EvtIoRead*](https://msdn.microsoft.com/library/windows/hardware/ff541776), [*EvtIoWrite*](https://msdn.microsoft.com/library/windows/hardware/ff541813), [*EvtIoDeviceControl*](https://msdn.microsoft.com/library/windows/hardware/ff541758), and [*EvtIoInternalDeviceControl*](https://msdn.microsoft.com/library/windows/hardware/ff541768)

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
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff552808" data-raw-source="[Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808)">Static Driver Verifier</a> and specify the <strong>RequestCompleted</strong> rule.</p>
Use the following steps to run an analysis of your code:
<ol>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/hh454281#preparing-your-source-code" data-raw-source="[Prepare your code (use role type declarations).](https://msdn.microsoft.com/library/windows/hardware/hh454281#preparing-your-source-code)">Prepare your code (use role type declarations).</a></li>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/hh454281#running-static-driver-verifier" data-raw-source="[Run Static Driver Verifier.](https://msdn.microsoft.com/library/windows/hardware/hh454281#running-static-driver-verifier)">Run Static Driver Verifier.</a></li>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/hh454281#viewing-and-analyzing-the-results" data-raw-source="[View and analyze the results.](https://msdn.microsoft.com/library/windows/hardware/hh454281#viewing-and-analyzing-the-results)">View and analyze the results.</a></li>
</ol>
<p>For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/hh454281" data-raw-source="[Using Static Driver Verifier to Find Defects in Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454281)">Using Static Driver Verifier to Find Defects in Drivers</a>.</p></td>
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
[**WdfWorkItemEnqueue**](https://msdn.microsoft.com/library/windows/hardware/ff551203)
 

 





