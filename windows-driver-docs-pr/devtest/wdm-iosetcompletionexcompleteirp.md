---
title: IoSetCompletionExCompleteIrp rule (wdm)
description: The IoSetCompletionExCompleteIrp rule specifies that the IoSetCompletionRoutineEx routine returns an NTSTATUS value.
ms.assetid: 892ADDF3-9FC0-48A9-AECC-71722A10B2BE
ms.date: 05/21/2018
keywords: ["IoSetCompletionExCompleteIrp rule (wdm)"]
topic_type:
- apiref
api_name:
- IoSetCompletionExCompleteIrp
api_type:
- NA
ms.localizationpriority: medium
---

# IoSetCompletionExCompleteIrp rule (wdm)


The **IoSetCompletionExCompleteIrp** rule specifies that the [**IoSetCompletionRoutineEx**](https://msdn.microsoft.com/library/windows/hardware/ff549686) routine returns an NTSTATUS value. The driver must check this value to determine if the [*IoCompletion*](https://msdn.microsoft.com/library/windows/hardware/ff548354) routine was successfully registered before calling [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336) or [**PoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff559654) and if **IoSetCompletionRoutineEx** fails then the IRP should be completed and the dispatch routine should return.

|              |     |
|--------------|-----|
| Driver model | WDM |

|                                   |                                                                                                                                       |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187) (0x0004100F) |

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>IoSetCompletionExCompleteIrp</strong> rule.</p>
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

<table>
<colgroup>
<col width="100%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">At run time</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Run [Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448) and select the [DDI compliance checking](https://msdn.microsoft.com/library/windows/hardware/hh454208) option.</p></td>
</tr>
</tbody>
</table>

 

Applies to
----------

[**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343)
[**IoSetCompletionRoutineEx**](https://msdn.microsoft.com/library/windows/hardware/ff549686)
 

 





