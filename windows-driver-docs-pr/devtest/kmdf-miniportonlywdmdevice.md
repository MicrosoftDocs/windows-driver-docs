---
title: MiniportOnlyWdmDevice rule (kmdf)
description: The MiniportOnlyWdmDevice rule specifies that WDF drivers should not use IoCreateDevice and IoCreateDeviceSecure functions to create bare WDM device objects.
ms.assetid: 23B9431E-3932-42F3-B797-0820D9A43295
keywords: ["MiniportOnlyWdmDevice rule (kmdf)"]
topic_type:
- apiref
api_name:
- MiniportOnlyWdmDevice
api_type:
- NA
---

# MiniportOnlyWdmDevice rule (kmdf)


The **MiniportOnlyWdmDevice** rule specifies that WDF drivers should not use [**IoCreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548397) and [**IoCreateDeviceSecure**](https://msdn.microsoft.com/library/windows/hardware/ff548407) functions to create bare WDM device objects. This will cause a the computer to crash if someone tries to send an IRP to the WDM device. This is because IRP dispatch entries of the device are set to WDF-specific entries, but the framework hasn’t created a WDF device. However, miniport drivers can use the DDIs because driver dispatch entry points aren’t set for them.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>MiniportOnlyWdmDevice</strong> rule.</p>
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

[**WdfDriverCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547175)
[**IoCreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548397)
[**IoCreateDeviceSecure**](https://msdn.microsoft.com/library/windows/hardware/ff548407)
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20MiniportOnlyWdmDevice%20rule%20%28kmdf%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




