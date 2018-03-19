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

 

 

 





