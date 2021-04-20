---
title: Rules for AVStream Drivers
description: The DDI compliance rules for AVStream miniport drivers verify the DDI interface protocols between the kernel-streaming driver (ks.sys) and its miniport drivers.
ms.date: 05/21/2018
ms.localizationpriority: medium
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
<td align="left"><p><a href="ks-kscallbackreturn.md" data-raw-source="[&lt;strong&gt;KsCallbackReturn&lt;/strong&gt;](ks-kscallbackreturn.md)"><strong>KsCallbackReturn</strong></a></p></td>
<td align="left"><p>The KsCallbackReturn rule specifies that a kernel-streaming (KS) miniport driver callback function returns only allowed status values.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="ks-ksdevicemutex.md" data-raw-source="[&lt;strong&gt;KsDeviceMutex&lt;/strong&gt;](ks-ksdevicemutex.md)"><strong>KsDeviceMutex</strong></a></p></td>
<td align="left"><p>The <a href="ks-ksdevicemutex.md" data-raw-source="[&lt;strong&gt;KsDeviceMutex&lt;/strong&gt;](ks-ksdevicemutex.md)"><strong>KsDeviceMutex</strong></a> rule specifies that a kernel streaming miniport driver uses <a href="/windows-hardware/drivers/ddi/ks/nf-ks-ksacquiredevice" data-raw-source="[&lt;strong&gt;KsAcquireDevice&lt;/strong&gt;](/windows-hardware/drivers/ddi/ks/nf-ks-ksacquiredevice)"><strong>KsAcquireDevice</strong></a> and <a href="/windows-hardware/drivers/ddi/ks/nf-ks-ksreleasedevice" data-raw-source="[&lt;strong&gt;KsReleaseDevice&lt;/strong&gt;](/windows-hardware/drivers/ddi/ks/nf-ks-ksreleasedevice)"><strong>KsReleaseDevice</strong></a> in the correct sequence. That is, every call to <strong>KsAcquireDevice</strong> must have a corresponding call to <strong>KsReleaseDevice</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="ks-ksfiltermutex.md" data-raw-source="[&lt;strong&gt;KsFilterMutex&lt;/strong&gt;](ks-ksfiltermutex.md)"><strong>KsFilterMutex</strong></a></p></td>
<td align="left"><p>The KsFilterMutex rule specifies that a KS miniport driver acquires and releases the filter mutex in the correct sequence.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="ks-ksirqlddis.md" data-raw-source="[&lt;strong&gt;KsIrqlDDIs&lt;/strong&gt;](ks-ksirqlddis.md)"><strong>KsIrqlDDIs</strong></a></p></td>
<td align="left"><p>The KsIrqlDDIs rule specifies that a kernel-streaming (KS) miniport driver calls KS DDIs at the correct IRQL level.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="ks-ksirqldevicecallbacks.md" data-raw-source="[&lt;strong&gt;KsIrqlDeviceCallbacks&lt;/strong&gt;](ks-ksirqldevicecallbacks.md)"><strong>KsIrqlDeviceCallbacks</strong></a></p></td>
<td align="left"><p>The KsIrqlDeviceCallbacks rule specifies that a kernel-streaming (KS) miniport driver returns from a KS device callback function with the same IRQL it had when it was called.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="ks-ksinvalidstreampointer.md" data-raw-source="[&lt;strong&gt;KsInvalidStreamPointer&lt;/strong&gt;](ks-ksinvalidstreampointer.md)"><strong>KsInvalidStreamPointer</strong></a></p></td>
<td align="left"><p>The KsInvalidStreamPointer rule verifies if a KS miniport driver provides a valid KS Stream Pointer as a function argument.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="ks-ksirqlfiltercallbacks.md" data-raw-source="[&lt;strong&gt;KsIrqlFilterCallbacks&lt;/strong&gt;](ks-ksirqlfiltercallbacks.md)"><strong>KsIrqlFilterCallbacks</strong></a></p></td>
<td align="left"><p>The KsIrqlFilterCallbacks rule specifies that a kernel-streaming (KS) miniport driver returns from a KS filter callback function with the same IRQL it had when the callback function was called.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="ksmarkpendingirp.md" data-raw-source="[&lt;strong&gt;KsMarkPendingIrp&lt;/strong&gt;](ksmarkpendingirp.md)"><strong>KsMarkPendingIrp</strong></a></p></td>
<td align="left"><p>The KsMarkPendingIrp rule specifies that a kernel-stream (KS) miniport driver should mark IRPs as pending when returning with STATUS_PENDING from the following callback functions:</p>
<ul>
<li>AVStrMiniFilterClose</li>
<li>AVStrMiniPinClose</li>
<li>AVStrMiniPinCreate</li>
</ul></td>
</tr>
<tr class="even">
<td align="left"><p><a href="ks-ksirqlpincallbacks.md" data-raw-source="[&lt;strong&gt;KsIrqlPinCallbacks&lt;/strong&gt;](ks-ksirqlpincallbacks.md)"><strong>KsIrqlPinCallbacks</strong></a></p></td>
<td align="left"><p>The KsIrqlPinCallbacks rule specifies that a kernel-stream (KS) miniport driver returns from a KS Pin callback function with the same IRQL that it had when it was called.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="ks-ksprocessingmutex.md" data-raw-source="[&lt;strong&gt;KsProcessingMutex&lt;/strong&gt;](ks-ksprocessingmutex.md)"><strong>KsProcessingMutex</strong></a></p></td>
<td align="left"><p>The KsProcessingMutex rule specifies that a KS miniport driver uses the processing mutex in the correct sequence:</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="ks-ksstreampointerclone.md" data-raw-source="[&lt;strong&gt;KsStreamPointerClone&lt;/strong&gt;](ks-ksstreampointerclone.md)"><strong>KsStreamPointerClone</strong></a></p></td>
<td align="left"><p>The KsStreamPointerClone rule specifies that a kernel-stream (KS) miniport driver correctly uses the <a href="/windows-hardware/drivers/ddi/ks/nf-ks-ksstreampointerclone" data-raw-source="[&lt;strong&gt;KsStreamPointerClone&lt;/strong&gt;](/windows-hardware/drivers/ddi/ks/nf-ks-ksstreampointerclone)"><strong>KsStreamPointerClone</strong></a> and <a href="/windows-hardware/drivers/ddi/ks/nf-ks-ksstreampointerdelete" data-raw-source="[&lt;strong&gt;KsStreamPointerDelete&lt;/strong&gt;](/windows-hardware/drivers/ddi/ks/nf-ks-ksstreampointerdelete)"><strong>KsStreamPointerDelete</strong></a> functions.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="ks-ksstreampointerlock.md" data-raw-source="[&lt;strong&gt;KsStreamPointerLock&lt;/strong&gt;](ks-ksstreampointerlock.md)"><strong>KsStreamPointerLock</strong></a></p></td>
<td align="left"><p>The KsStreamPointerLock rule specifies that a kernel-streaming (KS) miniport driver uses the <a href="/windows-hardware/drivers/ddi/ks/nf-ks-ksstreampointerlock" data-raw-source="[&lt;strong&gt;KsStreamPointerLock&lt;/strong&gt;](/windows-hardware/drivers/ddi/ks/nf-ks-ksstreampointerlock)"><strong>KsStreamPointerLock</strong></a> and <a href="/windows-hardware/drivers/ddi/ks/nf-ks-ksstreampointerunlock" data-raw-source="[&lt;strong&gt;KsStreamPointerUnlock&lt;/strong&gt;](/windows-hardware/drivers/ddi/ks/nf-ks-ksstreampointerunlock)"><strong>KsStreamPointerUnlock</strong></a> functions in the correct sequence.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="ks-ksstreampointerunlock.md" data-raw-source="[&lt;strong&gt;KsStreamPointerUnlock&lt;/strong&gt;](ks-ksstreampointerunlock.md)"><strong>KsStreamPointerUnlock</strong></a></p></td>
<td align="left"><p>The KsStreamPointerUnlock rule specifies that a kernel-streaming (KS) miniport driver unlocks all stream pointers before the driver is unloaded (or the device stopped).</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="ks-kstimeddevicecallbacks.md" data-raw-source="[&lt;strong&gt;KsTimedDeviceCallbacks&lt;/strong&gt;](ks-kstimeddevicecallbacks.md)"><strong>KsTimedDeviceCallbacks</strong></a></p></td>
<td align="left"><p>The KsTimedDeviceCallbacks rule specifies that a kernel-streaming (KS) miniport driver returns from a device callback function within 500 ms.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="ks-kstimedfiltercallbacks.md" data-raw-source="[&lt;strong&gt;KsTimedFilterCallbacks&lt;/strong&gt;](ks-kstimedfiltercallbacks.md)"><strong>KsTimedFilterCallbacks</strong></a></p></td>
<td align="left"><p>The KsTimedFilterCallbacks rule specifies that a kernel-streaming (KS) miniport driver returns from a filter callback function within 500 ms.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="ks-kstimedpincallbacks.md" data-raw-source="[&lt;strong&gt;KsTimedPinCallbacks&lt;/strong&gt;](ks-kstimedpincallbacks.md)"><strong>KsTimedPinCallbacks</strong></a></p></td>
<td align="left"><p>The KsTimedPinCallbacks rule specifies that a kernel-streaming (KS) miniport driver returns from a pin callback function within 500 ms.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="ks-kstimedpinsetdevicestate.md" data-raw-source="[&lt;strong&gt;KsTimedPinSetDeviceState&lt;/strong&gt;](ks-kstimedpinsetdevicestate.md)"><strong>KsTimedPinSetDeviceState</strong></a></p></td>
<td align="left"><p>The KsTimedPinSetDeviceState rule specifies that a AVStream (KS) miniport driver makes state transitions using the AVStream minidriver's <a href="/windows-hardware/drivers/ddi/ks/nc-ks-pfnkspinsetdevicestate" data-raw-source="[&lt;em&gt;AVStrMiniPinSetDeviceState&lt;/em&gt;](/windows-hardware/drivers/ddi/ks/nc-ks-pfnkspinsetdevicestate)"><em>AVStrMiniPinSetDeviceState</em></a> routine within the required time.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="ks-kstimedprocessingmutex.md" data-raw-source="[&lt;strong&gt;KsTimedProcessingMutex&lt;/strong&gt;](ks-kstimedprocessingmutex.md)"><strong>KsTimedProcessingMutex</strong></a></p></td>
<td align="left"><p>The KsTimedProcessingMutex rule specifies that a KS miniport driver should not hold a processing mutex for more than 100 milliseconds.</p></td>
</tr>
</tbody>
</table>

 

