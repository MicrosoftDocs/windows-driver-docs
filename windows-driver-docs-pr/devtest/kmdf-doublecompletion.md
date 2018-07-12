---
title: DoubleCompletion rule (kmdf)
description: The DoubleCompletion rule specifies that drivers must not complete an I/O request twice.
ms.assetid: F005501B-29B5-42CE-8CAD-EDA00E1E5D82
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["DoubleCompletion rule (kmdf)"]
topic_type:
- apiref
api_name:
- DoubleCompletion
api_type:
- NA
---

# DoubleCompletion rule (kmdf)


The **DoubleCompletion** rule specifies that drivers must not complete an I/O request twice. The following methods should not be called twice in a row for the same request: [**WdfRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff549945), [**WdfRequestCompleteWithInformation**](https://msdn.microsoft.com/library/windows/hardware/ff549948), [**WdfRequestCompleteWithPriorityBoost**](https://msdn.microsoft.com/library/windows/hardware/ff549949).

The difference between this rule and the [DoubleCompletionLocal](kmdf-doublecompletionlocal.md) rule is that the DoubleCompletionLocal rule is only performed within the default I/O queue callback functions.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>DoubleCompletion</strong> rule.</p>
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

[**WdfIoQueueRetrieveFoundRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548456)
[**WdfIoQueueRetrieveNextRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548462)
[**WdfIoQueueRetrieveRequestByFileObject**](https://msdn.microsoft.com/library/windows/hardware/ff548470)
[**WdfRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff549945)
[**WdfRequestCompleteWithInformation**](https://msdn.microsoft.com/library/windows/hardware/ff549948)
[**WdfRequestCompleteWithPriorityBoost**](https://msdn.microsoft.com/library/windows/hardware/ff549949)
 

 





