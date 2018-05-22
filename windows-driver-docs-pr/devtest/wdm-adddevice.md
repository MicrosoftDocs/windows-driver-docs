---
title: AddDevice rule (wdm)
description: The AddDevice rule specifies that the driver's AddDevice routine calls IoAttachDeviceToDeviceStack only after calling IoCreateDevice.
ms.assetid: 6379633a-194f-45b8-8c21-85eecf300aeb
ms.author: windowsdriverdev
ms.date: 5/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["AddDevice rule (wdm)"]
topic_type:
- apiref
api_name:
- AddDevice
api_type:
- NA
---

# AddDevice rule (wdm)


The **AddDevice** rule specifies that the driver's [**AddDevice**](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine calls [**IoAttachDeviceToDeviceStack**](https://msdn.microsoft.com/library/windows/hardware/ff548300) only after calling [**IoCreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548397).

This rule applies only to drivers that have an [*AddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine.

This rule does not verify that the driver calls **IoCreateDevice** or **IoAttachDeviceToDeviceStack** and does not monitor calls to [**IoCreateDeviceSecure**](https://msdn.microsoft.com/library/windows/hardware/ff548407).

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>AddDevice</strong> rule.</p>
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

[**IoAttachDeviceToDeviceStack**](https://msdn.microsoft.com/library/windows/hardware/ff548300)
[**IoCreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548397)
 

 





