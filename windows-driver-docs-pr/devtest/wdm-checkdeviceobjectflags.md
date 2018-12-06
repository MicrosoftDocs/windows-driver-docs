---
title: CheckDeviceObjectFlags rule (wdm)
description: The CheckDeviceObjectFlags rule specifies that a bus driver must check that the device object flags for DO\_POWER\_PAGABLE and DO\_POWER\_INRUSH are set consistently for the FDO and the child PDOs. This rule only applies to bus drivers.
ms.assetid: E229D3A2-30CE-433A-9889-F762CA923803
ms.date: 05/21/2018
keywords: ["CheckDeviceObjectFlags rule (wdm)"]
topic_type:
- apiref
api_name:
- CheckDeviceObjectFlags
api_type:
- NA
ms.localizationpriority: medium
---

# CheckDeviceObjectFlags rule (wdm)


The **CheckDeviceObjectFlags** rule specifies that a bus driver must check that the device object flags for DO\_POWER\_PAGABLE and DO\_POWER\_INRUSH are set consistently for the FDO and the child PDOs. This rule only applies to bus drivers.

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
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff552808" data-raw-source="[Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808)">Static Driver Verifier</a> and specify the <strong>CheckDeviceObjectFlags</strong> rule.</p>
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

[**ExAllocatePoolWithTag**](https://msdn.microsoft.com/library/windows/hardware/ff544520)
[**IoCreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548397)
 

 





