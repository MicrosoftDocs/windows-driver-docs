---
title: AddDevice rule (wdm)
description: The AddDevice rule specifies that the driver's AddDevice routine calls IoAttachDeviceToDeviceStack only after calling IoCreateDevice.
ms.assetid: 6379633a-194f-45b8-8c21-85eecf300aeb
keywords: ["AddDevice rule (wdm)"]
topic_type:
- apiref
api_name:
- AddDevice
api_type:
- NA
---

# AddDevice rule (wdm)


The **AddDevice** rule specifies that the driver's [**AddDevice**](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine calls [**IoAttachDeviceToDeviceStack**](https://msdn.microsoft.com/library/windows/hardware/ff548300) only after calling [**IoCreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548397).

This rule applies only to drivers that have an [*AddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine.

This rule does not verify that the driver calls **IoCreateDevice** or **IoAttachDeviceToDeviceStack** and does not monitor calls to [**IoCreateDeviceSecure**](https://msdn.microsoft.com/library/windows/hardware/ff548407).

|              |     |
|--------------|-----|
| Driver model | WDM |

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>AddDevice</strong> rule.</p>
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

[**IoAttachDeviceToDeviceStack**](https://msdn.microsoft.com/library/windows/hardware/ff548300)
[**IoCreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548397)
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20AddDevice%20rule%20%28wdm%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




