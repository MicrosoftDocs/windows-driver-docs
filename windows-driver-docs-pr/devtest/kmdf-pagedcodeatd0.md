---
title: PagedCodeAtD0 rule (kmdf)
description: The PagedCodeAtD0 rule specifies that a driver must not mark code as pageable within callback functions that are in the power-up code path.
ms.assetid: e3e0ee8f-eebe-4855-be35-3d8b153dd09e
ms.author: windowsdriverdev
ms.date: 5/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["PagedCodeAtD0 rule (kmdf)"]
topic_type:
- apiref
api_name:
- PagedCodeAtD0
api_type:
- NA
---

# PagedCodeAtD0 rule (kmdf)


The **PagedCodeAtD0** rule specifies that a driver must not mark code as pageable within callback functions that are in the power-up code path.

When a function is marked pageable and the code section is subsequently paged out, the function generates a page fault, which could impact the fast resume behavior of the computer. This happens because the client driver will have to wait until the system drivers can service this page fault.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>PagedCodeAtD0</strong> rule.</p>
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
 

 





