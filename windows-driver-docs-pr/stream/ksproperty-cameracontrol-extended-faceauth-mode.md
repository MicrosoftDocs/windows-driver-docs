---
title: KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FACEAUTH\_MODE
description: KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FACEAUTH\_MODE is a property ID that is used to turn on and off face authentication.
ms.assetid: 240AABDB-585B-462E-B391-1CB55BA563D5
keywords: ["KSPROPERTY_CAMERACONTROL_EXTENDED_FACEAUTH_MODE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CAMERACONTROL_EXTENDED_FACEAUTH_MODE
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 09/10/2018
ms.localizationpriority: medium
---

# KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FACEAUTH\_MODE


**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FACEAUTH\_MODE** is a property ID that is used to turn on and off face authentication.

### Usage Summary Table

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
<td><p>Pin</p></td>
<td><p>Synchronous</p></td>
</tr>
</tbody>
</table>

 

The following bit flags control face authentication in the driver:

```cpp
#define KSCAMERA_EXTENDEDPROP_FACEAUTH_MODE_DISABLED                        0x0000000000000001
#define KSCAMERA_EXTENDEDPROP_FACEAUTH_MODE_ALTERNATIVE_FRAME_ILLUMINATION  0x0000000000000002
#define KSCAMERA_EXTENDEDPROP_FACEAUTH_MODE_BACKGROUND_SUBTRACTION          0x0000000000000004
```

The following table describes the flag capabilities:

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
<td><p><strong>KSCAMERA_EXTENDEDPROP_FACEAUTH_MODE_DISABLED</strong></p></td>
<td><p>Optional capability.</p>
<p>When specified, the video Face authentication mode is disabled in the driver. This flag is mutually exclusive with the <strong>KSCAMERA_EXTENDEDPROP_FACEAUTH_MODE_BACKGROUND_SUBTRACTION</strong> and <strong>KSCAMERA_EXTENDEDPROP_FACEAUTH_MODE_ALTERNATIVE_FRAME_ILLUMINATION</strong> flags.</p></td>
</tr>
<tr class="even">
<td><p><strong>KSCAMERA_EXTENDEDPROP_FACEAUTH_MODE_ALTERNATIVE_FRAME_ILLUMINATION</strong></p></td>
<td><p>Mandatory capability if <strong>KSCAMERA_EXTENDEDPROP_FACEAUTH_MODE_BACKGROUND_SUBTRACTION</strong> is not supported.</p>
<p>When specified, it is mandatory to set <strong>KSCAMERA_EXTENDEDPROP_FACEAUTH_MODE_ALTERNATIVE_FRAME_ILLUMINATION</strong> on each sample as described by the frame metadata. This flag is mutually exclusive with the <strong>KSCAMERA_EXTENDEDPROP_FACEAUTH_MODE_BACKGROUND_SUBTRACTION</strong> and <strong>KSCAMERA_EXTENDEDPROP_FACEAUTH_MODE_DISABLED</strong> flags. In this mode it is expected to alternate IR strobe on/off for each frame captured.</p></td>
</tr>
<tr class="odd">
<td><p><strong>KSCAMERA_EXTENDEDPROP_FACEAUTH_MODE_BACKGROUND_SUBTRACTION</strong></p></td>
<td><p>Mandatory capability if <strong>KSCAMERA_EXTENDEDPROP_FACEAUTH_MODE_ALTERNATIVE_FRAME_ILLUMINATION</strong> is not supported.</p>
<p>This flag is mutually exclusive with the <strong>KSCAMERA_EXTENDEDPROP_FACEAUTH_MODE_ALTERNATIVE_FRAME_ILLUMINATION</strong> and <strong>KSCAMERA_EXTENDEDPROP_FACEAUTH_MODE_DISABLED</strong> flags. In this mode it is expected to create an IR image with background ambient IR light subtracted.</p></td>
</tr>
</tbody>
</table>

 

By default, the driver should have **KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FACEAUTH\_MODE** set to **KSCAMERA\_EXTENDEDPROP\_FACEAUTH\_MODE\_DISABLED** if it is a general purpose IR camera. Otherwise it should be set to **KSCAMERA\_EXTENDEDPROP\_FACEAUTH\_MODE\_BACKGROUND\_SUBTRACTION** or **KSCAMERA\_EXTENDEDPROP\_FACEAUTH\_MODE\_ALTERNATIVE\_FRAME\_ILLUMINATION**.

IR cameras should advertise **KSCAMERA\_EXTENDEDPROP\_FACEAUTH\_MODE\_DISABLED** if they are expected to work for general scenarios besides Windows Hello.

IR cameras used for face login should support either **KSCAMERA\_EXTENDEDPROP\_FACEAUTH\_MODE\_ALTERNATIVE\_FRAME\_ILLUMINATION** or **KSCAMERA\_EXTENDEDPROP\_FACEAUTH\_MODE\_BACKGROUND\_SUBTRACTION** capability they should only support one of these flags not both.

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
<td><p>Must be advertised on only one pin on the filter. The pin must be type <strong>PINNAME_VIDEO_CAPTURE</strong> or <strong>PINNAME_VIDEO_PREVIEW</strong>, must produce IR sensor data, and be marked shareable for FrameServer.</p></td>
</tr>
<tr class="odd">
<td><p>Size</p></td>
<td><p>This must be <strong>sizeof</strong>(<strong>KSCAMERA_EXTENDEDPROP_HEADER</strong>) + <strong>sizeof</strong>(<a href="https://msdn.microsoft.com/library/windows/hardware/dn567566" data-raw-source="[&lt;strong&gt;KSCAMERA_EXTENDEDPROP_VIDEOPROCSETTING&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn567566)"><strong>KSCAMERA_EXTENDEDPROP_VIDEOPROCSETTING</strong></a>).</p></td>
</tr>
<tr class="even">
<td><p>Result</p></td>
<td><p>Indicates the error results of the last SET operation. If no SET operation has taken place, this must be 0.</p></td>
</tr>
<tr class="odd">
<td><p>Capability</p></td>
<td><p>Must be a bit wise OR of the supported <strong>KSCAMERA_EXTENDEDPROP_ FACEAUTH_MODE_xxx</strong> flags as defined above.</p>
<p>The driver should not advertise both <strong>KSCAMERA_EXTENDEDPROP_FACEAUTH_MODE_ALTERNATIVE_FRAME_ILLUMINATION</strong> and <strong>KSCAMERA_EXTENDEDPROP_FACEAUTH_MODE_BACKGROUND_SUBTRACTION</strong></p></td>
</tr>
<tr class="even">
<td><p>Flags</p></td>
<td><p>This is a read/write field. This can be any one of the <strong>KSCAMERA_EXTENDEDPROP_ FACEAUTH_MODE_xxx</strong> flags defined above.</p></td>
</tr>
</tbody>
</table>

 

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
