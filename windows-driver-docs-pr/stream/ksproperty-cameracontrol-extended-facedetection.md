---
title: KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FACEDETECTION
description: KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FACEDETECTION is a property ID that is used to turn on and off face detection.
ms.assetid: F503939D-D6EF-47BD-855B-4404E1AAA15C
keywords: ["KSPROPERTY_CAMERACONTROL_EXTENDED_FACEDETECTION Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CAMERACONTROL_EXTENDED_FACEDETECTION
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 09/10/2018
ms.localizationpriority: medium
---

# KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FACEDETECTION


KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FACEDETECTION is a property ID that is used to turn on and off face detection.

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

 

The following flags can be placed in the KSCAMERA\_EXTENDEDPROP\_HEADER.Flags field to control face detection in the driver. By default, the driver should have FACEDETECTION\_OFF.

```cpp
#define KSCAMERA_EXTENDEDPROP_FACEDETECTION_PREVIEW         0x0000000000000001
#define KSCAMERA_EXTENDEDPROP_FACEDETECTION_VIDEO           0x0000000000000002
#define KSCAMERA_EXTENDEDPROP_FACEDETECTION_PHOTO           0x0000000000000004
#define KSCAMERA_EXTENDEDPROP_FACEDETECTION_BLINK           0x0000000000000008
#define KSCAMERA_EXTENDEDPROP_FACEDETECTION_SMILE           0x0000000000000010
```

If the driver supports this control, it must support FACEDETECTION\_OFF and any one of FACEDETECTION\_PREVIEW, FACEDETECTION\_VIDEO, or FACEDETECTION\_PHOTO. The driver should further perform dominate face analysis and feed the dominate face to 3A directly when face detection is enabled.

If the driver does not support face detection, the driver should not implement this control.

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
<td><p>KSCAMERA_EXTENDEDPROP_FACEDETECTION_OFF</p></td>
<td><p>This is a mandatory capability. When specified, the face detection is disabled in the driver.</p></td>
</tr>
<tr class="even">
<td><p>KSCAMERA_EXTENDEDPROP_FACEDETECTION_PREVIEW</p></td>
<td><p>This is an optional capability. When specified, the face detection is enabled in the driver and the driver must provide the face info, and the timestamp associated if supported, as a metadata through the preview pin. This flag is mutually exclusive with the OFF flag and can be used with the other flags.</p></td>
</tr>
<tr class="odd">
<td><p>KSCAMERA_EXTENDEDPROP_FACEDETECTION_VIDEO</p></td>
<td><p>This capability is optional. When specified, the face detection is enabled in the driver and the driver that supports such capability must provide the face info, and the timestamp associated if supported, as a metadata through the video pin. This flag is mutually exclusive with the OFF flag and can be used with the other flags.</p></td>
</tr>
<tr class="even">
<td><p>KSCAMERA_EXTENDEDPROP_FACEDETECTION_PHOTO</p></td>
<td><p>This capability is optional. When specified, the face detection is enabled in the driver and the driver that supports such capability must provide the face info, and the timestamp associated if supported, as a metadata through the photo pin. This flag is mutually exclusive with the OFF flag and can be used with the other flags.</p></td>
</tr>
<tr class="odd">
<td><p>KSCAMERA_EXTENDEDPROP_FACEDETECTION_BLINK</p></td>
<td><p>This capability is optional. This flag can only be specified when PREVIEW, VIDEO, and\or PHOTO flags are specified. When specified, the driver that supports such capability must additionally provide the blink info as a metadata through the corresponding pin.</p></td>
</tr>
<tr class="even">
<td><p>KSCAMERA_EXTENDEDPROP_FACEDETECTION_SMILE</p></td>
<td><p>This capability is optional. This flag can only be specified when PREVIEW, VIDEO, and\or PHOTO flags are specified. When specified, the driver that supports such capability must additionally provide the smile info as a metadata through the corresponding pin.</p></td>
</tr>
</tbody>
</table>

 

**Note**  MFT0 shall further attach the face information as a MF\_CAPTURE\_METADATA\_FACEROIS, the timestamp as a MF\_CAPTURE\_METADATA\_FACEROITIMESTAMPS, and the blink and/or smile information as a MF\_CAPTURE\_METADATA\_FACEROICHARACTERIZATIONS on the sample.

 

**Note**  PREVIEW, VIDEO, and PHOTO capabilities are optional. However, at least one of PREVIEW, VIDEO, and PHOTO capabilities must be supported if this control is supported.

 

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
<td><p>This must be sizeof(KSCAMERA_EXTENDEDPROP_HEADER) + sizeof(KSCAMERA_EXTENDEDPROP_VIDEOPROCSETTING).</p></td>
</tr>
<tr class="even">
<td><p>Result</p></td>
<td><p>Indicates the error results of the last SET operation. If no SET operation has taken place, this must be 0.</p></td>
</tr>
<tr class="odd">
<td><p>Capability</p></td>
<td><p>Must be a bitwise OR of the supported KSCAMERA_EXTENDEDPROP_FACEDETECTION_* flags as defined above.</p></td>
</tr>
<tr class="even">
<td><p>Flags</p></td>
<td><p>This is a read/write field. This can be a bit wise OR of the KSCAMERA_EXTENDEDPROP_FACEDETECTION_OFF/PREVIEW/VIDEO/PHOTO flags defined above, or a bit wise OR of KSCAMERA_EXTENDEDPROP_FACEDETECTION_BLINK and/or KSCAMERA_EXTENDEDPROP_FACEDETECTION_SMILE with any combinations of the KSCAMERA_EXTENDEDPROP_FACEDETECTION_PREVIEW/VIDEO/PHOTO flags.</p></td>
</tr>
</tbody>
</table>

 

The table below contains the descriptions and requirements for the KSCAMERA\_EXTENDEDPROP\_VIDEOPROCSETTING structure fields for the KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FACEDETECTION property. This structure is defined in Ksmedia.h.

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
<td><p>Mode</p></td>
<td><p>Unused. Must be 0.</p></td>
</tr>
<tr class="even">
<td><p>Min/Max/Step</p></td>
<td><p>The Min/Max/Step contains the minimum/maximum/increment of the number of faces that the camera driver can detect or search for in which Min must be &gt;= 1 and Step must be 1. Driver must return these for GET operations.</p></td>
</tr>
<tr class="odd">
<td><p>VideoProc</p></td>
<td><p>If <strong>FACEDETECTION_PREVIEW</strong>, <strong>FACEDETECTION_VIDEO</strong> or <strong>FACEDETECTION_PHOTO</strong> are specified in the Flags field of the <strong>KSCAMERA_EXTENDEDPROP_HEADER</strong>, <strong>VideoProc.Value.ul</strong> must also specify the maximum number of the faces that the driver should search for.</p>
<p>If FACEDETECTION_OFF is specified, for SET operations, the VideoProc field is ignored.</p>
<p>For GET operations, the driver must return the maximum number of faces that the driver is currently searching for. If face detection is OFF, 0 should be returned.</p></td>
</tr>
<tr class="even">
<td><p>Reserved</p></td>
<td><p>This is unused. This must be ignored by the driver.</p></td>
</tr>
</tbody>
</table>

 

### Remarks

When face detection is turned on, the face region of interests (ROIs) can be consumed directly by the driver to aid 3A processing as needed. If any user specified ROIs are configured via KSPROPERTY\_CAMERACONTROL\_EXTENDED\_ROI\_ISPCONTROL at the same time, the user specified ROIs will take precedence over the face ROIs detected. If the user specified ROIs are cleared, the face ROIs detected will take effect.

Requirements
------------

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
