---
title: UsbContReader rule (kmdf)
description: The UsbContReader rule specifies that a continuous reader is configured correctly within a driver's EvtDevicePrepareHardware event callback function, where the driver makes a call to the WdfUsbTargetPipeConfigContinuousReader method.
ms.assetid: f9bb885e-2da0-4f4d-ad62-6d450d9a64dd
ms.date: 05/21/2018
keywords: ["UsbContReader rule (kmdf)"]
topic_type:
- apiref
api_name:
- UsbContReader
api_type:
- NA
ms.localizationpriority: medium
---

# UsbContReader rule (kmdf)


The **UsbContReader** rule specifies that a continuous reader is configured correctly within a driver's [*EvtDevicePrepareHardware*](https://msdn.microsoft.com/library/windows/hardware/ff540880) event callback function, where the driver makes a call to the [**WdfUsbTargetPipeConfigContinuousReader**](https://msdn.microsoft.com/library/windows/hardware/ff551130) method.

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
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff552808" data-raw-source="[Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808)">Static Driver Verifier</a> and specify the <strong>UsbContReader</strong> rule.</p>
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

[**WdfUsbTargetPipeConfigContinuousReader**](https://msdn.microsoft.com/library/windows/hardware/ff551130)
 

 





