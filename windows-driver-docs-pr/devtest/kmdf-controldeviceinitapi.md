---
title: ControlDeviceInitAPI rule (kmdf)
description: The ControlDeviceInitAPI rule specifies that WdfControlDeviceInitAllocate and all other device object initialization DDIs that set up a WDFDEVICE\_INIT structure for the control device must be called before WdfDeviceCreate for the control device.
ms.assetid: 136ee6d8-d104-4ae8-a3f7-d93179808e29
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["ControlDeviceInitAPI rule (kmdf)"]
topic_type:
- apiref
api_name:
- ControlDeviceInitAPI
api_type:
- NA
---

# ControlDeviceInitAPI rule (kmdf)


The ControlDeviceInitAPI rule specifies that [**WdfControlDeviceInitAllocate**](https://msdn.microsoft.com/library/windows/hardware/ff545841) and all other device object initialization DDIs that set up a [**WDFDEVICE\_INIT**](https://msdn.microsoft.com/library/windows/hardware/ff546951) structure for the control device must be called before [**WdfDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/ff545926) for the control device.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>ControlDeviceInitAPI</strong> rule.</p>
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
[**WdfControlDeviceInitSetShutdownNotification**](https://msdn.microsoft.com/library/windows/hardware/ff545847)
[**WdfDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/ff545926)
[**WdfDeviceInitAssignName**](https://msdn.microsoft.com/library/windows/hardware/ff546029)
[**WdfDeviceInitAssignWdmIrpPreprocessCallback**](https://msdn.microsoft.com/library/windows/hardware/ff546043)
[**WdfDeviceInitSetCharacteristics**](https://msdn.microsoft.com/library/windows/hardware/ff546074)
[**WdfDeviceInitSetDeviceClass**](https://msdn.microsoft.com/library/windows/hardware/ff546084)
[**WdfDeviceInitSetExclusive**](https://msdn.microsoft.com/library/windows/hardware/ff546097)
[**WdfDeviceInitSetFileObjectConfig**](https://msdn.microsoft.com/library/windows/hardware/ff546107)
[**WdfDeviceInitSetIoInCallerContextCallback**](https://msdn.microsoft.com/library/windows/hardware/ff546119)
[**WdfDeviceInitSetIoType**](https://msdn.microsoft.com/library/windows/hardware/ff546128)
[**WdfDeviceInitSetRequestAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff546786)
 

 





