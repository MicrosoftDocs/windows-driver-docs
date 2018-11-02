---
title: NonPnPDrvPowerPolicyOwnerAPI rule (kmdf)
description: The NonPnPDrvPowerPolicyOwnerAPI rule specifies that non-PnP drivers cannot call certain DDIs related to power management.
ms.assetid: d15211d2-cf53-4b60-bd26-a6c82d50bd42
ms.date: 05/21/2018
keywords: ["NonPnPDrvPowerPolicyOwnerAPI rule (kmdf)"]
topic_type:
- apiref
api_name:
- NonPnPDrvPowerPolicyOwnerAPI
api_type:
- NA
ms.localizationpriority: medium
---

# NonPnPDrvPowerPolicyOwnerAPI rule (kmdf)


The **NonPnPDrvPowerPolicyOwnerAPI** rule specifies that non-PnP drivers cannot call certain DDIs related to power management.

If the driver does not register the [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback function, the following DDIs cannot be called:

[**WdfDeviceAssignS0IdleSettings**](https://msdn.microsoft.com/library/windows/hardware/ff545903)
[**WdfDeviceInitSetPowerPolicyEventCallbacks**](https://msdn.microsoft.com/library/windows/hardware/ff546774)
[**WdfDeviceAssignSxWakeSettings**](https://msdn.microsoft.com/library/windows/hardware/ff545909)
[**WdfDeviceGetDevicePowerState**](https://msdn.microsoft.com/library/windows/hardware/ff545985)
[**WdfDeviceGetDevicePowerPolicyState**](https://msdn.microsoft.com/library/windows/hardware/ff545974)
[**WdfDeviceInitSetPnpPowerEventCallbacks**](https://msdn.microsoft.com/library/windows/hardware/ff546135)
[**WdfDeviceInitSetPowerPolicyOwnership**](https://msdn.microsoft.com/library/windows/hardware/ff546776)
[**WdfDeviceInitRegisterPowerStateChangeCallback**](https://msdn.microsoft.com/library/windows/hardware/ff546071)
[**WdfDeviceInitRegisterPowerPolicyStateChangeCallback**](https://msdn.microsoft.com/library/windows/hardware/ff546066)
[**WdfDeviceInitSetPowerNotPageable**](https://msdn.microsoft.com/library/windows/hardware/ff546147)
[**WdfDeviceInitSetPowerPageable**](https://msdn.microsoft.com/library/windows/hardware/ff546766)
[**WdfDeviceInitSetPowerInrush**](https://msdn.microsoft.com/library/windows/hardware/ff546142)
[**WdfDeviceSetPowerCapabilities**](https://msdn.microsoft.com/library/windows/hardware/ff546901)

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
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff552808" data-raw-source="[Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808)">Static Driver Verifier</a> and specify the <strong>NonPnPDrvPowerPolicyOwnerAPI</strong> rule.</p>
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









