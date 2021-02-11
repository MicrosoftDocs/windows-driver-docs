---
title: KSPROPERTY\_CAMERACONTROL\_EXTENDED\_ROI\_ISPCONTROL
description: The KSPROPERTY\_CAMERACONTROL\_EXTENDED\_ROI\_ISPCONTROL property ID that is defined in the KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PROPERTY enumeration is used to get or configure the ROI settings and apply the desired processing.
keywords: ["KSPROPERTY_CAMERACONTROL_EXTENDED_ROI_ISPCONTROL Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CAMERACONTROL_EXTENDED_ROI_ISPCONTROL
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 09/11/2018
ms.localizationpriority: medium
---

# KSPROPERTY\_CAMERACONTROL\_EXTENDED\_ROI\_ISPCONTROL

The **KSPROPERTY\_CAMERACONTROL\_EXTENDED\_ROI\_ISPCONTROL** property ID that is defined in the [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PROPERTY**](/windows-hardware/drivers/ddi/ksmedia/ne-ksmedia-ksproperty_cameracontrol_extended_property) enumeration is used to get or configure the ROI settings and apply the desired processing.

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
<td><p>Asynchronous, Cancelable</p></td>
</tr>
</tbody>
</table>

To get the current ROI settings from the driver or to configure the ROI settings and apply the desired processing (3As), the **KSPROPERTY\_CAMERACONTROL\_EXTENDED\_ROI\_ISPCONTROL** extended property control is sent to the driver along with a standard [**KSCAMERA\_EXTENDEDPROP\_HEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) structure followed by a [**KSCAMERA\_EXTENDEDPROP\_ROI\_ISPCONTROLHEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_roi_ispcontrolheader) structure followed by a [**KSCAMERA\_EXTENDEDPROP\_ROI\_ISPCONTROL**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_roi_ispcontrol) structure and then by one or more corresponding ISP specific control payload structures. The following list illustrates a data structure layout with one focus ROI and two exposure ROIs.

-   **KSCAMERA\_EXTENDEDPROP\_HEADER**

-   **KSCAMERA\_EXTENDEDPROP\_ROI\_ISPCONTROLHEADER**

-   **KSCAMERA\_EXTENDEDPROP\_ROI\_ISPCONTROL** (Focus)

-   **KSCAMERA\_EXTENDEDPROP\_ROI\_FOCUS**

-   **KSCAMERA\_EXTENDEDPROP\_ROI\_ISPCONTROL** (Exposure with 2 ROIs)

-   **KSCAMERA\_EXTENDEDPROP\_ROI\_EXPOSURE** (ROI 1)

-   **KSCAMERA\_EXTENDEDPROP\_ROI\_EXPOSURE** (ROI 2)

The table below contains the descriptions and requirements for the **KSCAMERA\_EXTENDEDPROP\_HEADER** structure fields when using the **KSPROPERTY\_CAMERACONTROL\_EXTENDED\_ROI\_ISPCONTROL** property of the extended ROI control.

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
<td><p>For the initial GET call (when no SET call has ever taken place) this must be sizeof(<strong>KSCAMERA_EXTENDEDPROP_HEADER</strong>) + sizeof(<strong>KSCAMERA_EXTENDEDPROP_ROI_ISPCONTROLHEADER</strong>). In addition, the driver must return 0 within ControlCount in its ISO control header payload.</p>
<p>For any other SET or GET calls, this must be sizeof(<strong>KSCAMERA_EXTENDEDPROP_HEADER</strong>) + sizeof(<strong>KSCAMERA_EXTENDEDPROP_ ROI_ISPCONTROLHEADER</strong>) + ControlCount * sizeof(<strong>KSCAMERA_EXTENDEDPROP_ROI_ISPCONTROL</strong>) + sizeof(<strong>KSCAMERA_EXTENDEDPROP_ROI_FOCUS</strong>) * ROICount(focus) + sizeof(<strong>KSCAMERA_EXTENDEDPROP_EXPOSURE</strong>) * ROICount(exposure) + sizeof(<strong>KSCAMERA_EXTENDEDPROP_WHITEBALANCE</strong>) * ROICount(whitebalance).</p></td>
</tr>
<tr class="even">
<td><p>Result</p></td>
<td><p>This indicates the error results of the last SET operation. If no SET operation has taken place, this must be 0. The value 0 indicates that no errors were detected for all ISP controls configured.</p></td>
</tr>
<tr class="odd">
<td><p>Capability</p></td>
<td><p>This must be a bit-wise OR of <strong>KSCAMERA_EXTENDEDPROP_CAPS_ASYNCONTROL</strong> and <strong>KSCAMERA_EXTENDEDPROP_CAPS_CANCELLABLE</strong>.</p></td>
</tr>
<tr class="even">
<td><p>Flags</p></td>
<td><p>This is a read/write field This may be <strong>KSCAMERA_EXTENDEDPROP_FLAG_CANCELOPERATION</strong> for a SET call. This must be 0 for a GET call.</p></td>
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
