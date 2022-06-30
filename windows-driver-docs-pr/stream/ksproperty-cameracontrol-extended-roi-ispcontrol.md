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

## Adjustable Output Window Considerations
The 3A ROI coordinates sent to the camera are sent relative to the current output window of the camera. If the field of view has been modified due to use of a control such as [Zoom, Pan or Tilt](https://docs.microsoft.com/en-us/windows-hardware/drivers/stream/propsetid-vidcap-cameracontrol) or [Digital Window](https://docs.microsoft.com/en-us/windows-hardware/drivers/stream/digital-window-overview), the camera (or component implementing the Digital Window/PTZ control) is responsible for mapping the provided coordinates back to the sensor's full field of view, taking the current output window into consideration to ensure that the camera's 3A algorithm is targeting the correct spot. Depending on where the field of view modification occurs, the coordinate mapping may need to be bidirectional. For example, if a camera uses the Windows Platform DMFT for face detection, but the field of view modification is implemented in a component after the Platform DMFT in the driver chain, ROI coordinates provided by the application need to be mapped back to the full field of view before sending down to the camera and ROI coordinates calculated in the Platform DMFT need to be mapped to the modified field of view before being sent to an app requesting them.

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
