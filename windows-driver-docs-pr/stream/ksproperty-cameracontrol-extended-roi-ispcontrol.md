---
title: KSPROPERTY\_CAMERACONTROL\_EXTENDED\_ROI\_ISPCONTROL
description: The KSPROPERTY\_CAMERACONTROL\_EXTENDED\_ROI\_ISPCONTROL property ID that is defined in the KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PROPERTY enumeration is used to get or configure the ROI settings and apply the desired processing.
ms.assetid: 47F6C327-3279-44C2-9B18-50E6EC9C5E77
keywords: ["KSPROPERTY_CAMERACONTROL_EXTENDED_ROI_ISPCONTROL Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CAMERACONTROL_EXTENDED_ROI_ISPCONTROL
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# KSPROPERTY\_CAMERACONTROL\_EXTENDED\_ROI\_ISPCONTROL


The **KSPROPERTY\_CAMERACONTROL\_EXTENDED\_ROI\_ISPCONTROL** property ID that is defined in the [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PROPERTY**](https://msdn.microsoft.com/library/windows/hardware/dn917962) enumeration is used to get or configure the ROI settings and apply the desired processing.

## <span id="Usage_summary_table"></span><span id="usage_summary_table"></span><span id="USAGE_SUMMARY_TABLE"></span>Usage summary table


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
<td><p>Asynchronous, Cancellable</p></td>
</tr>
</tbody>
</table>

 

To get the current ROI settings from the driver or to configure the ROI settings and apply the desired processing (3As), the **KSPROPERTY\_CAMERACONTROL\_EXTENDED\_ROI\_ISPCONTROL** extended property control is sent to the driver along with a standard [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn925136) structure followed by a [**KSCAMERA\_EXTENDEDPROP\_ROI\_ISPCONTROLHEADER**](https://msdn.microsoft.com/library/windows/hardware/dn925175) structure followed by a [**KSCAMERA\_EXTENDEDPROP\_ROI\_ISPCONTROL**](https://msdn.microsoft.com/library/windows/hardware/dn925171) structure and then by one or more corresponding ISP specific control payload structures. The following list illustrates a data structure layout with one focus ROI and two exposure ROIs.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPERTY_CAMERACONTROL_EXTENDED_ROI_ISPCONTROL%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




