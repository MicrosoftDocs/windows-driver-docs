---
title: IrqlKeWaitForMultipleObjects rule (wdm)
description: The IrqlKeWaitForMultipleObjects rule specifies that callers of the KeWaitForMultipleObjects routine must be running at proper IRQL based upon the Timeout parameter.
ms.assetid: FC3E3544-95FB-4283-B030-66D74D0F7848
ms.date: 05/21/2018
keywords: ["IrqlKeWaitForMultipleObjects rule (wdm)"]
topic_type:
- apiref
api_name:
- IrqlKeWaitForMultipleObjects
api_type:
- NA
ms.localizationpriority: medium
---

# IrqlKeWaitForMultipleObjects rule (wdm)


The **IrqlKeWaitForMultipleObjects** rule specifies that callers of the [**KeWaitForMultipleObjects**](https://msdn.microsoft.com/library/windows/hardware/ff553324) routine must be running at proper IRQL based upon the *Timeout* parameter.

Callers of **IrqlKeWaitForMultipleObjects** routine can be running at IRQL &lt;= DISPATCH\_LEVEL, except in the following situations:

-   If *Timeout* &lt;&gt; 0, the caller of the [**KeWaitForMultipleObjects**](https://msdn.microsoft.com/library/windows/hardware/ff553324) routine must be running at IRQL &lt;= APC\_LEVEL.
-   If *Timeout* != NULL and \**Timeout* = 0, the caller of the [**KeWaitForMultipleObjects**](https://msdn.microsoft.com/library/windows/hardware/ff553324) routine must be running at IRQL = DISPATCH\_LEVEL.

-   If *Timeout* = **NULL**, or \**Timeout* != 0, the caller of the [**KeWaitForMultipleObjects**](https://msdn.microsoft.com/library/windows/hardware/ff553324) routine must running at IRQL &lt;= APC\_LEVEL.

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
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff552808" data-raw-source="[Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808)">Static Driver Verifier</a> and specify the <strong>IrqlKeWaitForMultipleObjects</strong> rule.</p>
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

[**KeWaitForMultipleObjects**](https://msdn.microsoft.com/library/windows/hardware/ff553324)
 

 





