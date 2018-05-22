---
title: CheckDeviceObjectFlags rule (wdm)
description: The CheckDeviceObjectFlags rule specifies that a bus driver must check that the device object flags for DO\_POWER\_PAGABLE and DO\_POWER\_INRUSH are set consistently for the FDO and the child PDOs. This rule only applies to bus drivers.
ms.assetid: E229D3A2-30CE-433A-9889-F762CA923803
ms.author: windowsdriverdev
ms.date: 5/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["CheckDeviceObjectFlags rule (wdm)"]
topic_type:
- apiref
api_name:
- CheckDeviceObjectFlags
api_type:
- NA
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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>CheckDeviceObjectFlags</strong> rule.</p>
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
[**IoCreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548397)
 

 





