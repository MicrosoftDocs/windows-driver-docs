---
title: DeviceInitAPI rule (kmdf)
description: For an FDO device, the framework device object initialization methods and the framework FDO initialization methods must be called before the driver calls the WdfDeviceCreate method for the device object.
ms.assetid: 526807b8-748e-4bc1-b795-9971ed98509c
ms.date: 05/21/2018
keywords: ["DeviceInitAPI rule (kmdf)"]
topic_type:
- apiref
api_name:
- DeviceInitAPI
api_type:
- NA
ms.localizationpriority: medium
---

# DeviceInitAPI rule (kmdf)


For an FDO device, the framework device object initialization methods and the framework FDO initialization methods must be called before the driver calls the [**WdfDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/ff545926) method for the device object.

For an FDO device, the framework device object initialization methods and framework FDO initialization methods, which store information in the [WDFDEVICE\_INIT](https://msdn.microsoft.com/library/windows/hardware/ff546951) structure, cannot be called after the driver calls [**WdfDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/ff545926) for the framework device object.

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
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff552808" data-raw-source="[Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808)">Static Driver Verifier</a> and specify the <strong>DeviceInitAPI</strong> rule.</p>
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
[**WdfDeviceInitAssignName**](https://msdn.microsoft.com/library/windows/hardware/ff546029)
[**WdfDeviceInitAssignSDDLString**](https://msdn.microsoft.com/library/windows/hardware/ff546035)
[**WdfDeviceInitAssignWdmIrpPreprocessCallback**](https://msdn.microsoft.com/library/windows/hardware/ff546043)
[**WdfDeviceInitRegisterPnpStateChangeCallback**](https://msdn.microsoft.com/library/windows/hardware/ff546057)
[**WdfDeviceInitRegisterPowerPolicyStateChangeCallback**](https://msdn.microsoft.com/library/windows/hardware/ff546066)
[**WdfDeviceInitRegisterPowerStateChangeCallback**](https://msdn.microsoft.com/library/windows/hardware/ff546071)
[**WdfDeviceInitSetCharacteristics**](https://msdn.microsoft.com/library/windows/hardware/ff546074)
[**WdfDeviceInitSetDeviceClass**](https://msdn.microsoft.com/library/windows/hardware/ff546084)
[**WdfDeviceInitSetDeviceType**](https://msdn.microsoft.com/library/windows/hardware/ff546090)
[**WdfDeviceInitSetExclusive**](https://msdn.microsoft.com/library/windows/hardware/ff546097)
[**WdfDeviceInitSetFileObjectConfig**](https://msdn.microsoft.com/library/windows/hardware/ff546107)
[**WdfDeviceInitSetIoInCallerContextCallback**](https://msdn.microsoft.com/library/windows/hardware/ff546119)
[**WdfDeviceInitSetIoType**](https://msdn.microsoft.com/library/windows/hardware/ff546128)
[**WdfDeviceInitSetPnpPowerEventCallbacks**](https://msdn.microsoft.com/library/windows/hardware/ff546135)
[**WdfDeviceInitSetPowerInrush**](https://msdn.microsoft.com/library/windows/hardware/ff546142)
[**WdfDeviceInitSetPowerNotPageable**](https://msdn.microsoft.com/library/windows/hardware/ff546147)
[**WdfDeviceInitSetPowerPageable**](https://msdn.microsoft.com/library/windows/hardware/ff546766)
[**WdfDeviceInitSetPowerPolicyEventCallbacks**](https://msdn.microsoft.com/library/windows/hardware/ff546774)
[**WdfDeviceInitSetPowerPolicyOwnership**](https://msdn.microsoft.com/library/windows/hardware/ff546776)
[**WdfDeviceInitSetRequestAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff546786)
[**WdfFdoInitAllocAndQueryProperty**](https://msdn.microsoft.com/library/windows/hardware/ff547239)
[**WdfFdoInitOpenRegistryKey**](https://msdn.microsoft.com/library/windows/hardware/ff547249)
[**WdfFdoInitQueryProperty**](https://msdn.microsoft.com/library/windows/hardware/ff547254)
[**WdfFdoInitSetDefaultChildListConfig**](https://msdn.microsoft.com/library/windows/hardware/ff547258)
[**WdfFdoInitSetEventCallbacks**](https://msdn.microsoft.com/library/windows/hardware/ff547268)
[**WdfFdoInitSetFilter**](https://msdn.microsoft.com/library/windows/hardware/ff547273)
[**WdfFdoInitWdmGetPhysicalDevice**](https://msdn.microsoft.com/library/windows/hardware/ff547281)
 

 





