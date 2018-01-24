---
title: SpinLockSafe rule (wdm)
description: The SpinLockSafe rule specifies that IoStartNextPacket and IoCompleteRequest are not called while holding a spin lock.
ms.assetid: 64a18cb0-80a3-4830-a5b0-131fc1ebdf60
keywords: ["SpinLockSafe rule (wdm)"]
topic_type:
- apiref
api_name:
- SpinLockSafe
api_type:
- NA
---

# SpinLockSafe rule (wdm)


The **SpinLockSafe** rule specifies that [**IoStartNextPacket**](https://msdn.microsoft.com/library/windows/hardware/ff550358) and [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343) are not called while holding a spin lock.

This rule also specifies that the driver calls [**KeAcquireSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff551917) or [**KeAcquireSpinLockAtDpcLevel**](https://msdn.microsoft.com/library/windows/hardware/ff551921) before calling [**KeReleaseSpinLockFromDpcLevel**](https://msdn.microsoft.com/library/windows/hardware/ff553150) or [**KeReleaseSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff553145), and that it calls [**IoAcquireCancelSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff548196) before calling [**IoReleaseCancelSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff549550).

Static Driver Verifier can report false violations of this rule if the driver includes nested SpinLocks, even if those spin locks are acquired and released correctly.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>SpinLockSafe</strong> rule.</p>
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
[**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343)
[**IoReleaseCancelSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff549550)
[**IoStartNextPacket**](https://msdn.microsoft.com/library/windows/hardware/ff550358)
[**KeAcquireSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff551917)
[**KeAcquireSpinLockRaiseToDpc**](https://msdn.microsoft.com/library/windows/hardware/ff551928)
[**KeReleaseSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff553145)
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20SpinLockSafe%20rule%20%28wdm%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




