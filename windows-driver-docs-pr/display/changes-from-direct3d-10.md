---
title: Changes from Direct3D 10
description: Changes from Direct3D 10
ms.assetid: 014a5e44-f8c4-45c0-96e8-d82f37b8b28d
keywords:
- Direct3D version 11 WDK Windows 7 display , changes from Direct3D version 10
- Direct3D version 11 WDK Windows Server 2008 R2 display , changes from Direct3D version 10
- Direct3D version 10 WDK Windows 7 display
- Direct3D version 10 WDK Windows 7 display , changes in Direct3D version 11
- Direct3D version 10 WDK Windows Server 2008 R2 display , changes in Direct3D version 11
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Changes from Direct3D 10


This section applies only to Windows 7 and later, and Windows Server 2008 R2 and later versions of Windows operating system.

The following sections describe how Direct3D 11 has changed from Direct3D 10.

### Driver Callback Functions to Kernel-Mode Services

The device-specific callback functions that the Direct3D version 11 runtime supplies in the [**D3DDDI\_DEVICECALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff544512) structure when the runtime calls the user-mode display driver's [**CreateDevice(D3D10)**](https://msdn.microsoft.com/library/windows/hardware/ff540635) function isolate the driver from kernel handles and kernel function signatures. The Direct3D version 11 runtime changes the callback semantics and, therefore, the implementation of the callback functions to support a free-threaded mode of operation, whereas previous Direct3D version runtimes did not support a free-threaded mode of operation. The rules for free-threaded mode operation apply after the driver indicates that it supports free-threaded mode (D3D11DDICAPS\_FREETHREADED); otherwise, the previous heavily restricted rules apply. For information about how the driver indicates support for free-threaded mode, see [Threading and Command Lists](supporting-threading--command-lists--and-3-d-pipeline.md). The following restrictions still exist for Direct3D version 11:

-   Only a single thread can work against an HCONTEXT at a time. Existing callback functions that currently use an HCONTEXT are [**pfnPresentCb**](https://msdn.microsoft.com/library/windows/hardware/ff568916), [**pfnRenderCb**](https://msdn.microsoft.com/library/windows/hardware/ff568923), [*pfnEscapeCb*](https://msdn.microsoft.com/library/windows/hardware/ff568908), [**pfnDestroyContextCb**](https://msdn.microsoft.com/library/windows/hardware/ff568900), [**pfnWaitForSynchronizationObjectCb**](https://msdn.microsoft.com/library/windows/hardware/ff569014), and [**pfnSignalSynchronizationObjectCb**](https://msdn.microsoft.com/library/windows/hardware/ff568933). Therefore, if more than one thread call these callback functions and use the same HCONTEXT, the driver must synchronize the calls to the callback functions. Satisfying this requirement is quite natural because these callback functions are likely to be called only from the thread that manipulates the immediate context.

-   The driver must call the following callback functions only during calls to the following driver functions by using the same threads that called those driver functions:

    <span id="pfnAllocateCb"></span><span id="pfnallocatecb"></span><span id="PFNALLOCATECB"></span>[**pfnAllocateCb**](https://msdn.microsoft.com/library/windows/hardware/ff568893)  
    The driver must call [*pfnAllocateCb*](https://msdn.microsoft.com/library/windows/hardware/ff568893) on the thread that called the driver's [**CreateResource(D3D11)**](https://msdn.microsoft.com/library/windows/hardware/ff540694) function when shared resources are created. Regular non-shared allocations with the device are fully free-threaded.

    <span id="pfnPresentCb"></span><span id="pfnpresentcb"></span><span id="PFNPRESENTCB"></span>[**pfnPresentCb**](https://msdn.microsoft.com/library/windows/hardware/ff568916)  
    The driver must call [**pfnPresentCb**](https://msdn.microsoft.com/library/windows/hardware/ff568916) only during calls to the driver's [**PresentDXGI**](https://msdn.microsoft.com/library/windows/hardware/ff569179) function.

    <span id="pfnSetDisplayModeCb"></span><span id="pfnsetdisplaymodecb"></span><span id="PFNSETDISPLAYMODECB"></span>[**pfnSetDisplayModeCb**](https://msdn.microsoft.com/library/windows/hardware/ff568926)  
    The driver must call [**pfnSetDisplayModeCb**](https://msdn.microsoft.com/library/windows/hardware/ff568926) only during calls to the driver's [**SetDisplayModeDXGI**](https://msdn.microsoft.com/library/windows/hardware/ff569536) function.

    <span id="pfnRenderCb"></span><span id="pfnrendercb"></span><span id="PFNRENDERCB"></span>[**pfnRenderCb**](https://msdn.microsoft.com/library/windows/hardware/ff568923)  
    The driver must call [*pfnRenderCb*](https://msdn.microsoft.com/library/windows/hardware/ff568923) on the thread that called the driver's [**Flush(D3D10)**](https://msdn.microsoft.com/library/windows/hardware/ff565961) function. This restriction is quite natural because of the HCONTEXT restrictions.

-   The [*pfnDeallocateCb*](https://msdn.microsoft.com/library/windows/hardware/ff568898) callback function deserves special mention because the driver is not required to call *pfnDeallocateCb* before the driver returns from its [**DestroyResource(D3D10)**](https://msdn.microsoft.com/library/windows/hardware/ff552797) function for most resource types. Because DestroyResource(D3D10) is a free-threaded function, the driver must defer destruction of the object until the driver can efficiently ensure that no existing immediate context reference remains (that is, the driver must call [**pfnRenderCb**](https://msdn.microsoft.com/library/windows/hardware/ff568923) before *pfnDeallocateCb*). This restriction applies even to shared resources or to any other callback function that uses HRESOURCE to complement HRESOURCE usage with [**pfnAllocateCb**](https://msdn.microsoft.com/library/windows/hardware/ff568893). However, this restriction does not apply to primaries. For more information about primary exceptions, see [Primary Exceptions](#primary-exceptions). Because some applications might require the appearance of synchronous destruction, the driver must ensure that it calls *pfnDeallocateCb* for any previously destroyed shared resources during a call to its [**Flush(D3D10)**](https://msdn.microsoft.com/library/windows/hardware/ff565961) function. A driver must also cleanup any previously destroyed objects (only those that will not stall the pipeline) during a call to its Flush(D3D10) function; the driver must do so to ensure that the runtime calls Flush(D3D10) as an official mechanism to cleanup deferred destroyed objects for those few applications that might require such a mechanism. For more information about this mechanism, see [Deferred Destruction and Flush(D3D10)](#deferred-destruction-and-flush-d3d10). The driver must also ensure that any objects for which destruction was deferred are fully destroyed before the driver's [**DestroyDevice(D3D10)**](https://msdn.microsoft.com/library/windows/hardware/ff552768) function returns during cleanup.

### Deprecate Ability to Allow Modification of Free-Threaded DDIs

For Direct3D version 11, the API-level concept of a display device and an immediate context are still bundled together at the DDI level by the legacy concept of a display device. This bundling of display device and immediate context maximizes compatibility with prior-version DDIs (such as, the [Direct3D version 10 DDI](https://msdn.microsoft.com/library/windows/hardware/ff552909)) and reduces driver churn when supporting multiple versions of APIs through multiple versions of DDIs. However, this bundling of display device and immediate context results in a more confusing DDI because the threading domains are not extremely explicit. Instead, to understand the threading requirements of multiple interfaces and the functions within those interfaces, driver developers must refer to the documentation.

A primary feature of the Direct3D version 11 API is that it allows multiple threads to enter create and destroy functions simultaneously. Such a feature is incompatible with allowing the driver to swap out the function table pointers for create and destroy, as the Direct3D version 10 DDI semantics for functions that are specified in [**D3D10DDI\_DEVICEFUNCS**](https://msdn.microsoft.com/library/windows/hardware/ff541833) and [**D3D10\_1DDI\_DEVICEFUNCS**](https://msdn.microsoft.com/library/windows/hardware/ff541873) allowed. Therefore, after the driver passes back the function pointers for creates ([**CreateDevice(D3D10)**](https://msdn.microsoft.com/library/windows/hardware/ff540635)), the driver should not attempt to change behavior by modifying these particular function pointers when the driver runs under the Direct3D version 11 DDI and while the driver supports DDI threading. This restriction applies to all device functions that start with *pfnCreate*, *pfnOpen*, *pfnDestroy*, *pfnCalcPrivate*, and *pfnCheck*. All the rest of the device functions are strongly associated with the immediate context. Because a single thread manipulates the immediate context at a time, it is well-defined to continue to allow the driver to hot-swap immediate context function table entries.

### pfnRenderCb Versus pfnPerformAmortizedProcessingCb

The Direct3D version 10 API functions hooked the Direct3D runtime's [**pfnRenderCb**](https://msdn.microsoft.com/library/windows/hardware/ff568923) kernel callback function to perform amortized processing (that is, instead of executing certain operations for every API function call, the driver performed amortized operations for every so many API function calls). The API typically uses this opportunity to trim high watermarks and flush out its deferred object destruction queue, among other things.

To allow the kernel callback functions to be as free-threaded as possible for the driver, the Direct3D API no longer uses [**pfnRenderCb**](https://msdn.microsoft.com/library/windows/hardware/ff568923) when the driver supports the Direct3D version 11 DDI. Therefore, drivers that support the Direct3D version 11 DDI must manually call the [**pfnPerformAmortizedProcessingCb**](https://msdn.microsoft.com/library/windows/hardware/ff568915) kernel callback function from the same thread that entered the driver DDI function after the driver submits a command buffer on the immediate context (or similar frequency). Because the operation should trim high watermarks, it would be advantageous to do it before the driver generates command buffer preambles when leveraging the [state-refresh DDI callback functions](https://msdn.microsoft.com/library/windows/hardware/ff552885).

In addition, the driver should be aware of the API amortization issue, and try to balance how often it uses the [**pfnPerformAmortizedProcessingCb**](https://msdn.microsoft.com/library/windows/hardware/ff568915) kernel callback function. On one extreme, the driver might cause over-processing. For example, if the driver always called *pfnPerformAmortizedProcessingCb* twice (back-to-back), possibly due to multiple-engine usage, it would be more efficient for the driver to call *pfnPerformAmortizedProcessingCb* only once. On the other extreme, the driver might not allow the Direct3D API to do any work for a whole frame if the driver never called *pfnPerformAmortizedProcessingCb*, possibly due to an alternating frame rendering design. The driver is not required to call *pfnPerformAmortizedProcessingCb* any more often than it naturally would, as that is overkill (for example, if the driver did not call *pfnPerformAmortizedProcessingCb* in a 1 millisecond timeframe, it must be time to pump the API). The driver is required to only determine which of the existing [**pfnRenderCb**](https://msdn.microsoft.com/library/windows/hardware/ff568923) calls should be accompanied by **pfnPerformAmortizedProcessingCb** and, naturally, conform to the threading semantics of the operation.

For drivers that support command lists, those drivers must also call [**pfnPerformAmortizedProcessingCb**](https://msdn.microsoft.com/library/windows/hardware/ff568915) from deferred contexts whenever those drivers run out of room (a similar frequency as every immediate context flush). The Direct3D version 11 runtime expects to, at least, trim its high-watermarks during such an operation. Because the threading semantic that is related to [**pfnRenderCb**](https://msdn.microsoft.com/library/windows/hardware/ff568923) has been relaxed for Direct3D version 11, concurrency issues must be solved in order to allow Direct3D version 11 to continue to hook **pfnRenderCb**, without restriction.

### New DDI Error Code

The D3DDDIERR\_APPLICATIONERROR error code is created to allow drivers to participate in validation where the Direct3D version 11 API did not. Previously, if the driver returned the E\_INVALIDARG error code, it would cause the API to raise an exception. The presence of the debug layer would cause debugging output and indicate that the driver had returned an internal error. The debugging output would suggest to the developer that the driver had a bug. If the driver returns D3DDDIERR\_APPLICATIONERROR, the debug layer determines that the application is at fault, instead.

### Retroactively Requiring Free-Threaded CalcPrivate DDIs

Direct3D version 11 retroactively requires driver functions that begin with *pfnCalcPrivate* on Direct3D version 10 DDI functions to be free threaded. This retroactive requirement matches the behavior of the Direct3D version 11 DDI to always require *pfnCalcPrivate\** and [**pfnCalcDeferredContextHandleSize**](https://msdn.microsoft.com/library/windows/hardware/ff538272) functions to be free threaded even if the driver indicates it does not support DDI threading. For more information about this retroactive requirement, see [Retroactively Requiring Free-Threaded CalcPrivate DDIs](retroactively-requiring-free-threaded-calcprivate-ddis.md).

### Deferred Destruction and Flush D3D10

Because all the destroy functions are now free-threaded, the Direct3D runtime cannot flush a command buffer during destruction. Therefore, the destroy functions must defer the actual destruction of an object until the driver can ensure that the thread that manipulates the immediate context is no longer dependent on that object to survive. Each discrete immediate context method cannot efficiently use synchronization to solve this destruction issue; therefore, the driver should use synchronization only when it flushes a command buffer. The Direct3D runtime also uses this same design when it must deal with similar issues.

Due to the ratification of deferred destruction, the Direct3D runtime advocates that those applications that cannot tolerate deferred-destruction workarounds instead use explicit mechanisms. Therefore, the driver must process its deferred-destruction queue during calls to its [**Flush(D3D10)**](https://msdn.microsoft.com/library/windows/hardware/ff565961) function (even if the command buffer is empty) to ensure that these mechanisms actually work.

Those applications that require a form of synchronous destruction must use one of the following patterns, depending on how heavyweight a destruction they require:

-   After the application ensures that all dependencies on that object are released (that is, command lists, views, middle ware, and so on), the application uses the following pattern:
    ```cpp
    Object::Release(); // Final release
    ImmediateContext::ClearState(); // Remove all ImmediateContext references as well.
    ImmediateContext::Flush(); // Destroy all objects as quickly as possible.
    ```

-   The following pattern is a more heavywight destruction:
    ```cpp
    Object::Release(); // Final release
    ImmediateContext::ClearState(); // Remove all ImmediateContext references as well.
    ImmediateContext::Flush();
    ImmediateContext::End( EventQuery );
    while( S_FALSE == ImmediateContext::GetData( EventQuery ) ) ;
    ImmediateContext::Flush(); // Destroy all objects, completely.
    ```

### Primary Exceptions

Primaries are resources that the runtime creates in calls to the driver's [**CreateResource(D3D11)**](https://msdn.microsoft.com/library/windows/hardware/ff540694) function. The runtime creates a primary by setting the **pPrimaryDesc** member of the [**D3D11DDIARG\_CREATERESOURCE**](https://msdn.microsoft.com/library/windows/hardware/ff542062) structure to a valid pointer to a [**DXGI\_DDI\_PRIMARY\_DESC**](https://msdn.microsoft.com/library/windows/hardware/ff557511) structure. Primaries have the following notable exceptions in regard to the preceding changes from Direct3D 10 to Direct3D 11:

-   Both the driver's [**CreateResource(D3D11)**](https://msdn.microsoft.com/library/windows/hardware/ff540694) and [**DestroyResource(D3D10)**](https://msdn.microsoft.com/library/windows/hardware/ff552797) functions for primaries are not free-threaded, and they share the immediate context threading domain. Concurrency can still exist with functions that start with *pfnCreate* and *pfnDestroy*, which includes CreateResource(D3D11) and DestroyResource(D3D10). However, concurrency cannot exist with **CreateResource(D3D11)** and **DestroyResource(D3D10)** for primaries. For example, the driver can detect that a call to its CreateResource(D3D11) or DestroyResource(D3D10) function is for a primary, and thereby determine that it can safely use or touch immediate context memory for the duration of the function call.

-   Primary destruction cannot be deferred by the Direct3D runtime, and the driver must call the [*pfnDeallocateCb*](https://msdn.microsoft.com/library/windows/hardware/ff568898) function appropriately within a call to the driver's [**DestroyResource(D3D10)**](https://msdn.microsoft.com/library/windows/hardware/ff552797) function.

 

 

