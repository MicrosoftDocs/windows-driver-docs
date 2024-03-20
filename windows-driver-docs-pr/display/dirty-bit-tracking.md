---
title: Dirty Bit Tracking
description: Describes the GPU fence synchronization object that can be used for true GPU-to-GPU synchronization in GPU hardware scheduling stage 2.
keywords:
- WDDM, dirty bit tracking
- WDDM, GPU fence synchronization object
- WDDM, hardware scheduling
ms.date: 03/21/2024
---

# Dirty bit tracking

This article describes the dirty bit tracking feature, which is supported starting in Windows 11, version 24H2 (WDDM 3.2).

## Introduction

As GPUs in cloud scenarios become more popular, there is an increasing need to make sure that migration of virtual machines from one physical host to another maintains reasonable performance. This need is not only to reduce user impact, but also to avoid issues such as TCP request timeouts as the VM is migrated.

Transferring memory contents between the physical hosts is done in two overall passes:

1. *Brownout*: During the brownout period, the virtual machine is still running, but the system performs an iterative save of any dirty data. The goal here is that the amount of data being dirtied during each iteration gets smaller until it converges on a smaller subset of data that can be copied very quickly. This data amount will vary depending on the workload of the machine, and isn't guaranteed to converge to any particular size.

2. *Blackout*: During the blackout period, the virtual machine is paused, and all remaining dirty data is copied. This copy ensures that the resulting data on the destination machine is in the same state as the source.

Without dirty bit tracking, the system must rely on a single full copy of the GPU's frame buffer during the blackout period. To support the brownout pass, the hardware must be able to actively track dirtied memory pages and report it back to the OS so that the OS knows only what memory to copy.

## Detailed design

### Reporting capabilities

During adapter initialization, *Dxgkrnl* queries the driver to ask information about the format of the dirty bitplane used by the hardware; namely, the page size (or amount of data) represented by each bit.

### Starting and stopping dirty capture

If tracking dirty information has a high cost on the hardware's performance, then it makes sense to only enable dirty tracking during the brownout period. During this time, minimizing the costs of migration are more important than the potential performance impact of the tracking.

However, if there is negligible or no impact at all on performance, there is also benefit in enabling this behavior at all times. Some users might not perform heavy GPU workloads on their VMs, so the memory might not be heavily dirtied from the start. By enabling dirty bit tracking at startup time, then the first iteration of the brownout can immediately use the dirty data without the need for a full copy of the frame buffer. If the amount of user-dirtied memory is small (for example, the user is doing primarily CPU workloads), then the cost savings of the migration can be quite significant.

### Querying dirty bits

Dirty information is represented as a bitplane of dirty pages. Each bit in the bit plane represents one "page" of memory. The page size of the dirty data doesn't need to align with the natural pages sizes of the virtual addressing on the GPU (for example, 4KB/64KB), and can be whatever is most optimal for the particular hardware. The driver reports this page size during initialization.

During the brownout period, *Dxgkrnl* queries the hardware for dirty data between each iteration. At this time, the driver must be able to atomically query and reset the bitplane data. That is, the hardware must be able to query the value and reset it to zero in a single atomic operation in order to prevent a loss of data in the dirty information.

Virtual machines are not necessarily all migrated to the same destination, and therefore migration of the frame buffer occurs for each virtual GPU instance. This means that the driver must be able to query the bitplane information for a specified sub range of the overall frame buffer that represents that particular virtual GPU instance. For example, an 8GB GPU split four ways must be able to individually query and reset the bits of the bitplane for each 2GB range of VRAM separately without affecting the other dirty bit data.

## DDI Changes

### Capabilities

The following caps are added to [**DXGK_QUERYADAPTERINFOTYPE**](/windows-hardware/drivers/ddi/d3dkmddi/ne-d3dkmddi-_dxgk_queryadapterinfotype).

* **DXGKQAITYPE_DIRTYBITTRACKINGCAPS**

  The system now calls KMD's [**DxgkDdiQueryAdapterInfo**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_queryadapterinfo) function with a [**DXGK_QUERYADAPTERINFOTYPE**](/windows-hardware/drivers/ddi/d3dkmddi/ne-d3dkmddi-_dxgk_queryadapterinfotype) of **DXGKQAITYPE_DIRTYBITTRACKINGCAPS** during adapter initialization to determine driver and hardware capabilities for dirty bit tracking.

  KMD should fill in the provided [**DXGK_DIRTY_BIT_TRACKING_CAPS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-dxgk_dirty_bit_tracking_caps) structure that **pOutputData** points to.

* **DXGKQAITYPE_DIRTYBITTRACKINGSEGMENTCAPS**

  If KMD has set [**DirtyBitTrackingSupported**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-dxgk_dirty_bit_tracking_caps) to TRUE, the system calls KMD's [**DxgkDdiQueryAdapterInfo**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_queryadapterinfo) function with a [**DXGK_QUERYADAPTERINFOTYPE**](/windows-hardware/drivers/ddi/d3dkmddi/ne-d3dkmddi-_dxgk_queryadapterinfotype) of **DXGKQAITYPE_DIRTYBITTRACKINGSEGMENTCAPS** for each memory segment on the system to query information about dirty bit tracking support.

  KMD should fill in the provided [**DXGK_DIRTY_BIT_TRACKING_SEGMENT_CAPS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-dxgk_dirty_bit_tracking_segment_caps) structure that **pOutputData** points to.

### Memory basis DDIs

The tracking of modify operations on VRAM is for allocations that might not be backed contiguously. An initial use in [Live Migration](live-migration-on-gpup-devices.md), for example, applies to tracking on the framebuffer reserve for a virtual function. So the physical addresses represented in the tracking of dirty bits consist of a collection of ranges representing the allocation being operated on.

It's important to ensure that the operations are matched to the same ranges. In many cases, this matching needs to be an enforced invariant of the interfaces to ensure proper tracking of state. To assist this tracking with the KMD, the following interfaces are introduced:

* [**DxgkDdiCreateMemoryBasis**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_creatememorybasis)

* [**DxgkDdiDestroyMemoryBasis**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_destroymemorybasis)

* [**DxgkDdiStartDirtyTracking**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_startdirtytracking)

* [**DxgkDdiStopDirtyTracking**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_stopdirtytracking)

* [**DxgkDdiQueryDirtyBitData**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_querydirtybitdata)
