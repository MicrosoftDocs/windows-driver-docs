---
title: ControlDeviceDeleted rule (kmdf)
description: The ControDeviceDeleted rule specifies that if a PnP driver creates a control device object, the driver must delete the control device object in one of the cleanup callback functions before the driver unloads.
ms.assetid: 869f1c1c-8a9f-4e0b-bcbb-386e93663567
ms.date: 05/21/2018
keywords: ["ControlDeviceDeleted rule (kmdf)"]
topic_type:
- apiref
api_name:
- ControlDeviceDeleted
api_type:
- NA
ms.localizationpriority: medium
---

# ControlDeviceDeleted rule (kmdf)


The ControDeviceDeleted rule specifies that if a PnP driver creates a control device object, the driver must delete the control device object in one of the cleanup callback functions before the driver unloads.

If an FDO or filter driver calls [**WdfDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/ff545926) for the control device object, the driver must call [**WdfObjectDelete**](https://msdn.microsoft.com/library/windows/hardware/ff548734) for the control device object from the driver's cleanup callback function for the WDFDEVICE object, the destroy callback function for WDFDEVICE object, or the [*EvtDeviceSelfManagedIoCleanup*](https://msdn.microsoft.com/library/windows/hardware/ff540898) event callback function.

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
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff552808" data-raw-source="[Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808)">Static Driver Verifier</a> and specify the <strong>ControlDeviceDeleted</strong> rule.</p>
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

[**WdfDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/ff545926)
[**WdfObjectDelete**](https://msdn.microsoft.com/library/windows/hardware/ff548734)
 

 





