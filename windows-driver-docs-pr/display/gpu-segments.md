---
title: GPU Segments
description: Describes how WDDM uses a segmentation model to abstract GPU access to physical memory.
keywords:
- WDDM , GPU segments, memory segments, aperture segments, system memory segments, physical memory reference, accessed physically, primary surfaces
ms.date: 12/18/2024
ms.topic: concept-article
---

# GPU segments

Starting in WDDM 2.0, a segmentation model is used to abstract GPU access to physical memory. The kernel-mode driver (KMD) expresses the physical memory resources available to a GPU by enumerating a set of segments. The video memory manager (*VidMm*) then manages these segments.

## Segment types

There are three types of segments:

* [Memory Segments](#memory-segments)
* [Aperture Segments](#aperture-segments)
* [System Memory Segments](#system-memory-segments)

### Memory Segments

A memory segment represents memory dedicated to a GPU. It can be VRAM on a discrete GPU or firmware/driver-reserved memory on an integrated GPU. A driver can enumerate multiple memory segments.

Starting in WDDM 2.0, *VidMm* manages a memory segment as a pool of physical pages that are either 4 KB or 64 KB in size. Surface data is copied into and out of a memory segment using *Fill*/*Transfer*/*Discard*/*FillVirtual*/*TransferVirtual* paging operations.

The CPU can access the content of a memory segment in one of two ways:

* A memory segment can be visible in the physical address space of the CPU, in which case *VidMm* simply maps CPU virtual addresses directly to allocations within the segment.
* Starting in WDDM 2.0, *VidMm* also supports accessing the content of a memory segment through a programmable CPU host aperture associated with that segment.

### Aperture Segments

An aperture segment is a global page table used to make discontinuous system memory pages appears contiguous from the perspective of a GPU engine.

In WDDM 2.0, a single aperture segment must be reported.

### System Memory Segments

The system memory segment is an implicit segment representing system memory references (that is, a guest physical address). The KMD doesn't directly enumerate a system memory segment. Instead, *VidMm* implicitly enumerates it and always assigns `SegmentId==0`. To place an allocation in the system memory segment, the KMD needs to use the aperture segment ID.

## Physical memory reference

In the DDI, physical memory references always take the form of a segment ID-segment offset pair.

## Accessing allocations by physical address

GPU engines that don't support GPU virtual addressing need to access allocations through their physical addresses. This requirement has implications on how an allocation gets assigned resources from a segment. Physical references imply that an allocation must be allocated either contiguously in a memory segment or occupy a contiguous range in the aperture segment.

To avoid unnecessary and expensive contiguous allocations, the KMD must explicitly identify allocations that require a rendering engine to access them physically. KMD does so by setting the [**DXGK_ALLOCATIONINFOFLAGS2**](./dxgk-allocationinfoflags2.md)::**AccessedPhysically** flag during allocation creation.

Such allocations will be mapped to the aperture segment when they're resident in system memory. The allocations will be contiguous when resident in a memory segment. Allocations created this way can be referenced through the allocation list on engines, operating in the physical addressing mode.

For allocations that don't have this flag set, *VidMm* will allocate them as a set of pages in a memory segment or a set of pages in system memory, either of which are accessed through GPU virtual addresses. Allocations created this way can't be referenced through the allocation list. Any command buffer submission referencing the allocation that way will be rejected.

Primary surfaces, which are the main images displayed by a computer, are implicitly physically accessed by the display controller. These surfaces will be allocated contiguously in a memory segment or mapped into the aperture segment when displayed. The KMD should only set the **AccessedPhysically** flags when its rendering engine will access the allocation physically. The distinction between the implicit physical access on primary surface and the explicit flags is when the allocation will be mapped into the aperture:

* When the **AccessedPhysically** flags is set, the allocation will be mapped into the aperture whenever it's resident.

* Primary surfaces that don't have this flag set will be mapped into the aperture only when being displayed. This approach helps to remove pressure on the aperture segment. That is, typically there are only a few primary surfaces actively being displayed, while a large number of them might exist and be rendered to. For example, all *FlipEx* swapchains are created as primary and potentially displayable surfaces in *dFlip*/*iFlip* scenarios.

The following table summarizes how different types of allocations within GPU segments are accessed based on their physical access requirements.

| Segment type | AccessedPhysically==0 | AccessedPhysically==1 | Primary && AccessedPhysically==0 |
| ------------ | --------------------- | --------------------- | -------------------------------- |
| Memory Segment | Set of pages. Only GPU virtual access is allowed. | Contiguous. GPU physical access is allowed | Contiguous. Only GPU virtual access is allowed by rendering engines. |
| Aperture Segment | Not mapped. System memory pages, only mapped by GPU page tables, not to the aperture segment. Only GPU virtual access is allowed. | Mapped when resident. GPU physical access is allowed. | Mapped when displayed. Only GPU virtual access is allowed by rendering engines. |
