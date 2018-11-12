---
title: WdfIoQueueFindRequestFailed rule (kmdf)
description: The WdfIoQueueFindRequestFailed rule specifies that WdfIoQueueRetrieveFoundRequest or WdfObjectDereference should only be called after WdfIoQueueFindRequestFailed returns STATUS\_SUCCESS.
ms.assetid: 9D211A0A-36CB-4083-B379-EE1C34A7B50F
ms.date: 05/21/2018
keywords: ["WdfIoQueueFindRequestFailed rule (kmdf)"]
topic_type:
- apiref
api_name:
- WdfIoQueueFindRequestFailed
api_type:
- NA
ms.localizationpriority: medium
---

# WdfIoQueueFindRequestFailed rule (kmdf)


The **WdfIoQueueFindRequestFailed** rule specifies that [**WdfIoQueueRetrieveFoundRequest**](kmdf-wdfioqueueretrievefoundrequest.md) or [**WdfObjectDereference**](https://msdn.microsoft.com/library/windows/hardware/ff548739) should only be called after **WdfIoQueueFindRequestFailed** returns STATUS\_SUCCESS.

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
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff552808" data-raw-source="[Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808)">Static Driver Verifier</a> and specify the <strong>WdfIoQueueFindRequestFailed</strong> rule.</p>
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
 

 





