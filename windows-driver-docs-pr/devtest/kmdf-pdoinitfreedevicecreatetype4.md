---
title: PdoInitFreeDeviceCreateType4 rule (kmdf)
description: The PdoInitFreeDeviceCreateType4 rule specifies that the driver must call WdfDeviceInitFree if an error occurs when the driver calls WdfDeviceCreate.
ms.assetid: 9293f293-7de6-476a-ab35-09174b7b3480
ms.date: 05/21/2018
keywords: ["PdoInitFreeDeviceCreateType4 rule (kmdf)"]
topic_type:
- apiref
api_name:
- PdoInitFreeDeviceCreateType4
api_type:
- NA
ms.localizationpriority: medium
---

# PdoInitFreeDeviceCreateType4 rule (kmdf)


The PdoInitFreeDeviceCreateType4 rule specifies that the driver must call [**WdfDeviceInitFree**](https://msdn.microsoft.com/library/windows/hardware/ff546050) if an error occurs when the driver calls [**WdfDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/ff545926).

If your driver encounters an error when it calls [**WdfDriverCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547175), and if the driver received the [WDFDEVICE\_INIT](https://msdn.microsoft.com/library/windows/hardware/ff546951) structure from a call to [**WdfPdoInitAllocate**](https://msdn.microsoft.com/library/windows/hardware/ff548786), the driver must call [**WdfDeviceInitFree**](https://msdn.microsoft.com/library/windows/hardware/ff546050).

|              |      |
|--------------|------|
| Driver model | KMDF |

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
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff552808" data-raw-source="[Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808)">Static Driver Verifier</a> and specify the <strong>PdoInitFreeDeviceCreateType4</strong> rule.</p>
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

[**WdfDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/ff545926)
[**WdfDeviceInitFree**](https://msdn.microsoft.com/library/windows/hardware/ff546050)
[**WdfPdoInitAllocate**](https://msdn.microsoft.com/library/windows/hardware/ff548786)
 

 





