---
title: Comparing UMDF 2 Functionality to KMDF
description: This topic compares the functionality available to a Kernel-Mode Driver Framework (KMDF) driver with that available to a User-Mode Driver Framework (UMDF) 2 driver.
ms.assetid: 9D4DD1A9-DA49-4132-B98F-AFEC8B427272
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Comparing UMDF 2 Functionality to KMDF


This topic compares the functionality available to a Kernel-Mode Driver Framework (KMDF) driver with that available to a User-Mode Driver Framework (UMDF) 2 driver. It is designed to help you decide whether you should write a UMDF 2 driver or a KMDF driver.

While UMDF version 2 offers a significant subset of functionality that was previously available only to KMDF drivers, the following features are available only to KMDF drivers. If your driver requires one of these features, you must write a KMDF driver.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Feature</th>
<th align="left">Related information</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">Direct memory access (DMA)</td>
<td align="left"><a href="handling-dma-operations-in-kmdf-drivers.md" data-raw-source="[Handling DMA Operations in KMDF Drivers](handling-dma-operations-in-kmdf-drivers.md)">Handling DMA Operations in KMDF Drivers</a></td>
</tr>
<tr class="even">
<td align="left">Bus enumeration</td>
<td align="left"><a href="enumerating-the-devices-on-a-bus.md" data-raw-source="[Enumerating the Devices on a Bus](enumerating-the-devices-on-a-bus.md)">Enumerating the Devices on a Bus</a></td>
</tr>
<tr class="odd">
<td align="left">Functional power states (limited support is available in UMDF)</td>
<td align="left"><a href="supporting-functional-power-states.md" data-raw-source="[Supporting Functional Power States](supporting-functional-power-states.md)">Supporting Functional Power States</a></td>
</tr>
<tr class="even">
<td align="left">Access to WDM objects and IRPs</td>
<td align="left"><a href="obtaining-wdm-information.md" data-raw-source="[Obtaining WDM Information](obtaining-wdm-information.md)">Obtaining WDM Information</a></td>
</tr>
<tr class="odd">
<td align="left">Neither Buffered Nor Direct I/O</td>
<td align="left"><p><a href="accessing-data-buffers-in-wdf-drivers.md#neither" data-raw-source="[Accessing Data Buffers in WDF Drivers](accessing-data-buffers-in-wdf-drivers.md#neither)">Accessing Data Buffers in WDF Drivers</a></p>
<p><a href="managing-i-o-queues.md#obtaining-requests-from-an-i-o-queue" data-raw-source="[Intercepting an I/O Request before it is Queued](managing-i-o-queues.md#obtaining-requests-from-an-i-o-queue)">Intercepting an I/O Request before it is Queued</a></p>
<ul>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/ff541764" data-raw-source="[&lt;em&gt;EvtIoInCallerContext&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff541764)"><em>EvtIoInCallerContext</em></a></li>
</ul></td>
</tr>
<tr class="even">
<td align="left">Internal device control requests (IOCTLs)</td>
<td align="left"><p><a href="sending-i-o-requests-synchronously.md" data-raw-source="[Sending I/O Requests Synchronously](sending-i-o-requests-synchronously.md)">Sending I/O Requests Synchronously</a></p>
<ul>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/ff548656" data-raw-source="[&lt;strong&gt;WdfIoTargetSendInternalIoctlSynchronously&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548656)"><strong>WdfIoTargetSendInternalIoctlSynchronously</strong></a></li>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/ff548651" data-raw-source="[&lt;strong&gt;WdfIoTargetSendInternalIoctlOthersSynchronously&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548651)"><strong>WdfIoTargetSendInternalIoctlOthersSynchronously</strong></a></li>
</ul>
<p><a href="sending-i-o-requests-asynchronously.md" data-raw-source="[Sending I/O Requests Asynchronously](sending-i-o-requests-asynchronously.md)">Sending I/O Requests Asynchronously</a></p>
<ul>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/ff548595" data-raw-source="[&lt;strong&gt;WdfIoTargetFormatRequestForInternalIoctl&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548595)"><strong>WdfIoTargetFormatRequestForInternalIoctl</strong></a></li>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/ff548599" data-raw-source="[&lt;strong&gt;WdfIoTargetFormatRequestForInternalIoctlOthers&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548599)"><strong>WdfIoTargetFormatRequestForInternalIoctlOthers</strong></a></li>
</ul></td>
</tr>
<tr class="odd">
<td align="left">Remove lock opt-in for I/O requests</td>
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/hh451095" data-raw-source="[&lt;strong&gt;WdfDeviceInitSetRemoveLockOptions&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh451095)"><strong>WdfDeviceInitSetRemoveLockOptions</strong></a></td>
</tr>
<tr class="even">
<td align="left">WMI</td>
<td align="left"><a href="introduction-to-wmi-for-kmdf-drivers.md" data-raw-source="[Introduction to WMI for KMDF Drivers](introduction-to-wmi-for-kmdf-drivers.md)">Introduction to WMI for KMDF Drivers</a></td>
</tr>
</tbody>
</table>

 

If your driver does not require any of the above, you can write a UMDF 2 driver instead of using KMDF. Because the two frameworks share many interfaces, you can convert your driver to KMDF later if the need arises. For information about why you might want to choose UMDF, see [Advantages of Writing UMDF Drivers](advantages-of-writing-umdf-drivers.md).

For more information about the framework objects and which are supported by KMDF and UMDF, see [Summary of Framework Objects](summary-of-framework-objects.md).

For a table showing all Windows Driver Frameworks (WDF) callbacks and methods and their framework applicability, see [Summary of WDF Callbacks and Methods](https://msdn.microsoft.com/library/windows/hardware/dn265591).

 

 





