---
title: CtlDeviceFinishInitDrEntry rule (kmdf)
description: The CtlDeviceFinishInitDrEntry rule specifies that if a driver creates a control device object in a DriverEntry callback function, it must call WdfControlFinishInitializing after the device has been created and before it exits from the EvtDriverDeviceAdd callback function. This rule does not apply for non-PnP drivers.
ms.assetid: b6470bc1-c4db-4b46-b83b-edcf4da56087
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["CtlDeviceFinishInitDrEntry rule (kmdf)"]
topic_type:
- apiref
api_name:
- CtlDeviceFinishInitDrEntry
api_type:
- NA
ms.localizationpriority: medium
---

# CtlDeviceFinishInitDrEntry rule (kmdf)


The CtlDeviceFinishInitDrEntry rule specifies that if a driver creates a control device object in a [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff540807) callback function, it must call [**WdfControlFinishInitializing**](https://msdn.microsoft.com/library/windows/hardware/ff545854) after the device has been created and before it exits from the [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback function. This rule does not apply for non-PnP drivers.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>CtlDeviceFinishInitDrEntry</strong> rule.</p>
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

[**WdfControlDeviceInitAllocate**](https://msdn.microsoft.com/library/windows/hardware/ff545841)
[**WdfControlFinishInitializing**](https://msdn.microsoft.com/library/windows/hardware/ff545854)
[**WdfDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/ff545926)
[**WdfObjectDelete**](https://msdn.microsoft.com/library/windows/hardware/ff548734)
 

 





