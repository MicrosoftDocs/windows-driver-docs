---
title: WdfIoQueueRetrieveNextRequest rule (kmdf)
description: The WdfIoQueueRetrieveNextRequest rule specifies that WdfIoQueueRetrieveNextRequest is not called after WdfIoQueueFindRequest is called.
ms.assetid: D6BB8920-16A1-4E87-A904-137ACAB7418A
ms.author: windowsdriverdev
ms.date: 5/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["WdfIoQueueRetrieveNextRequest rule (kmdf)"]
topic_type:
- apiref
api_name:
- WdfIoQueueRetrieveNextRequest
api_type:
- NA
---

# WdfIoQueueRetrieveNextRequest rule (kmdf)


The **WdfIoQueueRetrieveNextRequest** rule specifies that [**WdfIoQueueRetrieveNextRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548462) is not called after [**WdfIoQueueFindRequest**](https://msdn.microsoft.com/library/windows/hardware/ff547415) is called.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>WdfIoQueueRetrieveNextRequest</strong> rule.</p>
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

[**WdfIoQueueFindRequest**](https://msdn.microsoft.com/library/windows/hardware/ff547415)
[**WdfIoQueueRetrieveNextRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548462)
 

 





