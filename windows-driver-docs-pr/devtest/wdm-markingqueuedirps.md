---
title: MarkingQueuedIrps rule (wdm)
description: The MarkingQueuedIrps rule specifies that the driver calls IoMarkIrpPending for an IRP that requires further processing only while holding a spin lock. This rule applies only when the driver adds the IRP to a driver-managed queue.
ms.assetid: 3a70ba52-c62f-4574-9a2e-4ba7aed82529
keywords: ["MarkingQueuedIrps rule (wdm)"]
topic_type:
- apiref
api_name:
- MarkingQueuedIrps
api_type:
- NA
---

# MarkingQueuedIrps rule (wdm)


The **MarkingQueuedIrps** rule specifies that the driver calls [**IoMarkIrpPending**](https://msdn.microsoft.com/library/windows/hardware/ff549422) for an IRP that requires further processing only while holding a spin lock. This rule applies only when the driver adds the IRP to a driver-managed queue.

Specifically, the driver violates this rule only when *all* of the following events occur.

-   The driver calls [**KeAcquireSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff551917) or [**KeAcquireInStackQueuedSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff551899) to acquire a spin lock.

-   The driver calls one of the following routines to add an IRP to a driver-managed queue:
    -   [**InsertHeadList**](https://msdn.microsoft.com/library/windows/hardware/ff547820)
    -   [**InsertTailList**](https://msdn.microsoft.com/library/windows/hardware/ff547823)
    -   [**KeInsertDeviceQueue**](https://msdn.microsoft.com/library/windows/hardware/ff552180)
    -   [**KeInsertQueueDpc**](https://msdn.microsoft.com/library/windows/hardware/ff552185)
    -   [**KeInsertByKeyDeviceQueue**](https://msdn.microsoft.com/library/windows/hardware/ff552178)
-   The driver calls [**KeReleaseSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff553145) or [**KeReleaseInStackQueuedSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff553130) to release the spin lock before it calls **IoMarkIrpPending**.

-   The driver returns a status of STATUS\_PENDING for the IRP.

Drivers should call **IoMarkIrpPending** for a queued IRP only while holding a spin lock. Otherwise, an IRP could be dequeued, completed by another driver routine, and freed by the system before the call to **IoMarkIrpPending** occurs, thereby causing a crash.

For more information, see [**Synchronizing IRP Cancellation**](https://msdn.microsoft.com/library/windows/hardware/ff564531).

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>MarkingQueuedIrps</strong> rule.</p>
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

[**InsertHeadList**](https://msdn.microsoft.com/library/windows/hardware/ff547820)
[**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336)
[**IoMarkIrpPending**](https://msdn.microsoft.com/library/windows/hardware/ff549422)
[**KeAcquireInStackQueuedSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff551899)
[**KeAcquireSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff551917)
[**KeInsertByKeyDeviceQueue**](https://msdn.microsoft.com/library/windows/hardware/ff552178)
[**KeInsertDeviceQueue**](https://msdn.microsoft.com/library/windows/hardware/ff552180)
[**KeInsertQueueDpc**](https://msdn.microsoft.com/library/windows/hardware/ff552185)
[**KeReleaseInStackQueuedSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff553130)
[**KeReleaseSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff553145)
[**PoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff559654)
[**RemoveHeadList**](https://msdn.microsoft.com/library/windows/hardware/ff561032)
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20MarkingQueuedIrps%20rule%20%28wdm%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




