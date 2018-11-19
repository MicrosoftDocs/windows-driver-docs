---
title: KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PHOTOTHUMBNAIL
description: This property gets or sets the thumbnail capability for the camera.
ms.assetid: 859620FD-02ED-4AA1-83B7-B92517F23B0C
keywords: ["KSPROPERTY_CAMERACONTROL_EXTENDED_PHOTOTHUMBNAIL Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CAMERACONTROL_EXTENDED_PHOTOTHUMBNAIL
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 09/11/2018
ms.localizationpriority: medium
---

# KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PHOTOTHUMBNAIL

This property gets or sets the thumbnail capability for the camera. If a scaling factor is provided, then thumbnails are enabled at the selected scale.

## Usage Summary Table

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th>Get</th>
<th>Set</th>
<th>Target</th>
<th>Property descriptor type</th>
<th>Property value type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Pin</p></td>
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier" data-raw-source="[&lt;strong&gt;KSPROPERTY&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier)"><strong>KSPROPERTY</strong></a></p></td>
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header" data-raw-source="[&lt;strong&gt;KSCAMERA_EXTENDEDPROP_HEADER&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header)"><strong>KSCAMERA_EXTENDEDPROP_HEADER</strong></a></p></td>
</tr>
</tbody>
</table>

The property value (operation data) contains a [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) structure and a [**KSCAMERA\_EXTENDEDPROP\_VALUE**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_value) structure. The **KSCAMERA\_EXTENDEDPROP\_VALUE** is required but the **Value** member is ignored.

The total property data size is **sizeof**(KSCAMERA\_EXTENDEDPROP\_HEADER) + **sizeof**(KSCAMERA\_EXTENDEDPROP\_VALUE). The **Size** member of [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) is set to this total property data size.

The **Capability** member of [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) contains a bitwise OR combination of one or more of the following scale values supported.

| Thumbnail scale flag                            | Description                            |
|-------------------------------------------------|----------------------------------------|
| KSCAMERA\_EXTENDEDPROP\_PHOTOTHUMBNAIL\_DISABLE | Thumbnails are disabled.               |
| KSCAMERA\_EXTENDEDPROP\_PHOTOTHUMBNAIL\_2X      | Thumbnail resolution is X/2 and Y/2.   |
| KSCAMERA\_EXTENDEDPROP\_PHOTOTHUMBNAIL\_2X      | Thumbnail resolution is X/4 and Y/4.   |
| KSCAMERA\_EXTENDEDPROP\_PHOTOTHUMBNAIL\_8X      | Thumbnail resolution is X/8 and Y/8.   |
| KSCAMERA\_EXTENDEDPROP\_PHOTOTHUMBNAIL\_16X     | Thumbnail resolution is X/16 and Y/16. |

The **Flags** member of [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) contains the thumbnail scale value currently set for the camera. If thumbnail generation is not enabled, then only KSCAMERA\_EXTENDEDPROP\_PHOTOTHUMBNAIL\_DISABLE is set in **Flags**.

This property control is asynchronous and not cancelable.

## Remarks

### Getting the property

When responding to a KSPROPERTY\_TYPE\_GET request, the driver sets the members of the [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) to the following.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Member</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Version</td>
<td>1</td>
</tr>
<tr class="even">
<td>PinId</td>
<td>The pin ID for the photo pin.</td>
</tr>
<tr class="odd">
<td>Size</td>
<td><p>sizeof(KSCAMERA_EXTENDEDPROP_HEADER) + sizeof(KSCAMERA_EXTENDEDPROP_VALUE)</p></td>
</tr>
<tr class="even">
<td>Result</td>
<td><p>An error value resulting from the attempt to get the thumbnail settings.</p></td>
</tr>
<tr class="odd">
<td>Capability</td>
<td>KSCAMERA_EXTENDEDPROP_CAPS_ASYNCCONTROL | (thumbnail scale values supported).</td>
</tr>
<tr class="even">
<td>Flags</td>
<td>The current thumbnail value setting (only one value).</td>
</tr>
</tbody>
</table>

### Setting the property

When the property is set, a KSPROPERTY\_TYPE\_SET request, the **Flags** member of [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) will contain one of the thumbnail scale flags.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Available starting with Windows 8.1.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ksmedia.h (include Ksmedia.h)</td>
</tr>
</tbody>
</table>

## See also

[**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header)

[**KSCAMERA\_EXTENDEDPROP\_VALUE**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_value)
