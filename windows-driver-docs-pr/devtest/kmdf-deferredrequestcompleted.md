---
title: DeferredRequestCompleted rule (kmdf)
description: The DeferredRequestCompleted rule specifies that if an I/O request presented to a driver's default I/O queue is not completed in the callback function but is deferred for later processing, the request must be completed in a deferred processing callback function, unless the request is forwarded and delivered to the framework, or unless the WdfRequestStopAcknowledge method is called.
ms.date: 05/21/2018
keywords: ["DeferredRequestCompleted rule (kmdf)"]
topic_type:
- apiref
api_name:
- DeferredRequestCompleted
api_type:
- NA
ms.localizationpriority: medium
---

# DeferredRequestCompleted rule (kmdf)


The **DeferredRequestCompleted** rule specifies that if an I/O request presented to a driver's default I/O queue is not completed in the callback function but is deferred for later processing, the request must be completed in a deferred processing callback function, unless the request is forwarded and delivered to the framework, or unless the [**WdfRequestStopAcknowledge**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequeststopacknowledge) method is called.

The **DeferredRequestCompleted** rule requires that you identify the deferred requests using the **\_\_sdv\_save\_request** and **\_\_sdv\_retrieve\_request** macros. For information about how to use these macros, see [Using \_\_sdv\_save\_request and \_\_sdv\_retrieve\_request for Deferred Procedure Calls](./using---sdv-save-request-and---sdv-retrieve-request-for-deferred-proce.md). The precondition rule **AliasWithinTimerDpc** checks for the presence of these macros.

A request presented to the driver's default queue through one of the queue callback functions and deferred, must be completed before it exits from the I/O request callback functions, except in the following cases:

-   The I/O request was forwarded to an I/O target or to another queue

-   The I/O request was delivered to the framework (by calling [**WdfDeviceEnqueueRequest**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceenqueuerequest))

-   The **WdfRequestStopAcknowledge** method was called

The rule is verified when the driver exits from the following callback functions:

-   **EvtIoStop**, **EvtCleanupCallback** or **EvtDestroyCallback** for the queue

-   **EvtCleanupCallback** or **EvtDestroyCallback** for the file object

-   **EvtFileClose**, **EvtFileCleanup**, **EvtDeviceSelfManagedIoSuspend**, **EvtDeviceSelfManagedIoFlush**, **EvtDeviceSelfManagedIoCleanup**, **EvtDeviceShutdownNotification**, **EvtDeviceSurpriseRemoval**, **EvtCleanupCallback** or **EvtDestroyCallback** for the device

-   **EvtDriverUnload**

The I/O queue callback functions for the I/O request presentation are **EvtIoDefault**, **EvtIoRead**, **EvtIoWrite**, **EvtIoDeviceControl**, and **EvtIoInternalDeviceControl**.

The deferred processing callback functions for an I/O request are **EvtTimerFunc**, **EvtDpcFunc**, **EvtInterruptDpc**, **EvtInterruptEnable**, **EvtInterruptDisable**, and **EvtWorkItem**.

The **DeferredRequestCompleted** rule uses calls to the **WdfRequestMarkCancelable**, **WdfDmaTransactionInitializeUsingRequest**, **WdfDmaTransactionInitialize**, or **WdfWorkItemEnqueue** methods to indicate that the I/O request is being deferred.

**Driver model: KMDF**

## How to test

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
<td align="left"><p>Run <a href="/windows-hardware/drivers/devtest/static-driver-verifier" data-raw-source="[Static Driver Verifier](./static-driver-verifier.md)">Static Driver Verifier</a> and specify the <strong>DeferredRequestCompleted</strong> rule.</p>
Use the following steps to run an analysis of your code:
<ol>
<li><a href="/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#preparing-your-source-code" data-raw-source="[Prepare your code (use role type declarations).](./using-static-driver-verifier-to-find-defects-in-drivers.md#preparing-your-source-code)">Prepare your code (use role type declarations).</a></li>
<li><a href="/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#running-static-driver-verifier" data-raw-source="[Run Static Driver Verifier.](./using-static-driver-verifier-to-find-defects-in-drivers.md#running-static-driver-verifier)">Run Static Driver Verifier.</a></li>
<li><a href="/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#viewing-and-analyzing-the-results" data-raw-source="[View and analyze the results.](./using-static-driver-verifier-to-find-defects-in-drivers.md#viewing-and-analyzing-the-results)">View and analyze the results.</a></li>
</ol>
<p>For more information, see <a href="/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers" data-raw-source="[Using Static Driver Verifier to Find Defects in Drivers](./using-static-driver-verifier-to-find-defects-in-drivers.md)">Using Static Driver Verifier to Find Defects in Drivers</a>.</p></td>
</tr>
</tbody>
</table>

## Applies to

[**WdfDeviceEnqueueRequest**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceenqueuerequest)
[**WdfDmaTransactionInitialize**](/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactioninitialize)
[**WdfDmaTransactionInitializeUsingRequest**](/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactioninitializeusingrequest)
[**WdfIoTargetSendInternalIoctlOthersSynchronously**](/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetsendinternalioctlotherssynchronously)
[**WdfIoTargetSendInternalIoctlSynchronously**](/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetsendinternalioctlsynchronously)
[**WdfIoTargetSendIoctlSynchronously**](/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetsendioctlsynchronously)
[**WdfIoTargetSendReadSynchronously**](/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetsendreadsynchronously)
[**WdfIoTargetSendWriteSynchronously**](/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetsendwritesynchronously)
[**WdfRequestComplete**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestcomplete)
[**WdfRequestCompleteWithInformation**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestcompletewithinformation)
[**WdfRequestCompleteWithPriorityBoost**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestcompletewithpriorityboost)
[**WdfRequestForwardToIoQueue**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestforwardtoioqueue)
[**WdfRequestMarkCancelable**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestmarkcancelable)
[**WdfRequestMarkCancelableEx**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestmarkcancelableex)
[**WdfRequestSend**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestsend)
[**WdfRequestStopAcknowledge**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequeststopacknowledge)
[**WdfRequestUnmarkCancelable**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestunmarkcancelable)
[**WdfWorkItemEnqueue**](/windows-hardware/drivers/ddi/wdfworkitem/nf-wdfworkitem-wdfworkitemenqueue)
