---
title: Calculating Graphics Memory
description: Calculating Graphics Memory
ms.date: 08/29/2024
---

# Calculating Graphics Memory

Before [*VidMm*](video-memory-management-and-gpu-scheduling.md) can [report an accurate account](reporting-graphics-memory.md) to clients, it must first calculate the total amount of graphics memory. *VidMm* uses the following memory types and formulas to calculate graphics memory numbers:

* Total system memory

  This value is the total amount of system memory accessible to the operating system. Memory that the BIOS allocates doesn't appear in this number. For example, a computer with a 1 GB DIMM (1,024 MB) that has a BIOS that reserves 1 MB of memory appears to have 1,023 MB of system memory.

* Total system memory that's available for graphics use

  This value is the total amount of system memory that is dedicated or shared to the GPU. This number is calculated as follows:

  ```cpp
  TotalSystemMemoryAvailableForGraphics = MAX((TotalSystemMemory / 2), 64MB)
  ```

* Commit limit on aperture segment

  This value is the amount of system memory that *VidMm* allows kernel-mode display miniport drivers (KMDs) to pin down for GPU use at any given instant. That is, it's the amount of system memory that KMDs can memory map through an aperture segment. The total amount of system memory that is allocated for the GPU might exceed the commit limit greatly; however, *VidMm* ensures that only up to a commit limit amount is actually resident in an aperture segment at any one time.

  By default, the commit limit on a particular aperture segment is the size of that segment. The KMD can specify a different commit limit in the **CommitLimit** member of the [**DXGK_SEGMENTDESCRIPTOR**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_segmentdescriptor) structure when the driver describes the segment. A commit limit that is specified in such a way applies only to the particular segment that the driver describes.

  In addition to per-segment commit limit, there's a global commit limit on all aperture segments. This global commit limit is also referred to as shared system memory. *VidMm* computes this value. A KMD can reduce this value to a lower value in the **ApertureSegmentCommitLimit** member of the [**DXGK_DRIVERCAPS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_drivercaps) structure; however, we don't recommend this practice.

  *VidMm* doesn't allow a KMD to violate the per-segment commit limit nor the global commit limit. If a particular segment has a commit limit of 1 GB but the global commit limit is 256 MB, *VidMm* doesn't allow a KMD to map more than 256 MB of system memory into that segment.

* Dedicated video memory

  This value is the sum of the size of all memory segments for which the KMD didn't specify the **PopulatedFromSystemMemory** member in the [**DXGK_SEGMENTFLAGS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_segmentflags) structure for each segment.

* Dedicated system memory
  
  This value is the sum of the size of all memory segments for which the KMD specifies the **PopulatedFromSystemMemory** member in the [**DXGK_SEGMENTFLAGS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_segmentflags) structure for each segment. This number can't be greater than the total system memory that is available for graphics use (**TotalSystemMemoryAvailableForGraphics**).

* Maximum shared system memory  

  This value is the maximum amount of system memory that is shared to the GPU. *VidMm* uses the following formula to calculate it:

  ```cpp
  MaxSharedSystemMemory = TotalSystemMemoryAvailableForGraphics - DedicatedSystemMemory
  ```

* Shared system memory  

  This value is the amount of system memory that is shared to the GPU. *VidMm* uses the following formula to calculate it:

  ```cpp
  SharedSystemMemory = MIN(MIN(SumOfCommitLimitOnAllApertureSegment, DXGK_DRIVERCAPS.ApertureSegmentCommitLimit), MaxSharedSystemMemory)
  ```

* Total video memory  

  This value is the total amount of video memory. *VidMm* uses the following formula to calculate it:

  ```cpp
  TotalVideoMemory = DedicatedVideoMemory + DedicatedSystemMemory + SharedSystemMemory
  ```

Related articles include:

* [Reporting Graphics Memory](reporting-graphics-memory.md)

* [Examples of Graphics Memory Reporting](examples-of-graphics-memory-reporting.md)

* [Retrieving Graphics Memory Numbers](retrieving-graphics-memory-numbers.md)