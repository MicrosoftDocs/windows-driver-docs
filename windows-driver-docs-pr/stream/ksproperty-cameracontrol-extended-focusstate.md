---
title: KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FOCUSSTATE
description: The KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FOCUSSTATE property ID that is defined in the KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PROPERTY enumeration is used to get the focus state from the driver. This is a read-only filter-level property.
keywords: ["KSPROPERTY_CAMERACONTROL_EXTENDED_FOCUSSTATE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CAMERACONTROL_EXTENDED_FOCUSSTATE
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 09/10/2018
ms.localizationpriority: medium
---

# KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FOCUSSTATE

The **KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FOCUSSTATE** property ID that is defined in the [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PROPERTY**](/windows-hardware/drivers/ddi/ksmedia/ne-ksmedia-ksproperty_cameracontrol_extended_property) enumeration is used to get the focus state from the driver. This is a read-only filter-level property.

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
<td><p>Synchronous (read-only)</p></td>
</tr>
</tbody>
</table>

For the [**KSCAMERA\_EXTENDEDPROP\_HEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header), the flags value contains the focus state returned by the camera driver. This is a synchronous get only control. The available focus state values are provided in the [**KSCAMERA\_EXTENDEDPROP\_FOCUSSTATE**](/windows-hardware/drivers/ddi/ksmedia/ne-ksmedia-kscamera_extendedprop_focusstate) enumeration.

The table below contains the descriptions and requirements for the **KSCAMERA\_EXTENDEDPROP\_HEADER** structure fields when using the focus state control.

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
<td><p>This must be 1,</p></td>
</tr>
<tr class="even">
<td><p>PinId</p></td>
<td><p>This must be <strong>KSCAMERA_EXTENDEDPROP_FILTERSCOPE</strong> (0xFFFFFFFF),</p></td>
</tr>
<tr class="odd">
<td><p>Size</p></td>
<td><p>This must be sizeof(<strong>KSCAMERA_EXTENDEDPROP_HEADER</strong>)+sizeof(<a href="/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_value" data-raw-source="[&lt;strong&gt;KSCAMERA_EXTENDEDPROP_VALUE&lt;/strong&gt;](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_value)"><strong>KSCAMERA_EXTENDEDPROP_VALUE</strong></a>)</p></td>
</tr>
<tr class="even">
<td><p>Result</p></td>
<td><p>This must be 0.</p></td>
</tr>
<tr class="odd">
<td><p>Capability</p></td>
<td><p>This must be 0.</p></td>
</tr>
<tr class="even">
<td><p>Flags</p></td>
<td><p>This is a read-only field. This contains the focus state returned by the driver. For more information about focus states, see the <a href="/windows-hardware/drivers/ddi/ksmedia/ne-ksmedia-kscamera_extendedprop_focusstate" data-raw-source="[&lt;strong&gt;KSCAMERA_EXTENDEDPROP_FOCUSSTATE&lt;/strong&gt;](/windows-hardware/drivers/ddi/ksmedia/ne-ksmedia-kscamera_extendedprop_focusstate)"><strong>KSCAMERA_EXTENDEDPROP_FOCUSSTATE</strong></a> topic.</p></td>
</tr>
</tbody>
</table>

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
