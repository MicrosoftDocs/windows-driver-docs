---
title: WdfIoQueueRetrieveFoundRequest rule (kmdf)
description: The WdfIoQueueRetrieveFoundRequest rule specifies that WdfIoQueueRetrieveFoundRequest method is called only after WdfIoQueueFindRequest is called and returned STATUS\_SUCCESS and no WdfObjectDereference is called on the same request.
ms.assetid: CF545174-5E6D-429B-AC6D-BA7A84852FC1
ms.date: 05/21/2018
keywords: ["WdfIoQueueRetrieveFoundRequest rule (kmdf)"]
topic_type:
- apiref
api_name:
- WdfIoQueueRetrieveFoundRequest
api_type:
- NA
ms.localizationpriority: medium
---

# WdfIoQueueRetrieveFoundRequest rule (kmdf)


The **WdfIoQueueRetrieveFoundRequest** rule specifies that [**WdfIoQueueRetrieveFoundRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548456) method is called only after [**WdfIoQueueFindRequest**](https://msdn.microsoft.com/library/windows/hardware/ff547415) is called and returned STATUS\_SUCCESS and no [**WdfObjectDereference**](https://msdn.microsoft.com/library/windows/hardware/ff548739) is called on the same request.

If [**WdfIoQueueFindRequest**](https://msdn.microsoft.com/library/windows/hardware/ff547415) returns STATUS\_SUCCESS it increments the reference count of the output request object, the driver must call [**WdfObjectDereference**](https://msdn.microsoft.com/library/windows/hardware/ff548739) after it has finished using this request handle.

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
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff552808" data-raw-source="[Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808)">Static Driver Verifier</a> and specify the <strong>WdfIoQueueRetrieveFoundRequest</strong> rule.</p>
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

[**WdfIoQueueFindRequest**](https://msdn.microsoft.com/library/windows/hardware/ff547415)
[**WdfIoQueueRetrieveFoundRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548456)
[**WdfObjectDereference**](https://msdn.microsoft.com/library/windows/hardware/ff548739)
 

 





