---
title: WmiForward rule (wdm)
description: The WmiForward rule specifies that the driver must forward WMI minor IRPs when forwarding is required.
ms.assetid: c62f37d2-ebd5-4705-9590-d1bf17137802
keywords: ["WmiForward rule (wdm)"]
topic_type:
- apiref
api_name:
- WmiForward
api_type:
- NA
---

# WmiForward rule (wdm)


The **WmiForward** rule specifies that the driver must forward [**WMI minor IRPs**](https://msdn.microsoft.com/library/windows/hardware/ff566361) when forwarding is required.

Specifically, when the driver calls [**WmiSystemControl**](https://msdn.microsoft.com/library/windows/hardware/ff565834) and the value of the *IrpDisposition* parameter is **IrpForward**, the driver must call [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336) or [**PoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff559654) to forward the IRP before returning from the dispatch routine.

This rule does not apply to bus drivers.

A *WMI minor IRP* is an [**IRP\_MJ\_SYSTEM\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550813) request with a WMI minor function code.

For more information about processing WMI minor IRPs, see [**WMI Requirements for WDM Drivers**](https://msdn.microsoft.com/library/windows/hardware/ff566370), [**Handling WMI Requests**](https://msdn.microsoft.com/library/windows/hardware/ff546968), [**Windows Management Instrumentation Routines**](https://msdn.microsoft.com/library/windows/hardware/ff565794), and [**WMI Library Support Routines**](https://msdn.microsoft.com/library/windows/hardware/ff566359).

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>WmiForward</strong> rule.</p>
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

[**IoAcquireRemoveLock**](https://msdn.microsoft.com/library/windows/hardware/ff548204)
[**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336)
[**PoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff559654)
See also
--------

[**WMI Requirements for WDM Drivers**](https://msdn.microsoft.com/library/windows/hardware/ff566370)
[**Handling WMI Requests**](https://msdn.microsoft.com/library/windows/hardware/ff546968)
[**WMI Library Support Routines**](https://msdn.microsoft.com/library/windows/hardware/ff566359)
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20WmiForward%20rule%20%28wdm%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




