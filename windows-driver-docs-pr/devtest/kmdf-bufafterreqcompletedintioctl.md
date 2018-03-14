---
title: BufAfterReqCompletedIntIoctl rule (kmdf)
description: The BufAfterReqCompletedIntIoctl rule specifies that after a request is completed, its buffer cannot be accessed (inside EvtIoInternalDeviceControl callback function only).
ms.assetid: 6632262F-8163-4B4C-9B07-BCBD7CDA6E33
keywords: ["BufAfterReqCompletedIntIoctl rule (kmdf)"]
topic_type:
- apiref
api_name:
- BufAfterReqCompletedIntIoctl
api_type:
- NA
---

# BufAfterReqCompletedIntIoctl rule (kmdf)


The **BufAfterReqCompletedIntIoctl** rule specifies that after a request is completed, its buffer cannot be accessed (inside [*EvtIoInternalDeviceControl*](https://msdn.microsoft.com/library/windows/hardware/ff541768) callback function only). The buffer is retrieved by calling [**WdfRequestRetrieveOutputBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff550018) or [**WdfRequestRetrieveUnsafeUserOutputBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff550024) or [**WdfRequestRetrieveInputBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff550014) or [**WdfRequestRetrieveUnsafeUserInputBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff550022).

Within the [*EvtIoInternalDeviceControl*](https://msdn.microsoft.com/library/windows/hardware/ff541768) I/O queue event callback function, the request buffer retrieved by calling [**WdfRequestRetrieveInputBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff550014), [**WdfRequestRetrieveOutputBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff550018), [**WdfRequestRetrieveUnsafeUserInputBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff550022), or [**WdfRequestRetrieveUnsafeUserOutputBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff550024) cannot be accessed after the request is completed. The request is completed by calling [**WdfRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff549945), [**WdfRequestCompleteWithInformation**](https://msdn.microsoft.com/library/windows/hardware/ff549948), or **WdfRequestComplete**, [**WdfRequestCompleteWithPriorityBoost**](https://msdn.microsoft.com/library/windows/hardware/ff549949). The following possible buffer access functions are considered: **WdfRequestRetrieveOutputBuffer**, **WdfRequestRetrieveUnsafeUserOutputBuffer**, **WdfRequestRetrieveInputBuffer** and **WdfRequestRetrieveUnsafeUserInputBuffer**.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>BufAfterReqCompletedIntIoctl</strong> rule.</p>
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
[**WdfRequestRetrieveInputBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff550014)
[**WdfRequestRetrieveOutputBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff550018)
[**WdfRequestRetrieveUnsafeUserInputBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff550022)
[**WdfRequestRetrieveUnsafeUserOutputBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff550024)
 

 





