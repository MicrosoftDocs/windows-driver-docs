---
title: MiniportOnlyWdmDevice rule (kmdf)
description: The MiniportOnlyWdmDevice rule specifies that WDF drivers should not use IoCreateDevice and IoCreateDeviceSecure functions to create bare WDM device objects.
ms.assetid: 23B9431E-3932-42F3-B797-0820D9A43295
ms.date: 05/21/2018
keywords: ["MiniportOnlyWdmDevice rule (kmdf)"]
topic_type:
- apiref
api_name:
- MiniportOnlyWdmDevice
api_type:
- NA
ms.localizationpriority: medium
---

# MiniportOnlyWdmDevice rule (kmdf)


The **MiniportOnlyWdmDevice** rule specifies that WDF drivers should not use [**IoCreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548397) and [**IoCreateDeviceSecure**](https://msdn.microsoft.com/library/windows/hardware/ff548407) functions to create bare WDM device objects. This will cause a the computer to crash if someone tries to send an IRP to the WDM device. This is because IRP dispatch entries of the device are set to WDF-specific entries, but the framework hasn’t created a WDF device. However, miniport drivers can use the DDIs because driver dispatch entry points aren’t set for them.

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
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff552808" data-raw-source="[Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808)">Static Driver Verifier</a> and specify the <strong>MiniportOnlyWdmDevice</strong> rule.</p>
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

[**WdfDriverCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547175)
[**IoCreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548397)
[**IoCreateDeviceSecure**](https://msdn.microsoft.com/library/windows/hardware/ff548407)
 

 





