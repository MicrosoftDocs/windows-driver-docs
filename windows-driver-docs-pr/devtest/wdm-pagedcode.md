---
title: PagedCode rule (wdm)
description: The PagedCode rule specifies that the driver calls the PAGED\_CODE macro only when it is executing at IRQL�  APC\_LEVEL.
ms.assetid: de272bc2-8391-41b1-9526-3e135a586258
keywords: ["PagedCode rule (wdm)"]
topic_type:
- apiref
api_name:
- PagedCode
api_type:
- NA
---

# PagedCode rule (wdm)


The **PagedCode** rule specifies that the driver calls the [**PAGED\_CODE**](https://msdn.microsoft.com/library/windows/hardware/ff558773) macro only when it is executing at **IRQL &lt;= APC\_LEVEL**.

|              |     |
|--------------|-----|
| Driver model | WDM |

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
 

 





