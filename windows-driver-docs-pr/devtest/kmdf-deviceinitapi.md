---
title: DeviceInitAPI rule (kmdf)
description: For an FDO device, the framework device object initialization methods and the framework FDO initialization methods must be called before the driver calls the WdfDeviceCreate method for the device object.
ms.assetid: 526807b8-748e-4bc1-b795-9971ed98509c
keywords: ["DeviceInitAPI rule (kmdf)"]
topic_type:
- apiref
api_name:
- DeviceInitAPI
api_type:
- NA
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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>DeviceInitAPI</strong> rule.</p>
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
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20DeviceInitAPI%20rule%20%28kmdf%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




