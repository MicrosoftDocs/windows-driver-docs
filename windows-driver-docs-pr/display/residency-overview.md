---
title: Residency overview
description: Residency overview
ms.assetid: E610C2B8-354C-4DF5-8B25-6472A9313B15
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Residency overview


## <span id="Overview"></span><span id="overview"></span><span id="OVERVIEW"></span>Overview


Today the user mode driver builds allocation and patch location list information along with every command buffer it builds. This information is used by the video memory manager for two purposes:

-   The allocation list and patch location list are used to patch command buffers with actual segment addresses before they are submitted to a graphics processing unit (GPU) engine. GPU virtual address support in the Windows Display Driver Model (WDDM) v2 removes the need for this patching.
-   The allocation list and patch location list are used by the video memory manager to control residency of allocation. The video memory manager ensures that any allocations referenced by a command buffer are made resident before the command buffer is sent to execution for a particular engine.

With the introduction of the new residency model, residency is being moved to an explicit list on the device instead of the per-command buffer list. The video memory manager will ensure that all allocations on a particular device residency requirement list are resident before any contexts belonging to that device are scheduled for execution.

To manage residency, the user mode driver will have access to two new device driver interfaces (DDIs), [*MakeResident*](https://msdn.microsoft.com/library/windows/hardware/dn906357) and [*Evict*](https://msdn.microsoft.com/library/windows/hardware/dn906355), as well as be required to implement a new [*TrimResidency*](https://msdn.microsoft.com/library/windows/hardware/dn906364) callback. *MakeResident* will add one or more allocations to a device residency requirement list. *Evict* will remove one of more allocations from that list. The *TrimResidency* callback will be called by the video memory manager when it needs the user mode driver to reduce its residency requirement.

[*MakeResident*](https://msdn.microsoft.com/library/windows/hardware/dn906357) and [*Evict*](https://msdn.microsoft.com/library/windows/hardware/dn906355) have also been updated to keep an internal reference count, meaning multiple calls to *MakeResident* will require an equal number of *Evict* calls to actually evict the allocation.

Under the new residency model, the per-command buffer allocation and patch location list are being slowly phased out. While these lists will exist in some scenarios, they will no longer have any control over residency.

**Important**  Residency in the WDDM v2 is controlled exclusively by the device residency requirement list. This is true across all engines of the GPU and for every API.

 

## <span id="Phasing_out_allocation_and_patch_location_list"></span><span id="phasing_out_allocation_and_patch_location_list"></span><span id="PHASING_OUT_ALLOCATION_AND_PATCH_LOCATION_LIST"></span>Phasing out allocation and patch location list


The role of the allocation and patch location list will get significantly reduced with the introduction of the new residency model and will actually go completely away with the introduction of hardware assisted scheduling.

Under the packet based scheduling model, the allocation list will continue to exist as follows:

-   For engines which don't support GPU virtual addressing, the allocation list and patch location list will continue to exist, however, they will be used purely for patching purposes and will no longer have any control over residency. The allocation list and patch location list will be provided to both the user mode driver and the kernel mode driver in the various usual DDIs, but any references to allocations that are not resident will cause the GPU scheduler to reject the submission and put the device in error (lost). This mode of operation is considered legacy and we expect all GPU engines to get support for GPU virtual addressing in future hardware releases. It is expected that this mode of operation will be dropped in future versions of the WDDM.
-   For engines which do support GPU virtual addressing, a new context creation flag (**DXGK\_CONTEXTINFO\_NO\_PATCHING\_REQUIRED**) is added to indicate that the particular context doesn't require any patching. When this flag is specified, no patch location list will be allocated and only a very small allocation list (16 entries) will be allocated. The allocation list will be used to keep track of write references to primary surfaces and for no other purpose. The GPU scheduler needs to know when a particular command buffer is writing to a primary surface such that it may properly synchronize execution of that buffer with respect to flip potentially occurring to the primary surface.

Similarly, the allocation list is used in the kernel mode driver *Present* path today to pass information to the driver about the source and destination of the *Present* operation. In this context the allocation list will continue to exist to pass parameters around, however, the allocation list will not be used for residency. On GPUs requiring patching the *Present* allocation list will contain pre-patch information like it does today and the *Present* packet will be re-patched before being scheduled if any of the resources move around in memory between the time they are queued to the scheduler and the time they are scheduled for execution on the GPU.

The table below summarizes when a WDDM v2 driver should expect to receive an allocation and patch location list in various user mode driver and kernel mode driver DDIs.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">GPU Engine</th>
<th align="left">Allocation List?</th>
<th align="left">Patch Location List?</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">No GPU virtual address support (require patching, default)</td>
<td align="left"><p>Yes, full size, but purely use for patching purposes.</p>
Any reference to allocation that is not resident will result in the submitting device being put in error (lost) and the submission rejected by the scheduler.</td>
<td align="left">Yes, full size.</td>
</tr>
<tr class="even">
<td align="left">GPU virtual address support (<strong>DXGK_CONTEXTINFO_NO_PATCHING_REQUIRED</strong> flag set)</td>
<td align="left"><p>Yes, 16 entries.</p>
References the primary surface, if any, being written to by the command buffer. Used by the GPU scheduler for synchronization with lips occurring on the display controller. The primary surface must already be on the device residency requirement list or the reference will be rejected.</td>
<td align="left">No</td>
</tr>
<tr class="odd">
<td align="left">GPU virtual address support + hardware scheduling</td>
<td align="left">No</td>
<td align="left">No</td>
</tr>
</tbody>
</table>

 

 

 





