---
title: PdoInitFreeDeviceCreateType4 rule (kmdf)
description: The PdoInitFreeDeviceCreateType4 rule specifies that the driver must call WdfDeviceInitFree if an error occurs when the driver calls WdfDeviceCreate.
ms.assetid: 9293f293-7de6-476a-ab35-09174b7b3480
ms.author: windowsdriverdev
ms.date: 5/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["PdoInitFreeDeviceCreateType4 rule (kmdf)"]
topic_type:
- apiref
api_name:
- PdoInitFreeDeviceCreateType4
api_type:
- NA
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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>PdoInitFreeDeviceCreateType4</strong> rule.</p>
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

[**WdfDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/ff545926)
[**WdfDeviceInitFree**](https://msdn.microsoft.com/library/windows/hardware/ff546050)
[**WdfPdoInitAllocate**](https://msdn.microsoft.com/library/windows/hardware/ff548786)
 

 





