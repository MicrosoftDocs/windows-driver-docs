---
title: ControlDeviceInitAPI rule (kmdf)
description: The ControlDeviceInitAPI rule specifies that WdfControlDeviceInitAllocate and all other device object initialization DDIs that set up a WDFDEVICE\_INIT structure for the control device must be called before WdfDeviceCreate for the control device.
ms.assetid: 136ee6d8-d104-4ae8-a3f7-d93179808e29
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
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20ControlDeviceInitAPI%20rule%20%28kmdf%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




