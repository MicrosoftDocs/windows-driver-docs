---
title: StartIoCancel rule (wdm)
description: The StartIoCancel rule specifies that the driver must not call IoSetStartIoAttributes with the NonCancelable parameter set to FALSE before calling IoSetCancelRoutine with a non-NULLCancel routine.
ms.assetid: 08fde0b1-4f4e-473a-9e07-3b39683a3a1b
keywords: ["StartIoCancel rule (wdm)"]
topic_type:
- apiref
api_name:
- StartIoCancel
api_type:
- NA
---

# StartIoCancel rule (wdm)


The **StartIoCancel** rule specifies that the driver must not call [**IoSetStartIoAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff550330) with the *NonCancelable* parameter set to **FALSE** before calling [**IoSetCancelRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff549674) with a non-**NULL**[**Cancel**](https://msdn.microsoft.com/library/windows/hardware/ff540742) routine.

Setting the *NonCancelable* parameter to **FALSE** before registering the [**Cancel**](https://msdn.microsoft.com/library/windows/hardware/ff540742) routine can result in a cancellation race condition.

Because a driver's [**Cancel**](https://msdn.microsoft.com/library/windows/hardware/ff540742) routine must include a call to [**IoReleaseCancelSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff549550) (to release the spin lock that the I/O Manager acquires before calling the **Cancel** routine), consider verifying your driver with both the **StartIoCancel** rule and the [**CancelSpinLock**](wdm-cancelspinlock.md) rule.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>StartIoCancel</strong> rule.</p>
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

[**IoSetCancelRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff549674)
[**IoSetStartIoAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff550330)
See also
--------

[**CancelSpinLock**](wdm-cancelspinlock.md)
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20StartIoCancel%20rule%20%28wdm%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




