---
title: CancelSpinLock rule (wdm)
description: The CancelSpinLock rule specifies that the driver calls IoAcquireCancelSpinLock before calling IoReleaseCancelSpinLock and that the driver calls IoReleaseCancelSpinLock before any subsequent calls to IoAcquireCancelSpinLock.
ms.assetid: 8f21a70f-a82b-4b2b-abff-892a1950da41
keywords: ["CancelSpinLock rule (wdm)"]
topic_type:
- apiref
api_name:
- CancelSpinLock
api_type:
- NA
---

# CancelSpinLock rule (wdm)


The CancelSpinLock rule specifies that the driver calls [**IoAcquireCancelSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff548196) before calling [**IoReleaseCancelSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff549550) and that the driver calls **IoReleaseCancelSpinLock** before any subsequent calls to **IoAcquireCancelSpinLock**.

This rule also specifies that the driver must not hold any spin locks when the dispatch routine or cancel routine ends. Nested calls are permitted.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>CancelSpinLock</strong> rule.</p>
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

[**IoAcquireCancelSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff548196)
[**IoReleaseCancelSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff549550)
[**RemoveHeadList**](https://msdn.microsoft.com/library/windows/hardware/ff561032)
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20CancelSpinLock%20rule%20%28wdm%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




