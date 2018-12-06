---
title: AddDevice rule (wdm)
description: The AddDevice rule specifies that the driver's AddDevice routine calls IoAttachDeviceToDeviceStack only after calling IoCreateDevice.
ms.assetid: 6379633a-194f-45b8-8c21-85eecf300aeb
ms.date: 05/21/2018
keywords: ["AddDevice rule (wdm)"]
topic_type:
- apiref
api_name:
- AddDevice
api_type:
- NA
ms.localizationpriority: medium
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
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff552808" data-raw-source="[Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808)">Static Driver Verifier</a> and specify the <strong>AddDevice</strong> rule.</p>
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

[**IoAttachDeviceToDeviceStack**](https://msdn.microsoft.com/library/windows/hardware/ff548300)
[**IoCreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548397)
 

 





