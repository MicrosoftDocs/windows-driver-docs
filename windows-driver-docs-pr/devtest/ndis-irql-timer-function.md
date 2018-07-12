---
title: Irql\_Timer\_Function rule (ndis)
description: The Irql\_Timer\_Function rule specifies that the NDIS timer service functions must be called at correct IRQL levels.
ms.assetid: 4c946f79-7661-4ff6-b2a3-1a5851c9e215
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["Irql_Timer_Function rule (ndis)"]
topic_type:
- apiref
api_name:
- Irql_Timer_Function
api_type:
- NA
---

# Irql\_Timer\_Function rule (ndis)


The Irql\_Timer\_Function rule specifies that the NDIS timer service functions must be called at correct IRQL levels.

This rule verifies the following NDIS functions:

**NdisAllocateTimerObject**
**NdisCancelTimerObject**
**NdisFreeTimerObject**
**NdisSetTimerObject**
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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>Irql_Timer_Function</strong> rule.</p>
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

[**NdisAllocateTimerObject**](https://msdn.microsoft.com/library/windows/hardware/ff561618)
[**NdisCancelTimerObject**](https://msdn.microsoft.com/library/windows/hardware/ff561624)
[**NdisFreeTimerObject**](https://msdn.microsoft.com/library/windows/hardware/ff562605)
[**NdisSetTimerObject**](https://msdn.microsoft.com/library/windows/hardware/ff564563)
 

 





