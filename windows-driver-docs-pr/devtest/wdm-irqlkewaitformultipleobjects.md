---
title: IrqlKeWaitForMultipleObjects rule (wdm)
description: The IrqlKeWaitForMultipleObjects rule specifies that callers of the KeWaitForMultipleObjects routine must be running at proper IRQL based upon the Timeout parameter.
ms.assetid: FC3E3544-95FB-4283-B030-66D74D0F7848
ms.author: windowsdriverdev
ms.date: 5/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["IrqlKeWaitForMultipleObjects rule (wdm)"]
topic_type:
- apiref
api_name:
- IrqlKeWaitForMultipleObjects
api_type:
- NA
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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>IrqlKeWaitForMultipleObjects</strong> rule.</p>
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

[**KeWaitForMultipleObjects**](https://msdn.microsoft.com/library/windows/hardware/ff553324)
 

 





