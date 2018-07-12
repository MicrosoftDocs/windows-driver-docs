---
title: WdfIoQueueFindRequestFailed rule (kmdf)
description: The WdfIoQueueFindRequestFailed rule specifies that WdfIoQueueRetrieveFoundRequest or WdfObjectDereference should only be called after WdfIoQueueFindRequestFailed returns STATUS\_SUCCESS.
ms.assetid: 9D211A0A-36CB-4083-B379-EE1C34A7B50F
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["WdfIoQueueFindRequestFailed rule (kmdf)"]
topic_type:
- apiref
api_name:
- WdfIoQueueFindRequestFailed
api_type:
- NA
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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>WdfIoQueueFindRequestFailed</strong> rule.</p>
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
[**WdfIoQueueRetrieveFoundRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548456)
[**WdfObjectDereference**](https://msdn.microsoft.com/library/windows/hardware/ff548739)
 

 





