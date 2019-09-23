---
title: Camera Control Properties
description: Camera Control Properties
ms.assetid: 36a57245-e89e-4418-b0c4-a4c1479413b2
keywords:
- camera control properties WDK video capture
- control properties WDK video capture
- PROPSETID_VIDCAP_CAMERACONTROL
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Camera Control Properties


The [PROPSETID\_VIDCAP\_CAMERACONTROL](https://docs.microsoft.com/windows-hardware/drivers/stream/propsetid-vidcap-cameracontrol) property set contains properties related to the control of video cameras. The following table describes the properties that are part of the PROPSETID\_VIDCAP\_CAMERACONTROL property set.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>PROPSETID_VIDCAP_CAMERACONTROL KS properties</th>
<th>Property description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-exposure" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_EXPOSURE&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-exposure)"><strong>KSPROPERTY_CAMERACONTROL_EXPOSURE</strong></a></p></td>
<td><p>Controls a camera's digital exposure time.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-focus" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_FOCUS&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-focus)"><strong>KSPROPERTY_CAMERACONTROL_FOCUS</strong></a></p></td>
<td><p>Controls a camera's focus setting.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-iris" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_IRIS&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-iris)"><strong>KSPROPERTY_CAMERACONTROL_IRIS</strong></a></p></td>
<td><p>Controls a camera's aperture setting.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-zoom" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_ZOOM&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-zoom)"><strong>KSPROPERTY_CAMERACONTROL_ZOOM</strong></a></p></td>
<td><p>Controls a camera's zoom setting.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-pan" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_PAN&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-pan)"><strong>KSPROPERTY_CAMERACONTROL_PAN</strong></a></p></td>
<td><p>Controls a camera's pan setting.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-roll" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_ROLL&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-roll)"><strong>KSPROPERTY_CAMERACONTROL_ROLL</strong></a></p></td>
<td><p>Controls a camera's roll setting.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-tilt" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_TILT&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-tilt)"><strong>KSPROPERTY_CAMERACONTROL_TILT</strong></a></p></td>
<td><p>Controls a camera's tilt setting.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-scanmode" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_SCANMODE&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-scanmode)"><strong>KSPROPERTY_CAMERACONTROL_SCANMODE</strong></a></p></td>
<td><p>Controls the scanning mode of a camera's sensor, such as interleaved, or non-interleaved.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-privacy" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_PRIVACY&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-privacy)"><strong>KSPROPERTY_CAMERACONTROL_PRIVACY</strong></a></p></td>
<td><p>Controls whether a camera sensor should capture video, or is prevented from capturing video.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-pantilt" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_PANTILT&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-pantilt)"><strong>KSPROPERTY_CAMERACONTROL_PANTILT</strong></a></p></td>
<td><p>Controls a camera's absolute pan and tilt setting.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-pan-relative" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_PAN_RELATIVE&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-pan-relative)"><strong>KSPROPERTY_CAMERACONTROL_PAN_RELATIVE</strong></a></p></td>
<td><p>Controls a camera's relative rotation about the vertical axis from its current value.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-tilt-relative" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_TILT_RELATIVE&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-tilt-relative)"><strong>KSPROPERTY_CAMERACONTROL_TILT_RELATIVE</strong></a></p></td>
<td><p>Controls a camera's relative rotation about the horizontal axis from its current position.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-roll-relative" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_ROLL_RELATIVE&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-roll-relative)"><strong>KSPROPERTY_CAMERACONTROL_ROLL_RELATIVE</strong></a></p></td>
<td><p>Controls a camera's relative rotation about the image viewing axis from its current value.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-zoom-relative" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_ZOOM_RELATIVE&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-zoom-relative)"><strong>KSPROPERTY_CAMERACONTROL_ZOOM_RELATIVE</strong></a></p></td>
<td><p>Controls a camera's relative zoom setting from its current value.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-exposure-relative" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_EXPOSURE_RELATIVE&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-exposure-relative)"><strong>KSPROPERTY_CAMERACONTROL_EXPOSURE_RELATIVE</strong></a></p></td>
<td><p>Controls a camera's relative shutter speed from its current value.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-iris-relative" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_IRIS_RELATIVE&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-iris-relative)"><strong>KSPROPERTY_CAMERACONTROL_IRIS_RELATIVE</strong></a></p></td>
<td><p>Specifies a camera's relative aperture setting from its current value.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-focus-relative" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_FOCUS_RELATIVE&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-focus-relative)"><strong>KSPROPERTY_CAMERACONTROL_FOCUS_RELATIVE</strong></a></p></td>
<td><p>Controls a camera's relative focus setting from its current value.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-pantilt-relative" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_PANTILT_RELATIVE&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-pantilt-relative)"><strong>KSPROPERTY_CAMERACONTROL_PANTILT_RELATIVE</strong></a></p></td>
<td><p>Controls a camera's relative pan and tilt setting from their current values.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-focal-length" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_FOCAL_LENGTH&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-focal-length)"><strong>KSPROPERTY_CAMERACONTROL_FOCAL_LENGTH</strong></a></p></td>
<td><p>Specifies a camera's focal length.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-auto-exposure-priority" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_AUTO_EXPOSURE_PRIORITY&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-auto-exposure-priority)"><strong>KSPROPERTY_CAMERACONTROL_AUTO_EXPOSURE_PRIORITY</strong></a></p></td>
<td><p>Specifies whether the device can dynamically vary the frame rate.</p></td>
</tr>
</tbody>
</table>

 

## Windows 8 extended camera control properties


Starting with Windows 8, these additional properties are supported for user-mode clients to get or set a camera's control settings. For more information, see [Extended Camera Control Properties](extended-camera-control-properties.md) and [How To Implement Extended Camera Control Properties](how-to-implement-extended-camera-control-properties.md).

| PROPSETID\_VIDCAP\_CAMERACONTROL KS properties                                                                                           | Property description                                                                                                  |
|------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| [**KSPROPERTY\_CAMERACONTROL\_FLASH\_PROPERTY**](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-flash-property)                                         | User-mode clients optionally use this property to get or set a camera's flash control characteristics.                |
| [**KSPROPERTY\_CAMERACONTROL\_IMAGE\_PIN\_CAPABILITY\_PROPERTY**](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-image-pin-capability-property)         | User-mode clients use this property to identify whether the camera's image pin and record pin are mutually exclusive. |
| [**KSPROPERTY\_CAMERACONTROL\_REGION\_OF\_INTEREST\_PROPERTY**](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-region-of-interest-property)             | User-mode clients optionally use this property to get or set a camera's region of interest characteristics.           |
| [**KSPROPERTY\_CAMERACONTROL\_VIDEO\_STABILIZATION\_MODE\_PROPERTY**](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-video-stabilization-mode-property) | User-mode clients optionally use this property to get or set a camera's video stabilization characteristics.          |

 

## <a href="" id="win8-1-extended-props"></a>Windows 8.1 extended camera control properties


Starting with Windows 8.1, the [KSPROPERTYSETID\_ExtendedCameraControl](https://docs.microsoft.com/windows-hardware/drivers/stream/kspropertysetid-extendedcameracontrol) property set provides additional controls for camera photo sequencing. For more info on how to implement these controls, see these topics:

-   [Extended Camera Control Properties](extended-camera-control-properties.md)
-   [How To Implement Extended Camera Control Properties](how-to-implement-extended-camera-control-properties.md)
-   [Extended Camera Control Payloads](extended-camera-control-payloads.md)
-   [Photo Sequence Mode](photo-sequence-mode.md)

 

 




