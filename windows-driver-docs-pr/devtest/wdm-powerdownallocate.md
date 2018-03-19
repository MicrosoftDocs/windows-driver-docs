---
title: PowerDownAllocate rule (wdm)
description: The PowerDownAllocate rule specifies that an FDO and FIDO driver should not allocate memory when processing an IRP\_MN\_SET\_POWER request for a SystemPowerState transition that goes from s0 to \ S1...S5\ .
ms.assetid: 01737B5F-C1DF-4012-85F2-E9B7517EA53A
keywords: ["PowerDownAllocate rule (wdm)"]
topic_type:
- apiref
api_name:
- PowerDownAllocate
api_type:
- NA
---

# PowerDownAllocate rule (wdm)


The **PowerDownAllocate** rule specifies that an FDO and FIDO driver should not allocate memory when processing an IRP\_MN\_SET\_POWER request for a **SystemPowerState** transition that goes from s0 to \[S1...S5\].

This rule only applies to FDO and FIDO drivers.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>PowerDownAllocate</strong> rule.</p>
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

[**ExAllocatePoolWithTag**](https://msdn.microsoft.com/library/windows/hardware/ff544520)
[**IoAcquireRemoveLock**](https://msdn.microsoft.com/library/windows/hardware/ff548204)
 

 





