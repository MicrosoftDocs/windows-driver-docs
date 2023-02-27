---
title: KSPROPERTY\_CAMERACONTROL\_EXTENDED\_VIDEOTEMPORALDENOISING
description: KSPROPERTY\_CAMERACONTROL\_EXTENDED\_VIDEOTEMPORALDENOISING is used to control Video Temporal Denoising on the driver.
keywords: ["KSPROPERTY_CAMERACONTROL_EXTENDED_VIDEOTEMPORALDENOISING Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_CAMERACONTROL_EXTENDED_VIDEOTEMPORALDENOISING
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 04/03/2019
ms.custom: 19H1
---

# KSPROPERTY\_CAMERACONTROL\_EXTENDED\_VIDEOTEMPORALDENOISING

KSPROPERTY\_CAMERACONTROL\_EXTENDED\_VIDEOTEMPORALDENOISING is used to control Video Temporal Denoising on the driver.

## Overview

When operating a camera system in suboptimal light conditions, 3A statistic logic in the image signal processor (ISP) will tend to increase analog and digital gain to increase light sensitivity of the camera system to compensate for the lack of photons hitting the sensor at the imposed capture frame rate. This has the side effect of amplifying shot noise, which increases perceived noise in the frames produced by the sensor. This can still be apparent even after it has been processed through the ISP pipeline.

Aside from altering the image of the scene with chroma and luma aberrations, due to the stochastic nature of this shot noise, temporal incoherence of pixel values is particularly noticeable in video (preview or record) and can lead to a bad experience for the user.

The intent of Video Temporal Denoising (VTD) is to address noise and reduce temporal incoherence of noisy pixels by accumulating and combining information from multiple frames to produce a cleaner output frame in a time-constrained context where frame latency matters such as with a video source.

This additional processing is meant to be executing in a real-time fashion with very minimal delay to enhance image quality without blocking the user from operating the camera normally and without requiring any post-processing steps.

## Usage summary table

| Scope | Control | Type |
| --- | --- | --- |
| Version 1 | Filter | Synchronous |

The following are flags that can be placed in the KSCAMERA\_EXTENDEDPROP\_HEADER.Flags field to control Video Temporal Denoising on the driver.

```cpp
#define KSCAMERA_EXTENDEDPROP_VIDEOTEMPORALDENOISING_AUTO   0x0000000000000001
#define KSCAMERA_EXTENDEDPROP_VIDEOTEMPORALDENOISING_OFF    0x0000000000000002
#define KSCAMERA_EXTENDEDPROP_VIDEOTEMPORALDENOISING_ON     0x0000000000000004
```

If the driver supports this control, it must at the very least support either VIDEOTEMPORALDENOISING_AUTO or both VIDEOTEMPORALDENOISING_ON and VIDEOTEMPORALDENOISING_OFF.

If the driver does not support Video Temporal Denoising, the driver should not implement this control.

This is a synchronous control that can be controlled dynamically while streaming from all supported pins.  

The following table describes the flag capabilities.

| Flag | Description |
| --- | --- |
| KSCAMERA_EXTENDEDPROP_VIDEOTEMPORALDENOISING_AUTO | This is a mandatory capability if KSCAMERA_EXTENDEDPROP_VIDEOTEMPORALDENOISING_OFF and KSCAMERA_EXTENDEDPROP_VIDEOTEMPORALDENOISING_ON are not supported. When specified, Video Temporal Denoising is automatically enabled or disabled in the driver and affects all supported pins streaming pixels in the visible spectrum of light. While this is not guaranteeing actual processing of frames at all time, this implies that it may take place at the implementer’s discretions given the video signal passing through the ISP. |
| KSCAMERA_EXTENDEDPROP_VIDEOTEMPORALDENOISING_OFF | This is a mandatory capability if KSCAMERA_EXTENDEDPROP_VIDEOTEMPORALDENOISING_AUTO is not supported and optional if it is. When specified, Video Temporal Denoising is disabled in the driver at all time for all supported pins streaming pixels in the visible spectrum of light. |
| KSCAMERA_EXTENDEDPROP_VIDEOTEMPORALDENOISING_ON | This is a mandatory capability if KSCAMERA_EXTENDEDPROP_VIDEOTEMPORALDENOISING_AUTO is not supported and optional if it is. When specified, Video Temporal Denoising is enabled in the driver at all time for all supported pins streaming pixels in the visible spectrum of light. |

The table below contains the descriptions and requirements for the [**KSCAMERA\_EXTENDEDPROP\_HEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) structure fields when using the control.

| Member | Description |
| --- | --- |
| Version | Must be 1. |
| PinId | Must be KSCAMERA_EXTENDEDPROP_FILTERSCOPE (0xFFFFFFFF). |
| Size | Must be sizeof(KSCAMERA_EXTENDEDPROP_HEADER)+ sizeof(KSCAMERA_EXTENDEDPROP_VALUE ). |
| Result | Indicates the error results of the last SET operation.  If no SET operation has taken place, this must be 0. |
| Capability | Must be a bitwise OR of the supported KSCAMERA_EXTENDEDPROP_VIDEOTEMPORALDENOISING_* flags defined above. |
| Flags | This is a read/write field.  This must be any one of the KSCAMERA_EXTENDEDPROP_VIDEOTEMPORALDENOISING_XXX flags defined above. Note that these flags are mutually exclusive and can not be set in any bitwise OR combination. |

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
