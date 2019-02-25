---
title: KSPROPERTY\_CAMERACONTROL\_EXTENDED\_OPTIMIZATIONHINT
description: KSPROPERTY\_CAMERACONTROL\_EXTENDED\_OPTIMIZATIONHINT is used to control the primary use case of photo capture vs. video capture. In Windows 10, this control is extended to support expanded hardware optimization hints.
ms.assetid: 1E2787B7-4BC2-4FBC-8909-ACB122B87F08
keywords: ["KSPROPERTY_CAMERACONTROL_EXTENDED_OPTIMIZATIONHINT Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CAMERACONTROL_EXTENDED_OPTIMIZATIONHINT
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 09/10/2018
ms.localizationpriority: medium
---

# KSPROPERTY\_CAMERACONTROL\_EXTENDED\_OPTIMIZATIONHINT

KSPROPERTY\_CAMERACONTROL\_EXTENDED\_OPTIMIZATIONHINT is used to control the primary use case of photo capture vs. video capture. In Windows 10, this control is extended to support expanded hardware optimization hints.

## Usage summary table

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Scope</th>
<th>Control</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Version 1</p></td>
<td><p>Filter</p></td>
<td><p>Synchronous</p></td>
</tr>
</tbody>
</table>

The following flags can be placed in the KSCAMERA\_EXTENDEDPROP\_HEADER.Flags field to hardware optimization hints in the driver.

The PHOTO and VIDEO hints will continue to be used to specify the primary use case.

For Windows 10, additional bit flags aid the tradeoff of quality, speed, and power consumption in the driver. By default, the driver should have KSCAMERA\_EXTENDEDPROP\_OPTIMIZATION\_PHOTO.

```cpp
#define KSCAMERA_EXTENDEDPROP_OPTIMIZATION_DEFAULT      0x0000000000000000
#define KSCAMERA_EXTENDEDPROP_OPTIMIZATION_PHOTO        0x0000000000000001
#define KSCAMERA_EXTENDEDPROP_OPTIMIZATION_VIDEO        0x0000000000000002
#define KSCAMERA_EXTENDEDPROP_OPTIMIZATION_QUALITY      0x0000000000000004
#define KSCAMERA_EXTENDEDPROP_OPTIMIZATION_LATENCY      0x0000000000000008
#define KSCAMERA_EXTENDEDPROP_OPTIMIZATION_POWER        0x0000000000000010
```

f the driver supports this control, it must support KSCAMERA\_EXTENDEDPROP\_OPTIMIZATION\_PHOTO and KSCAMERA\_EXTENDEDPROP\_OPTIMIZATION\_VIDEO.

If the driver does not support optimization hints, the driver should not implement this control.

The following table describes the flag capabilities.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Flag</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>KSCAMERA_EXTENDEDPROP_OPTIMIZATION_DEFAULT</p></td>
<td><p>This is a mandatory capability. When specified, the driver should clear up the hints previously set on the driver and apply the driver’s default power, quality, latency tradeoff.</p></td>
</tr>
<tr class="even">
<td><p>KSCAMERA_EXTENDEDPROP_OPTIMIZATION_PHOTO</p></td>
<td><p>This is a mandatory capability. When specified, the primary use case is photo capture and the driver shall prioritize the photo capture over the video recording. This flag can be specified when the preview pin is in the stopped state to select a sensor mode in favor of photo quality, or in the running state for photo capture during video recording only. When specified for photo capture during video recording, glitch in video stream is acceptable in favor of better photo quality. This flag is mutually exclusive with the VIDEO flag and can be used with any one or two of the QUALITY, LATENCY, and POWER flags.</p></td>
</tr>
<tr class="odd">
<td><p>KSCAMERA_EXTENDEDPROP_OPTIMIZATION_VIDEO</p></td>
<td><p>This is a mandatory capability. When specified, the primary use case is video capture and the driver shall prioritize the video recording over the photo capture. This flag can be specified when the preview pin is in the stopped state to select a sensor mode in favor of video recording, or in the running state for photo capture during video recording only. When specified for photo capture during video recording, glitch in video stream is not allowed. This flag is mutually exclusive with the PHOTO flag and can be used with any one or two of the QUALITY, LATENCY, and POWER flags.</p></td>
</tr>
<tr class="even">
<td><p>KSCAMERA_EXTENDEDPROP_OPTIMIZATION_QUALITY</p></td>
<td><p>This capability is optional. When specified, the driver shall optimize the image quality for the photo capture and the video quality for the video recording. This flag can be specified before the photo capture (including regular photo, VPS, and PS without history frames) and/or video recording starts, or when the pin is in the stopped state. This flag can be used with the PHOTO flag, or with LATENCY or POWER flags along with the VIDEO flag.</p></td>
</tr>
<tr class="odd">
<td><p>KSCAMERA_EXTENDEDPROP_OPTIMIZATION_LATENCY</p></td>
<td><p>This capability is optional. When specified, the driver shall optimize the speed and latency for the photo capture and the video recording. This flag can be specified before the photo capture (including regular photo, VPS, and PS without history frames) and\or video recording starts, or when the pin is in the stopped state. This flag can be used with the PHOTO flag, or with QUALITY or POWER flags along with the VIDEO flag.</p></td>
</tr>
<tr class="even">
<td><p>KSCAMERA_EXTENDEDPROP_OPTIMIZATION_POWER</p></td>
<td><p>This capability is optional. When specified, the driver shall optimize the power consumption for the photo capture and the video recording. This flag can be specified before the photo capture (including regular photo, VPS, and PS without history) and/or video recording starts, or when the pin is in the stopped state. This flag can be used with the QUALITY or LATENCY flag, along with the VIDEO flag.</p></td>
</tr>
</tbody>
</table>

The following table contains the descriptions and requirements for the [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) structure fields when using the control.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Member</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>This must be 1.</p></td>
</tr>
<tr class="even">
<td><p>PinId</p></td>
<td><p>Must be KSCAMERA_EXTENDEDPROP_FILTERSCOPE (0xFFFFFFFF).</p></td>
</tr>
<tr class="odd">
<td><p>Size</p></td>
<td><p>This must be sizeof(KSCAMERA_EXTENDEDPROP_HEADER) + sizeof(KSCAMERA_EXTENDEDPROP_VALUE).</p></td>
</tr>
<tr class="even">
<td><p>Result</p></td>
<td><p>Indicates the error results of the last SET operation. If no SET operation has taken place, this must be 0.</p></td>
</tr>
<tr class="odd">
<td><p>Capability</p></td>
<td><p>Must be a bitwise OR of the supported KSCAMERA_EXTENDEDPROP_OPTIMIZATION_* flags as defined above.</p></td>
</tr>
<tr class="even">
<td><p>Flags</p></td>
<td><p>This is a read/write field. This can be any valid combinations of the supported KSCAMERA_EXTENDEDPROP_OPTIMIZATION_* flags defined above.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

Keep the following items in mind when using optimization hints:

-   QUALITY/LATENCY/POWER and PHOTO/VIDEO are two sets of independent hints. They can be specified together at the same time or independently at different time. Setting QUALITY/LATENCY/POWER does not overwrite PHOTO/VIDEO and vice versa. When specified at different time, the driver should return the current settings of both sets of hints in a GET call.

-   For QUALITY/LATENCY/POWER, when hints are set, the driver should optimize within its constraints. If no optimization is available, the driver should ignore the hints.

-   When two hints are specified at the same time for the video use case, the optimization of each hint may be less than when only one hint is specified. More specifically:

    -   LATENCY takes precedence over QUALITY or POWER when QUALITY or POWER is also specified. In such cases, the quality may be less than when only QUALITY is specified, and the power consumption may be higher than when only POWER is specified.

    -   When both QUALITY and POWER are specified, the quality may be less than when only QUALITY is specified, and the power consumption may be higher than when only POWER is specified.

-   An optimization hint is only served as a hint to the driver to facilitate the processing tradeoffs in 3A, ISP processing, sensor selection, etc., within the constraints of the capture scenarios specified by the application. It is important for the app developer to select and configure the most suitable controls and APIs for a specific capture scenario in order to achieve the best results. Otherwise, the optimization hints alone may have a diminished effect. For example, for high quality photo capture, VPS or LowLagPhoto/TakePhoto should be used instead of PS on certain IHV platforms in order to make use of the QUALITY hint. Similarly, video stabilization should be disabled if even lower latency or power consumption is desired.

-   Optimization hints shall be ignored if received at the time/state other than what is specified under each capability flag.

When the video stabilization control is also enabled on the driver (ON or AUTO):

-   The driver may apply the lowest aggressive video stabilization which includes low latency and/or low power video stabilization algorithm to reduce the processing latency and/or power consumption if the LATENCY and/or POWER hint is set. When video stabilization is set to AUTO, the driver may turn off video stabilization to further reduce the latency and/or power consumption.

-   The driver may apply the highest aggressive video stabilization to improve the video quality if the QUALITY hint is set.


## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Ksmedia.h</td>
</tr>
</tbody>
</table>
