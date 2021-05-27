---
title: DriverEntry of Video Miniport Driver function
description: DriverEntry is the initial entry point into the video miniport driver.
keywords: ["DriverEntry function Display Devices"]
topic_type:
- apiref
api_name:
- DriverEntry
api_location:
- NtosKrnl.exe
api_type:
- DllExport
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# DriverEntry of Video Miniport Driver function


**DriverEntry** is the initial entry point into the video miniport driver.

## Syntax

```cpp
ULONG DriverEntry(
  _In_ PVOID Context1,
  _In_ PVOID Context2
);
```

## Parameters

*Context1* \[in\]
Pointer to a context value with which the miniport driver must call [**VideoPortInitialize**](/windows-hardware/drivers/ddi/video/nf-video-videoportinitialize). This context value identifies the driver object created by the system for this miniport driver.

*Context2* \[in\]
Pointer to a second context value with which the miniport driver must call [**VideoPortInitialize**](/windows-hardware/drivers/ddi/video/nf-video-videoportinitialize). This context value identifies the registry path for this miniport driver.

## Return value

**DriverEntry** returns the value returned by [**VideoPortInitialize**](/windows-hardware/drivers/ddi/video/nf-video-videoportinitialize).

## Remarks

Each miniport driver must have a function explicitly named **DriverEntry** in order to be loaded. **DriverEntry** is called directly by the I/O system.

**DriverEntry** must perform the following steps:

-   Allocate memory on the stack for a [**VIDEO\_HW\_INITIALIZATION\_DATA**](/windows-hardware/drivers/ddi/video/ns-video-_video_hw_initialization_data) structure, and call [**VideoPortZeroMemory**](/windows-hardware/drivers/ddi/video/nf-video-videoportzeromemory) to zero-initialize it.

-   Fill in driver-specific and adapter-specific values in the VIDEO\_HW\_INITIALIZATION\_DATA members, including the miniport driver's entry points. The following entry points must be set to a miniport driver-supplied routine:

    [*HwVidFindAdapter*](/windows-hardware/drivers/ddi/video/nc-video-pvideo_hw_find_adapter)

    [*HwVidInitialize*](/windows-hardware/drivers/ddi/video/nc-video-pvideo_hw_initialize)

    [*HwVidStartIO*](/windows-hardware/drivers/ddi/video/nc-video-pvideo_hw_start_io)

    [*HwVidInterrupt*](/windows-hardware/drivers/ddi/video/nc-video-pvideo_hw_interrupt)

    [*HwVidQueryInterface*](/windows-hardware/drivers/ddi/video/nc-video-pvideo_hw_query_interface)

    [*HwVidGetVideoChildDescriptor*](/windows-hardware/drivers/ddi/video/nc-video-pvideo_hw_get_child_descriptor)

    [*HwVidGetPowerState*](/windows-hardware/drivers/ddi/video/nc-video-pvideo_hw_power_get)

    [*HwVidSetPowerState*](/windows-hardware/drivers/ddi/video/nc-video-pvideo_hw_power_set)

-   If the driver's hardware supports legacy resources, the driver must report them. **DriverEntry** should do the following if the resource list is known at driver compile time:

    -   Claim and report all such resources in the **HwLegacyResourceList** and **HwLegacyResourceCount** members of the [**VIDEO\_HW\_INITIALIZATION\_DATA**](/windows-hardware/drivers/ddi/video/ns-video-_video_hw_initialization_data) structure. Legacy resources are those resources not listed in the device's PCI configuration space but that are decoded by the device.
    -   Fill in the **RangePassive** field accordingly for each [**VIDEO\_ACCESS\_RANGE**](/windows-hardware/drivers/ddi/video/ns-video-_video_access_range) structure defined in the miniport driver.

    If the legacy resource list cannot be determined until run time, the driver should instead implement a [*HwVidLegacyResources*](/windows-hardware/drivers/ddi/video/nc-video-pvideo_hw_legacyresources) function to report them.

-   Call [**VideoPortInitialize**](/windows-hardware/drivers/ddi/video/nf-video-videoportinitialize), passing *Context1* and *Context2* as the first two parameters, a pointer to the VIDEO\_HW\_INITIALIZATION\_DATA structure as the third parameter, and **NULL** as the fourth parameter.

**DriverEntry** should propagate the value returned by [**VideoPortInitialize**](/windows-hardware/drivers/ddi/video/nf-video-videoportinitialize) back to the caller.

If **DriverEntry** does claim resources, it should include only those resources that the hardware decodes but that are not claimed by PCI. The miniport driver can "reclaim" these legacy resources again in subsequent call(s) to [**VideoPortVerifyAccessRanges**](/windows-hardware/drivers/ddi/video/nf-video-videoportverifyaccessranges); however, the video port driver will just ignore requests for any such previously claimed resources. Power management and docking will be disabled in the system if the miniport driver attempts to claim a legacy access range in **VideoPortVerifyAccessRanges** that was not previously claimed in the **HwLegacyResourceList** member of the [**VIDEO\_HW\_INITIALIZATION\_DATA**](/windows-hardware/drivers/ddi/video/ns-video-_video_hw_initialization_data) structure during **DriverEntry** (or in [*HwVidLegacyResources*](/windows-hardware/drivers/ddi/video/nc-video-pvideo_hw_legacyresources), if implemented).

For Microsoft Windows 2000 and later drivers that also support computers running Windows NT 4.0, hardware configuration constants are defined in *video.h*. These constants are described in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Constant</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>SIZE_OF_NT4_VIDEO_PORT_CONFIG_INFO</p></td>
<td align="left"><p>The size, in bytes, of the Windows NT 4.0 <a href="/windows-hardware/drivers/ddi/video/ns-video-_video_port_config_info" data-raw-source="[&lt;strong&gt;VIDEO_PORT_CONFIG_INFO&lt;/strong&gt;](/windows-hardware/drivers/ddi/video/ns-video-_video_port_config_info)"><strong>VIDEO_PORT_CONFIG_INFO</strong></a> structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p>SIZE_OF_NT4_VIDEO_HW_INITIALIZATION_DATA</p></td>
<td align="left"><p>The size, in bytes, of the Windows NT 4.0 <a href="/windows-hardware/drivers/ddi/video/ns-video-_video_hw_initialization_data" data-raw-source="[&lt;strong&gt;VIDEO_HW_INITIALIZATION_DATA&lt;/strong&gt;](/windows-hardware/drivers/ddi/video/ns-video-_video_hw_initialization_data)"><strong>VIDEO_HW_INITIALIZATION_DATA</strong></a> structure. If <a href="/windows-hardware/drivers/ddi/video/nf-video-videoportinitialize" data-raw-source="[&lt;strong&gt;VideoPortInitialize&lt;/strong&gt;](/windows-hardware/drivers/ddi/video/nf-video-videoportinitialize)"><strong>VideoPortInitialize</strong></a> fails, the video miniport driver should set the <strong>HwInitDataSize</strong> member of the VIDEO_HW_INITIALIZATION_DATA structure to the size of either the Windows 2000 (and later) version of this structure or the Windows NT 4.0 version. Choose the appropriate structure size to match the operating system version on which the miniport driver will run. The video miniport driver should then call <strong>VideoPortInitialize</strong> again. For an example of use, please see the video miniport driver samples that were included in the Windows Driver Development Kit (DDK).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>SIZE_OF_W2K_VIDEO_HW_INITIALIZATION_DATA</p></td>
<td align="left"><p>The size, in bytes, of the Windows 2000 and later <a href="/windows-hardware/drivers/ddi/video/ns-video-_video_hw_initialization_data" data-raw-source="[&lt;strong&gt;VIDEO_HW_INITIALIZATION_DATA&lt;/strong&gt;](/windows-hardware/drivers/ddi/video/ns-video-_video_hw_initialization_data)"><strong>VIDEO_HW_INITIALIZATION_DATA</strong></a> structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p>SIZE_OF_WXP_VIDEO_HW_INITIALIZATION_DATA</p></td>
<td align="left"><p>The size, in bytes, of the Windows Vista and later <a href="/windows-hardware/drivers/ddi/video/ns-video-_video_hw_initialization_data" data-raw-source="[&lt;strong&gt;VIDEO_HW_INITIALIZATION_DATA&lt;/strong&gt;](/windows-hardware/drivers/ddi/video/ns-video-_video_hw_initialization_data)"><strong>VIDEO_HW_INITIALIZATION_DATA</strong></a> structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>SIZE_OF_WXP_VIDEO_PORT_CONFIG_INFO</p></td>
<td align="left"><p>The size, in bytes, of the Windows Vista <a href="/windows-hardware/drivers/ddi/video/ns-video-_video_port_config_info" data-raw-source="[&lt;strong&gt;VIDEO_PORT_CONFIG_INFO&lt;/strong&gt;](/windows-hardware/drivers/ddi/video/ns-video-_video_port_config_info)"><strong>VIDEO_PORT_CONFIG_INFO</strong></a> structure.</p></td>
</tr>
</tbody>
</table>

 

**DriverEntry** should be made pageable.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Target platform</p></td>
<td align="left">Desktop</td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Video.h (include Video.h)</td>
</tr>
<tr class="odd">
<td align="left"><p>Library</p></td>
<td align="left">NtosKrnl.lib</td>
</tr>
<tr class="even">
<td align="left"><p>DLL</p></td>
<td align="left">NtosKrnl.exe</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[*HwVidFindAdapter*](/windows-hardware/drivers/ddi/video/nc-video-pvideo_hw_find_adapter)

[*HwVidLegacyResources*](/windows-hardware/drivers/ddi/video/nc-video-pvideo_hw_legacyresources)

[**VIDEO\_HW\_INITIALIZATION\_DATA**](/windows-hardware/drivers/ddi/video/ns-video-_video_hw_initialization_data)

[**VideoPortInitialize**](/windows-hardware/drivers/ddi/video/nf-video-videoportinitialize)

[**VideoPortVerifyAccessRanges**](/windows-hardware/drivers/ddi/video/nf-video-videoportverifyaccessranges)

[**VideoPortZeroMemory**](/windows-hardware/drivers/ddi/video/nf-video-videoportzeromemory)

