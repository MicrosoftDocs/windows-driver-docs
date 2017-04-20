---
title: Camera Control Properties
author: windows-driver-content
description: Camera Control Properties
ms.assetid: 36a57245-e89e-4418-b0c4-a4c1479413b2
keywords:
- camera control properties WDK video capture
- control properties WDK video capture
- PROPSETID_VIDCAP_CAMERACONTROL
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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
<td><p>[<strong>KSPROPERTY_CAMERACONTROL_EXPOSURE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564401)</p></td>
<td><p>Controls a camera's digital exposure time.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>KSPROPERTY_CAMERACONTROL_FOCUS</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564410)</p></td>
<td><p>Controls a camera's focus setting.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>KSPROPERTY_CAMERACONTROL_IRIS</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564415)</p></td>
<td><p>Controls a camera's aperture setting.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>KSPROPERTY_CAMERACONTROL_ZOOM</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564459)</p></td>
<td><p>Controls a camera's zoom setting.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>KSPROPERTY_CAMERACONTROL_PAN</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564424)</p></td>
<td><p>Controls a camera's pan setting.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>KSPROPERTY_CAMERACONTROL_ROLL</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564432)</p></td>
<td><p>Controls a camera's roll setting.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>KSPROPERTY_CAMERACONTROL_TILT</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564454)</p></td>
<td><p>Controls a camera's tilt setting.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>KSPROPERTY_CAMERACONTROL_SCANMODE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564452)</p></td>
<td><p>Controls the scanning mode of a camera's sensor, such as interleaved, or non-interleaved.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>KSPROPERTY_CAMERACONTROL_PRIVACY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564430)</p></td>
<td><p>Controls whether a camera sensor should capture video, or is prevented from capturing video.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>KSPROPERTY_CAMERACONTROL_PANTILT</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564425)</p></td>
<td><p>Controls a camera's absolute pan and tilt setting.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>KSPROPERTY_CAMERACONTROL_PAN_RELATIVE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564429)</p></td>
<td><p>Controls a camera's relative rotation about the vertical axis from its current value.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>KSPROPERTY_CAMERACONTROL_TILT_RELATIVE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564456)</p></td>
<td><p>Controls a camera's relative rotation about the horizontal axis from its current position.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>KSPROPERTY_CAMERACONTROL_ROLL_RELATIVE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564435)</p></td>
<td><p>Controls a camera's relative rotation about the image viewing axis from its current value.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>KSPROPERTY_CAMERACONTROL_ZOOM_RELATIVE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564460)</p></td>
<td><p>Controls a camera's relative zoom setting from its current value.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>KSPROPERTY_CAMERACONTROL_EXPOSURE_RELATIVE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564404)</p></td>
<td><p>Controls a camera's relative shutter speed from its current value.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>KSPROPERTY_CAMERACONTROL_IRIS_RELATIVE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564417)</p></td>
<td><p>Specifies a camera's relative aperture setting from its current value.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>KSPROPERTY_CAMERACONTROL_FOCUS_RELATIVE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564413)</p></td>
<td><p>Controls a camera's relative focus setting from its current value.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>KSPROPERTY_CAMERACONTROL_PANTILT_RELATIVE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564427)</p></td>
<td><p>Controls a camera's relative pan and tilt setting from their current values.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>KSPROPERTY_CAMERACONTROL_FOCAL_LENGTH</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564406)</p></td>
<td><p>Specifies a camera's focal length.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>KSPROPERTY_CAMERACONTROL_AUTO_EXPOSURE_PRIORITY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564399)</p></td>
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Camera%20Control%20Properties%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


