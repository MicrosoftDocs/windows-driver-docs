---
title: NoIoQueuePurgeSynchronously rule (kmdf)
ms.assetid: 9255C644-1141-4D9A-8B84-BF98FB9E262A
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
description: 
keywords: ["NoIoQueuePurgeSynchronously rule (kmdf)"]
topic_type:
- apiref
api_name:
- NoIoQueuePurgeSynchronously
api_type:
- NA
---

# NoIoQueuePurgeSynchronously rule (kmdf)


The **NoIoQueuePurgeSynchronously** rule verifies that WDF drivers don't call the [**WdfIoQueueStopSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff548489), [**WdfIoQueueDrainSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff547412), [**WdfIoQueueStopAndPurgeSynchronously**](https://msdn.microsoft.com/library/windows/hardware/hh439293), or [**WdfIoQueuePurgeSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff548449) functions from the following EvtIO queue object event callback functions:

[*EvtIoDefault*](https://msdn.microsoft.com/library/windows/hardware/ff541757)
[*EvtIoDeviceControl*](https://msdn.microsoft.com/library/windows/hardware/ff541758)
[*EvtIoInternalDeviceControl*](https://msdn.microsoft.com/library/windows/hardware/ff541768)
[*EvtIoRead*](https://msdn.microsoft.com/library/windows/hardware/ff541776)
[*EvtIoWrite*](https://msdn.microsoft.com/library/windows/hardware/ff541813)
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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>NoIoQueuePurgeSynchronously</strong> rule.</p>
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

[**WdfRequestCancelSentRequest**](https://msdn.microsoft.com/library/windows/hardware/ff549941)
[**WdfRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff549945)
[**WdfRequestCompleteWithInformation**](https://msdn.microsoft.com/library/windows/hardware/ff549948)
[**WdfRequestCompleteWithPriorityBoost**](https://msdn.microsoft.com/library/windows/hardware/ff549949)
[**WdfRequestMarkCancelable**](https://msdn.microsoft.com/library/windows/hardware/ff549983)
[**WdfRequestMarkCancelableEx**](https://msdn.microsoft.com/library/windows/hardware/ff549984)
[**WdfRequestStopAcknowledge**](https://msdn.microsoft.com/library/windows/hardware/ff550033)
[**WdfRequestUnmarkCancelable**](https://msdn.microsoft.com/library/windows/hardware/ff550035)
 

 





