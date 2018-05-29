---
title: IoBuildDeviceControlNoFree rule (wdm)
description: The IoBuildDeviceControlNoFree rule specifies that a driver that calls IoBuildDeviceIoControlRequest must not call IoFreeIrp.
ms.assetid: 36DAB9A8-2B6F-43EE-86CC-97B66FE0AEB8
ms.author: windowsdriverdev
ms.date: 5/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["IoBuildDeviceControlNoFree rule (wdm)"]
topic_type:
- apiref
api_name:
- IoBuildDeviceControlNoFree
api_type:
- NA
---

# IoBuildDeviceControlNoFree rule (wdm)


The **IoBuildDeviceControlNoFree** rule specifies that a driver that calls [**IoBuildDeviceIoControlRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548318) must not call [**IoFreeIrp**](https://msdn.microsoft.com/library/windows/hardware/ff549113).

A driver that calls [**IoBuildDeviceIoControlRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548318) must not call [**IoFreeIrp**](https://msdn.microsoft.com/library/windows/hardware/ff549113) because the I/O manager frees these synchronous IRPs after [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343) has been called.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>IoBuildDeviceControlNoFree</strong> rule.</p>
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

[**IoBuildDeviceIoControlRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548318)
[**IoFreeIrp**](https://msdn.microsoft.com/library/windows/hardware/ff549113)
 

 





