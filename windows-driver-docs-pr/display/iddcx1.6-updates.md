---
title: Updates for IddCx Versions 1.5 and 1.6 and Later
description: IddCx version 1.5 and 1.6 updates for console and remote indirect display drivers
ms.date: 10/02/2024
keywords:
- Console and remote indirect display driver , IddCx versions 1.5 and later , IddCx versions 1.6 and later
- Console and remote IDD , IddCx versions 1.5 and later , IddCx versions 1.6 and later
- Console indirect display driver
- Console IDD
- Remote indirect display driver
- Remote IDD
---

# Updates for IddCx versions 1.5, 1.6 and later

The following updates in IddCx versions 1.5 and 1.6 apply to both console and remote indirect display drivers (IDDs).

## Updated IddCxGetVersion version

The IddCx version returned by [**IddCxGetVersion**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxgetversion) was updated to 0x1500 for version 1.5 and 0x1600 for version 1.6. See [IddCx versions](iddcx-versions.md) for a complete list of IddCx-related version information.

## WPP information in public IddCx symbols

Starting with IddCx version 1.5, the public IddCx symbol files contain all the Windows software trace processor (WPP) information. This change means that the [**!wmitrace.logdump**](../debuggercmds/-wmitrace-logdump.md) debugger command decodes and displays the WPP message in the kernel debugger.

## Ability to access buffers allocated in system memory

In certain scenarios, swapchain buffers are resident in system memory; for example, when WARP (Windows Advanced Rasterization Platform, the system-supplied software renderer) is the render adapter being used. IddCx 1.5 adds the following OS callbacks that allow the driver to access buffers in system memory thus avoiding a subresource copy:

* [**IddCxSwapChainInSystemMemory**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxswapchaininsystemmemory) allows an IDD to check whether the buffers for a swapchain are resident in system memory. The result of this callback remains constant throughout the lifetime of the swapchain. The driver should check the value of this callback in its[**EvtIddCxMonitorAssignSwapChain**](/windows-hardware/drivers/ddi/iddcx/nc-iddcx-evt_idd_cx_monitor_assign_swapchain) callback and set up state to release and acquire buffers.

* [**IddCxSwapChainReleaseAndAcquireSystemBuffer**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxswapchainreleaseandacquiresystembuffer) allows an IDD to release and acquire a buffer, as well as obtain information for accessing the buffer (such as a system memory pointer, pitch/stride of the buffer, and surface format and dimensions). The returned buffer is valid until the next successful call to this function.

  At the point of assignment of a new swapchain, the driver must decide which variant of **IddCxSwapChainReleaseAndAcquireBuffer**/**IddCxSwapChainReleaseAndAcquireSystemBuffer** it's going to call for the particular swapchain and must continue using that variant for the rest of lifetime of that swapchain. To decide, the driver should consider its specific requirements and the result of the call to [**IddCxSwapChainInSystemMemory**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxswapchaininsystemmemory). A driver causes the operating system to bug check the UMDF process if it:

  * Calls the other variant of **IddCxSwapChainReleaseAndAcquireSystemBuffer**/**IddCxSwapChainReleaseAndAcquireBuffer**.
  * Calls **IddCxSwapChainReleaseAndAcquireSystemBuffer** when **IddCxSwapChainInSystemMemory** returns false.

Drivers are recommended but not required to use these callback functions. The behavior before IddCx 1.5 remains supported.

## Ability to access buffers in physically contiguous memory

> [!NOTE]
> **IddCxSwapChainGetPhysicallyContiguousAddress** isn't supported on any Windows 10 system, and will likely be deprecated in the future.

Starting with IddCx 1.6, the [**IDDCX_ADAPTER_FLAGS_PREFER_PHYSICALLY_CONTIGUOUS**](/windows-hardware/drivers/ddi/iddcx/ne-iddcx-iddcx_adapter_flags) flag and [**IddCxSwapChainGetPhysicallyContiguousAddress**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxswapchaingetphysicallycontiguousaddress) OS callback function were added so that buffers can be accessed in physically contiguous memory.

Display drivers can request that primary surfaces be allocated in physically contiguous system memory by setting the [**IDDCX_ADAPTER_FLAGS_PREFER_PHYSICALLY_CONTIGUOUS**](/windows-hardware/drivers/ddi/iddcx/ne-iddcx-iddcx_adapter_flags) flag in [**IDDCX_ADAPTER_CAPS**](/windows-hardware/drivers/ddi/iddcx/ns-iddcx-iddcx_adapter_caps). This capability allows a driver to directly scan out a surface without an intermediate copy.

The driver's request during initialization isn't guaranteed to succeed. If the request doesn't succeed, the call to [**IddCxAdapterInitAsync**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxadapterinitasync) won't fail. Instead, once the driver performs a [**IddCxSwapChainReleaseAndAcquireBuffer**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxswapchainreleaseandacquirebuffer) (or [**IddCxSwapChainReleaseAndAcquireSystemBuffer**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxswapchainreleaseandacquirebuffer)), it should call [**IddCxSwapChainGetPhysicallyContiguousAddress**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxswapchaingetphysicallycontiguousaddress) to retrieve the physical address of the surface. **IddCxSwapChainGetPhysicallyContiguousAddress** will first wait for any pending render commands, then flush and invalidate the CPU caches associated with the address range where the surface is stored. However, if the initial request for the surfaces to be allocated in physically contiguous memory failed then **IddCxSwapChainGetPhysicallyContiguousAddress** returns E_NOINTERFACE.
