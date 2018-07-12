---
title: AccessHardwareKey rule (kmdf)
description: The AccessHardwareKey rule specifies that a bus driver should not try to access the hardware key of a child device from EvtChildListCreateDevice.
ms.assetid: D5A03DC2-65C9-42A2-A718-CFDE1ED040E7
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["AccessHardwareKey rule (kmdf)"]
topic_type:
- apiref
api_name:
- AccessHardwareKey
api_type:
- NA
---

# AccessHardwareKey rule (kmdf)


The **AccessHardwareKey** rule specifies that a bus driver should not try to access the hardware key of a child device from [*EvtChildListCreateDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540828).

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>AccessHardwareKey</strong> rule.</p>
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
[**WdfDeviceOpenRegistryKey**](https://msdn.microsoft.com/library/windows/hardware/ff546804)
 

 





