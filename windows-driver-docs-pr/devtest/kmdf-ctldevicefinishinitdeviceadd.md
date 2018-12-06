---
title: CtlDeviceFinishInitDeviceAdd rule (kmdf)
description: The CtlDeviceFinishInitDeviceAdd rule specifies that if a driver creates control device object in an EvtDriverDeviceAdd callback function, it must call WdfControlFinishInitializing after the device has been created and before it exits from the EvtDriverDeviceAdd callback function. This rule does not apply for non-PnP drivers.
ms.assetid: 162a0013-1215-487c-af72-05e75ef0bdbd
ms.date: 05/21/2018
keywords: ["CtlDeviceFinishInitDeviceAdd rule (kmdf)"]
topic_type:
- apiref
api_name:
- CtlDeviceFinishInitDeviceAdd
api_type:
- NA
ms.localizationpriority: medium
---

# CtlDeviceFinishInitDeviceAdd rule (kmdf)


The **CtlDeviceFinishInitDeviceAdd** rule specifies that if a driver creates control device object in an [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback function, it must call [**WdfControlFinishInitializing**](https://msdn.microsoft.com/library/windows/hardware/ff545854) after the device has been created and before it exits from the **EvtDriverDeviceAdd** callback function. This rule does not apply for non-PnP drivers.

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
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff552808" data-raw-source="[Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808)">Static Driver Verifier</a> and specify the <strong>CtlDeviceFinishInitDeviceAdd</strong> rule.</p>
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

[**WdfControlDeviceInitAllocate**](https://msdn.microsoft.com/library/windows/hardware/ff545841)
[**WdfControlFinishInitializing**](https://msdn.microsoft.com/library/windows/hardware/ff545854)
[**WdfDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/ff545926)
[**WdfObjectDelete**](https://msdn.microsoft.com/library/windows/hardware/ff548734)
 

 





