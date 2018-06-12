---
title: ReqNotCanceledLocal rule (kmdf)
description: The ReqNotCanceledLocal rule specifies that if a request marked as cancelable is completed in a default I/O queue callback function, the WdfRequestUnmarkCancelable method must be called on the I/O request before completion.
ms.assetid: 3cc3d517-6fb9-46b2-9d22-6bdbef442007
ms.author: windowsdriverdev
ms.date: 5/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["ReqNotCanceledLocal rule (kmdf)"]
topic_type:
- apiref
api_name:
- ReqNotCanceledLocal
api_type:
- NA
---

# ReqNotCanceledLocal rule (kmdf)


The **ReqNotCanceledLocal** rule specifies that if a request marked as cancelable is completed in a default I/O queue callback function, the [**WdfRequestUnmarkCancelable**](https://msdn.microsoft.com/library/windows/hardware/ff550035) method must be called on the I/O request before completion. The I/O request must be completed, unless the request is canceled before it calls **WdfRequestUnmarkCancelable**.

If a request that was marked as cancelable by [**WdfRequestMarkCancelable**](https://msdn.microsoft.com/library/windows/hardware/ff549983) is completed (by calling [**WdfRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff549945), [**WdfRequestCompleteWithInformation**](https://msdn.microsoft.com/library/windows/hardware/ff549948), or [**WdfRequestCompleteWithPriorityBoost**](https://msdn.microsoft.com/library/windows/hardware/ff549949)), the [**WdfRequestUnmarkCancelable**](https://msdn.microsoft.com/library/windows/hardware/ff550035) method must be called before the I/O request is completed. The request can be completed unless the **WdfRequestUnmarkCancelable** method returns status that is equal to **STATUS\_CANCELLED**.

The default I/O queue callback functions for a request are [*EvtIoDefault*](https://msdn.microsoft.com/library/windows/hardware/ff541757), [*EvtIoRead*](https://msdn.microsoft.com/library/windows/hardware/ff541776), [*EvtIoWrite*](https://msdn.microsoft.com/library/windows/hardware/ff541813), [*EvtIoDeviceControl*](https://msdn.microsoft.com/library/windows/hardware/ff541758), [*EvtIoInternalDeviceControl*](https://msdn.microsoft.com/library/windows/hardware/ff541768).

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>ReqNotCanceledLocal</strong> rule.</p>
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

[**WdfRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff549945)
[**WdfRequestCompleteWithInformation**](https://msdn.microsoft.com/library/windows/hardware/ff549948)
[**WdfRequestCompleteWithPriorityBoost**](https://msdn.microsoft.com/library/windows/hardware/ff549949)
[**WdfRequestMarkCancelable**](https://msdn.microsoft.com/library/windows/hardware/ff549983)
[**WdfRequestMarkCancelableEx**](https://msdn.microsoft.com/library/windows/hardware/ff549984)
[**WdfRequestUnmarkCancelable**](https://msdn.microsoft.com/library/windows/hardware/ff550035)
 

 





