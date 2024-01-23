---
title: IddCx versions
description: Provides version
ms.date: 09/20/2023
keywords:
- IddCx versions, WDK
- IddCx versions, Windows versions
---

# IddCx versions

This page provides information about IddCx versions, including version numbers, associated version value returned by [**IddCxGetVersion**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxgetversion), and high-level changes made to each version.

This page also lists the IddCx version (and **IddCxGetVersion** value) shipped with Windows 11, Windows 10, and Windows Server releases.

## IddCx versions and features

| IddCx version | IddCxGetVersion returned | Changes from previous public version |
| ------------- | ------------------------ | ------------------------------------ |
| [1.10](iddcx1.10-updates.md) | 0x1A80 | Add HDR10 and SDR Wide Color Gamut (WCG) support - Windows 2024 |
| [1.10](iddcx1.10-updates.md) | 0x1A00 | Add HDR10 and SDR Wide Color Gamut (WCG) support - Windows 11 23H2 |
| [1.9](iddcx1.9-updates.md) | 0x1900 | Add [**IddCxSetRealtimeGPUPriority**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxsetrealtimegpupriority); disallow UMDF process pooling |
| [1.8](iddcx1.8-updates.md) | 0x1800 | Add [**IDDCX_ADAPTER_FLAGS_PREFER_PRECISE_PRESENT_REGIONS**](/windows-hardware/drivers/ddi/iddcx/ne-iddcx-iddcx_adapter_flags) |
| [1.7](iddcx1.7-updates.md) | 0x1700 | Add [**IddCxMonitorQueryHardwareCursor2**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxmonitorqueryhardwarecursor2) and deprecate [**IDDCX_ADAPTER_FLAGS_CAN_USE_MOVE_REGIONS**](/windows-hardware/drivers/ddi/iddcx/ne-iddcx-iddcx_adapter_flags) |
| [1.6](iddcx1.6-updates.md) | 0x1600 | Add [**IddCxSwapChainInSystemMemory**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxswapchaininsystemmemory), [**IddCxSwapChainReleaseAndAcquireSystemBuffer**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxswapchainreleaseandacquiresystembuffer) and [**IddCxSwapChainGetPhysicallyContiguousAddress**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxswapchaingetphysicallycontiguousaddress) |
| 1.5                        | 0x1500 | Internal IddCx version update |
| [1.4](iddcx1.4-updates.md) | 0x1400 | Add support for remote session ID drivers, [**EvtIddCxMonitorGetPhysicalSize**](/windows-hardware/drivers/ddi/iddcx/nc-iddcx-evt_idd_cx_monitor_get_physical_size), [**IddCxAdapterSetRenderAdapter**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxadaptersetrenderadapter) and [**IddCxAdapterDisplayConfigUpdate**](/windows-hardware/drivers/ddi/iddcx/nc-iddcx-pfn_iddcxadapterdisplayconfigupdate) |
| 1.3                        | 0x1300 | Add ability to load a driver built against IddCx 1.3 or above |
| 1.2                        | 0x1200 | Add [**IddCxGetVersion**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxgetversion), [**IddCxReportCriticalError**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxreportcriticalerror), [**IddCxMonitorSetSrmList**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxmonitorsetsrmlist) and [**IddCxMonitorGetSrmListVersion**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxmonitorgetsrmlistversion) |
| 1.1                        | N/A    | Internal IddCx version update |
| 1.0                        | N/A    | Initial version |

## IddCx version info for Windows 11 releases

| Build number | Release codename | Release name         | IddCx version | IddCxGetVersion returned |
| ------------ | ---------------- | -------------------- | ------------- | ------------------------ |
| 22631        | n/a              | Windows 11 23H2      | 1.10          | 0x1A00 |
| 22621        | SV2              | Windows 11 22H2      | 1.9           | 0x1900 |
| 22000        | SV1              | Windows 11 21H2      | 1.8           | 0x1800 |

## IddCx version info for Windows 10 releases

| Build number | Release codename | Release name         | IddCx version | IddCxGetVersion returned |
| ------------ | ---------------- | -------------------- | ------------- | ------------------------ |
| 19044        | 21H2             | Nov 2021 Update      | 1.5           | 0x1500 |
| 19043        | 21H1             | May 2021 Update      | 1.5           | 0x1500 |
| 19042        | 20H2             | October 2020 Update  | 1.5           | 0x1500 |
| 19041        | 20H1/Vb          | May 2020 Update      | 1.5           | 0x1500 |
| 18363        | 19H2             | Nov 2019 Update      | 1.4           | 0x1400 |
| 18362        | 19H1             | May 2019 Update      | 1.4           | 0x1400 |
| 17763        | RS5              | October 2018 Update  | 1.3           | 0x1380 |
| 17134        | RS4              | April 2018 Update    | 1.3           | 0x1300 |
| 16299        | RS3              | Fall Creators Update | 1.2           | 0x1200 |
| 15063        | RS2              | Creators Update      | 1.0           | N/A    |
| 14393        | RS1              | Anniversary Update   | 1.0           | N/A    |

## IddCx version info for Windows Server releases

| Build number | Release codename | Release name | IddCx version | IddCxGetVersion returned |
| ------------ | ---------------- | ------------ | ------------- | ------------------------ |
| 20348        | 21H1/Iron        | Server 2022  | 1.7           | 0x1700 |
| 19042        | 20H2             | Server 20H2  | 1.5           | 0x1500 |
| 18363        | 19H2             | Server 1909  | 1.4           | 0x1400 |
| 17763        | RS5              | Server 2019  | 1.3           | 0x1380 |
