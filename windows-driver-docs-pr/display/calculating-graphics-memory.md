---
title: Calculating Graphics Memory
description: Calculating Graphics Memory
ms.assetid: 030a332b-d1f0-4a86-b11f-cfd2fbe42ac2
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Calculating Graphics Memory


The video memory manager must calculate the total amount of graphics memory before it can report an accurate account of graphics memory. The following list of items describes how the video memory manager calculates the graphics memory numbers:

<span id="Total_system_memory"></span><span id="total_system_memory"></span><span id="TOTAL_SYSTEM_MEMORY"></span>Total system memory  
Total amount of system memory that is accessible to the operating system. Memory that the BIOS allocates does not appear in this total-system-memory number. For example, a computer with a 1 GB DIMM (that is, 1024 MB) and that also has a BIOS that reserves 1 MB of memory appears to have 1023 MB of system memory.

<span id="Total_system_memory_that_is_available_for_graphics_use"></span><span id="total_system_memory_that_is_available_for_graphics_use"></span><span id="TOTAL_SYSTEM_MEMORY_THAT_IS_AVAILABLE_FOR_GRAPHICS_USE"></span>Total system memory that is available for graphics use  
Total amount of system memory that is dedicated or shared to the GPU. This number is calculated as follows:

```cpp
TotalSystemMemoryAvailableForGraphics = MAX((TotalSystemMemory / 2), 64MB)
```

<span id="Commit_limit_on_aperture_segment"></span><span id="commit_limit_on_aperture_segment"></span><span id="COMMIT_LIMIT_ON_APERTURE_SEGMENT"></span>Commit limit on aperture segment  
The amount of system memory that the video memory manager allows display miniport drivers to pin down (that is, the amount of system memory that display miniport drivers can memory map through an aperture segment) for GPU use at any given instant. The total amount of system memory that is allocated for the GPU might exceed the commit limit greatly; however, the video memory manager ensures that only up to a commit limit amount is actually resident in an aperture segment at any one time.

By default, the commit limit on a particular aperture segment is the size of that segment. The display miniport driver can specify a different commit limit in the **CommitLimit** member of the [**DXGK\_SEGMENTDESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff562035) structure when the driver describes the segment. A commit limit that is specified in such a way applies only to the particular segment that the driver describes.

In addition to per-segment commit limit, there is a global commit limit on all aperture segments. This global commit limit is also referred to as shared system memory. This value is computed by the video memory manager. However, although the display miniport driver can reduce this value to a lower value in the **ApertureSegmentCommitLimit** member of the [**DXGK\_DRIVERCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff561062) structure, we do not recommend this practice.

The video memory manager does not allow a display miniport driver to violate the per-segment commit limit nor the global commit limit. If a particular segment has a commit limit of 1 GB but the global commit limit is 256 MB, the video memory manager does not allow a display miniport driver to map more than 256 MB of system memory into that segment.

<span id="Dedicated_video_memory"></span><span id="dedicated_video_memory"></span><span id="DEDICATED_VIDEO_MEMORY"></span>Dedicated video memory  
Sum of the size of all memory segments for which the display miniport driver did not specify the **PopulatedFromSystemMemory** member in the [**DXGK\_SEGMENTFLAGS**](https://msdn.microsoft.com/library/windows/hardware/ff562039) structure for each segment.

<span id="Dedicated_system_memory"></span><span id="dedicated_system_memory"></span><span id="DEDICATED_SYSTEM_MEMORY"></span>Dedicated system memory  
Sum of the size of all memory segments for which the display miniport driver specifies the **PopulatedFromSystemMemory** member in the [**DXGK\_SEGMENTFLAGS**](https://msdn.microsoft.com/library/windows/hardware/ff562039) structure for each segment. This number cannot be greater than the total system memory that is available for graphics use (TotalSystemMemoryAvailableForGraphics).

<span id="Shared_system_memory"></span><span id="shared_system_memory"></span><span id="SHARED_SYSTEM_MEMORY"></span>Shared system memory  
The maximum amount of system memory that is shared to the GPU. This number is calculated as follows:

```cpp
MaxSharedSystemMemory = TotalSystemMemoryAvailableForGraphics - DedicatedSystemMemory
```

The amount of system memory that is shared to the GPU. This number is calculated as follows:

```cpp
SharedSystemMemory = MIN(MIN(SumOfCommitLimitOnAllApertureSegment, DXGK_DRIVERCAPS.ApertureSegmentCommitLimit), MaxSharedSystemMemory)
```

<span id="Total_video_memory"></span><span id="total_video_memory"></span><span id="TOTAL_VIDEO_MEMORY"></span>Total video memory  
The total amount of video memory. This number is calculated as follows:

```cpp
TotalVideoMemory = DedicatedVideoMemory + DedicatedSystemMemory + SharedSystemMemory
```

 

 





