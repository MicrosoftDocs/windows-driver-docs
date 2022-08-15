---
title: Calculating Graphics Memory
description: Calculating Graphics Memory
ms.date: 03/18/2022
---

# Calculating Graphics Memory

The video memory manager must calculate the total amount of graphics memory before it can report an accurate account of graphics memory. It uses the following to calculate graphics memory numbers:

* Total system memory  

  This is the total amount of system memory accessible to the operating system. Memory that the BIOS allocates does not appear in this number. For example, a computer with a 1 GB DIMM (that is, 1024 MB) and that also has a BIOS that reserves 1 MB of memory appears to have 1023 MB of system memory.

* Total system memory that is available for graphics use  

  This is the total amount of system memory that is dedicated or shared to the GPU. This number is calculated as follows:

  ```cpp
  TotalSystemMemoryAvailableForGraphics = MAX((TotalSystemMemory / 2), 64MB)
  ```

* Commit limit on aperture segment  

  This is the amount of system memory that the video memory manager allows display miniport drivers to pin down (that is, the amount of system memory that miniport drivers can memory map through an aperture segment) for GPU use at any given instant. The total amount of system memory that is allocated for the GPU might exceed the commit limit greatly; however, the video memory manager ensures that only up to a commit limit amount is actually resident in an aperture segment at any one time.

  By default, the commit limit on a particular aperture segment is the size of that segment. The display miniport driver can specify a different commit limit in the **CommitLimit** member of the [**DXGK_SEGMENTDESCRIPTOR**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_segmentdescriptor) structure when the driver describes the segment. A commit limit that is specified in such a way applies only to the particular segment that the driver describes.

  In addition to per-segment commit limit, there is a global commit limit on all aperture segments. This global commit limit is also referred to as shared system memory. This value is computed by the video memory manager. However, although the display miniport driver can reduce this value to a lower value in the **ApertureSegmentCommitLimit** member of the [**DXGK_DRIVERCAPS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_drivercaps) structure, we do not recommend this practice.

  The video memory manager does not allow a display miniport driver to violate the per-segment commit limit nor the global commit limit. If a particular segment has a commit limit of 1 GB but the global commit limit is 256 MB, the video memory manager does not allow a display miniport driver to map more than 256 MB of system memory into that segment.

* Dedicated video memory  

  This is the sum of the size of all memory segments for which the display miniport driver did not specify the **PopulatedFromSystemMemory** member in the [**DXGK_SEGMENTFLAGS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_segmentflags) structure for each segment.

* Dedicated system memory
  
  Sum of the size of all memory segments for which the display miniport driver specifies the **PopulatedFromSystemMemory** member in the [**DXGK_SEGMENTFLAGS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_segmentflags) structure for each segment. This number cannot be greater than the total system memory that is available for graphics use (TotalSystemMemoryAvailableForGraphics).

* Maximum shared system memory  

  This is the maximum amount of system memory that is shared to the GPU. This number is calculated as follows:

  ```cpp
  MaxSharedSystemMemory = TotalSystemMemoryAvailableForGraphics - DedicatedSystemMemory
  ```

* Shared system memory  

  This is the amount of system memory that is shared to the GPU. This number is calculated as follows:

  ```cpp
  SharedSystemMemory = MIN(MIN(SumOfCommitLimitOnAllApertureSegment, DXGK_DRIVERCAPS.ApertureSegmentCommitLimit), MaxSharedSystemMemory)
  ```

* Total video memory  

  This is the total amount of video memory. This number is calculated as follows:

  ```cpp
  TotalVideoMemory = DedicatedVideoMemory + DedicatedSystemMemory + SharedSystemMemory
  ```
