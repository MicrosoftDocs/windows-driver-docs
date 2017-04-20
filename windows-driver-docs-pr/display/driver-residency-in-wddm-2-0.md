---
title: Driver residency in WDDM 2.0
description: This section provides details about the driver residency changes for Windows Display Driver Model (WDDM) 2.0. The functionality described is available starting with Windows 10.
ms.assetid: 9BD0138A-E957-4675-8E08-2750825A5C87
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Driver residency in WDDM 2.0


This section provides details about the driver residency changes for Windows Display Driver Model (WDDM) 2.0. The functionality described is available starting with Windows 10.

## <span id="in_this_section"></span>In this section


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
<td align="left"><p>[Residency overview](residency-overview.md)</p></td>
<td align="left"><p>With the introduction of the new residency model, residency is being moved to an explicit list on the device instead of the per-command buffer list. The video memory manager will ensure that all allocations on a particular device residency requirement list are resident before any contexts belonging to that device are scheduled for execution.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Allocation usage tracking](allocation-usage-tracking.md)</p></td>
<td align="left"><p>With the allocation list going away, the video memory manager no longer has visibility into the allocations being referenced in a particular command buffer. As a result of this, the video memory manager is no longer in a position to track allocation usage and to handle related synchronization. This responsibility will now fall to the user mode driver. In particular, the user mode driver will have to handle the synchronization with respect to direct CPU access to allocation as well as renaming.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Offer and reclaim changes](offer-and-reclaim-changes.md)</p></td>
<td align="left"><p>For WDDM v2, requirements around <em>Offer</em> and <em>Reclaim</em> are being relaxed. User mode drivers are no longer required to use offer and reclaim on internal allocations. Idle/suspended applications will get rid of driver internal resources by using the <strong>Trim</strong>API that was introduced in Microsoft DirectX 11.1.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Access to non-resident allocation](access-to-non-resident-allocation.md)</p></td>
<td align="left"><p>Graphics processing unit (GPU) access to allocations which are not resident is illegal and will result in a device removed for the application that generated the error.</p>
<p>There are two distinct models of handling such invalid access dependent on whether the faulting engine supports GPU virtual addressing or not:</p>
<ul>
<li>For engines which donâ€™t support GPU virtual addressing and use the allocation and patch location list to patch memory references, an invalid access occurs when the user mode driver submits an allocation list which references an allocation which is not resident on the device (i.e. the user mode driver hasnâ€™t called [<em>MakeResidentCb</em>](https://msdn.microsoft.com/library/windows/hardware/dn906357) on that allocation). When this occurs, the graphics kernel will put the faulty context/device in error.</li>
<li>For engines which do support GPU virtual addressing but access a GPU virtual address that is invalid, either because there is no allocation behind the virtual address or there is a valid allocation but it hasnâ€™t been made resident, the GPU is expected to raise an unrecoverable page fault in the form of an interrupt. When the page fault interrupt occurs, the kernel mode driver will need to forward the error to the graphics kernel through a new page fault notification. Upon receiving this notification, the graphics kernel will initiate an engine reset on the faulting engine and put the faulty context/device in error. If the engine reset is unsuccessful, the graphics kernel will promote the error to a full adapter wide timeout detection and recovery (TDR).</li>
</ul></td>
</tr>
<tr class="odd">
<td align="left"><p>[Process residency budgets](process-residency-budgets.md)</p></td>
<td align="left"><p>In WDDM v2, processes will be assigned budgets for how much memory they can keep resident. This budget can change over time, but generally will only be imposed when the system is under memory pressure. Prior to Microsoft Direct3D 12, the budget is handled by the user mode driver in the form of <em>Trim</em> notifications and <em>MakeResident</em> failures with <strong>STATUS_NO_MEMORY</strong>. <em>TrimToBudget</em> notification, [<em>Evict</em>](https://msdn.microsoft.com/library/windows/hardware/dn906355), and failed [<em>MakeResident</em>](https://msdn.microsoft.com/library/windows/hardware/dn906357) calls all return the latest budget in the form of an integer <strong>NumBytesToTrim</strong> value that indicates how much needs to be trimmed in order to fit in the new budget.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Driver%20residency%20in%20WDDM%202.0%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




