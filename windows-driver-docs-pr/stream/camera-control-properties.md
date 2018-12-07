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


The [PROPSETID\_VIDCAP\_CAMERACONTROL](https://msdn.microsoft.com/library/windows/hardware/ff567802) property set contains properties related to the control of video cameras. The following table describes the properties that are part of the PROPSETID\_VIDCAP\_CAMERACONTROL property set.

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
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564401" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_EXPOSURE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564401)"><strong>KSPROPERTY_CAMERACONTROL_EXPOSURE</strong></a></p></td>
<td><p>Controls a camera&#39;s digital exposure time.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564410" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_FOCUS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564410)"><strong>KSPROPERTY_CAMERACONTROL_FOCUS</strong></a></p></td>
<td><p>Controls a camera&#39;s focus setting.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564415" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_IRIS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564415)"><strong>KSPROPERTY_CAMERACONTROL_IRIS</strong></a></p></td>
<td><p>Controls a camera&#39;s aperture setting.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564459" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_ZOOM&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564459)"><strong>KSPROPERTY_CAMERACONTROL_ZOOM</strong></a></p></td>
<td><p>Controls a camera&#39;s zoom setting.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564424" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_PAN&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564424)"><strong>KSPROPERTY_CAMERACONTROL_PAN</strong></a></p></td>
<td><p>Controls a camera&#39;s pan setting.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564432" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_ROLL&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564432)"><strong>KSPROPERTY_CAMERACONTROL_ROLL</strong></a></p></td>
<td><p>Controls a camera&#39;s roll setting.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564454" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_TILT&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564454)"><strong>KSPROPERTY_CAMERACONTROL_TILT</strong></a></p></td>
<td><p>Controls a camera&#39;s tilt setting.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564452" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_SCANMODE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564452)"><strong>KSPROPERTY_CAMERACONTROL_SCANMODE</strong></a></p></td>
<td><p>Controls the scanning mode of a camera&#39;s sensor, such as interleaved, or non-interleaved.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564430" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_PRIVACY&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564430)"><strong>KSPROPERTY_CAMERACONTROL_PRIVACY</strong></a></p></td>
<td><p>Controls whether a camera sensor should capture video, or is prevented from capturing video.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564425" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_PANTILT&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564425)"><strong>KSPROPERTY_CAMERACONTROL_PANTILT</strong></a></p></td>
<td><p>Controls a camera&#39;s absolute pan and tilt setting.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564429" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_PAN_RELATIVE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564429)"><strong>KSPROPERTY_CAMERACONTROL_PAN_RELATIVE</strong></a></p></td>
<td><p>Controls a camera&#39;s relative rotation about the vertical axis from its current value.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564456" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_TILT_RELATIVE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564456)"><strong>KSPROPERTY_CAMERACONTROL_TILT_RELATIVE</strong></a></p></td>
<td><p>Controls a camera&#39;s relative rotation about the horizontal axis from its current position.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564435" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_ROLL_RELATIVE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564435)"><strong>KSPROPERTY_CAMERACONTROL_ROLL_RELATIVE</strong></a></p></td>
<td><p>Controls a camera&#39;s relative rotation about the image viewing axis from its current value.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564460" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_ZOOM_RELATIVE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564460)"><strong>KSPROPERTY_CAMERACONTROL_ZOOM_RELATIVE</strong></a></p></td>
<td><p>Controls a camera&#39;s relative zoom setting from its current value.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564404" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_EXPOSURE_RELATIVE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564404)"><strong>KSPROPERTY_CAMERACONTROL_EXPOSURE_RELATIVE</strong></a></p></td>
<td><p>Controls a camera&#39;s relative shutter speed from its current value.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564417" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_IRIS_RELATIVE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564417)"><strong>KSPROPERTY_CAMERACONTROL_IRIS_RELATIVE</strong></a></p></td>
<td><p>Specifies a camera&#39;s relative aperture setting from its current value.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564413" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_FOCUS_RELATIVE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564413)"><strong>KSPROPERTY_CAMERACONTROL_FOCUS_RELATIVE</strong></a></p></td>
<td><p>Controls a camera&#39;s relative focus setting from its current value.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564427" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_PANTILT_RELATIVE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564427)"><strong>KSPROPERTY_CAMERACONTROL_PANTILT_RELATIVE</strong></a></p></td>
<td><p>Controls a camera&#39;s relative pan and tilt setting from their current values.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564406" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_FOCAL_LENGTH&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564406)"><strong>KSPROPERTY_CAMERACONTROL_FOCAL_LENGTH</strong></a></p></td>
<td><p>Specifies a camera&#39;s focal length.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564399" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_AUTO_EXPOSURE_PRIORITY&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564399)"><strong>KSPROPERTY_CAMERACONTROL_AUTO_EXPOSURE_PRIORITY</strong></a></p></td>
<td><p>Specifies whether the device can dynamically vary the frame rate.</p></td>
</tr>
</tbody>
</table>

 

## Windows 8 extended camera control properties


Starting with Windows 8, these additional properties are supported for user-mode clients to get or set a camera's control settings. For more information, see [Extended Camera Control Properties](extended-camera-control-properties.md) and [How To Implement Extended Camera Control Properties](how-to-implement-extended-camera-control-properties.md).

| PROPSETID\_VIDCAP\_CAMERACONTROL KS properties                                                                                           | Property description                                                                                                  |
|------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| [**KSPROPERTY\_CAMERACONTROL\_FLASH\_PROPERTY**](https://msdn.microsoft.com/library/windows/hardware/jj156041)                                         | User-mode clients optionally use this property to get or set a camera's flash control characteristics.                |
| [**KSPROPERTY\_CAMERACONTROL\_IMAGE\_PIN\_CAPABILITY\_PROPERTY**](https://msdn.microsoft.com/library/windows/hardware/jj553706)         | User-mode clients use this property to identify whether the camera's image pin and record pin are mutually exclusive. |
| [**KSPROPERTY\_CAMERACONTROL\_REGION\_OF\_INTEREST\_PROPERTY**](https://msdn.microsoft.com/library/windows/hardware/jj156042)             | User-mode clients optionally use this property to get or set a camera's region of interest characteristics.           |
| [**KSPROPERTY\_CAMERACONTROL\_VIDEO\_STABILIZATION\_MODE\_PROPERTY**](https://msdn.microsoft.com/library/windows/hardware/jj156043) | User-mode clients optionally use this property to get or set a camera's video stabilization characteristics.          |

 

## <a href="" id="win8-1-extended-props"></a>Windows 8.1 extended camera control properties


Starting with Windows 8.1, the [KSPROPERTYSETID\_ExtendedCameraControl](https://msdn.microsoft.com/library/windows/hardware/dn567570) property set provides additional controls for camera photo sequencing. For more info on how to implement these controls, see these topics:

-   [Extended Camera Control Properties](extended-camera-control-properties.md)
-   [How To Implement Extended Camera Control Properties](how-to-implement-extended-camera-control-properties.md)
-   [Extended Camera Control Payloads](extended-camera-control-payloads.md)
-   [Photo Sequence Mode](photo-sequence-mode.md)

 

 




