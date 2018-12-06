---
title: Setting up Video Adapter Access Ranges
description: Setting up Video Adapter Access Ranges
ms.assetid: 250c5611-c6f5-49b5-94bc-93a1b43312e6
keywords:
- video adapter access ranges WDK video miniport
- ranges WDK video miniport
- logical range addresses WDK video miniport
- adapter access ranges WDK video miniport
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Setting up Video Adapter Access Ranges


## <span id="ddk_setting_up_video_adapter_access_ranges_gg"></span><span id="DDK_SETTING_UP_VIDEO_ADAPTER_ACCESS_RANGES_GG"></span>


An array of [**VIDEO\_ACCESS\_RANGE**](https://msdn.microsoft.com/library/windows/hardware/ff570498)-type elements describes one or more ranges of memory and/or I/O ports that a video adapter decodes. Each access range element in this array contains bus-relative physical address values.

The miniport driver's [*HwVidFindAdapter*](https://msdn.microsoft.com/library/windows/hardware/ff567332) routine must claim all PCI memory and ports or ranges of ports that the adapter will respond to. Depending on the adapter and the **AdapterInterfaceType** value in [**VIDEO\_PORT\_CONFIG\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff570531), *HwVidFindAdapter* can call some of the following **VideoPort***Xxx* functions to get the necessary bus-relative configuration data:

[**VideoPortGetAccessRanges**](https://msdn.microsoft.com/library/windows/hardware/ff570302)

[**VideoPortGetBusData**](https://msdn.microsoft.com/library/windows/hardware/ff570306)

[**VideoPortGetDeviceData**](https://msdn.microsoft.com/library/windows/hardware/ff570311)

[**VideoPortGetRegistryParameters**](https://msdn.microsoft.com/library/windows/hardware/ff570316)

[**VideoPortVerifyAccessRanges**](https://msdn.microsoft.com/library/windows/hardware/ff570377)

If *HwVidFindAdapter* cannot get bus-relative access ranges information by calling **VideoPortGetBusData** or **VideoPortGetAccessRanges**, or from the registry with **VideoPortGetDeviceData** or **VideoPortGetRegistryParameters**, the miniport driver should have a set of bus-relative default values for access ranges.

Every *HwVidFindAdapter* function must map each claimed bus-relative physical address range to a range in kernel-mode address space with [**VideoPortGetDeviceBase**](https://msdn.microsoft.com/library/windows/hardware/ff570310) before the miniport driver attempts to communicate with an adapter. The HAL can remap bus-relative access range values to [*system space*](https://msdn.microsoft.com/library/windows/hardware/ff556336#wdkgloss-system-space) logical address ranges, particularly in multiple bus machines.

With mapped logical range addresses, the driver can call the **VideoPortRead***Xxx* and **VideoPortWrite***Xxx* functions to read from or write to an adapter. These kernel-mode addresses also can be passed to [**VideoPortCompareMemory**](https://msdn.microsoft.com/library/windows/hardware/ff570285), [**VideoPortMoveMemory**](https://msdn.microsoft.com/library/windows/hardware/ff570332), [**VideoPortZeroDeviceMemory**](https://msdn.microsoft.com/library/windows/hardware/ff570492), and/or [**VideoPortZeroMemory**](https://msdn.microsoft.com/library/windows/hardware/ff570493). For a mapped range in I/O space, the miniport driver calls the **VideoPortReadPort***Xxx* and **VideoPortWritePort***Xxx* functions. For a mapped range in memory, the miniport driver calls the **VideoPortReadRegister***Xxx* and **VideoPortWriteRegister***Xxx* functions.

The [*HwVidFindAdapter*](https://msdn.microsoft.com/library/windows/hardware/ff567332) function *must always* call [**VideoPortVerifyAccessRanges**](https://msdn.microsoft.com/library/windows/hardware/ff570377) or [**VideoPortGetAccessRanges**](https://msdn.microsoft.com/library/windows/hardware/ff570302) successfully *before* it calls [**VideoPortGetDeviceBase**](https://msdn.microsoft.com/library/windows/hardware/ff570310).

-   Any successful call to **VideoPortVerifyAccessRanges** or **VideoPortGetAccessRanges** establishes a miniport driver's claim on bus-specific video memory and register addresses or I/O ports for its adapter in the registry. It is critical to note, however, that any subsequent call to **VideoPortVerifyAccessRanges** or **VideoPortGetAccessRanges** will cause that driver's previously claimed resources to be erased and replaced with the ranges passed to the most recently called function. Therefore, if a driver claims ranges by separate calls to these functions, it must pass in all range arrays, including those already claimed.

-   *HwVidFindAdapter* can claim a small set of access ranges for an adapter, use this set to determine whether the adapter is one that the miniport driver supports, and claim a full set of access ranges for a supported adapter with another call to **VideoPortGetAccessRanges** or **VideoPortVerifyAccessRanges**. Again, each successful call to these **VideoPort..AccessRanges** routines for a particular adapter overwrites the caller's previous claims in the registry.

-   To claim other types of hardware resources, such as an interrupt vector, a miniport driver should set appropriate values in the VIDEO\_PORT\_CONFIG\_INFO and call **VideoPortVerifyAccessRanges**, or it should call **VideoPortGetAccessRanges**.

-   Calling **VideoPortGetAccessRanges** or **VideoPortVerifyAccessRanges** successfully ensures that a miniport driver does not try to use register or device memory addresses already in use by another driver.

-   Claiming an adapter's bus-relative hardware resources in the registry prevents drivers that load later from attempting to use the same access ranges (and other hardware resources) for their adapters. It also prevents a subsequently loaded driver from changing the initialized state of the video adapter.

The miniport driver of hardware that decodes legacy resources must claim these resources in its **DriverEntry** routine, or if implemented, its *HwVidLegacyResources* routine. Legacy resources are those resources not listed in the device's PCI configuration space but that are decoded by the device. See [Claiming Legacy Resources](claiming-legacy-resources.md) for details.

After a miniport driver is loaded and its [*HwVidInitialize*](https://msdn.microsoft.com/library/windows/hardware/ff567345) function is run, the miniport driver's [*HwVidStartIO*](https://msdn.microsoft.com/library/windows/hardware/ff567367) function is called to map any access range of video memory that the miniport driver makes visible to its corresponding display driver.

 

 





