---
title: Updates for IddCx versions 1.8 and later
description: IddCx version 1.8 updates for console and remote indirect display drivers
ms.date: 08/09/2022
keywords:
- IddCx version 1.8
- Console and remote indirect display driver, IddCx versions 1.8 and later
- Console and remote IDD, IddCx versions 1.8 and later
- Console indirect display driver
- Console IDD
- Remote indirect display driver
- Remote IDD
---

# Updates for IddCx versions 1.8 and later

This page describes the changes made in IddCx 1.8. A single indirect display driver (IDD) binary built against IddCx 1.8 can run on Windows 10, version 1803 and above using runtime checks to verify whether DDI changes in IddCx 1.8 are available on that system. See [Building a WDF driver for multiple versions of Windows](/windows-hardware/drivers/wdf/building-a-wdf-driver-for-multiple-versions-of-windows) for more info.

## Updated IddCxGetVersion version

The IddCx version returned by [**IddCxGetVersion**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxgetversion) on Windows 11 was updated to IDDCX_VERSION_COBALT (0x1800).

## IDDCX_ADAPTER_FLAGS_PREFER_PRECISE_PRESENT_REGIONS flag was added

The **IDDCX_ADAPTER_FLAGS_PREFER_PRECISE_PRESENT_REGIONS** adapter flag was added to [**IDDCX_ADAPTER_FLAGS**](/windows-hardware/drivers/ddi/iddcx/ne-iddcx-iddcx_adapter_flags). A driver that sets this flag is requesting the OS to track dirty regions of the desktop updates more accurately. This more accurate tracking will have a small CPU usage overhead so drivers should only set this flag if smaller dirty regions will be beneficial to the driver.

## Defining logical operators for IddCx flags

The WDK's **DEFINE_ENUM_FLAG_OPERATORS** macro defines operator overloads to enable bit operations on enum values that are used to define flags. Starting in IddCx 1.8, *Iddcx.h* use this macro to define flag operators for the following enums:

* [**IDDCX_ADAPTER_FLAGS**](/windows-hardware/drivers/ddi/iddcx/ne-iddcx-iddcx_adapter_flags)
* [**IDDCX_PATH_FLAGS**](/windows-hardware/drivers/ddi/iddcx/ne-iddcx-iddcx_path_flags)
* [**IDDCX_FRAME_STATISTICS_FLAGS**](/windows-hardware/drivers/ddi/iddcx/ne-iddcx-iddcx_frame_statistics_flags)

If the source code for an Indirect Display driver already defines operators for these enums then it might encounter build breaks using the new header file. In that case the driver-defined versions should be removed so the *IddCx.h* versions can be used.
