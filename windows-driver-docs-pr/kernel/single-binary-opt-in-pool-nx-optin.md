---
title: Single Binary Opt-In POOL_NX_OPTIN
description: To build a single driver binary that runs both in Windows 8 and in earlier versions of Windows, use the POOL_NX_OPTIN opt-in mechanism.
ms.assetid: BE9D3C85-0212-4206-A59B-4D53FB842C39
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Single Binary Opt-In: POOL\_NX\_OPTIN


To build a single driver binary that runs both in Windows 8 and in earlier versions of Windows, use the POOL\_NX\_OPTIN opt-in mechanism. This is a porting aid for third-party hardware vendors who supply a single driver binary to support multiple Windows versions.

To use this opt-in mechanism, do the following:

-   Define POOL\_NX\_OPTIN = 1 for all source files that you want to opt-in. To do this, include the following preprocessor definition in the appropriate property page for your driver project:

    `C_DEFINES=$(C_DEFINES) -DPOOL_NX_OPTIN=1`

-   In your [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) (or equivalent) routine, include the following function call:

    `ExInitializeDriverRuntime(DrvRtPoolNxOptIn);`

    This call must occur before the driver makes any allocations that use the **NonPagedPool** pool type or makes any calls to the [**ExInitializeNPagedLookasideList**](https://msdn.microsoft.com/library/windows/hardware/ff545301) routine. **ExInitializeDriverRuntime** is a force inline function and can be called on Windows 8 or later versions of Windows.

For most drivers, these two tasks are sufficient to enable the opt-in mechanism for the single driver binary.

## Implementation details


POOL\_NX\_OPTIN works by replacing **NonPagedPool** with a global [**POOL\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/ff559707) variable, `ExDefaultNonPagedPoolType`, which is initialized either to **NonPagedPoolNx** (for Windows 8 and later versions of Windows) or to **NonPagedPoolExecute** (for earlier versions of Windows). This opt-in mechanism enables your kernel-mode driver to run both on Windows 8, with the enhanced protection of NX pool, and on earlier versions of Windows, which do not support NX pool. The macro that converts instances of the **NonPagedPool** constant name to **NonPagedPoolNx** also converts instances of **NonPagedPoolCacheAligned** to **NonPagedPoolNxCacheAligned**.

## Support for static libraries (.lib projects)


You can use the POOL\_NX\_OPTIN opt-in mechanism for a .lib project, but projects that link to the .lib generally must also use POOL\_NX\_OPTIN. At a minimum, the project that implements the [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine must contain the following function call:

`ExInitializeDriverRuntime(DrvRtPoolNxOptIn);`

 

 




