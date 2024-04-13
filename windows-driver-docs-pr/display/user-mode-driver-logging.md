---
title: User-mode Driver Logging
description: To get a more actionable breakdown of video memory, the Windows Display Driver Model (WDDM) driver must expose the relationship between Microsoft Direct3D resources and video memory allocations.
ms.date: 04/20/2017
---

# <span id="display.user-mode_driver_logging"></span>User-mode driver logging


To get a more actionable breakdown of video memory, the Windows Display Driver Model (WDDM) driver must expose the relationship between Microsoft Direct3D resources and video memory allocations. This is made possible starting with Windows 8 with the introduction of additional user-mode driver (UMD) logging interfaces. With this information added to Event Tracing for Windows (ETW) traces, it's possible to see the video memory allocations from the API perspective.

**Minimum WDDM version**: 1.2

**Minimum Windows version**: 8

**Driver implementation—Full graphics and Render only**: Mandatory

**[WHCK](/windows-hardware/test/hlk/windows-hardware-lab-kit) requirements and tests**: **Device.Graphics¦UMDLogging**


 

For developers, UMD logging can clarify memory costs that are currently very hard to see, such as internal fragmentation or the impact of rapidly discarding surfaces. It enables Microsoft to better work with customers and partners who provide traces for analysis of performance problems. In particular, this feature can help to overcome a common blocking point in investigating memory-related performance issues: the application is using too large a working set, but you cannot determine which API resources or calls are causing the problem.

The driver must expose the relationship between Direct3D resources and video memory allocations by implementing the UMD ETW interfaces. In addition to the logging events, the driver must be able to report all existing mappings between resources and allocations at any point in time.

## <span id="UMD_driver_allocation_logging_DDI"></span><span id="umd_driver_allocation_logging_ddi"></span><span id="UMD_DRIVER_ALLOCATION_LOGGING_DDI"></span>UMD driver allocation logging DDI


The user-mode driver allocation logging device driver interface (DDI) provides events under the Event Tracing for Windows (ETW) kernel-level tracing facility that show which API resources are associated with which kernel allocations in the Microsoft DirectX graphics kernel subsystem (Dxgkrnl.sys).

You can use the DDI to discover internal memory fragmentation or the impact of surfaces being rapidly discarded, to provide better trace information for Microsoft to help you identify performance problems, and to help determine when an app's resources or API calls are causing it to use too large a working set of memory.

Use these functions, enumeration, and structure from the Umdprovider.h header to log events in your user-mode display driver:

-   [**UMDEtwLogMapAllocation**](/windows-hardware/drivers/ddi/umdprovider/nf-umdprovider-umdetwlogmapallocation) function
-   [**UMDEtwLogUnmapAllocation**](/windows-hardware/drivers/ddi/umdprovider/nf-umdprovider-umdetwlogunmapallocation) function
-   [**UMDEtwRegister**](/windows-hardware/drivers/ddi/umdprovider/nf-umdprovider-umdetwregister) function
-   [**UMDEtwUnregister**](/windows-hardware/drivers/ddi/umdprovider/nf-umdprovider-umdetwunregister) function
-   [**UMDETW\_ALLOCATION\_SEMANTIC**](/windows-hardware/drivers/ddi/umdprovider/ne-umdprovider-_umdetw_allocation_semantic) enumeration
-   [**UMDETW\_ALLOCATION\_USAGE**](/windows-hardware/drivers/ddi/umdprovider/ns-umdprovider-_umdetw_allocation_usage) structure

Also see the Umdetw.h header.

## <span id="Hardware_certification_requirements"></span><span id="hardware_certification_requirements"></span><span id="HARDWARE_CERTIFICATION_REQUIREMENTS"></span>Hardware certification requirements


For info on requirements that hardware devices must meet when they implement this feature, refer to the relevant [WHCK documentation](/windows-hardware/test/hlk/windows-hardware-lab-kit) on **Device.Graphics ¦ UMDLogging**.

See [WDDM 1.2 features](wddm-v1-2-features.md) for a review of features added with Windows 8.

 

