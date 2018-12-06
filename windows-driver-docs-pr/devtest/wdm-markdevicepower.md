---
title: MarkDevicePower rule (wdm)
description: The MarkDevicePower rule specifies that an IRP\_MJ\_POWER with IRP\_MN\_SET\_POWER for SystemPowerState IRP going to S0 is pended.
ms.assetid: 5B46FF9C-C955-4D10-86FB-17BDC57E17B6
ms.date: 05/21/2018
keywords: ["MarkDevicePower rule (wdm)"]
topic_type:
- apiref
api_name:
- MarkDevicePower
api_type:
- NA
ms.localizationpriority: medium
---

# MarkDevicePower rule (wdm)


The **MarkDevicePower** rule specifies that an IRP\_MJ\_POWER with IRP\_MN\_SET\_POWER for SystemPowerState IRP going to S0 is pended.

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
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff552808" data-raw-source="[Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808)">Static Driver Verifier</a> and specify the <strong>MarkDevicePower</strong> rule.</p>
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

[**IoAcquireRemoveLock**](https://msdn.microsoft.com/library/windows/hardware/ff548204)
[**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336)
[**IoMarkIrpPending**](https://msdn.microsoft.com/library/windows/hardware/ff549422)
[**PoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff559654)
[**PoRequestPowerIrp**](https://msdn.microsoft.com/library/windows/hardware/ff559734)
 

 





