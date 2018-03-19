---
title: PeriodicTimer rule (ndis)
description: The PeriodicTimer rule specifies that the caller of NdisCancelTimerObject must be running at IRQL PASSIVE\_LEVEL if a nonzero value was specified in the MillisecondsPeriod parameter of the NdisSetTimerObject function.
ms.assetid: a6bda698-5150-4fd5-b665-d460b88fe0ac
keywords: ["PeriodicTimer rule (ndis)"]
topic_type:
- apiref
api_name:
- PeriodicTimer
api_type:
- NA
---

# PeriodicTimer rule (ndis)


The **PeriodicTimer** rule specifies that the caller of [**NdisCancelTimerObject**](https://msdn.microsoft.com/library/windows/hardware/ff561624) must be running at **IRQL = PASSIVE\_LEVEL** if a nonzero value was specified in the *MillisecondsPeriod* parameter of the [**NdisSetTimerObject**](https://msdn.microsoft.com/library/windows/hardware/ff564563) function. If the *MillisecondsPeriod* parameter of the **NdisSetTimerObject** function was zero, callers of **NdisCancelTimerObject** can be running at **IRQL &lt;= DISPATCH\_LEVEL**.

|              |      |
|--------------|------|
| Driver model | NDIS |

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>PeriodicTimer</strong> rule.</p>
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

[**NdisCancelTimerObject**](https://msdn.microsoft.com/library/windows/hardware/ff561624)
[**NdisSetTimerObject**](https://msdn.microsoft.com/library/windows/hardware/ff564563)
 

 





