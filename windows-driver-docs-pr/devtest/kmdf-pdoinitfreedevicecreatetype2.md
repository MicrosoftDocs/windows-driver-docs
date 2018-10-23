---
title: PdoInitFreeDeviceCreateType2 rule (kmdf)
description: The PdoInitFreeDeviceCreateType2 rule specifies that a driver must not call WdfDeviceCreate after it calls WdfDeviceInitFree.
ms.assetid: 0e5c9a97-7bc9-43c7-8bc7-a252e1a1b3d0
ms.date: 05/21/2018
keywords: ["PdoInitFreeDeviceCreateType2 rule (kmdf)"]
topic_type:
- apiref
api_name:
- PdoInitFreeDeviceCreateType2
api_type:
- NA
ms.localizationpriority: medium
---

# PdoInitFreeDeviceCreateType2 rule (kmdf)


The PdoInitFreeDeviceCreateType2 rule specifies that a driver must not call [**WdfDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/ff545926) after it calls [**WdfDeviceInitFree**](https://msdn.microsoft.com/library/windows/hardware/ff546050).

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>PdoInitFreeDeviceCreateType2</strong> rule.</p>
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
 

 





