---
title: IddCx 1.4 Updates for Console and Remote IDDs
description: IddCx version 1.4 updates for console and remote indirect display drivers
ms.date: 08/09/2022
keywords:
- Console and remote indirect display driver, IddCx versions 1.4 and later
- Console and remote IDD, IddCx versions 1.4 and later
- Console indirect display driver
- Console IDD
- Remote indirect display driver
- Remote IDD
---

# IddCx 1.4 updates for console and remote IDDs

The following updates to IddCx version 1.4 apply to both console and remote indirect display drivers (IDDs).

Developers of remote IDDs should also see [IddCx 1.4 updates for remote IDDs](iddcx1.4-updates-for-remote-idds.md) for additional remote-specific updates.

## Update IddCxGetVersion version

The IddCx version returned by [**IddCxGetVersion**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxgetversion) on Windows 10, version 1903 was updated to IDDCX_VERSION_19H1 (0x1400). See [IddCx versions](iddcx-versions.md) for a complete list of IddCx-related version information.

## Provide a preferred rendering adapter used to render the desktop into the swapchain

IddCx versions before IddCx 1.4 used the [power-on self-test (POST) adapter](plug-and-play--pnp--start-and-stop-cases.md) to render the desktop image passed to the IDD if it was not PnpStopped. If the POST adapter was PnpStopped, the system-supplied Windows Advanced Rasterization Platform (WARP) was used instead. However, there are configurations and scenarios where using the POST adapter does not provide the best user experience.

IddCx 1.4 includes an optional [**IddCxAdapterSetRenderAdapter**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxadaptersetrenderadapter) OS callback. The IDD can call **IddCxAdapterSetRenderAdapter** to set the render adapter it wants to use for all the swapchains on that adapter.

Windows also has a Graphics Settings page in the Settings application that allows a user to set their preference for power saving or high-performance GPU. The following table describes how these two features combine on a Surface Book device that has an Intel-integrated and Nvidia discrete GPU.

| IDD's GPU pref\* | User/OS pref\*\* | Enum for DWM\+ | Enum for App\+\+ | Intel path~ | Nvidia path~~ | Swapchain GPU^ |
| ----------------- | ------ | ------ | ------ | -------------------- | -------------------- | ------ |
| **None or Intel** | System | Intel  | Intel  | Same adapter         | Hybrid cross adapter | Intel  |
| **None or Intel** | Power  | Intel  | Intel  | Same adapter         | Hybrid cross adapter | Intel  |
| **None or Intel** | Perf   | Intel  | Nvidia | Same adapter         | Hybrid cross adapter | Intel  |
| **Nvidia**        | System | Nvidia | Nvidia | Hybrid cross adapter | Same adapter         | Nvidia |
| **Nvidia**        | Power  | Nvidia | Intel  | Hybrid cross adapter | Same adapter         | Nvidia |
| **Nvidia**        | Perf   | Nvidia | Nvidia | Hybrid cross adapter | Same adapter         | Nvidia |

Where:

* \*IDD's GPU pref = The IDD's preferred GPU
* \*\*User/OS pref = The GPU preference of the user (application) or the OS
* \+Enum for DWM = The GPU that the DX runtime enumerates the ID monitor on for Desktop Windows Manager (DWM)
* \+\+Enum for App = The GPU that the DX runtime enumerates the ID monitor on for the application
* ~Intel path = The application-to-DWM presentation path when the application is on Intel
* ~~Nvidia path = The application-to-DWM presentation path when the application is on Nvidia
* ^Swapchain GPU = The GPU that the indirect display's swapchain is created on

## Update EvtIddCxMonitorAssignSwapChain error handling for Windows 10, version 1903 and later

Starting with Windows 10, version 1903, IddCx error handling for the [**EvtIddCxMonitorAssignSwapChain**](/windows-hardware/drivers/ddi/iddcx/nc-iddcx-evt_idd_cx_monitor_assign_swapchain) callback has changed for all driver versions, and introduces a new status code. See [**EvtIdCxMonitorAssignSwapChain** error handling](idd-evtiddcxmonitorassignswapchain-error-handling.md) for details.

## For EDID-less scenarios, add EVT_IDD_CX_MONITOR_GET_PHYSICAL_SIZE to provide the physical width and height of the monitor

Sometimes an IDD needs to provide the physical monitor size even when a monitor description is not available (for example, when a non-Windows platform is used as a monitor). Unlike other desktop configuration properties, a monitor's physical size is a function of the monitor and hence cannot be changed once the monitor is added. If an IDD supplies a monitor description, the OS will take the physical size from that description. If the IDD cannot provide a description, the OS will call the optional [**EVT_IDD_CX_MONITOR_GET_PHYSICAL_SIZE**](/windows-hardware/drivers/ddi/iddcx/nc-iddcx-evt_idd_cx_monitor_get_physical_size) driver callback to retrieve the physical size. This callback is called as part of the [**IddCxMonitorArrival**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxmonitorarrival) call.

## Build IddCx v1.4 drivers that run on multiple versions of IddCx

Due to changes made in IddCx 1.3 for Windows 10 version 1809, and to changes made in IddCx 1.4, a single IDD can be built to run on Windows 10 version 1809 and later. See [Building IddCx 1.4 drivers](building-iddcx1.4-drivers.md) for details.
