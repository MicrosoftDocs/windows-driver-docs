---
title: PagedCode rule (storport)
description: This rule verifies that when the PAGED\_CODE macro is called, the driver is at IRQL DISPATCH\_LEVEL. Any code executing at IRQL DISPATCH\_LEVEL must be in non-paged memory to avoid causing page faults.
ms.assetid: 7FED3FEF-E6E5-4C26-8777-0A4BCCE0E1EE
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["PagedCode rule (storport)"]
topic_type:
- apiref
api_name:
- PagedCode
api_type:
- NA
---

# PagedCode rule (storport)


This rule verifies that when the [**PAGED\_CODE**](https://msdn.microsoft.com/library/windows/hardware/ff558773) macro is called, the driver is at **IRQL &lt; DISPATCH\_LEVEL**. Any code executing at **IRQL &gt;= DISPATCH\_LEVEL** must be in non-paged memory to avoid causing page faults.

|              |          |
|--------------|----------|
| Driver model | Storport |

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>PagedCode</strong> rule.</p>
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

[**PAGED\_CODE**](https://msdn.microsoft.com/library/windows/hardware/ff558773)
 

 





