---
title: MarkDevicePower rule (wdm)
description: The MarkDevicePower rule specifies that an IRP\_MJ\_POWER with IRP\_MN\_SET\_POWER for SystemPowerState IRP going to S0 is pended.
ms.assetid: 5B46FF9C-C955-4D10-86FB-17BDC57E17B6
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>MarkDevicePower</strong> rule.</p>
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

[**IoAcquireRemoveLock**](https://msdn.microsoft.com/library/windows/hardware/ff548204)
[**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336)
[**IoMarkIrpPending**](https://msdn.microsoft.com/library/windows/hardware/ff549422)
[**PoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff559654)
[**PoRequestPowerIrp**](https://msdn.microsoft.com/library/windows/hardware/ff559734)
 

 





