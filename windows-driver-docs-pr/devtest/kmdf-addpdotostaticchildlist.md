---
title: AddPdotoStaticChildlist rule (kmdf)
description: The AddPdotoStaticChildlist rule specifies that for a PDO device, the framework function WdfFdoAddStaticChild must be called after the driver calls WdfPdoInitAllocate and WdfDeviceCreate successfully.
ms.assetid: 31ECB3D2-1EAC-484A-8C3A-DF94AC473334
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["AddPdotoStaticChildlist rule (kmdf)"]
topic_type:
- apiref
api_name:
- AddPdotoStaticChildlist
api_type:
- NA
ms.localizationpriority: medium
---

# AddPdotoStaticChildlist rule (kmdf)


The AddPdotoStaticChildlist rule specifies that for a PDO device, the framework function [**WdfFdoAddStaticChild**](https://msdn.microsoft.com/library/windows/hardware/ff547225) must be called after the driver calls [**WdfPdoInitAllocate**](https://msdn.microsoft.com/library/windows/hardware/ff548786) and [**WdfDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/ff545926) successfully.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>AddPdotoStaticChildlist</strong> rule.</p>
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
[**WdfFdoAddStaticChild**](https://msdn.microsoft.com/library/windows/hardware/ff547225)
[**WdfObjectDelete**](https://msdn.microsoft.com/library/windows/hardware/ff548734)
[**WdfPdoInitAllocate**](https://msdn.microsoft.com/library/windows/hardware/ff548786)
 

 





