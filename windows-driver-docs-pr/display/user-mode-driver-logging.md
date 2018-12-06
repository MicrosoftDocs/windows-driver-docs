---
title: User-mode driver logging
description: To get a more actionable breakdown of video memory, the Windows Display Driver Model (WDDM) driver must expose the relationship between Microsoft Direct3D resources and video memory allocations.
ms.assetid: E850E148-821D-4544-A778-00B1B9D13964
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# <span id="display.user-mode_driver_logging"></span>User-mode driver logging


To get a more actionable breakdown of video memory, the Windows Display Driver Model (WDDM) driver must expose the relationship between Microsoft Direct3D resources and video memory allocations. This is made possible starting with Windows 8 with the introduction of additional user-mode driver (UMD) logging interfaces. With this information added to Event Tracing for Windows (ETW) traces, it's possible to see the video memory allocations from the API perspective.

|                                                                                   |                                  |
|-----------------------------------------------------------------------------------|----------------------------------|
| Minimum WDDM version                                                              | 1.2                              |
| Minimum Windows version                                                           | 8                                |
| Driver implementation—Full graphics and Render only                               | Mandatory                        |
| [WHCK](https://docs.microsoft.com/windows-hardware/test/hlk/windows-hardware-lab-kit) requirements and tests | **Device.Graphics¦UMDLogging** |

 

For developers, UMD logging can clarify memory costs that are currently very hard to see, such as internal fragmentation or the impact of rapidly discarding surfaces. It enables Microsoft to better work with customers and partners who provide traces for analysis of performance problems. In particular, this feature can help to overcome a common blocking point in investigating memory-related performance issues: the application is using too large a working set, but you cannot determine which API resources or calls are causing the problem.

The driver must expose the relationship between Direct3D resources and video memory allocations by implementing the UMD ETW interfaces. In addition to the logging events, the driver must be able to report all existing mappings between resources and allocations at any point in time.

## <span id="UMD_driver_allocation_logging_DDI"></span><span id="umd_driver_allocation_logging_ddi"></span><span id="UMD_DRIVER_ALLOCATION_LOGGING_DDI"></span>UMD driver allocation logging DDI


The user-mode driver allocation logging device driver interface (DDI) provides events under the Event Tracing for Windows (ETW) kernel-level tracing facility that show which API resources are associated with which kernel allocations in the Microsoft DirectX graphics kernel subsystem (Dxgkrnl.sys).

You can use the DDI to discover internal memory fragmentation or the impact of surfaces being rapidly discarded, to provide better trace information for Microsoft to help you identify performance problems, and to help determine when an app's resources or API calls are causing it to use too large a working set of memory.

Use these functions, enumeration, and structure from the Umdprovider.h header to log events in your user-mode display driver:

-   [**UMDEtwLogMapAllocation**](https://msdn.microsoft.com/library/windows/hardware/jj542437) function
-   [**UMDEtwLogUnmapAllocation**](https://msdn.microsoft.com/library/windows/hardware/jj542438) function
-   [**UMDEtwRegister**](https://msdn.microsoft.com/library/windows/hardware/jj542439) function
-   [**UMDEtwUnregister**](https://msdn.microsoft.com/library/windows/hardware/jj542440) function
-   [**UMDETW\_ALLOCATION\_SEMANTIC**](https://msdn.microsoft.com/library/windows/hardware/jj542441) enumeration
-   [**UMDETW\_ALLOCATION\_USAGE**](https://msdn.microsoft.com/library/windows/hardware/jj542442) structure

Also see the Umdetw.h header.

## <span id="Hardware_certification_requirements"></span><span id="hardware_certification_requirements"></span><span id="HARDWARE_CERTIFICATION_REQUIREMENTS"></span>Hardware certification requirements


For info on requirements that hardware devices must meet when they implement this feature, refer to the relevant [WHCK documentation](https://docs.microsoft.com/windows-hardware/test/hlk/windows-hardware-lab-kit) on **Device.Graphics ¦ UMDLogging**.

See [WDDM 1.2 features](wddm-v1-2-features.md) for a review of features added with Windows 8.

 

 





