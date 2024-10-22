---
title: User-mode Driver Logging
description: Describes user-mode driver logging in the Windows Display Driver Model (WDDM)
keywords:
- Windows Display Driver Model (WDDM) , debugging
- WDDM driver , debugging
- WDDM , user-mode driver logging
ms.date: 10/21/2024
---

# User-mode driver logging

This article provides an overview of user-mode driver logging in WDDM.

To get a more actionable breakdown of video memory, a WDDM driver needs to expose the relationship between Direct3D resources and video memory allocations. Starting with Windows 8, this capability is possible with the addition of user-mode driver (UMD) logging interfaces. With this information added to Event Tracing for Windows (ETW) traces, it's possible to see the video memory allocations from the API perspective.

Requirements:

* Minimum WDDM version: 1.2
* Minimum Windows version: 8
* Driver implementation—Full graphics and Render only: Mandatory
* [WHLK](/windows-hardware/test/hlk/windows-hardware-lab-kit) requirements and tests: **Device.Graphics¦UMDLogging**

For developers, UMD logging can clarify memory costs, such as internal fragmentation or the effect of rapidly discarding surfaces. It enables Microsoft to better work with customers and partners who provide traces for analysis of performance problems. In particular, this feature can help to overcome a common blocking point in investigating memory-related performance issues: the application is using too large a working set, but you can't determine which API resources or calls are causing the problem.

The driver must expose the relationship between Direct3D resources and video memory allocations by implementing the UMD ETW interfaces. In addition to the logging events, the driver must be able to report all existing mappings between resources and allocations at any point in time.

## UMD driver allocation logging DDI

The UMD allocation logging DDI provides events under the ETW kernel-level tracing facility that show which API resources are associated with which kernel allocations in the DirectX graphics kernel subsystem (*Dxgkrnl.sys*).

You can use the DDI to:

* Discover internal memory fragmentation or the effect of surfaces being rapidly discarded.
* Provide better trace information for Microsoft to help you identify performance problems.
* Help determine when an app's resources or API calls are causing it to use too large a working set of memory.

Use these functions, enumeration, and structure from the *umdprovider.h* header to log events in your UMD:

* [**UMDEtwLogMapAllocation**](/windows-hardware/drivers/ddi/umdprovider/nf-umdprovider-umdetwlogmapallocation) function
* [**UMDEtwLogUnmapAllocation**](/windows-hardware/drivers/ddi/umdprovider/nf-umdprovider-umdetwlogunmapallocation) function
* [**UMDEtwRegister**](/windows-hardware/drivers/ddi/umdprovider/nf-umdprovider-umdetwregister) function
* [**UMDEtwUnregister**](/windows-hardware/drivers/ddi/umdprovider/nf-umdprovider-umdetwunregister) function
* [**UMDETW_ALLOCATION\_SEMANTIC**](/windows-hardware/drivers/ddi/umdprovider/ne-umdprovider-_umdetw_allocation_semantic) enumeration
* [**UMDETW_ALLOCATION_USAGE**](/windows-hardware/drivers/ddi/umdprovider/ns-umdprovider-_umdetw_allocation_usage) structure

See also the *umdetw.h* header.

## Hardware certification requirements

For information on requirements that hardware devices must meet when they implement this feature, see the [WHLK documentation](/windows-hardware/test/hlk/windows-hardware-lab-kit) on **Device.Graphics ¦ UMDLogging**.

See [WDDM 1.2 features](wddm-v1-2-features.md) for a review of features added with Windows 8.
