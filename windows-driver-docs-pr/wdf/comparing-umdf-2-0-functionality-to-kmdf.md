---
title: Comparing UMDF 2 Functionality to KMDF
author: windows-driver-content
description: This topic compares the functionality available to a Kernel-Mode Driver Framework (KMDF) driver with that available to a User-Mode Driver Framework (UMDF) 2 driver.
ms.assetid: 9D4DD1A9-DA49-4132-B98F-AFEC8B427272
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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
<td align="left">[Handling DMA Operations in KMDF Drivers](handling-dma-operations-in-kmdf-drivers.md)</td>
</tr>
<tr class="even">
<td align="left">Bus enumeration</td>
<td align="left">[Enumerating the Devices on a Bus](enumerating-the-devices-on-a-bus.md)</td>
</tr>
<tr class="odd">
<td align="left">Functional power states (limited support is available in UMDF)</td>
<td align="left">[Supporting Functional Power States](supporting-functional-power-states.md)</td>
</tr>
<tr class="even">
<td align="left">Access to WDM objects</td>
<td align="left">[Obtaining WDM Information](obtaining-wdm-information.md)</td>
</tr>
<tr class="odd">
<td align="left">Neither Buffered Nor Direct I/O</td>
<td align="left"><p>[Accessing Data Buffers in WDF Drivers](accessing-data-buffers-in-wdf-drivers.md#neither)</p>
<p>[Intercepting an I/O Request before it is Queued](managing-i-o-queues.md#obtaining-requests-from-an-i-o-queue)</p>
<ul>
<li>[<em>EvtIoInCallerContext</em>](https://msdn.microsoft.com/library/windows/hardware/ff541764)</li>
</ul></td>
</tr>
<tr class="even">
<td align="left">Internal device control requests (IOCTLs)</td>
<td align="left"><p>[Sending I/O Requests Synchronously](sending-i-o-requests-synchronously.md)</p>
<ul>
<li>[<strong>WdfIoTargetSendInternalIoctlSynchronously</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548656)</li>
<li>[<strong>WdfIoTargetSendInternalIoctlOthersSynchronously</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548651)</li>
</ul>
<p>[Sending I/O Requests Asynchronously](sending-i-o-requests-asynchronously.md)</p>
<ul>
<li>[<strong>WdfIoTargetFormatRequestForInternalIoctl</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548595)</li>
<li>[<strong>WdfIoTargetFormatRequestForInternalIoctlOthers</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548599)</li>
</ul></td>
</tr>
<tr class="odd">
<td align="left">Remove lock opt-in for I/O requests</td>
<td align="left">[<strong>WdfDeviceInitSetRemoveLockOptions</strong>](https://msdn.microsoft.com/library/windows/hardware/hh451095)</td>
</tr>
</tbody>
</table>

 

If your driver does not require any of the above, you can write a UMDF 2 driver instead of using KMDF. Because the two frameworks share many interfaces, you can convert your driver to KMDF later if the need arises. For information about why you might want to choose UMDF, see [Advantages of Writing UMDF Drivers](advantages-of-writing-umdf-drivers.md).

For more information about the framework objects and which are supported by KMDF and UMDF, see [Summary of Framework Objects](summary-of-framework-objects.md).

For a table showing all Windows Driver Frameworks (WDF) callbacks and methods and their framework applicability, see [Summary of WDF Callbacks and Methods](https://msdn.microsoft.com/library/windows/hardware/dn265591).

 

 





