---
title: PdoInitFreeDeviceCreate rule (kmdf)
description: The PdoInitFreeDeviceCreate rule specifies that a driver must call WdfDeviceInitFree instead of WdfDeviceCreate if an error occurs in one of the device object initialization functions and if the driver received the WDFDEVICE\_INIT structure from a call to WdfPdoInitAllocate.
ms.assetid: d73401dd-ec96-4870-9f6d-aa399deab173
keywords: ["PdoInitFreeDeviceCreate rule (kmdf)"]
topic_type:
- apiref
api_name:
- PdoInitFreeDeviceCreate
api_type:
- NA
---

# PdoInitFreeDeviceCreate rule (kmdf)


The **PdoInitFreeDeviceCreate** rule specifies that a driver must call [**WdfDeviceInitFree**](https://msdn.microsoft.com/library/windows/hardware/ff546050) instead of [**WdfDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/ff545926) if an error occurs in one of the device object initialization functions and if the driver received the WDFDEVICE\_INIT structure from a call to [**WdfPdoInitAllocate**](https://msdn.microsoft.com/library/windows/hardware/ff548786).

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>PdoInitFreeDeviceCreate</strong> rule.</p>
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
[**WdfDeviceInitFree**](https://msdn.microsoft.com/library/windows/hardware/ff546050)
[**WdfDeviceInitRegisterPnpStateChangeCallback**](https://msdn.microsoft.com/library/windows/hardware/ff546057)
[**WdfDeviceInitRegisterPowerPolicyStateChangeCallback**](https://msdn.microsoft.com/library/windows/hardware/ff546066)
[**WdfDeviceInitRegisterPowerStateChangeCallback**](https://msdn.microsoft.com/library/windows/hardware/ff546071)
[**WdfPdoInitAddCompatibleID**](https://msdn.microsoft.com/library/windows/hardware/ff548776)
[**WdfPdoInitAddDeviceText**](https://msdn.microsoft.com/library/windows/hardware/ff548780)
[**WdfPdoInitAddHardwareID**](https://msdn.microsoft.com/library/windows/hardware/ff548784)
[**WdfPdoInitAllocate**](https://msdn.microsoft.com/library/windows/hardware/ff548786)
[**WdfPdoInitAssignDeviceID**](https://msdn.microsoft.com/library/windows/hardware/ff548797)
[**WdfPdoInitAssignInstanceID**](https://msdn.microsoft.com/library/windows/hardware/ff548799)
[**WdfPdoInitAssignRawDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548802)
See also
--------

[**InitFreeDeviceCallback**](kmdf-initfreedevicecallback.md)
[**InitFreeDeviceCreate**](kmdf-initfreedevicecreate.md)
[**InitFreeDeviceCreateType2**](kmdf-initfreedevicecreatetype2.md)
[**PdoInitFreeDeviceCreateType2**](kmdf-pdoinitfreedevicecreatetype2.md)
[**InitFreeDeviceCreateType4**](kmdf-initfreedevicecreatetype4.md)
[**PdoInitFreeDeviceCallback**](kmdf-pdoinitfreedevicecallback.md)
[**PdoInitFreeDeviceCreateType4**](kmdf-pdoinitfreedevicecreatetype4.md)
[**InitFreeNull**](kmdf-initfreenull.md)
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20PdoInitFreeDeviceCreate%20rule%20%28kmdf%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




