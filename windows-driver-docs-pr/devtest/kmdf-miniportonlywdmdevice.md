---
title: MiniportOnlyWdmDevice rule (kmdf)
description: The MiniportOnlyWdmDevice rule specifies that WDF drivers should not use IoCreateDevice and IoCreateDeviceSecure functions to create bare WDM device objects.
ms.assetid: 23B9431E-3932-42F3-B797-0820D9A43295
ms.author: windowsdriverdev
ms.date: 5/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["MiniportOnlyWdmDevice rule (kmdf)"]
topic_type:
- apiref
api_name:
- MiniportOnlyWdmDevice
api_type:
- NA
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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>MiniportOnlyWdmDevice</strong> rule.</p>
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

[**WdfDriverCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547175)
[**IoCreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548397)
[**IoCreateDeviceSecure**](https://msdn.microsoft.com/library/windows/hardware/ff548407)
 

 





