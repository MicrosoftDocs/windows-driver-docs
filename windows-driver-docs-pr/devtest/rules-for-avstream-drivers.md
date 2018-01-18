---
title: Rules for AVStream Drivers
description: The DDI compliance rules for AVStream miniport drivers verify the DDI interface protocols between the kernel-streaming driver (ks.sys) and its miniport drivers.
ms.assetid: 0A104ADF-8607-4708-A0E3-1697F55B0CF5
---

# Rules for AVStream Drivers


The DDI compliance rules for AVStream miniport drivers verify the DDI interface protocols between the kernel-streaming driver (ks.sys) and its miniport drivers.

## In this section


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Topic</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<strong>KsCallbackReturn</strong>](ks-kscallbackreturn.md)</p></td>
<td align="left"><p>The KsCallbackReturn rule specifies that a kernel-streaming (KS) miniport driver callback function returns only allowed status values.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>KsDeviceMutex</strong>](ks-ksdevicemutex.md)</p></td>
<td align="left"><p>The [<strong>KsDeviceMutex</strong>](ks-ksdevicemutex.md) rule specifies that a kernel streaming miniport driver uses [<strong>KsAcquireDevice</strong>](https://msdn.microsoft.com/library/windows/hardware/ff560911) and [<strong>KsReleaseDevice</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566783) in the correct sequence. That is, every call to <strong>KsAcquireDevice</strong> must have a corresponding call to <strong>KsReleaseDevice</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>KsFilterMutex</strong>](ks-ksfiltermutex.md)</p></td>
<td align="left"><p>The KsFilterMutex rule specifies that a KS miniport driver acquires and releases the filter mutex in the correct sequence.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>KsIrqlDDIs</strong>](ks-ksirqlddis.md)</p></td>
<td align="left"><p>The KsIrqlDDIs rule specifies that a kernel-streaming (KS) miniport driver calls KS DDIs at the correct IRQL level.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>KsIrqlDeviceCallbacks</strong>](ks-ksirqldevicecallbacks.md)</p></td>
<td align="left"><p>The KsIrqlDeviceCallbacks rule specifies that a kernel-streaming (KS) miniport driver returns from a KS device callback function with the same IRQL it had when it was called.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>KsIrqlFilterCallbacks</strong>](ks-ksirqlfiltercallbacks.md)</p></td>
<td align="left"><p>The KsIrqlFilterCallbacks rule specifies that a kernel-streaming (KS) miniport driver returns from a KS filter callback function with the same IRQL it had when the callback function was called.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>KsMarkPendingIrp</strong>](ksmarkpendingirp.md)</p></td>
<td align="left"><p>The KsMarkPendingIrp rule specifies that a kernel-stream (KS) miniport driver should mark IRPs as pending when returning with STATUS_PENDING from the following callback functions:</p>
<ul>
<li>AVStrMiniFilterClose</li>
<li>AVStrMiniPinClose</li>
<li>AVStrMiniPinCreate</li>
</ul></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>KsIrqlPinCallbacks</strong>](ks-ksirqlpincallbacks.md)</p></td>
<td align="left"><p>The KsIrqlPinCallbacks rule specifies that a kernel-stream (KS) miniport driver returns from a KS Pin callback function with the same IRQL that it had when it was called.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>KsProcessingMutex</strong>](ks-ksprocessingmutex.md)</p></td>
<td align="left"><p>The KsProcessingMutex rule specifies that a KS miniport driver uses the processing mutex in the correct sequence:</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>KsStreamPointerClone</strong>](ks-ksstreampointerclone.md)</p></td>
<td align="left"><p>The KsStreamPointerClone rule specifies that a kernel-stream (KS) miniport driver correctly uses the [<strong>KsStreamPointerClone</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567129) and [<strong>KsStreamPointerDelete</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567130) functions.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>KsStreamPointerLock</strong>](ks-ksstreampointerlock.md)</p></td>
<td align="left"><p>The KsStreamPointerLock rule specifies that a kernel-streaming (KS) miniport driver uses the [<strong>KsStreamPointerLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567134) and [<strong>KsStreamPointerUnlock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567137) functions in the correct sequence.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>KsStreamPointerUnlock</strong>](ks-ksstreampointerunlock.md)</p></td>
<td align="left"><p>The KsStreamPointerUnlock rule specifies that a kernel-streaming (KS) miniport driver unlocks all stream pointers before the driver is unloaded (or the device stopped).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>KsTimedDeviceCallbacks</strong>](ks-kstimeddevicecallbacks.md)</p></td>
<td align="left"><p>The KsTimedDeviceCallbacks rule specifies that a kernel-streaming (KS) miniport driver returns from a device callback function within 500 ms.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>KsTimedFilterCallbacks</strong>](ks-kstimedfiltercallbacks.md)</p></td>
<td align="left"><p>The KsTimedFilterCallbacks rule specifies that a kernel-streaming (KS) miniport driver returns from a filter callback function within 500 ms.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>KsTimedPinCallbacks</strong>](ks-kstimedpincallbacks.md)</p></td>
<td align="left"><p>The KsTimedPinCallbacks rule specifies that a kernel-streaming (KS) miniport driver returns from a pin callback function within 500 ms.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>KsTimedPinSetDeviceState</strong>](ks-kstimedpinsetdevicestate.md)</p></td>
<td align="left"><p>The KsTimedPinSetDeviceState rule specifies that a AVStream (KS) miniport driver makes state transitions using the AVStream minidriver's [<em>AVStrMiniPinSetDeviceState</em>](https://msdn.microsoft.com/library/windows/hardware/ff556359) routine within the required time.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>KsTimedProcessingMutex</strong>](ks-kstimedprocessingmutex.md)</p></td>
<td align="left"><p>The KsTimedProcessingMutex rule specifies that a KS miniport driver should not hold a processing mutex for more than 100 milliseconds.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20Rules%20for%20AVStream%20Drivers%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




