---
title: SpReturnValue rule (storport)
description: This rule verifies that the driver's implementations of HwStorFindAdapter and VirtualHwStorFindAdapter return a valid status. A valid status is one of the following SP\_RETURN\_FOUND, SP\_RETURN\_ERROR, SP\_RETURN\_BAD\_CONFIG, or SP\_RETURN\_NOT\_FOUND.
ms.assetid: 4F9E0FE3-4B1B-4C06-9DA0-8307C43E0DBA
ms.date: 05/21/2018
keywords: ["SpReturnValue rule (storport)"]
topic_type:
- apiref
api_name:
- SpReturnValue
api_type:
- NA
ms.localizationpriority: medium
---

# SpReturnValue rule (storport)


This rule verifies that the driver's implementations of [**HwStorFindAdapter**](https://msdn.microsoft.com/library/windows/hardware/ff557390) and [**VirtualHwStorFindAdapter**](https://msdn.microsoft.com/library/windows/hardware/ff568008) return a valid status. A valid status is one of the following: **SP\_RETURN\_FOUND**, **SP\_RETURN\_ERROR**, **SP\_RETURN\_BAD\_CONFIG**, or **SP\_RETURN\_NOT\_FOUND**.

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
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff552808" data-raw-source="[Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808)">Static Driver Verifier</a> and specify the <strong>SpReturnValue</strong> rule.</p>
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

 

 





