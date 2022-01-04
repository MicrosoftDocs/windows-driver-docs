---
title: KSPROPERTY\_CAMERACONTROL\_EXTENDED\_ROI\_CONFIGCAPS
description: The KSPROPERTY\_CAMERACONTROL\_EXTENDED\_ROI\_CONFIGCAPS property ID that is defined in the KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PROPERTY enumeration is used to query ROI capabilities.
keywords: ["KSPROPERTY_CAMERACONTROL_EXTENDED_ROI_CONFIGCAPS Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CAMERACONTROL_EXTENDED_ROI_CONFIGCAPS
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 09/11/2018
---

# KSPROPERTY\_CAMERACONTROL\_EXTENDED\_ROI\_CONFIGCAPS

The **KSPROPERTY\_CAMERACONTROL\_EXTENDED\_ROI\_CONFIGCAPS** property ID that is defined in the [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PROPERTY**](/windows-hardware/drivers/ddi/ksmedia/ne-ksmedia-ksproperty_cameracontrol_extended_property) enumeration is used to query ROI capabilities.

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

To query the ROI capabilities with the driver, the **KSPROPERTY\_CAMERACONTROL\_EXTENDED\_ROI\_CONFIGCAPS** extended property control is sent to the driver along with a standard [**KSCAMERA\_EXTENDEDPROP\_HEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) structure followed by a [**KSCAMERA\_EXTENDEDPROP\_ROI\_CONFIGCAPSHEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_roi_configcapsheader) structure, which is followed by one or more [**KSCAMERA\_EXTENDEDPROP\_ROI\_CONFIGCAPS**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_roi_configcaps) structures. The following list illustrates the data structure with two ROI config caps.

-   **KSCAMERA\_EXTENDEDPROP\_HEADER**

-   **KSCAMERA\_EXTENDEDPROP\_ROI\_CONFIGCAPSHEADER** (ConfigCapCount = 2)

-   **KSCAMERA\_EXTENDEDPROP\_ROI\_CONFIGCAPS**

-   **KSCAMERA\_EXTENDEDPROP\_ROI\_CONFIGCAPS**

The table below contains the descriptions and requirements for the **KSCAMERA\_EXTENDEDPROP\_HEADER** structure fields when using the **KSPROPERTY\_CAMERACONTROL\_EXTENDED\_ROI\_CONFIGCAPS** property of the extended ROI control.

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
<td><p>This must be sizeof(<strong>KSCAMERA_EXTENDEDPROP_HEADER</strong> + sizeof(<strong>KSCAMERA_EXTENDEDPROP_ROI_CONFIGCAPSHEADER</strong>) + sizeof (<strong>KSCAMERA_EXTENDEDPROP_ROI_CONFIGCAPS</strong>) * ConfigCapCount.</p></td>
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
<td><p>This is a read-only field. This must be 0.</p></td>
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
